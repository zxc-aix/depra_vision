from PySide6.QtCore import QObject, QPoint, Slot

from app.utils.interaction.modes import (
    BoxHandler,
    CrossHandler,
    DefaultHandler,
    LDTHandler,
    MorrisHandler,
    SizeHandler,
    TCSHandler,
    YMTHandler,
)


class FieldSettingsController(QObject):
    def __init__(self, dialog_ui, field_configure):
        super().__init__()
        self.dialog_ui = dialog_ui
        self.field_configure = field_configure  # class FieldConfig

        self.mode_settings = {
            "default": {
                "handler": DefaultHandler(),
                "page": None,
                "max_points": 10,
                "param": {},
            },
            "size": {
                "handler": SizeHandler(),
                "page": None,
                "max_points": 2,
                "param": {},
            },
            "box": {
                "handler": BoxHandler(),
                "page": 0,
                "max_points": 1,
                "param": self.field_configure.box,
            },
            "cross": {
                "handler": CrossHandler(),
                "page": 1,
                "max_points": 1,
                "param": self.field_configure.cross,
            },
            "morris": {
                "handler": MorrisHandler(),
                "page": 2,
                "max_points": 2,
                "param": self.field_configure.morris,
            },
            "ldt": {
                "handler": LDTHandler(),
                "page": 3,
                "max_points": 1,
                "param": self.field_configure.ldt,
            },
            "ymt": {
                "handler": YMTHandler(),
                "page": 4,
                "max_points": 1,
                "param": self.field_configure.ymt,
            },
            "tcs": {
                "handler": TCSHandler(),
                "page": 5,
                "max_points": 1,
                "param": self.field_configure.tcs,
            },
        }
        # init variables
        self.handler = None
        self.field_configure.scale = self.dialog_ui.get_scale_value()

        self.apply_state_to_ui()
        self._setup_signals()

    def get_configuration(self):
        return self.field_configure

    def _setup_signals(self):
        self.dialog_ui.mode_size_activated.connect(self.apply_mode)
        self.dialog_ui.field_type_changed.connect(self.apply_mode)
        self.dialog_ui.field_param_changed.connect(self.on_field_param_changed)
        self.dialog_ui.accept.connect(self.accept)

        self.dialog_ui.move_point_up_clicked.connect(self.move_point_up)
        self.dialog_ui.move_point_down_clicked.connect(self.move_point_down)
        self.dialog_ui.move_point_left_clicked.connect(self.move_point_left)
        self.dialog_ui.move_point_right_clicked.connect(self.move_point_right)

        self.dialog_ui.point_selected.connect(self.on_point_selected)

    @Slot(str)
    def apply_mode(self, new_mode=None):
        if new_mode != self.field_configure.mode:
            self.field_configure.mode = new_mode

            if self.handler is not None:
                self.handler.points_changed.disconnect()
                self.handler.detach()

            print("mode in apply_mode:", new_mode)
            self.handler, page_number, max_points, params = self.mode_settings.get(
                new_mode, self.mode_settings["default"]
            ).values()
            print(
                f"Applying mode: {new_mode}, page: {page_number}, max_points: {max_points}, params: {params}"
            )

            points_restored = self.get_points_restored()

            self.handler.set_max_points(max_points)
            self.handler.set_params(params)
            self.handler.set_points_restored(points_restored)

            self.dialog_ui.ui.stackedWidget.show()
            self.dialog_ui.ui.stackedWidget.setCurrentIndex(
                page_number
            ) if page_number is not None else self.dialog_ui.ui.stackedWidget.hide()

            self.handler.points_changed.connect(self.update_points_combo)
            self.dialog_ui.ui.lblImage.set_handler(self.handler)
            self.dialog_ui.ui.cbPoints.clear()

            self.on_field_param_changed()

    def get_points_restored(self):
        points = []

        if self.field_configure.p_center is not None:
            points.append(self.field_configure.p_center)

        if self.field_configure.p:
            points.extend(self.field_configure.p)

        return points

    @Slot()
    def on_field_param_changed(self):
        mode = self.field_configure.mode

        print(f"Field parameter changed for mode: {mode}")
        if mode == "size":
            points = self.handler.get_points()
            if len(points) == 2:
                p1, p2 = points
                distance_pixel = (
                    (p2.x() - p1.x()) ** 2 + (p2.y() - p1.y()) ** 2
                ) ** 0.5

                main_params = self.dialog_ui.get_main_data()
                field_size = main_params.get("field_size", 0)
                self.field_configure.distance_pixel = distance_pixel

                pixel_size = field_size / distance_pixel if distance_pixel > 0 else 0
                self.field_configure.pixel_size = pixel_size

                print(f"Измеренное расстояние: {distance_pixel} пикселей")
                print(f"Размер пикселя: {pixel_size} cм/пиксель")
                return

        if not isinstance(
            self.dialog_ui.ui.lblImage._handler,
            (
                BoxHandler,
                CrossHandler,
                MorrisHandler,
                LDTHandler,
                YMTHandler,
                TCSHandler,
            ),
        ):
            return
        if self.field_configure.pixel_size is None:
            self.dialog_ui.show_warning("First, set the field size!")
            return

        scale = (
            1 / self.field_configure.pixel_size
            if self.field_configure.pixel_size != 0
            else 0
        )
        max_points = self.mode_settings[mode]["max_points"]

        if mode == "box":
            params = self.dialog_ui.get_box_data(scale)
            self.field_configure.box = params
            self.handler.set_params(params)
            self.handler.set_max_points(max_points + params["countObject"])

            points = self.handler.get_points()
            n = len(points) - 1

            if points and params["countObject"] < n:
                delta = params["countObject"] - n
                self.handler.set_points(points[:delta])

                self.update_points_combo()

        elif mode == "cross":
            params = self.dialog_ui.get_cross_data(scale)
            self.handler.set_params(params)

        elif mode == "morris":
            main_params = self.dialog_ui.get_main_data(scale)
            params = self.dialog_ui.get_morris_data(scale)
            params["field_size"] = main_params.get("field_size", 0)
            self.handler.set_params(params)

        elif mode == "ldt":
            params = self.dialog_ui.get_ldt_data(scale)
            self.handler.set_params(params)

            points = self.handler.get_points()
            self.handler.set_max_points(max_points + params["has_dark_room"])

            if len(points) > 2 and not params["has_dark_room"]:
                self.handler.set_points(points[:2])

        elif mode == "ymt":
            params = self.dialog_ui.get_ymt_data(scale)
            self.handler.set_params(params)
            self.handler.set_max_points(max_points + params["countObject"])

            points = self.handler.get_points()
            n = len(points) - 1

            if points and params["countObject"] < n:
                delta = params["countObject"] - n
                self.handler.set_points(points[:delta])

                self.update_points_combo()

        elif mode == "tcs":
            params = self.dialog_ui.get_tcs_data(scale)

            self.handler.set_params(params)
            self.handler.set_max_points(max_points + params["countObject"])

            points = self.handler.get_points()
            n = len(points) - 1

            if points and params["countObject"] < n:
                delta = params["countObject"] - n
                self.handler.set_points(points[:delta])

                self.update_points_combo()

        self.handler.update_display()

    def apply_state_to_ui(self):
        cfg = self.field_configure

        if cfg.field_size is not None:
            self.dialog_ui.ui.spinbSize.setValue(cfg.field_size)
        else:
            self.dialog_ui.ui.spinbSize.setValue(40)

        if cfg.model is not None:
            self.dialog_ui.ui.cbModel.setCurrentText(cfg.model)
        else:
            self.dialog_ui.ui.cbModel.setCurrentIndex(0)

        if cfg.box:
            self.dialog_ui.ui.spinb1.setValue(cfg.box.get("small", 10))
            self.dialog_ui.ui.spinb2.setValue(cfg.box.get("medium", 25))
            self.dialog_ui.ui.spinb3.setValue(cfg.box.get("large", 40))
            self.dialog_ui.ui.sbBOXCountObject.setValue(cfg.box.get("countObject", 0))
            self.dialog_ui.ui.sbBOXAreaInt.setValue(cfg.box.get("areaInt", 0))

        if cfg.morris:
            self.dialog_ui.ui.sbPlatform.setValue(cfg.morris.get("areaInt", 10))
            self.dialog_ui.ui.sbSpace.setValue(cfg.morris.get("space", 150))
            self.dialog_ui.ui.sbAngle.setValue(cfg.morris.get("angle", 0))
            diam = cfg.morris.get("diam", 0)
            self.dialog_ui.ui.sbDiam.setValue(diam)

            index = 1 if diam > 0 else 0
            self.dialog_ui.ui.cbMarkup.setCurrentIndex(index)

            for value in cfg.morris.get("custom_fields", []):
                self.dialog_ui.add_custom_field()
                self.dialog_ui.custom_fields[-1][1].setValue(int(value))

        if cfg.ldt:
            self.dialog_ui.ui.dsbLDTWidthArmsLight.setValue(
                cfg.ldt.get("widthArmsLight", 15)
            )
            self.dialog_ui.ui.dsbLDTLegthArmsLight.setValue(
                cfg.ldt.get("lengthArmsLight", 15)
            )
            self.dialog_ui.ui.dsbLDTWidthArmsDark.setValue(
                cfg.ldt.get("widthArmsDark", 15)
            )
            self.dialog_ui.ui.dsbLDTLegthArmsDark.setValue(
                cfg.ldt.get("lengthArmsDark", 15)
            )
            self.dialog_ui.ui.dsbLDTradius.setValue(cfg.ldt.get("radius", 5))
            self.dialog_ui.ui.dsbLDTSizePass.setValue(cfg.ldt.get("SizePass", 5))
            self.dialog_ui.ui.cbHasDarkRoom.setChecked(
                cfg.ldt.get("has_dark_room", False)
            )
            self.dialog_ui.has_dark_room(cfg.ldt.get("has_dark_room", False))

        if cfg.ymt:
            self.dialog_ui.ui.dsbWidthArms.setValue(cfg.ymt.get("widthArms", 32.5))
            self.dialog_ui.ui.dsbLegthArms.setValue(cfg.ymt.get("lengthArms", 10))
            self.dialog_ui.ui.sbAngleArms.setValue(cfg.ymt.get("angleArms", 0))
            self.dialog_ui.ui.sblCountObject.setValue(cfg.ymt.get("countObject", 0))
            self.dialog_ui.ui.sblAreaInt.setValue(cfg.ymt.get("areaInt", 0))
            self.dialog_ui.ui.sbYMTalpha1.setValue(cfg.ymt.get("alpha1", 0))
            self.dialog_ui.ui.sbYMTalpha2.setValue(cfg.ymt.get("alpha2", 0))
            self.dialog_ui.ui.sbYMTalpha3.setValue(cfg.ymt.get("alpha3", 0))

        if cfg.tcs:
            self.dialog_ui.ui.dsbTCSwidth.setValue(cfg.tcs.get("width", 40))
            self.dialog_ui.ui.dsbTCSlenght.setValue(cfg.tcs.get("length", 40))
            self.dialog_ui.ui.dsbTCSleftlegth.setValue(cfg.tcs.get("length_left", 10))
            self.dialog_ui.ui.dsbTCSrightlegth.setValue(cfg.tcs.get("length_right", 10))
            self.dialog_ui.ui.sbTCSCountObject.setValue(cfg.tcs.get("countObject", 0))
            self.dialog_ui.ui.sbTCSAreaInt.setValue(cfg.tcs.get("areaInt", 0))
            self.dialog_ui.ui.sbTCSSizePass.setValue(cfg.tcs.get("SizePass", 0))

        if cfg.cross:
            self.dialog_ui.ui.dsbCrossWidthArms.setValue(cfg.cross.get("widthArms", 4))
            self.dialog_ui.ui.dsbCrossLegthArms.setValue(
                cfg.cross.get("lengthArms", 15)
            )
            self.dialog_ui.ui.checkbCenter.setChecked(cfg.cross.get("center", False))
            self.dialog_ui.ui.checkbUp.setChecked(cfg.cross.get("up", False))
            self.dialog_ui.ui.checkbRight.setChecked(cfg.cross.get("right", False))
            self.dialog_ui.ui.checkbDown.setChecked(cfg.cross.get("down", False))
            self.dialog_ui.ui.checkbLeft.setChecked(cfg.cross.get("left", False))

    def move_point_up(self):
        if isinstance(
            self.dialog_ui.ui.lblImage._handler,
            (
                BoxHandler,
                CrossHandler,
                MorrisHandler,
                LDTHandler,
                YMTHandler,
                TCSHandler,
                DefaultHandler,
                SizeHandler,
            ),
        ):
            self.dialog_ui.ui.lblImage._handler.move_selected(dy=-1)
            self.on_field_param_changed()

    def move_point_down(self):
        if isinstance(
            self.dialog_ui.ui.lblImage._handler,
            (
                BoxHandler,
                CrossHandler,
                MorrisHandler,
                LDTHandler,
                YMTHandler,
                TCSHandler,
                DefaultHandler,
                SizeHandler,
            ),
        ):
            self.dialog_ui.ui.lblImage._handler.move_selected(dy=1)
            self.on_field_param_changed()

    def move_point_left(self):
        if isinstance(
            self.dialog_ui.ui.lblImage._handler,
            (
                BoxHandler,
                CrossHandler,
                MorrisHandler,
                LDTHandler,
                YMTHandler,
                TCSHandler,
                DefaultHandler,
                SizeHandler,
            ),
        ):
            self.dialog_ui.ui.lblImage._handler.move_selected(dx=-1)
            self.on_field_param_changed()

    def move_point_right(self):
        if isinstance(
            self.dialog_ui.ui.lblImage._handler,
            (
                BoxHandler,
                CrossHandler,
                MorrisHandler,
                LDTHandler,
                YMTHandler,
                TCSHandler,
                DefaultHandler,
                SizeHandler,
            ),
        ):
            self.dialog_ui.ui.lblImage._handler.move_selected(dx=1)
            self.on_field_param_changed()

    @Slot()
    def update_points_combo(self):
        points = self.handler.get_points()
        self.on_field_param_changed()

        combo = self.dialog_ui.ui.cbPoints
        combo.blockSignals(True)
        combo.clear()

        for i, p in enumerate(points):
            combo.addItem(f"Dot {i + 1} ({p.x()}, {p.y()})", i)

        if self.handler.selected_index is not None:
            combo.setCurrentIndex(self.handler.selected_index)
        combo.blockSignals(False)

    def on_point_selected(self, index: int):
        if self.handler is not None:
            self.handler.select(index)

    def accept(self):
        if self.field_configure.mode == "size":
            self.dialog_ui.show_warning("Choose field type!")
            return

        is_ok = self.update_field_configure()

        if not is_ok:
            return

        self.dialog_ui.accept()

    def update_field_configure(self):
        try:
            ui_data = self.dialog_ui.collect()
            points = self.handler.get_points()

            update = {}
            update |= self._collect_common(ui_data["main"])
            update |= self._collect_points(points, ui_data["main"])
            update |= self._collect_active_mode(ui_data)

            self.field_configure = self.field_configure.model_copy(update=update)
            self.field_configure.pixel_size = (
                self.field_configure.pixel_size * self.dialog_ui.get_scale_value()
            )

            return True

        except AttributeError:
            self.dialog_ui.show_warning("Choose field type!")
            return False
        except IndexError:
            self.dialog_ui.show_warning("Place the center of the field")
            return False
        except Exception as e:
            self.dialog_ui.show_warning(f"Error in {str(e)}")
            return False

    def _collect_common(self, main):
        return {"model": main["model"], "field_size": main["field_size"]}

    def _collect_active_mode(self, ui_data):
        mode = ui_data["main"]["mode"]
        return {"mode": mode, mode: ui_data["mode"][mode]}

    def _collect_points(self, points, main):
        label = main["sizes"]["label"]
        source = main["sizes"]["source"]

        # mode = main["mode"]
        # max_points = self.mode_settings[mode]["max_points"]-1

        update = {}
        print(f"DEBUG: points = {points}")
        update["p_center"] = self.convert_to_real_coords(
            points[0], label, source, keep_aspect=True
        )
        if len(points) > 1:
            other_points = [
                self.convert_to_real_coords(p, label, source, keep_aspect=True)
                for p in points[1:]
                if p is not None
            ]
            if other_points:
                update["p"] = other_points

        return update

    @staticmethod
    def convert_to_real_coords(
        point: QPoint,
        label: list[float, float],
        source: list[float, float],
        keep_aspect: bool = False,
    ) -> list[float, float]:
        src_w, src_h = source[0], source[1]
        lbl_w, lbl_h = label[0], label[1]

        if not keep_aspect:
            return (int(point.x() * (src_w / lbl_w)), int(point.y() * (src_h / lbl_h)))

        ratio = min(lbl_w / src_w, lbl_h / src_h)
        scaled_w = int(src_w * ratio)
        scaled_h = int(src_h * ratio)

        padding_x = (lbl_w - scaled_w) // 2
        padding_y = (lbl_h - scaled_h) // 2

        if (
            point.x() < padding_x
            or point.x() > padding_x + scaled_w
            or point.y() < padding_y
            or point.y() > padding_y + scaled_h
        ):
            return QPoint(-1, -1)

        x_in_img = point.x() - padding_x
        y_in_img = point.y() - padding_y

        x_src = int(x_in_img * (src_w / scaled_w))
        y_src = int(y_in_img * (src_h / scaled_h))

        return (x_src, y_src)

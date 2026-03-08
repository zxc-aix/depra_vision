from.zone_analyzer import BoxAnalyzer, CrossAnalyzer, MorrisAnalyzer, YMTAnalyzer, LDTAnalyzer, TCSAnalyzer
# from .ymt import YMTAnalyzer

def create_analyzer(points, config, add_params):
    mode = config.mode

    if mode == "box":
        return BoxAnalyzer(points, config, add_params)
    if mode == "cross":
        return CrossAnalyzer(points, config, add_params)
    if mode == "morris":
        return MorrisAnalyzer(points, config, add_params)
    if mode == "ymt":
        return YMTAnalyzer(points, config, add_params)
    if mode == "ldt":
        return LDTAnalyzer(points, config, add_params)
    if mode == "tcs":
        return TCSAnalyzer(points, config, add_params)


    raise ValueError(f"Unknown analysis mode: {mode}")

# typing
Interval = dict[str, str]
Root = str

# membuat tangga nada berdasarkan interval
def build_scale(root_name: Root, intervals: Interval, use: list[str]) -> list[str]:
    root_index = use.index(root_name)
    scale = [root_index]
    for interval in intervals:
        tuts = (scale[-1] + interval) % 12
        scale.append(tuts)
    return [use[n] for n in scale[:-1]]
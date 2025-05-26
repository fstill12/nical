# interval tangga nada

flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

rumus = {
    "judul": "rumus_interval_tangga_nada",
    "tangga_nada":{
        "mayor": [2, 2, 1, 2, 2, 2, 1],
        "minor": [2, 1, 2, 2, 1, 2, 2],
        "minor_natural": [2, 1, 2, 2, 1, 2, 2],
        "minor_harmonik": [2, 1, 2, 2, 1, 3, 1],
        "minor_melodik": [2, 1, 2, 2, 2, 2, 1],
        "kromatik": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    } 
}

# membuat tangga nada berdasarkan rumus
def build_scale(root_name, intervals, use_sharp=True):
    notes_names = sharp if use_sharp else flat
    root_index = notes_names.index(root_name)
    scale = [root_index]
    for interval in intervals:
        tuts = (scale[-1] + interval) % 12
        if tuts != 0:
            scale.append(tuts)
    return [notes_names[n] for n in scale]


if __name__=="__main__":
    # Nada dasar C
    print("C Mayor", build_scale(root_name="C", intervals=rumus["tangga_nada"]["mayor"]))
    print("A Minor", build_scale(root_name="A", intervals=rumus["tangga_nada"]["minor_natural"]))
    print()
    print("F Mayor", build_scale(root_name="F", intervals=rumus["tangga_nada"]["mayor"]))
    print("F Minor", build_scale(root_name="F", intervals=rumus["tangga_nada"]["minor_natural"]))
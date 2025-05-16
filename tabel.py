from tabulate import tabulate

data = [
    ["Herna", "Programmer", 25],
    ["Dina", "Designer", 23],
    ["Rudi", "Manager", 30]
]

headers = ["Nama", "Pekerjaan", "Usia"]

print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
def  rata_rata(data): 
    if len(data) == 0: 
        return None

    total = sum(data)
    return total / len(data)

data_uji = [
    [80, 90, 70],
    [100, 80],
    [75]
]

for data in data_uji:
    hasil = rata_rata(data)

    if hasil is None: 
        print(f"Data: {data}, Rata-rata: Tidak ada data")
    else:
        print(f"Data: {data}, Rata-rata: {hasil}")
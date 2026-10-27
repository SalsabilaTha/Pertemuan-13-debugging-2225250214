def hitung_rata_rata(nilai):
    return sum(nilai) / 5

data_nilai = [
    [80, 60, 90, 70],
    [100, 80],
    [75, 85, 95]
]

for data in data_nilai:
    print(f"Data: {data}")
    print("Rata-rata:", hitung_rata_rata(data))
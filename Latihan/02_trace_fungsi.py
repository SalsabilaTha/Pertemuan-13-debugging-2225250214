def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

harga = 200000
persen_diskon = 10

hasil = hitung_diskon(harga, persen_diskon)

print(f"Harga awal: {harga}")
print(f"Persentase diskon: {persen_diskon}%")
print(f"Harga setelah diskon: {hasil}")
def baca_nilai(nama_file): 
    with open(nama_file, "r", encoding="utf-8") as file: 
        nilai = [
            int(baris.strip())
            for baris in file
        ]
        
    return sum(nilai) / len(nilai)

nama_file = input("Masukkan nama file nilai: ")

hasil = baca_nilai(nama_file)

print("Rata-rata nilai:", hasil)
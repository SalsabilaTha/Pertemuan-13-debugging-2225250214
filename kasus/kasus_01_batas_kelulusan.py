def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak Lulus"

nilai_uji = [59, 60, 61]

for nilai in nilai_uji:
    print(f"Nilai: {nilai}, Status: {status_lulus(nilai)}")
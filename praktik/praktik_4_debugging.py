def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return None

    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


def jalankan_test_case():
    test_case = [
        ("T1", "rata-rata", [80, 60, 90, 70], 75.0),
        ("T2", "rata-rata", [100, 80], 90.0),
        ("T3", "status", 60, "Lulus"),
        ("T4", "status", 59, "Tidak lulus"),
        ("T5", "tertinggi", [80, 60, 90, 70], 90),
        ("T6", "rata-rata", [], None),
        ("T7", "tertinggi", [], None),
    ]

    for id_test, target, data, expected in test_case:
        if target == "rata-rata":
            actual = hitung_rata_rata(data)
        elif target == "status":
            actual = status(data)
        else:
            actual = nilai_tertinggi(data)

        hasil = "PASS" if actual == expected else "FAIL"

        print(f"{id_test} - {target}")
        print(f"Input    : {data}")
        print(f"Expected : {expected}")
        print(f"Actual   : {actual}")
        print(f"Status   : {hasil}")
        print("-" * 35)


if __name__ == "__main__":
    jalankan_test_case()
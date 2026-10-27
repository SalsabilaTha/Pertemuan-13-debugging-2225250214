# Pertemuan 13 - Debugging dan Testing

# Identitas Mahasiswa
- Nama: Salsabila Thahira
- NIM: 2225250214
- Kelas: 3B

## Kasus
Program yang diuji adalah program pengolahan nilai mahasiswa menggunakan Python. Program ini meliputi perhitungan rata-rata, penentuan status kelulusan, pencarian nilai tertinggi, serta penanganan data kosong. Pengujian dilakukan untuk menemukan kesalahan pada logika program dan memastikan hasil yang dihasilkan sesuai dengan yang diharapkan.

## Test Case
| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` untuk rata-rata | `75.0` | `60.0` | FAIL |
| T2 | `[100, 80]` untuk rata-rata | `90.0` | `36.0` | FAIL |
| T3 | `60` untuk status kelulusan | `Lulus` | `Tidak lulus` | FAIL |
| T4 | `59` untuk status kelulusan | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `[80, 60, 90, 70]` untuk nilai tertinggi | `90` | `0` | FAIL |
| T6 | `[]` untuk rata-rata | `None` | `ZeroDivisionError` | FAIL |
| T7 | `[]` untuk nilai tertinggi | `None` | `0` | FAIL |

## Bug Report
### Bug 1 — Perhitungan rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program membagi jumlah nilai dengan angka tetap, bukan dengan jumlah elemen yang sebenarnya.
- **Perbaikan:** Mengganti pembagi dengan `len(nilai)` dan menambahkan pengecekan jika list kosong.

### Bug 2 — Batas kelulusan
- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Kondisi menggunakan operator `>` sehingga nilai 60 tidak termasuk dalam kategori lulus.
- **Perbaikan:** Mengubah kondisi menjadi `>=` agar nilai 60 dianggap lulus.

### Bug 3 — Pencarian nilai tertinggi
- **Gejala:** Nilai tertinggi dari data `[80, 60, 90, 70]` menghasilkan 0.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Logika perbandingan tidak memperbarui variabel tertinggi dengan benar.
- **Perbaikan:** Menginisialisasi nilai tertinggi dengan elemen pertama dan menggunakan kondisi `x > tertinggi`.

### Bug 4 — Penanganan data kosong
- **Gejala:** Program error saat list kosong dan hasil tidak sesuai saat data kosong.
- **Lokasi:** Fungsi `hitung_rata_rata()` dan `nilai_tertinggi()`.
- **Akar penyebab:** Tidak ada pengecekan apakah list kosong sebelum melakukan operasi.
- **Perbaikan:** Mengembalikan `None` jika data kosong.

## Retest
| ID | Input | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` untuk rata-rata | `75.0` | `75.0` | PASS |
| T2 | `[100, 80]` untuk rata-rata | `90.0` | `90.0` | PASS |
| T3 | `60` untuk status kelulusan | `Lulus` | `Lulus` | PASS |
| T4 | `59` untuk status kelulusan | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `[80, 60, 90, 70]` untuk nilai tertinggi | `90` | `90` | PASS |
| T6 | `[]` untuk rata-rata | `None` | `None` | PASS |
| T7 | `[]` untuk nilai tertinggi | `None` | `None` | PASS |

## Cara Menjalankan
```bash
python praktik/praktik_4_debugging.py
```

## Refleksi
Teknik debugging yang paling membantu adalah membuat test case dan melakukan tracing. Test case membantu membandingkan hasil yang diharapkan dengan hasil aktual, sementara tracing membantu melihat perubahan nilai variabel pada setiap langkah eksekusi. Dengan cara ini, akar permasalahan dapat ditemukan lebih cepat dan perbaikan program menjadi lebih tepat.

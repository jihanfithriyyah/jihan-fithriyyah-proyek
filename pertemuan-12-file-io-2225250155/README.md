# Pertemuan 12 File I/O dan Error Handling
Nama: Jihan Fithriyyah
NIM: 2225250155
Kelas: 3A

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM, nilai

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case
- **Normal:** Semua baris valid -> Rekap dihitung dengan benar.
- **File Hilang:** `nilai.txt` tidak ada -> Menampilkan pesan error khusus tanpa membuat program *crash*.
- **Nilai Invalid (`A004, abc`):** Baris invalid dilewati dan dilaporkan, sementara record data lainnya tetap diproses dengan normal.
- **Baris Kosong:** Otomatis dilewati oleh program.

## Refleksi
Penanganan error menggunakan `ValueError` sangat membantu ketika membaca data dari file eksternal agar baris yang rusak atau salah ketik (berupa teks) tidak menghentikan keseluruhan proses eksekusi program.
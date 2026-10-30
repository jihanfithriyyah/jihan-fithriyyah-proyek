# File: latihan/04_proses_baris.py

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        # Bersihkan spasi atau karakter newline di awal dan akhir baris
        baris = baris.strip()
        
        # Lewati otomatis jika baris kosong
        if not baris:
            continue
        
        # Pastikan baris mengandung tanda koma sebelum di-split
        if "," in baris:
            nim, teks_nilai = baris.split(",")
            print(f"NIM: {nim.strip()}, Nilai: {teks_nilai.strip()}")
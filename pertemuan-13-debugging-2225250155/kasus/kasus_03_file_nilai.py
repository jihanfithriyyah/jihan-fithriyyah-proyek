def baca_file_nilai(nama_file):
    # Berpotensi memicu FileNotFoundError atau error jika file kosong
    file = open(nama_file, 'r')
    isi = file.read()
    file.close()
    return isi

print(baca_file_nilai("data_kosong.txt"))
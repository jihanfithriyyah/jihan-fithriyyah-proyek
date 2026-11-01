def cek_kelulusan(nilai):
    if nilai > 60:  # Bug: nilai tepat 60 tidak lulus karena kurang dari / sama dengan tidak diakomodasi
        return "Lulus"
    return "Tidak Lulus"

print("Nilai 60:", cek_kelulusan(60))
from datetime import datetime

def teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print('Input tidak boleh kosong.')

def angka(pesan, minimum=0):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < minimum:
                print('Minimal', minimum)
                continue
            return nilai
        except ValueError:
            print('Masukkan angka bulat yang benar.')

def cari(data, kunci, nilai):
    for item in data:
        if item[kunci] == nilai:
            return item
    return None

def tanggal(pesan):
    while True:
        try:
            return datetime.strptime(input(pesan).strip(), '%Y-%m-%d').date()
        except ValueError:
            print('Format tanggal harus YYYY-MM-DD dan tanggal harus valid.')

def garis():
    print('-' * 55)

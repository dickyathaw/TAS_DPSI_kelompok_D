from .utils import teks, angka, cari, garis
from .penyimpanan import simpan

def tampil(data):
    garis()
    if not data:
        print('Belum ada buku.')
    for b in data:
        print(f"{b['id']} | {b['judul']} | {b['penulis']} | {b['kategori']} | Stok: {b['stok']}")
    garis()

def tambah(data):
    kode = teks('Kode buku: ')
    if cari(data, 'id', kode):
        print('Kode buku sudah digunakan.')
        return
    buku = {'id': kode, 'judul': teks('Judul: '), 'penulis': teks('Penulis: '),
            'kategori': teks('Kategori: '), 'stok': angka('Jumlah stok: ', 0)}
    data.append(buku)
    simpan('buku', data)
    print('Buku berhasil ditambahkan.')

def ubah(data, pinjaman):
    b = cari(data, 'id', teks('Kode buku: '))
    if not b:
        print('Buku tidak ditemukan.')
        return
    print('1. Judul  2. Penulis  3. Kategori  4. Stok tersedia')
    pilihan = input('Pilih: ')
    kolom = {'1': 'judul', '2': 'penulis', '3': 'kategori'}
    if pilihan in kolom:
        b[kolom[pilihan]] = teks('Nilai baru: ')
    elif pilihan == '4':
        b['stok'] = angka('Stok tersedia baru: ', 0)
    else:
        print('Pilihan tidak valid.')
        return
    simpan('buku', data)
    print('Data buku diperbarui.')

def hapus(data, pinjaman):
    b = cari(data, 'id', teks('Kode buku: '))
    if not b:
        print('Buku tidak ditemukan.')
        return
    for p in pinjaman:
        if p['status'] == 'Dipinjam' and any(x['id_buku'] == b['id'] for x in p['items']):
            print('Buku sedang dipinjam, tidak bisa dihapus.')
            return
    data.remove(b)
    simpan('buku', data)
    print('Buku dihapus.')

def kategori(data):
    kelompok = set(b['kategori'] for b in data)
    if not kelompok:
        print('Belum ada kategori.')
    for k in sorted(kelompok):
        print('\nKategori:', k)
        for b in data:
            if b['kategori'] == k:
                print(' -', b['id'], b['judul'], '| stok:', b['stok'])

def menu(data, pinjaman):
    while True:
        print('\n=== MANAJEMEN BUKU ===\n1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus\n5. Kelompok kategori\n0. Kembali')
        p = input('Pilihan: ')
        if p == '1': tambah(data)
        elif p == '2': tampil(data)
        elif p == '3': ubah(data, pinjaman)
        elif p == '4': hapus(data, pinjaman)
        elif p == '5': kategori(data)
        elif p == '0': break
        else: print('Pilihan tidak valid.')

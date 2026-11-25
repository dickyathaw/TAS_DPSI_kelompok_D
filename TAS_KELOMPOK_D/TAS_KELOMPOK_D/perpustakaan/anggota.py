from .utils import teks, cari, garis
from .penyimpanan import simpan

def tampil(data):
    garis()
    if not data:
        print('Belum ada anggota.')
    for a in data:
        print(f"{a['id']} | {a['nama']} | {a['telepon']}")
    garis()

def tambah(data):
    kode = teks('ID anggota: ')
    if cari(data, 'id', kode):
        print('ID anggota sudah digunakan.')
        return
    data.append({'id': kode, 'nama': teks('Nama: '), 'telepon': teks('Telepon: ')})
    simpan('anggota', data)
    print('Anggota telah ditambahkan.')

def ubah(data):
    a = cari(data, 'id', teks('ID anggota: '))
    if not a:
        print('Anggota tidak ditemukan.')
        return
    print('1. Nama  2. Telepon')
    p = input('Pilihan: ')
    if p == '1': a['nama'] = teks('Nama baru: ')
    elif p == '2': a['telepon'] = teks('Telepon baru: ')
    else:
        print('Pilihan tidak valid.')
        return
    simpan('anggota', data)
    print('Anggota telah diperbarui.')

def hapus(data, pinjaman):
    a = cari(data, 'id', teks('ID anggota: '))
    if not a:
        print('Anggota tidak ditemukan.')
        return
    if any(p['id_anggota'] == a['id'] and p['status'] == 'Dipinjam' for p in pinjaman):
        print('Anggota masih memiliki pinjaman, tidak dapat dihapus.')
        return
    data.remove(a)
    simpan('anggota', data)
    print('Anggota telah dihapus.')

def menu(data, pinjaman):
    while True:
        print('\n=== MANAJEMEN ANGGOTA ===\n1. Tambah\n2. Tampilkan\n3. Ubah\n4. Hapus\n0. Kembali')
        p = input('Pilihan: ')
        if p == '1': tambah(data)
        elif p == '2': tampil(data)
        elif p == '3': ubah(data)
        elif p == '4': hapus(data, pinjaman)
        elif p == '0': break
        else: print('Pilihan tidak valid.')

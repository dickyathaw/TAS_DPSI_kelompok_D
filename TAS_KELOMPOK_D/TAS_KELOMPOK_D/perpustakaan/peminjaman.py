from datetime import date, timedelta
from .utils import teks, cari, garis
from .penyimpanan import simpan_semua

LAMA_PINJAM = 7
TARIF_DENDA = 1000
LAMA_PINJAM = 7
STATUS = ['Dipinjam', 'Dikembalikan']

def id_baru(data):
    nomor = 1
    kode_terpakai = {p['id'] for p in data}
    while 'p' + str(nomor).zfill(4) in kode_terpakai:
        nomor += 1
    return 'p' + str(nomor).zfill(4)

def pinjam(buku, anggota, pinjaman):
    if not buku or not anggota:
        print('Tambahkan data buku dan anggota terlebih dahulu.')
        return
    kode = teks('ID anggota: ')
    a = cari(anggota, 'id', kode)
    if not a:
        print('Anggota tidak ditemukan.')
        return
    if any(p['id_anggota'] == kode and p['status'] == STATUS[0] for p in pinjaman):
        print('Anggota masih punya kewajiban pengembalian.')
        return
    items = []
    while True:
        print('\nDaftar buku tersedia:')
        for b in buku:
            if b['stok'] > 0:
                print(b['id'], '|', b['judul'], '| stok:', b['stok'])
        kode_buku = teks('Kode buku (0 untuk selesai): ')
        if kode_buku == '0':
            break
        b = cari(buku, 'id', kode_buku)
        if not b:
            print('Buku tidak ditemukan.')
            continue
        sudah = sum(x['jumlah'] for x in items if x['id_buku'] == kode_buku)
        sisa = b['stok'] - sudah
        if sisa <= 0:
            print('Stok tidak cukup.')
            continue
        jumlah = angka ('Jumlah pinjam: ', 1)
        if jumlah > sisa:
            print('Jumlah melebihi stok tersedia:', sisa)
            continue
        items.append({'id_buku': kode_buku, 'judul': b['judul'], 'jumlah': jumlah})
        print('Buku masuk daftar pinjam.')
    if not items:
        print('Peminjaman dibatalkan (tidak ada buku).')
        return
    hari_ini = date.today()
    batas = hari_ini + timedelta(days=LAMA_PINJAM)
    print('\nAnggota:', a['nama'])
    for x in items:
        print('-', x['judul'], 'x', x['jumlah'])
    print('Tanggal pinjam:', hari_ini, '| Batas kembali:', batas)
    if input('Konfirmasi peminjaman? (y/n): ').strip().lower() != 'y':
        print('Dibatalkan.')
        return
    for x in items:
        cari(buku, 'id', x['id_buku'])['stok'] -= x['jumlah']
    transaksi = {'id': id_baru(pinjaman), 'id_anggota': kode, 'nama_anggota': a['nama'],
                 'items': items, 'tanggal_pinjam': hari_ini.isoformat(),
                 'batas_kembali': batas.isoformat(), 'tanggal_kembali': None,
                 'terlambat_hari': 0, 'denda': 0, 'status': STATUS[0]}
    pinjaman.append(transaksi)
    simpan_semua(buku, anggota, pinjaman)
    print('Peminjaman berhasil! Nomor:', transaksi['id'])

def kembali(buku, anggota, pinjaman):
    aktif = [p for p in pinjaman if p['status'] == STATUS[0]]
    if not aktif:
        print('Tidak ada peminjaman aktif.')
        return
    for p in aktif:
        print(p['id'], '|', p['nama_anggota'], '| batas:', p['batas_kembali'])
    p = cari(aktif, 'id', teks('Nomor peminjaman: '))
    if not p:
        print('Peminjaman aktif tidak ditemukan.')
        return
    hari_ini = date.today()
    batas = date.fromisoformat(p['batas_kembali'])
    terlambat = max(0, (hari_ini - batas).days)
    jumlah_buku = sum(x['jumlah'] for x in p['items'])
    denda = terlambat * TARIF_DENDA * jumlah_buku
    garis()
    print('BUKTI PENGEMBALIAN')
    print('Transaksi:', p['id'], '| Anggota:', p['nama_anggota'])
    print('Tanggal kembali:', hari_ini, '| Terlambat:', terlambat, 'hari')
    print('Total buku:', jumlah_buku, '| Denda: Rp', denda)
    garis()
    if input('Konfirmasi pengembalian? (y/n): ').strip().lower() != 'y':
        print('Dibatalkan.')
        return
    for x in p['items']:
        b = cari(buku, 'id', x['id_buku'])
        if b:
            b['stok'] += x['jumlah']
    p['tanggal_kembali'] = hari_ini.isoformat()
    p['terlambat_hari'] = terlambat
    p['denda'] = denda
    p['status'] = STATUS[1]
    simpan_semua(buku, anggota, pinjaman)
    print('Pengembalian berhasil. Stok sudah bertambah.')

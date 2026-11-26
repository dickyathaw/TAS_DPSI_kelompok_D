from .utils import garis, teks

def detail(p):
    garis()
    print('Nomor:', p['id'], '| Anggota:', p['nama_anggota'], '(' + p['id_anggota'] + ')')
    print('Pinjam:', p['tanggal_pinjam'], '| Batas:', p['batas_kembali'])
    print('Status:', p['status'], '| Kembali:', p['tanggal_kembali'] or '-')
    for item in p['items']:
        print(' -', item['judul'], '| Jumlah:', item['jumlah'])
    print('Terlambat:', p['terlambat_hari'], 'hari | Denda: Rp', p['denda'])
    garis()

def menu(buku, anggota, pinjaman):
    while True:
        print('\n=== LAPORAN ===\n1. Semua riwayat\n2. Riwayat per anggota\n3. Buku sedang dipinjam\n4. Buku tersedia\n5. Total denda\n0. Kembali')
        p = input('Pilihan: ')
        if p == '1':
            for x in pinjaman: detail(x)
            if not pinjaman: print('Belum ada transaksi.')
        elif p == '2':
            kode = teks('ID anggota: ')
            hasil = [x for x in pinjaman if x['id_anggota'] == kode]
            for x in hasil: detail(x)
            if not hasil: print('Tidak ada riwayat.')
        elif p == '3':
            hasil = [x for x in pinjaman if x['status'] == 'Dipinjam']
            for x in hasil: detail(x)
            if not hasil: print('Tidak ada buku yang dipinjam.')
        elif p == '4':
            hasil = [x for x in buku if x['stok'] > 0]
            for x in hasil: print(x['id'], '|', x['judul'], '| stok:', x['stok'])
            if not hasil: print('Tidak ada buku tersedia.')
        elif p == '5':
            print('Total denda keterlambatan: Rp', sum(x['denda'] for x in pinjaman))
        elif p == '0': break
        else: print('Pilihan tidak valid.')


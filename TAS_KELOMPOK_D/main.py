from perpustakaan.penyimpanan import baca
from perpustakaan import buku, anggota, peminjaman, laporan

def main():
    try:
        data_buku = baca('buku')
        data_anggota = baca('anggota')
        data_pinjaman = baca('peminjaman')
    except (OSError, ValueError):
        print('Data tidak dapat dibaca. Perbaiki file JSON terlebih dahulu.')
        return
    while True:
        print('\n' + '=' * 40)
        print('   SISTEM MANAJEMEN PERPUSTAKAAN')
        print('          TAS KELOMPOK D')
        print('=' * 40)
        print('1. Manajemen Buku')
        print('2. Manajemen Anggota')
        print('3. Peminjaman Buku')
        print('4. Pengembalian Buku')
        print('5. Riwayat dan Laporan')
        print('0. Keluar')
        pilihan = input('Pilih menu: ').strip()
        try:
            if pilihan == '1': buku.menu(data_buku, data_pinjaman)
            elif pilihan == '2': anggota.menu(data_anggota, data_pinjaman)
            elif pilihan == '3': peminjaman.pinjam(data_buku, data_anggota, data_pinjaman)
            elif pilihan == '4': peminjaman.kembali(data_buku, data_anggota, data_pinjaman)
            elif pilihan == '5': laporan.menu(data_buku, data_anggota, data_pinjaman)
            elif pilihan == '0':
                print('Terima kasih! Data sudah tersimpan.')
                break
            else: print('Pilihan tidak tersedia.')
        except OSError as error:
            print('Gagal menyimpan file:', error)
            print('Tutup aplikasi dan periksa file data sebelum melanjutkan.')
            break

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nAplikasi dihentikan.')

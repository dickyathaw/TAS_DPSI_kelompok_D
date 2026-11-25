# TAS Kelompok D — Sistem Manajemen Perpustakaan

## Cara menjalankan
1. Buka folder `TAS_KELOMPOK_D` di VS Code.
2. Pastikan Python 3.8+ terpasang.
3. Buka Terminal > New Terminal.
4. Jalankan `python main.py` (atau `py main.py` pada Windows).
5. Pilih menu dengan mengetik angka.

Tidak memerlukan instalasi package tambahan.

## Struktur
- `main.py`: menu utama
- `perpustakaan/buku.py`: CRUD buku dan kategori
- `perpustakaan/anggota.py`: CRUD anggota
- `perpustakaan/peminjaman.py`: transaksi peminjaman/pengembalian, stok dan denda
- `perpustakaan/laporan.py`: riwayat dan laporan
- `perpustakaan/penyimpanan.py`: simpan/baca JSON
- `perpustakaan/utils.py`: validasi input
- `data/*.json`: penyimpanan permanen

## Aturan yang diterapkan
- Kode buku dan anggota unik.
- Stok tidak boleh negatif dan pinjaman tidak boleh melebihi stok.
- Anggota yang masih meminjam tidak dapat meminjam lagi.
- Satu transaksi bisa memuat beberapa jenis buku.
- Stok berkurang saat pinjam dan bertambah saat kembali.
- Denda contoh: Rp1.000 per buku per hari terlambat, dengan batas pengembalian 7 hari setelah pinjam.
- Riwayat tetap tersimpan di JSON setelah program ditutup.
- Buku/anggota yang masih terkait peminjaman aktif tidak bisa dihapus.

## Pembagian kerja kelompok (usulan)
1. Anggota 1: `buku.py`
2. Anggota 2: `anggota.py`
3. Anggota 3: `peminjaman.py`
4. Anggota 4: `laporan.py`, `penyimpanan.py`, `utils.py`, integrasi `main.py`

## Catatan
Tarif denda dan lama pinjam adalah asumsi contoh karena PDF tidak menentukan nilainya. Sesuaikan pada konstanta `TARIF_DENDA` dan `LAMA_PINJAM` di `peminjaman.py`.
Pencatatan denda menghitung denda yang dikenakan, bukan pembayaran denda.
Untuk pemakaian kelas/simulasi. File JSON sederhana ini bukan database transaksi multi-user.

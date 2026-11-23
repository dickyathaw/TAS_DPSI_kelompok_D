import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
DATA_DIR.mkdir(exist_ok=True)

def baca(nama):
    lokasi = DATA_DIR / (nama + '.json')
    try:
        with open(lokasi, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError('Isi data harus berupa list')
            return data
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print('Gagal membaca', lokasi.name, ':', error)
        raise

def simpan(nama, data):
    lokasi = DATA_DIR / (nama + '.json')
    sementara = lokasi.with_suffix('.tmp')
    with open(sementara, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    sementara.replace(lokasi)

def simpan_semua(buku, anggota, peminjaman):
    simpan('buku', buku)
    simpan('anggota', anggota)
    simpan('peminjaman', peminjaman)

# TaskCash Manager

TaskCash Manager adalah aplikasi desktop PySide6 yang menggabungkan dua kebutuhan dalam satu program:

- Manajemen tugas harian melalui fitur to-do list
- Pencatatan pemasukan dan pengeluaran pribadi

Project ini dibuat mengikuti prinsip Separation of Concerns dengan pemisahan modul UI, controller, database, model, dan styling QSS eksternal.

## Fitur Utama

- Menu bar `Tentang Aplikasi`
- Form tambah dan edit dalam dialog terpisah
- Data to-do tersimpan di SQLite
- Data keuangan tersimpan di SQLite
- Ringkasan total pemasukan, pengeluaran, dan saldo
- Konfirmasi hapus menggunakan `QMessageBox`
- Nama mahasiswa dan NIM tampil di halaman utama dalam mode read-only
- Styling antarmuka menggunakan file eksternal `assets/style.qss`

## Struktur Project

```text
MiniProject/
├── app/
│   ├── config.py
│   ├── controllers/
│   │   └── main_controller.py
│   ├── database/
│   │   └── db_manager.py
│   ├── models/
│   │   ├── finance_model.py
│   │   └── todo_model.py
│   └── views/
│       ├── dialogs.py
│       └── main_window.py
├── assets/
│   └── style.qss
├── data/
│   └── pemvis_manager.db
└── main.py
```

## Cara Menjalankan

1. Install dependency:

```bash
pip install PySide6
```

2. Jalankan aplikasi:

```bash
python main.py
```

## Teknologi

- Python
- PySide6
- SQLite
- QSS

## Catatan

- Ganti nilai `STUDENT_NAME` dan `STUDENT_ID` pada `app/config.py` sesuai identitas Anda.
- Database akan dibuat otomatis saat aplikasi dijalankan pertama kali.

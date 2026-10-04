# SentiKampus API

API backend untuk aplikasi **SentiKampus** yang digunakan untuk melakukan prediksi sentimen menggunakan FastAPI.

## Teknologi

- Python
- FastAPI
- Uvicorn
- REST API

## Persyaratan

Pastikan sudah terinstall:

- Python 3.10 atau lebih baru
- pip
- Git

Cek versi Python:

```bash
python3 --version
```

Cek pip:

```bash
pip3 --version
```

## 1. Clone Repository

Clone repository ke komputer:

```bash
git clone git@github.com:alhilalakbar/sentikampus_api.git
```

Masuk ke folder project:

```bash
cd sentikampus_api
```

## 2. Membuat Virtual Environment

Buat virtual environment:

```bash
python3 -m venv .venv
```

Aktifkan virtual environment:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Setelah aktif, terminal akan menampilkan tanda seperti:

```text
(.venv)
```

## 3. Install Dependency

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Kemudian install dependency:

```bash
pip install -r requirements.txt
```

## 4. Menjalankan API

Jalankan server FastAPI dengan:

```bash
uvicorn app.main:app --reload
```

Jika berhasil, server akan berjalan di:

```text
http://127.0.0.1:8000
```

API juga dapat diakses melalui:

```text
http://localhost:8000
```

## 5. Dokumentasi API

FastAPI menyediakan dokumentasi interaktif secara otomatis.

### Swagger UI

Buka:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Buka:

```text
http://127.0.0.1:8000/redoc
```

Swagger UI dapat digunakan untuk mencoba endpoint API secara langsung tanpa aplikasi frontend.

## 6. Endpoint Prediksi Sentimen

Endpoint utama:

```text
POST /api/v1/predict
```

Contoh request:

```json
{
  "text": "Pelayanan kampus sangat lambat"
}
```

Contoh penggunaan menggunakan `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Pelayanan kampus sangat lambat"}'
```

Response:

```json
{
  "label": "negative",
  "score": 0.91
}
```

## 7. Menjalankan Tanpa `--reload`

Untuk menjalankan server tanpa mode development:

```bash
uvicorn app.main:app
```

Jika API perlu diakses dari perangkat lain dalam jaringan lokal:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Kemudian akses menggunakan IP komputer:

```text
http://IP-KOMPUTER:8000
```

Contoh:

```text
http://192.168.1.6:8000
```

## Struktur Project

Struktur dasar project:

```text
sentikampus_api/
├── app/
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Menghentikan Server

Untuk menghentikan server FastAPI:

```text
Ctrl + C
```

Untuk keluar dari virtual environment:

```bash
deactivate
```

## Alur Menjalankan Project

Setelah repository sudah di-clone, langkah singkatnya:

```bash
cd sentikampus_api

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Kemudian buka:

```text
http://127.0.0.1:8000/docs
```

API SentiKampus siap digunakan.

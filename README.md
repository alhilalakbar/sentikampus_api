# SentiKampus API

Backend API untuk aplikasi **SentiKampus** yang digunakan untuk melakukan prediksi sentimen menggunakan **FastAPI**.

## Teknologi

- Python
- FastAPI
- Uvicorn
- Pydantic
- REST API

## Persyaratan

Sebelum menjalankan project, pastikan sudah terinstall:

- Python 3.10 atau lebih baru
- pip
- Git
- Visual Studio Code

### Cek Python

**Windows:**

```powershell
py --version
```

**Linux / macOS:**

```bash
python3 --version
```

### Cek pip

**Windows:**

```powershell
pip --version
```

**Linux / macOS:**

```bash
pip3 --version
```

### Cek Git

```bash
git --version
```

---

## 1. Clone Repository

Clone repository:

```bash
git clone git@github.com:alhilalakbar/sentikampus_api.git
```

Atau menggunakan HTTPS:

```bash
git clone https://github.com/alhilalakbar/sentikampus_api.git
```

Masuk ke folder project:

```bash
cd sentikampus_api
```

Jika menggunakan VS Code:

```bash
code .
```

---

## 2. Membuat Virtual Environment

Virtual environment digunakan agar dependency Python project terpisah dari instalasi Python utama pada komputer.

### Windows

Sesuai langkah praktikum:

```powershell
py -m venv .venv
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Setelah selesai, folder `.venv` akan dibuat di dalam project.

---

## 3. Mengaktifkan Virtual Environment

### Windows

```powershell
.venv\Scripts\activate
```

Jika berhasil, akan muncul:

```text
(.venv)
```

di depan terminal.

Contoh:

```text
(.venv) PS D:\FlutterProject\sentikampus_api>
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Jika berhasil:

```text
(.venv) hillal@computer:~/sentikampus_api$
```

---

## 4. Install Dependency

Pastikan virtual environment sudah aktif.

Install seluruh dependency dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

Dependency utama project:

```text
fastapi
uvicorn[standard]
pydantic
```

Untuk memastikan FastAPI sudah terinstall:

```bash
pip show fastapi
```

---

## 5. Struktur Backend

Struktur backend:

```text
sentikampus_api/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── requirements.txt
└── README.md
```

Folder `.venv` digunakan untuk environment lokal dan tidak perlu di-upload ke GitHub.

Pastikan `.gitignore` memiliki:

```gitignore
.venv/
__pycache__/
*.pyc
```

---

## 6. Menjalankan FastAPI

Pastikan virtual environment masih aktif.

Jalankan:

```bash
uvicorn app.main:app --reload
```

Jika berhasil, server berjalan pada:

```text
http://127.0.0.1:8000
```

**Jangan tutup terminal tersebut** selama FastAPI masih digunakan.

---

## 7. Membuka Dokumentasi API

Buka browser dan akses:

```text
http://127.0.0.1:8000/docs
```

FastAPI akan menampilkan **Swagger UI**.

Swagger dapat digunakan untuk mencoba endpoint API secara langsung.

---

## 8. Menguji Health API

Pada Swagger UI, cari:

```text
GET /health
```

Klik:

```text
Try it out → Execute
```

Response yang diharapkan:

```json
{
  "status": "ok"
}
```

Jika response tersebut muncul, berarti FastAPI sudah berjalan dengan baik.

---

## 9. Menguji Prediksi Sentimen

Endpoint prediksi:

```text
POST /api/v1/predict
```

Pada Swagger:

1. Buka `POST /api/v1/predict`
2. Klik **Try it out**
3. Masukkan:

```json
{
  "text": "Pelayanan lambat"
}
```

4. Klik **Execute**

Response:

```json
{
  "label": "negative",
  "score": 0.91
}
```

Jika response tersebut muncul, berarti endpoint prediksi berhasil.

---

## 10. Validasi Input

API memiliki validasi panjang teks.

Teks harus memiliki:

- Minimal **3 karakter**
- Maksimal **500 karakter**

Contoh input yang tidak valid:

```json
{
  "text": "A"
}
```

Input tersebut akan menghasilkan error HTTP:

```text
422 Unprocessable Entity
```

---

## 11. Menjalankan API untuk Flutter

Alamat API bergantung pada tempat Flutter dijalankan.

### Browser pada komputer yang sama

Gunakan:

```text
http://127.0.0.1:8000
```

### Android Emulator

Gunakan:

```text
http://10.0.2.2:8000
```

### HP Android fisik

Gunakan IP komputer yang menjalankan FastAPI.

Contoh:

```text
http://192.168.1.10:8000
```

HP dan komputer harus berada pada jaringan yang dapat saling mengakses.

Jika API perlu diakses dari perangkat lain dalam jaringan lokal, jalankan:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 12. Endpoint API

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Prediksi Sentimen

```http
POST /api/v1/predict
```

Request:

```json
{
  "text": "Pelayanan lambat"
}
```

Response:

```json
{
  "label": "negative",
  "score": 0.91
}
```

---

## 13. Menghentikan FastAPI

Untuk menghentikan server:

```text
Ctrl + C
```

---

## 14. Menonaktifkan Virtual Environment

Setelah selesai menggunakan project:

```bash
deactivate
```

---

## 15. Menjalankan Project Kembali

Jika project sudah pernah di-setup sebelumnya, tidak perlu membuat virtual environment baru.

### Windows

```powershell
cd sentikampus_api
.venv\Scripts\activate
uvicorn app.main:app --reload
```

### Linux / macOS

```bash
cd sentikampus_api
source .venv/bin/activate
uvicorn app.main:app --reload
```

Kemudian buka:

```text
http://127.0.0.1:8000/docs
```

---

## 16. Troubleshooting

### `uvicorn` tidak ditemukan

Pastikan virtual environment sudah aktif.

Kemudian jalankan:

```bash
pip install -r requirements.txt
```

Atau:

```bash
python -m uvicorn app.main:app --reload
```

---

### `/docs` tidak dapat dibuka

Pastikan FastAPI masih berjalan:

```bash
uvicorn app.main:app --reload
```

Kemudian buka:

```text
http://127.0.0.1:8000/docs
```

---

### Flutter tidak dapat terhubung ke FastAPI

Periksa secara berurutan:

1. Pastikan FastAPI masih berjalan:

```bash
uvicorn app.main:app --reload
```

2. Pastikan `/docs` dapat dibuka:

```text
http://127.0.0.1:8000/docs
```

3. Periksa `baseUrl` Flutter.

Android Emulator:

```text
http://10.0.2.2:8000
```

HP Android:

```text
http://IP-KOMPUTER:8000
```

4. Pastikan endpoint benar:

```text
/api/v1/predict
```

Contoh untuk Android Emulator:

```text
http://10.0.2.2:8000/api/v1/predict
```

---

# Quick Start

## Windows

```powershell
git clone git@github.com:alhilalakbar/sentikampus_api.git

cd sentikampus_api

py -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Kemudian buka:

```text
http://127.0.0.1:8000/docs
```

## Linux / macOS

```bash
git clone git@github.com:alhilalakbar/sentikampus_api.git

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

---

## Alur Menjalankan Project

```text
Clone Repository
       ↓
Masuk ke Folder Project
       ↓
Buat Virtual Environment
       ↓
Aktifkan Virtual Environment
       ↓
Install Dependency
       ↓
Jalankan FastAPI
       ↓
Buka /docs
       ↓
Tes GET /health
       ↓
Tes POST /api/v1/predict
       ↓
Hubungkan dengan Flutter
```

**SentiKampus API siap digunakan.**

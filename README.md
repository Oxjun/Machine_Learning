# Machine Learning Projects

Repository ini berisi kumpulan proyek Machine Learning yang dikerjakan menggunakan Python. Proyek mencakup proses pengolahan data, eksplorasi data, pembangunan model Machine Learning, evaluasi model, hingga implementasi model untuk melakukan prediksi.

## 📁 Daftar Proyek

### 1. Tugas Car Prices Prediction

Proyek ini bertujuan untuk membangun model Machine Learning yang dapat memprediksi harga mobil berdasarkan karakteristik atau fitur yang tersedia pada dataset.

**Tahapan pengerjaan:**
- Data loading
- Data cleaning dan preprocessing
- Exploratory Data Analysis (EDA)
- Transformasi dan encoding data
- Pembagian data training dan testing
- Pelatihan model regresi menggunakan Gradient Boosting Regressor
- Evaluasi model
- Penyimpanan model menggunakan Joblib dan Pickle
- Implementasi model melalui Flask API
- Pengujian API untuk melakukan prediksi harga mobil
- Pembahasan monitoring model Machine Learning

**Tools yang digunakan:**
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Joblib
- Pickle
- Jupyter Notebook

#### 📊 Sumber Dataset

Dataset yang digunakan dalam proyek Car Prices berasal dari Kaggle.

- **Nama dataset:** Car Prices
- **Platform:** Kaggle
- **Link dataset:** https://www.kaggle.com/competitions/car-prices/data

File Dataset train.csv dan test.csv ini digunakan untuk proses data loading, data cleaning, eksplorasi data, pembangunan model regresi, dan prediksi harga mobil.

#### 🚀 Deployment Model

Model Machine Learning diimplementasikan menggunakan Flask API agar dapat menerima data masukan dan menghasilkan prediksi harga mobil.

File utama yang digunakan:
- `Tugas_car-prices.ipynb` — proses pengolahan data, pelatihan, dan evaluasi model.
- `testing_deploy.py` — implementasi Flask API untuk prediksi.
- `data.json` — contoh data masukan untuk pengujian API.
- `gbr_model.joblib` — model yang disimpan menggunakan Joblib.
- `gbr_model.pkl` — model yang disimpan menggunakan Pickle.
- `content/train.csv` — dataset training.
- `content/test.csv` — dataset testing atau data pengujian sesuai struktur proyek.

Untuk menjalankan API secara lokal, aktifkan virtual environment terlebih dahulu, kemudian jalankan:

```bash
python testing_deploy.py
```

Jika server berhasil berjalan, API dapat diakses melalui:

```text
http://127.0.0.1:5000
```

API tersebut berjalan secara lokal dan belum berarti model sudah di-hosting secara publik.

Contoh pengujian menggunakan cURL:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d @data.json
```

API akan menerima data dalam format JSON dan mengembalikan hasil prediksi harga mobil.

Salah satu hasil pengujian menghasilkan prediksi sekitar `34072.40`. Angka tersebut merupakan contoh hasil prediksi untuk input tertentu, bukan nilai akurasi model.

#### 📈 Monitoring Model

Monitoring model dibahas sebagai bagian dari proses pemeliharaan Machine Learning. Monitoring dapat digunakan untuk mengevaluasi hasil prediksi, mengamati perubahan karakteristik data, dan menentukan apakah model perlu dievaluasi atau dilatih ulang.

Pembahasan monitoring pada proyek ini merupakan gambaran konsep dan belum menunjukkan adanya sistem monitoring otomatis yang berjalan secara terus-menerus.

### 2. Latihan House Prices

Proyek ini berisi latihan pengolahan dan eksplorasi dataset harga rumah menggunakan Python.

**Tahapan pengerjaan:**
- Memuat dataset
- Memeriksa struktur dan tipe data
- Melakukan analisis statistik deskriptif
- Mengidentifikasi nilai yang hilang
- Melakukan data cleaning dan preprocessing
- Mengeksplorasi karakteristik dataset sebagai persiapan analisis Machine Learning

File dan tahapan yang tersedia dapat dilihat pada folder `Latihan_house-prices/`.

**Tools yang digunakan**

Teknologi dan tools yang digunakan dalam repository ini meliputi:

- **Python** — bahasa pemrograman utama.
- **Jupyter Notebook** — lingkungan untuk eksperimen dan dokumentasi analisis.
- **Pandas** — manipulasi dan pengolahan data.
- **NumPy** — operasi numerik.
- **Matplotlib dan Seaborn** — visualisasi data.
- **Scikit-learn** — preprocessing, pelatihan, dan evaluasi model Machine Learning.
- **Flask** — pembuatan API untuk model prediksi.
- **Joblib dan Pickle** — penyimpanan serta pemuatan model.
- **Git dan GitHub** — version control dan penyimpanan repository.

## 💻 Cara Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/Oxjun/Machine_Learning.git
```

### 2. Masuk ke Folder Repository

```bash
cd Machine_Learning
```

### 3. Buat Virtual Environment

```bash
python -m venv .venv
```

Aktifkan virtual environment di Windows:

```bash
.venv\Scripts\activate
```

Di Linux:

```bash
source .venv/bin/activate
```

### 4. Instal Dependensi

Jika tersedia file `requirements.txt`, jalankan:

```bash
pip install -r requirements.txt
```

Jika file tersebut belum tersedia, instal paket yang diperlukan sesuai proyek:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask joblib jupyter
```

### 5. Jalankan Notebook

Buka Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian buka notebook yang ingin dijalankan, misalnya `Tugas_car-prices.ipynb`.

### 6. Jalankan Flask API

Masuk ke folder `Tugas_car-prices`:

```bash
cd Tugas_car-prices
```

Kemudian jalankan:

```bash
python testing_deploy.py
```

Pastikan file model dan file lain yang diperlukan berada pada lokasi yang sesuai dengan path dalam kode program.

## 📌 Catatan

- Hasil prediksi bergantung pada data masukan dan model yang telah dilatih.
- Hasil prediksi untuk satu input tidak dapat dianggap sebagai ukuran akurasi model secara keseluruhan.
- API yang dijalankan melalui `127.0.0.1` hanya dapat diakses dari komputer lokal, kecuali dikonfigurasi untuk deployment eksternal.
- Pembahasan monitoring belum berarti sistem monitoring otomatis telah diterapkan.
- Dataset dan struktur file harus sesuai dengan kebutuhan kode pada masing-masing proyek.

## 👨‍💻 Author

**Oxjun**

GitHub: https://github.com/Oxjun

Repository: https://github.com/Oxjun/Machine_Learning

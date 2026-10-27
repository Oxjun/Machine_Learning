# Machine Learning 

Repository ini berisi kumpulan proyek Machine Learning yang dikerjakan menggunakan Python. Proyek mencakup proses pengolahan data, eksplorasi data, pembangunan model Machine Learning, evaluasi model, hingga implementasi model untuk melakukan prediksi.

## Struktur Repository

```text
Machine_Learning/
├── Latihan_house-prices/
│   ├── content/
│   └── Latihan.ipynb
│
├── Tugas_car-prices/
│   ├── content/
│   │   ├── train.csv
│   │   └── test.csv
│   ├── data.json
│   ├── gbr_model.joblib
│   ├── gbr_model.pkl
│   ├── testing_deploy.py
│   └── Tugas_car-prices.ipynb
│
├── .gitignore
└── README.md
```

**Catatan:** Folder `.venv` tidak disertakan dalam repository karena telah diatur dalam `.gitignore`. Virtual environment dan library dapat dibuat atau diinstal kembali pada komputer pengguna.

## Daftar Proyek

### 1. Tugas Car Prices Prediction

Proyek ini bertujuan untuk membangun model Machine Learning yang dapat memprediksi harga mobil berdasarkan karakteristik atau fitur yang tersedia pada dataset.

**Tahapan pengerjaan:**
- Data loading
- Data cleaning dan preprocessing
- Exploratory Data Analysis (EDA)
- Transformasi dan encoding data
- Pembagian data training dan testing
- Pelatihan model regresi menggunakan LARS, Linear Regression, dan Gradient Boosting Regressor
- Evaluasi dan perbandingan performa model
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

#### Sumber Dataset

Dataset yang digunakan dalam proyek Car Prices berasal dari Kaggle.

- **Nama dataset:** Car Prices
- **Platform:** Kaggle
- **Link dataset:** https://www.kaggle.com/competitions/car-prices/data

File dataset `train.csv` dan `test.csv` digunakan untuk proses data loading, data cleaning, eksplorasi data, pembangunan model regresi, dan prediksi harga mobil.

#### Evaluasi Model

Evaluasi dilakukan dengan membandingkan tiga model regresi, yaitu LARS, Linear Regression, dan Gradient Boosting Regressor. Metrik yang digunakan adalah Mean Absolute Error (MAE), Mean Squared Error (MSE), dan R² Score.

**Hasil evaluasi model:**

| Model | MAE | MSE | R² Score |
|---|---:|---:|---:|
| LARS | 12.192,26 | 254.757.100 | 0,4410 |
| Linear Regression | 10.719,67 | 202.967.700 | 0,5546 |
| Gradient Boosting Regressor | 9.377,33 | 171.404.500 | 0,6239 |

*Catatan: Nilai MSE ditampilkan dalam bentuk pembulatan dari hasil evaluasi notebook.*

**Interpretasi hasil evaluasi:**

- **MAE (Mean Absolute Error):** Mengukur rata-rata selisih absolut antara harga aktual dan harga prediksi. Semakin kecil nilainya, semakin baik performa model. Gradient Boosting Regressor memperoleh MAE sebesar 9.377,33, paling rendah di antara ketiga model.
- **MSE (Mean Squared Error):** Mengukur rata-rata kuadrat kesalahan prediksi sehingga kesalahan yang besar mendapat penalti lebih tinggi. Semakin kecil nilainya, semakin baik. Gradient Boosting Regressor memperoleh MSE sekitar 171.404.500, paling rendah di antara ketiga model.
- **R² Score (Coefficient of Determination):** Mengukur seberapa baik model menjelaskan variasi harga pada data uji. Nilai idealnya adalah 1. Gradient Boosting Regressor memperoleh R² sebesar 0,6239 atau sekitar 62,39%.

**Apakah MAE, MSE, dan R² sudah mendekati angka 1?**

MAE dan MSE tidak perlu mendekati angka 1 karena keduanya bergantung pada skala harga mobil dan satuan target yang digunakan. Penilaiannya berfokus pada seberapa kecil nilai kesalahannya dibandingkan model lain atau baseline yang sesuai.

Berbeda dengan kedua metrik tersebut, R² memiliki nilai ideal 1. Nilai 0,6239 menunjukkan bahwa Gradient Boosting Regressor mampu menjelaskan sekitar 62,39% variasi harga pada data uji. Hasil ini lebih baik dibandingkan LARS dan Linear Regression, tetapi masih memiliki ruang untuk peningkatan.

Berdasarkan ketiga metrik tersebut, **Gradient Boosting Regressor merupakan model terbaik di antara model yang diuji**, karena menghasilkan MAE dan MSE terendah serta R² tertinggi. Namun, hasil ini tidak berarti model sudah sempurna atau seluruh prediksinya akurat.

#### Referensi Evaluasi Model

Referensi ini digunakan sebagai landasan teori untuk memahami evaluasi model regresi, pemilihan model Machine Learning, serta metode Gradient Boosting Regressor.

1. **Emmert-Streib, F., & Dehmer, M. (2019).** *Evaluation of Regression Models: Model Assessment, Model Selection and Generalization Error.* Machine Learning and Knowledge Extraction, 1(1), 521–551.  
   DOI: https://doi.org/10.3390/make1010032  
   Relevansi: Membahas evaluasi dan pemilihan model regresi, generalization error, serta metode untuk menilai performa model.

2. **Chicco, D., Warrens, M. J., & Jurman, G. (2021).** *The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation.* PeerJ Computer Science, 7, e623.  
   DOI: https://doi.org/10.7717/peerj-cs.623  
   Relevansi: Membahas perbandingan metrik evaluasi regresi, termasuk MAE, MSE, dan R², serta interpretasi hasil evaluasinya.

3. **Friedman, J. H. (2001).** *Greedy function approximation: A gradient boosting machine.* The Annals of Statistics, 29(5), 1189–1232.  
   DOI: https://doi.org/10.1214/aos/1013203451  
   Relevansi: Menjelaskan dasar metode Gradient Boosting yang berkaitan dengan model terbaik pada proyek prediksi harga mobil ini.

#### Deployment Model

Model Machine Learning diimplementasikan menggunakan Flask API agar dapat menerima data masukan dan menghasilkan prediksi harga mobil.

File utama yang digunakan:
- `Tugas_car-prices.ipynb` — proses pengolahan data, pelatihan, dan evaluasi model.
- `testing_deploy.py` — implementasi Flask API untuk prediksi.
- `data.json` — contoh data masukan untuk pengujian API.
- `gbr_model.joblib` — model yang disimpan menggunakan Joblib.
- `gbr_model.pkl` — model yang disimpan menggunakan Pickle.
- `content/train.csv` — dataset training.
- `content/test.csv` — dataset pengujian sesuai struktur proyek.

Untuk menjalankan API secara lokal, aktifkan virtual environment terlebih dahulu, kemudian jalankan:

```bash
python testing_deploy.py
```

Jika server berhasil berjalan, API dapat diakses melalui:

```text
http://127.0.0.1:5000
```

API tersebut berjalan secara lokal dan belum berarti model sudah di-hosting secara publik.

Contoh pengujian menggunakan cURL di Windows PowerShell:

```powershell
curl.exe -X POST http://127.0.0.1:5000/predict `
  -H "Content-Type: application/json" `
  --data-binary "@data.json"
```

API akan menerima data dalam format JSON dan mengembalikan hasil prediksi harga mobil.

Salah satu hasil pengujian menghasilkan prediksi sekitar `34072.40`. Angka tersebut merupakan contoh hasil prediksi untuk input tertentu, bukan nilai akurasi model.

#### Monitoring Model

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

## Teknologi dan Tools

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

## Cara Menjalankan Proyek

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

```powershell
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

Kemudian buka notebook yang ingin dijalankan, misalnya `Tugas_car-prices.ipynb` di folder `Tugas_car-prices/`.

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
- Hasil prediksi untuk satu input tidak dapat dianggap sebagai ukuran performa model secara keseluruhan.
- MAE dan MSE dinilai semakin baik ketika nilainya semakin kecil, sedangkan R² idealnya mendekati 1.
- API yang dijalankan melalui `127.0.0.1` hanya dapat diakses dari komputer lokal, kecuali dikonfigurasi untuk deployment eksternal.
- Pembahasan monitoring belum berarti sistem monitoring otomatis telah diterapkan.
- Dataset dan struktur file harus sesuai dengan kebutuhan kode pada masing-masing proyek.

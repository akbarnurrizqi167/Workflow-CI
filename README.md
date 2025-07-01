# 🔁 Workflow CI – ML Project Automation (Dicoding MSML Submission)

Repositori ini merupakan bagian dari submission Proyek Akhir pada kelas **Membangun Sistem Machine Learning** dari Dicoding. Fokus utama dari repositori ini adalah implementasi **Continuous Integration (CI)** menggunakan **MLflow Projects** dan **GitHub Actions** untuk otomatisasi pelatihan model Machine Learning.

---

## 🎯 Tujuan Proyek

- Mengimplementasikan workflow otomatis yang mampu menjalankan ulang pelatihan model setiap kali terdapat perubahan pada dataset atau skrip pelatihan.
- Menyimpan artefak model hasil pelatihan secara otomatis ke dalam repositori GitHub.
- Mengadopsi prinsip MLOps dalam pengembangan dan pemeliharaan sistem machine learning yang andal dan terotomatisasi.

---

## 🧩 Komponen Utama

- **MLflow Project**: Mendefinisikan struktur eksperimen, dependensi, dan entry point pelatihan model.
- **GitHub Actions**: Menjalankan pelatihan model secara otomatis saat ada perubahan pada direktori `MLProject/`.
- **Environment Conda**: Menjamin kesesuaian dependensi dengan menjalankan training pada lingkungan yang terisolasi.
- **Dataset Preprocessing**: Dataset yang telah diproses pada tahap eksperimen digunakan ulang dalam CI untuk menjamin konsistensi.

---

## 📝 Hasil Review Dicoding

**Status Kriteria 3: Skilled ✅**

> Reviewer menyatakan bahwa sistem CI telah berhasil dijalankan dengan baik menggunakan MLflow Projects dan GitHub Actions. Pelatihan model dilakukan secara otomatis saat terjadi perubahan pada struktur proyek.

**Catatan Reviewer untuk Upgrade ke Advanced:**

- Workflow belum menerapkan *Docker Image building* dan *push* otomatis ke Docker Hub.
- Belum terdapat perintah `mlflow models build-docker` serta proses login dan upload image ke Docker melalui GitHub Actions.

> 🔄 Dengan menambahkan pipeline Docker dan integrasi Docker Hub, proyek ini dapat memenuhi syarat untuk dinilai sebagai **Advanced (4 poin)**.

---

## 🛠 Teknologi yang Digunakan

- **Python 3.10**
- **MLflow Projects**
- **GitHub Actions**
- **Conda Environment**
- **Dataset Telco Customer Churn (Kaggle)**

---

## 🧾 Kesimpulan

Proyek ini telah berhasil membangun sistem CI untuk pelatihan model ML berbasis MLflow yang dapat dijalankan secara otomatis melalui GitHub Actions. Struktur yang rapi dan standar penulisan yang baik memudahkan pengembangan dan pelacakan eksperimen. Repositori ini menjadi dasar kuat untuk pengembangan lebih lanjut dengan integrasi Docker dan CD.


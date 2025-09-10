# Adidos — PBP Django (MTV)

**Tautan Aplikasi PWS:** 
https://galih-nur41-adidos.pbp.cs.ui.ac.id

---

## 1) Step-by-step yang saya lakukan

1. **Menyiapkan ruang kerja proyek**

   * Membuat folder proyek lalu inisialisasi git.
   * Membuat *virtual environment* agar dependensi terisolasi.

2. **Mengatur dependensi**

   * Membuat `requirements.txt`, mengisi hal-hal yang dibutuhkan dan menginstallnya

3. **Membuat proyek Django**

   * Membuat project Django dengan nama `adidos` 

4. **Menyesuaikan `settings.py` untuk pengembangan**

   * Menambahkan `localhost` dan `127.0.0.1` pada `ALLOWED_HOSTS`.

5. **Membuat aplikasi `main`**

   * Menambahkan `'main'` ke `INSTALLED_APPS`.
   * Membuat folder templates di dalam `main` dan menambahkan file `main.html` sebagai halaman awal di web.
   * Membuat file `views.py` di dalam `main` dan membuat fungsi `show_main` untuk merender html nya
   * Membuat file `urls.py` di dalam folder project `adidos` dan juga `main` dan melakukan routing.

6. **Model awal**

   * Di dalam file `models.py`, saya membuat class `Product` dengan atribut-atribut yang sesuai pada ketentuan soal.

7. **Migrasi**

   * Menjalankan migrasi.

8. **Integrasi Git & GitHub**

   * Inisialisasi repo, commit, dan push di github saya.

10. **Deploy ke Pacil Web Service (PWS)**

    * Menyesuaikan `ALLOWED_HOSTS` agar memuat domain PWS dan melakukan migrate di lingkungan PWS jika diperlukan oleh pipeline.
    * Deploy ke PWS

---

## 2) Bagan alur request–response Django (MTV)

Bagan : https://drive.google.com/file/d/1jAUUMYYMUqVvlWSDVirFODL402E1ik3j/view?usp=sharing

**Kaitan komponen:**

* `urls.py` (project) meneruskan pola URL ke `urls.py` milik app.
* `urls.py` (app) menentukan fungsi view mana yang dieksekusi.
* `views.py` mengambil/menulis data via `models.py` (ORM) ke database.
* `views.py` merender `templates/*.html` dan mengembalikan `HttpResponse` ke klien.

---

## 3) Peran `settings.py` dalam proyek Django

`settings.py` adalah pusat konfigurasi proyek django, berfungsi sebagai pusat kendali yang memungkinkan developer untuk menyesuaikan perilaku proyek sesuai kebutuhan, dengan mengatur parameter yang digunakan oleh berbagai bagian dari aplikasi web Django.

---

## 4) Cara kerja migrasi database di Django

1. Mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru kamu.
2. Menjalankan `makemigrations`, menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.
3. Menjalankan `migrate`, mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.

---

## 5) Kenapa Django cocok sebagai permulaan belajar pengembangan perangkat lunak?

* Sintaks python mudah dipelajari
* Dokumentasi yang sangat baik
* Komunitas besar dan aktif
* Fitur bawaan lengkap
* Fleksibel

---

## 6) Feedback singkat untuk asisten dosen (Tutorial 1)

* Asisten dosen membantu saya menyelesaikan masalah `TemplateDoesNotExist`

---

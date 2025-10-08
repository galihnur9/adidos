# Adidos — Tugas 6

**Tautan Aplikasi PWS:** 
https://galih-nur41-adidos.pbp.cs.ui.ac.id

---

## 1) Apa perbedaan antara synchronous request dan asynchronous request?

Synchronous request adalah permintaan yang memblokir (pengguna harus menunggu), sedangkan asynchronous request adalah permintaan yang tidak memblokir (pengguna bisa lanjut melakukan hal lain). Analoginya, synchronous request seperti menelepon teman. Kamu akan terus memegang telepon dan menunggu sampai teman kamu menjawab. Kamu tidak bisa melakukan aktivitas lain selama menunggu. Sementara asynchronous request seperti mengirim pesan WhatsApp. Kamu mengirim pesan, lalu bisa langsung menutup aplikasi atau membalas pesan orang lain. Kamu akan mendapatkan notifikasi nanti ketika pesan kamu sudah dibalas.

---

## 2) Bagaimana AJAX bekerja di Django (alur request–response)?

AJAX di Django bekerja dengan JavaScript di browser yang mengirim permintaan ke URL Django khusus di latar belakang, lalu view Django merespons dengan data (biasanya JSON) alih-alih halaman HTML lengkap. JavaScript kemudian menggunakan data ini untuk memperbarui tampilan tanpa perlu me-reload halaman.

---

## 3) Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

Keuntungan utama menggunakan AJAX dibandingkan render biasa di Django adalah untuk menciptakan pengalaman pengguna (UX) yang jauh lebih cepat, mulus, dan interaktif karena halaman tidak perlu di-reload sepenuhnya untuk setiap aksi.
Berikut perbandingan singkat antara render biasa dengan AJAX
| Aspek | Render Biasa (Full Reload) | AJAX (Asynchronous) |
| :--- | :--- | :--- |
| **Pengalaman Pengguna** | Terputus-putus, harus menunggu | Mulus, cepat, dan interaktif |
| **Data yang Dikirim** | Seluruh halaman HTML | Hanya data yang dibutuhkan (JSON) |
| **Beban Server** | Lebih berat (*template rendering*) | Lebih ringan (hanya serialisasi data) |
| **Contoh Fitur** | Navigasi antar halaman statis | Tombol "Like", *chat*, *infinite scroll* |

---

## 4) Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

Caranya adalah sebagai berikut:
1. Mengimplementasikan HTTPS
Mengenkripsi semua data yang dikirim antara browser dan server untuk mencegah penyadapan username dan password di tengah jalan (Man-in-the-Middle attack).
2. Memanfaatkan proteksi CSRF bawaan Django
Memastikan bahwa permintaan untuk mengubah data (seperti login atau register) benar-benar berasal dari situs kamu, bukan dipicu oleh situs jahat lain, dengan mewajibkan pengiriman token rahasia yang unik di setiap request.
3. Melakukan validasi data di sisi server secara ketat
Memverifikasi ulang semua data yang diterima dari pengguna di backend untuk memastikan integritas dan keamanannya, karena validasi di frontend (JavaScript) dapat dengan mudah dilewati oleh penyerang.
4. Menangani error dengan aman
Memberikan pesan error yang generik (misalnya, "Username atau password tidak valid") untuk mencegah penyerang mengidentifikasi username mana yang valid dan terdaftar di sistem Anda (user enumeration).
5. Melindungi dari serangan brute-force
Membatasi jumlah percobaan login yang gagal dari satu alamat IP atau untuk satu akun dalam periode waktu tertentu, guna menghentikan skrip otomatis yang mencoba menebak password secara berulang-ulang.
6. Cegah XSS
Memperlakukan semua input dari pengguna sebagai teks biasa (bukan kode) saat menampilkannya kembali di halaman. Ini mencegah penyerang menyuntikkan skrip berbahaya yang dapat mencuri data pengguna lain.

---

## 5) Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

AJAX (Asynchronous JavaScript and XML) secara fundamental meningkatkan user experience (UX) dengan membuat website terasa lebih cepat, responsif, dan interaktif seperti aplikasi desktop, terutama dengan menghilangkan kebutuhan untuk memuat ulang (reload) seluruh halaman.

---
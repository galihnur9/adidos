# Adidos — Tugas 3

**Tautan Aplikasi PWS:** 
https://galih-nur41-adidos.pbp.cs.ui.ac.id

---

## 1) Step-by-step yang saya lakukan

1. **Membuat Fungsi Form dan Registrasi**

   * Menambahkan fungsi register di dalam `views.py`, dan menggunakan `UserCreationForm` yang telah diimpor
   * Membuat berkas baru dengan nama `register.html` pada direktori `main/templates`, lalu dirouting ke halaman register di `urls.py`

2. **Membuat Fungsi Login**

   * Menambahkan fungsi login_user di dalam `views.py`, dan menggunakan `AuthenticationForm` yang telah diimpor
   * Membuat berkas baru dengan nama `login.html` pada direktori `main/templates`, lalu dirouting ke halaman register di `urls.py`

3. **Membuat Fungsi Logout**

   * Menambahkan fungsi logout_user di dalam `views.py`
   * Update berkas `main.html` untuk menambahkan tombol logout
   * Update berkas `urls.py` agar dapat mengakses fungsi tersebut

4. **Merestriksi Akses Halaman Main dan News Detail**

   * Menambah potongan kode `@login_required(login_url='/login')` di atas fungsi `show_main` dan `show_product`, agar halaman utama dan product detail hanya dapat diakses oleh user yang sudah login

5. **Menggunakan Data dari Cookies**

   * Menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas `views.py`
   * Mengubah bagian kode `login_user` untuk menyimpan cookie baru bernama `last_login`
   * Update fungsi `show_main` dengan menambahkan potongan kode `'last_login': request.COOKIES['last_login']`
   * Ubah fungsi `logout_user` untuk menghapus cookie `last_login` setelah melakukan logout
   * Menambahkan parameter `last_login` dan `username` yang sekarang sedang login di berkas `main.html` di direktori `main/templates`

6. **Menghubungan Model Product dengan User**

   * Menambahkan potongan kode `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)` di `models.py` pada subdirektori `main`, agar dapat menghubungkan satu news dengan satu user melalui sebuah relationship
   * Modifikasi fungsi `create_product` dan `show_main` di `views.py` pada subdirektori `main`
   * Menambahkan tombol filter My dan All pada halaman `main.html` dan menampilkan nama author di `product_detail.html`

---

## 2) Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya

`AuthenticationForm` adalah kelas formulir bawaan Django yang digunakan untuk mengautentikasi pengguna dengan memvalidasi nama pengguna (atau email) dan kata sandi. Formulir ini merupakan bagian dari sistem autentikasi Django yang sudah teruji dan aman, dan dapat digunakan langsung untuk membuat tampilan login tanpa perlu mengimplementasikan logika validasi dari nol.
Kelebihan :
1. Cepat dan mudah digunakan
2. Keamanan bawaan
3. Terintegrasi penuh dengan ekosistem Django
Kekurangan :
1. Kurang fleksibel untuk login selain username
2. Kustomisasi tampilan lumayan sulit
3. Tidak cocok untuk alur autentikasi kompleks

---

## 3) Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses verifikasi "Siapa kamu", sedangkan otorisasi adalah proses verifikasi "Apa yang boleh kamu lakukan"
Autentikasi di Django :
1. Model User: Django menyediakan model User bawaan yang memiliki field penting seperti username, password, email, first_name, dan last_name.
2. Framework Autentikasi: Django memiliki serangkaian fungsi untuk mengelola siklus hidup login pengguna.
- `authenticate(request, username='...', password='...')`: Fungsi ini memeriksa kredensial terhadap database. Jika berhasil, fungsi ini mengembalikan objek user. Jika gagal, akan mengembalikan None.
- `login(request, user)`: Fungsi ini mengambil objek request dan objek user (dari authenticate) lalu membuat sesi (session) untuk pengguna tersebut di browser.
- `logout(request)`: Menghapus data sesi pengguna, sehingga pengguna keluar dari sistem.
3. Formulir Bawaan: Seperti AuthenticationForm untuk proses login dan UserCreationForm untuk registrasi, yang menyederhanakan proses pengambilan dan validasi input dari pengguna.
4. Middleware: SessionMiddleware dan AuthenticationMiddleware bekerja sama untuk mengaitkan sesi dengan request dan menambahkan objek user ke setiap objek request (request.user) setelah pengguna login.
Otorisasi di Django :
1. Izin Bawaan (Default Permissions): Saat Anda membuat sebuah model, Django secara otomatis menciptakan empat izin dasar: add, change, view, dan delete. Contoh: untuk model Article, akan ada izin blog.add_article, blog.change_article, dll.
2. Grup (Groups): Untuk mempermudah pengelolaan, Anda bisa membuat grup dan memberikan serangkaian izin ke grup tersebut.
3. Pemeriksaan Izin: Django menyediakan beberapa cara untuk memeriksa otorisasi pengguna sebelum mengizinkan sebuah aksi:
- Decorator di Views
- Mixin di Class-Based Views
- Pemeriksaan Manual

---

## 4) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web? 

Kelebihan Session (server-side)
1. Lebih aman, Data sebenarnya (misalnya, user_id, is_admin, isi keranjang belanja) disimpan di server.
2. Kapasitas penyimpanan lebih besar, karena data disimpan di server, batas penyimpanannya jauh lebih besar daripada cookie.
Kekurangan Session (server-side)
1. Skalabilitas Lebih Rumit, dalam lingkungan dengan banyak server (load balancing), pengelolaan sesi menjadi tantangan.
2. Beban pada Memori Server, setiap sesi pengguna yang aktif akan menggunakan memori atau penyimpanan di server.

Kelebihan Cookie (client-side)
1. Beban Server Ringan, karena data disimpan di sisi klien, server tidak perlu mengalokasikan memori untuk menyimpan informasi state pengguna
2. Implementasi Sederhana, sangat mudah untuk dibuat dan digunakan untuk menyimpan data sederhana
Kekurangan Cookie (clinet-side)
1. Tidak Aman, data disimpan dalam bentuk teks biasa di browser pengguna. Siapa pun yang memiliki akses fisik ke komputer atau melalui serangan Cross-Site Scripting (XSS) dapat membaca atau memodifikasi isinya.
2. Ukuran Terbatas, sebagian besar browser membatasi ukuran cookie hingga sekitar 4KB. Ini membuatnya tidak cocok untuk menyimpan data yang kompleks atau besar.

---

## 5) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak, penggunaan cookies tidak aman secara default. Sebaliknya, cookies secara inheren rentan terhadap beberapa serangan jika tidak dikelola dengan benar, karena data disimpan dan dikirim dari sisi klien (browser).
Risiko Potensial yang Harus Diwaspadai :
1. Cross-Site Scripting (XSS)
Ini adalah serangan di mana penyerang berhasil menyuntikkan skrip berbahaya (biasanya JavaScript) ke dalam halaman web yang dilihat oleh pengguna lain.
2. Cross-Site Request Forgery (CSRF)
Ini adalah serangan yang menipu pengguna yang sudah terautentikasi untuk melakukan tindakan yang tidak diinginkan di sebuah aplikasi web.

Bagaimana Django Mengamankan Penggunaan Cookies :
1. Perlindungan Terhadap CSRF: CsrfViewMiddleware
Django memiliki sistem pertahanan CSRF yang sangat efektif dan aktif secara default.
Cara Kerja:
- Django mengirimkan cookie CSRF dengan token rahasia yang acak ke pengguna.
- Saat me-render formulir HTML melalui {% csrf_token %}, Django menyisipkan input tersembunyi yang berisi nilai token yang sama.
- Ketika formulir dikirim (POST), Django akan memverifikasi bahwa token dari cookie cocok dengan token dari input tersembunyi.
Hasilnya, penyerang dari situs lain tidak akan tahu nilai token rahasia ini, sehingga setiap upaya pemalsuan permintaan akan gagal karena validasi token tidak cocok.
2. Perlindungan Terhadap XSS: Atribut HttpOnly
Ini adalah pertahanan utama terhadap pencurian cookie melalui XSS.
Cara Kerja: Django mengatur atribut HttpOnly menjadi True pada cookie sesinya secara default. Atribut ini memberitahu browser bahwa cookie tersebut tidak boleh diakses oleh skrip sisi klien (JavaScript).
Hasilnya, sekalipun penyerang berhasil menyuntikkan skrip jahat ke halaman Anda, skrip tersebut tidak akan bisa membaca cookie sesi, sehingga pembajakan sesi dapat dicegah. Anda dapat mengontrol ini melalui pengaturan SESSION_COOKIE_HTTPONLY.
3. Perlindungan Tambahan
- Atribut secure, memastikan cookie hanya dikirim melalui koneksi HTTPS yang terenkripsi, melindunginya dari penyadapan di jaringan yang tidak aman (Man-in-the-Middle attack).
- Atribut SameSite, memberikan lapisan pertahanan tambahan terhadap CSRF dengan mengontrol kapan cookie dikirim bersama permintaan lintas situs (cross-site).

---
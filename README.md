# Adidos — Tugas 5

**Tautan Aplikasi PWS:** 
https://galih-nur41-adidos.pbp.cs.ui.ac.id

---

## 1) Step-by-step yang saya lakukan

1. **Menambahkan Tailwind ke Aplikasi**

   * Tambahkan script cdn tailwind di bagian head di dalam `templates/base.html`.

2. **Menambahkan Fitur Edit Product dan Hapus Product**

   * Menambahkan fungsi `edit_product` dan `delete_product`  di dalam `views.py`
   * Membuat berkas baru dengan nama `edit_product.html` pada direktori `main/templates`
   * Menambahkan path url keduanya di `urls.py`

3. **Menambahkan Navigation Bar**

   * Membuat berkas baru bernama `navbar.html` pada folder `templates/` di root directory
   * Menautkan navbar tersebut ke dalam `main.html` dengan menggunakan tag `include`

4. **Konfigurasi Static Files**

   * Menambahkan middleware WhiteNoise pada `settings.py`
   * Konfigurasi variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL agar merujuk
   ke /static root project

5. **Styling dengan Tailwind dengan External CSS dan Inline CSS**

   * Modifikasi `global.css` di `static/css/global.css`, disini web saya menggunakan tema dark and white mirip web Adidas
   * Styling navbar, Menampilkan nama store yaitu Adidos, home, create product, nama username dan logout, dan akan slowly menghilang ketika discroll ke bawah
   * Styling halaman `login.html` dan `register.html` sehingga tema nya menjadi dark and white
   * Styling halaman home bagian menu produk, dengan membuat file `card_product.html` di directory `main/templates`
   * Jika belum ada produk, maka kita tampilkan foto `no_product.png` yang sudah dimasukkan di direktori `static/image`
   * Gunakan `card_product.html` dan gambar `no_product.png` ke dalam `main.html`
   * Saya menggunakan background carousel agar tampilan home utama terlihat menarik saat baru dibuka, referensi gambarnya saya ambil dari https://unsplash.com/
   * Styling halaman detail product, tambahkan tombol Edit dan Delete agar bisa mengimplementasikan fungsi yang sudah dibuat di awal tadi
   * Styling halaman Create Product dan Edit Product

---

## 2) Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Berikut adalah urutan prioritas dari yang paling rendah hingga yang paling tinggi:
1. Selector Universal (*): Ini adalah selector yang paling rendah dalam urutan prioritas dan memiliki nilai specificity 0.
2. Selector Elemen dan Pseudo-elemen: Selector ini memiliki bobot yang rendah, seperti `div`, `p`, atau `h1`, dan nilai specificity-nya adalah 0, 0, 1.
2. Class, Pseudo-class, dan Attribute Selector: Selector ini seperti `.container`, `:hover`, atau `[type="text"]` memiliki nilai specificity 0, 1, 0.
4. ID Selector: ID memiliki bobot yang lebih tinggi dibandingkan class dan elemen. Selector seperti `#header` memiliki nilai specificity 1, 0, 0.
5. Inline Styles: Jika Anda memberikan style langsung pada elemen melalui atribut `style`, seperti `<h1 style="color: red;">`, nilai specificity-nya adalah 1, 0, 0, 0.
6. !important: Meskipun ini bukan bagian dari specificity secara teknis, menambahkan `!important` pada aturan CSS akan mengesampingkan semua aturan lain kecuali inline styles yang juga menggunakan `!important`. Namun, penggunaan `!important` sebaiknya dibatasi karena bisa menyulitkan pemeliharaan kode di masa depan.


---

## 3) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design penting karena memastikan aplikasi web memberikan pengalaman pengguna (user experience) yang optimal di berbagai perangkat dengan ukuran layar berbeda, mulai dari desktop hingga ponsel.
Contoh aplikasi yang sudah menerapkan : https://kompas.com
Saat dibuka di desktop, Kompas.com menampilkan layout multi-kolom dengan banyak berita dan iklan di samping. Namun, saat diakses dari ponsel, layout secara otomatis berubah menjadi satu kolom vertikal. Ukuran font menjadi lebih besar dan mudah dibaca, menu navigasi disembunyikan di dalam ikon "hamburger" (☰), dan gambar menyesuaikan lebar layar. Ini dilakukan karena mayoritas pembaca berita mengaksesnya secara mobile, sehingga pengalaman membaca yang nyaman di perangkat kecil menjadi prioritas utama.
Contoh aplikasi yang belum menerapkan : https://academic.ui.ac.id/
Karena tidak responsif, pengguna di ponsel ngepinch untuk memperbesar (pinch-to-zoom) dan menggeser layar (pan) ke segala arah hanya untuk bisa membaca teks atau mengklik navigasi. Pengalaman ini sangat tidak nyaman dan menunjukkan dengan jelas masalah yang diselesaikan oleh responsive design.


---

## 4) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin adalah ruang transparan di luar border yang berfungsi untuk menciptakan jarak antara elemen tersebut dengan elemen lainnya. Border adalah garis yang mengelilingi konten dan padding, yang bisa diatur ketebalan, gaya, dan warnanya. Sedangkan padding adalah ruang transparan di dalam border yang berfungsi untuk memberi jarak antara border dengan konten di dalamnya.
Cara mengimplementasikan ketiga hal tersebut adalah :
`margin: 10px` untuk memberi jarak 10px dari elemen lain.
`padding: 10px` untuk memberi ruang 10px antara konten dan border.
`border: 1px solid black` untuk membuat garis batas setebal 1px.

---

## 5) Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox digunakan untuk tata letak satu dimensi (baris atau kolom) yang fokus pada penataan konten di dalam sebuah komponen, sedangkan Grid digunakan untuk tata letak dua dimensi (baris dan kolom) yang bertujuan membangun struktur atau kerangka utama halaman web.

---
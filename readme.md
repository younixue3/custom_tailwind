# Custom Tailwind CSS untuk Odoo

## Deskripsi
Modul ini berisi konfigurasi dan komponen Tailwind CSS yang disesuaikan untuk website Trinity Auto. Modul ini menyediakan kelas-kelas utilitas yang konsisten untuk digunakan di seluruh tampilan website dengan dukungan fitur JIT (Just-In-Time) compiler dari Tailwind CSS.

## Fitur
- Konfigurasi Tailwind CSS yang disesuaikan dengan brand Trinity Auto
- Komponen UI yang telah dioptimalkan untuk tampilan responsif
- Prefix `tw-` untuk menghindari konflik dengan gaya CSS lainnya
- Mendukung tampilan untuk berbagai layanan (Automotive, HE, Towing)
- Dukungan penuh untuk Tailwind JIT compiler yang memungkinkan:
  - Generasi CSS yang lebih cepat
  - Ukuran file CSS yang lebih kecil
  - Penggunaan kelas utilitas secara dinamis
  - Mode pengembangan yang lebih responsif
- Fitur-fitur Tailwind CSS yang tersedia:
  - Utility-first CSS framework
  - Responsive design dengan breakpoints yang mudah dikustomisasi
  - Dark mode support
  - Custom animations dan transitions
  - Flexbox dan Grid system yang powerful
  - Spacing dan sizing yang konsisten
  - Typography utilities yang lengkap
  - Custom variants dan plugins

## Proses Instalasi

### Requirements
- Node.js (versi 16 atau lebih baru)
- npm atau yarn

### Instalasi di Ubuntu

1. **Buat folder custom_addons dan masuk ke dalamnya**
   ```bash
   mkdir -p /path/to/odoo/custom_addons
   cd /path/to/odoo/custom_addons
   ```

2. **Clone repositori ini ke direktori addons Odoo**
   ```bash
   git clone https://github.com/younixue3/custom_tailwind.git
   ```

3. **Masuk ke direktori modul**
   ```bash
   cd custom_tailwind
   ```

4. **Instal dependensi Node.js**
   ```bash
   npm install
   # atau jika menggunakan yarn
   yarn install
   ```

5. **Buat file konfigurasi Tailwind CSS**
   ```bash
   npx tailwindcss init
   ```

6. **Tambahkan path modul ke file konfigurasi Odoo (odoo.conf)**
   ```ini
   [options]
   addons_path = /path/to/odoo/addons,/path/to/odoo/custom_addons
   ```

7. **Restart server Odoo**
   ```bash
   sudo systemctl restart odoo
   ```

8. **Aktifkan modul melalui Aplikasi Odoo**
   - Masuk ke Odoo dengan akun admin
   - Buka menu Aplikasi
   - Cari "Custom Tailwind"
   - Klik Instal

### Instalasi di Windows

1. **Buat folder custom_addons dan masuk ke dalamnya**
   Buka Command Prompt atau Git Bash, lalu jalankan:
   ```bash
   mkdir C:\path\to\odoo\custom_addons
   cd C:\path\to\odoo\custom_addons
   ```

2. **Clone repositori ini ke direktori addons Odoo**
   ```bash
   git clone https://github.com/younixue3/custom_tailwind.git
   ```

3. **Masuk ke direktori modul**
   ```bash
   cd custom_tailwind
   ```

4. **Instal dependensi Node.js**
   ```bash
   npm install
   # atau jika menggunakan yarn
   yarn install
   ```

5. **Buat file konfigurasi Tailwind CSS**
   ```bash
   npx tailwindcss init
   ```

6. **Tambahkan path modul ke file konfigurasi Odoo (odoo.conf)**
   Buka file odoo.conf dan tambahkan:
   ```ini
   [options]
   addons_path = C:\path\to\odoo\addons,C:\path\to\odoo\custom_addons
   ```

7. **Restart service Odoo**

8. **Aktifkan modul melalui Aplikasi Odoo**
   - Masuk ke Odoo dengan akun admin
   - Buka menu Aplikasi
   - Klik "Update App List"
   - Cari "Custom Tailwind"
   - Klik Instal

## Konfigurasi Tailwind CSS

### File Konfigurasi (tailwind.config.js)

    ```
    /** @type {import('tailwindcss').Config} */
    module.exports = {
    content: ["../../custom_addons/**/*.{html,js,xml}"], // Make sure to include your custom addons' paths here as well
    theme: {
        extend: {},
    },
    plugins: [],
    prefix: "tw-",
    blocklist: ["container", "collapse"], // Add classes to blocklist to avoid generating them
    };
    ```

### Development
Setiap kali melakukan perubahan pada tampilan XML, CSS, atau HTML di website, ikuti langkah berikut:

1. Buka terminal dan navigasikan ke direktori custom_tailwind
2. Jalankan perintah berikut untuk memproses dan memantau perubahan:
    ```bash
    npx tailwindcss -i ./static/src/css/input.css -o ./static/src/css/dist/output.css --watch
    ```
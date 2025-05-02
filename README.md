# Membangun ETL Pipeline Sederhana
## Submission Belajar Fundamental Pemrosesan Data (Dicoding)

Proyek ini merupakan implementasi dari dasar-dasar pemrosesan data dengan Python. Fokus utamanya adalah bagaimana cara mengambil, mengolah, dan menguji data dari berbagai sumber agar siap digunakan untuk keperluan praktis, seperti analisis data atau otomasi sederhana.

# Deskripsi singkat

Tujuan utama proyek ini adalah untuk mendapatkan pemahaman tentang bagaimana data dapat diambil dan dimanipulasi menggunakan Python. Metode-metode ini termasuk teknik scraping data dari web, merapikan data mentah agar lebih terstruktur, dan menambahkan pengujian otomatis untuk memastikan skrip berjalan dengan benar.

# Fitur Utama

beberapa fitur utama seperti:

- Web Scrapping untuk mengumpulkan data secara otomatis dari situs web tertentu, dan kemudian menyusunnya dalam format yang lebih mudah diproses.

- Transformasi Data untuk Mengatur dan memperbaiki data agar siap untuk analisis atau disimpan dalam format yang lebih teratur.

- Unit Testing untuk menyediakan pengujian otomatis untuk memastikan bahwa setiap modul atau fungsi berfungsi dengan baik.

# Cara menjalankan proyek

## Instal dependency

pip install -r requirements.txt

## Buat otomatis requirements

pip freeze > requirements.txt

## Jalanin Skrip

python main.py

## Jalanin unit test yang ada di folder tests

python -m unittest discover tests

## Jalanin test coverage yang ada di folder tests

coverage run -m unittest discover tests

## lihat hasil report

coverage report -m

## Link Google Sheets

<https://docs.google.com/spreadsheets/d/1DlzQ4lWkYNBDnt7nK3rzzbWeetIKqUUaKmt7o1j3xFA/edit?gid=0#gid=0>

![Deskripsi Gambar](https://raw.githubusercontent.com/XzyanQi/Simple-ETL-Pipeline/main/Nilai.jpg)

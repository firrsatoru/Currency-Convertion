# Currency_Converter

Sebuah script Python sederhana untuk mengonversi mata uang menggunakan library `requests` dan API eksternal

## How To Works

Script ini memanfaatkan API untuk mendapatkan nilai tukar terbaru, yang memungkinkan pengguna untuk mengonversi jumlah dari satu mata uang ke mata uang lain berdasarkan data waktu nyata

## Information 

Pastikan kamu sudah menginstal Python dan library `requests` di terminal kamu.

### Installation 

1. **Python 3.x** harus terpasang. Kamu bisa mengecek dengan menjalankan perintah berikut:

    ```bash
    python --version
    ```

2. Instal **requests** menggunakan pip:

    ```bash
    pip install requests
    ```

## Penggunaan

Setelah instalasi selesai, kamu bisa menjalankan script dengan cara berikut:

1. Salin kodenya kedalam file Python `currency_converter.py`:

2. Jalankan script dengan perintah:

    ```bash
    python currency_converter.py
    ```

3. Kamu akan diminta untuk memasukkan mata uang dasar, mata uang target, dan jumlah yang ingin dikonversi. Hasilnya akan ditampilkan di terminal dalam format:

    ```
    100 USD = 1500000.00 IDR
    ```

## Examples Code 

- **`requests.get(url)`**: Melakukan permintaan GET ke URL yang ditentukan untuk mengambil data nilai tukar
- **`data["rates"].get(target_currency)`**: Mengambil nilai tukar untuk mata uang target yang ditentukan dari respons
- **`print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")`**: Menampilkan jumlah yang sudah dikonversi dengan format dua angka desimal

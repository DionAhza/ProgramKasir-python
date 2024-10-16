total = 0
barang = []
harga = []

while True: 
    print("""
Daftar Barang
    1. Roti \t 5000
    2. Es Krim \t 7000
    3. Keripik \t 8000
    4. Coklat \t 12000
    5. Buku \t 10000
    6. Pensil \t 4000
    7. Penghapus \t 3000
    """)

    try:
        kode = int(input("Masukkan Kode Barang : "))
    except ValueError:
        print("Kode harus berupa angka!\n")
        continue

    if kode == 1:
        barang.append('Roti')
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append('Es Krim')
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append('Keripik')
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append('Coklat')
        harga.append(12000)
        total += 12000
    elif kode == 5:
        barang.append('Buku')
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append('Pensil')
        harga.append(4000)
        total += 4000
    elif kode == 7:
        barang.append('Penghapus')
        harga.append(3000)
        total += 3000
    else:
        print("Kode tidak valid!\n")
        continue

    lanjut = input('Lanjut belanja (y/n) : ').lower()
    if lanjut == 'n':
        print("\nDaftar Belanja:")
        for i in range(len(barang)):
            print(f"{i + 1}. {barang[i]} - {harga[i]}")
        print(f"\nTotal harga yang harus dibayar: {total}\n")
        break

while True:
    try:
        uang = int(input('Masukkan uang pembayaran: '))
    except ValueError:
        print("Masukkan jumlah uang yang valid!\n")
        continue

    if uang > total:
        print(f"Kembaliannya: {uang - total}\nTerima kasih telah berbelanja!")
        break
    elif uang == total:
        print("Uangnya pas. Terima kasih telah berbelanja!")
        break
    else:
        print(f"Uangnya kurang {total - uang}. Silakan masukkan jumlah yang tepat.\n")

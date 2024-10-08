total = 0
barang = []
harga = []

while True: 
    print("""Daftar Barang\n
        1. Roti \t 5000
        2. Es Krim \t 7000
        3. Keripik \t 8000
        4. Coklat \t 12000
        5. Buku \t 10000
        6. Pensil \t 4000
        7. Penghapus \t 3000
        """
          )
    
    kode = int(input("masukan Kode Barang : "))
    if kode == 1:
        barang.append('roti')
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append('es krim')
        barang.append(7000)
        total += 7000
    elif kode == 3:
        barang.append('keripik')
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append('coklat')
        harga.append(12000)
        total += 12000
    elif kode == 5:
        barang.append('buku')
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append('pensil')
        harga.append(4000)
        total += 4000
    elif kode == 7:
        barang.append('penghapus')
        harga.append(3000)
        total += 3000
    else:
        print('Kode tidak Valid')

    lanjut =  input('lanjut belanja (y/n) : ')
    if lanjut == 'n':
            print("")
            break
    print('barang yang dibeli:', barang)
    print('harga barang:', harga)
    print('total harga yang harus dibayar',total,'\n')

    uang = int(input('masukan uang pembayaran : '))
    if uang > total:
        print('kembaliannya : ',uang - total)
    elif uang == total:
        print('uangnya pas')
    else:
        print('uangnya kurang',uang - total)



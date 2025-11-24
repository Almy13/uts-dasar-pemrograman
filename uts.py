#1. Bilangan dimasukkan dari input pengguna
#Kita gunakan try-except untuk menangani jika pengguna masukkan selain angka
try: 
    angka_input = int(input("Masukkan sebuah bilangan ( maks 7 digit): "))

    # 2. Proses perhitungan nilai tempat 
    # Asumsi berdasarkan contoh, kita batasi hingga 9999999
    if 0 <= angka_input <= 9999999:

        # Ambil nilai jutaan
        jutaan = angka_input // 1000000
        sisa_jutaan = angka_input % 1000000

        # Ambil nilai ratusan_ribu dari sisa_jutaan
        ratusan_ribu = sisa_jutaan // 100000
        sisa_ratusan_ribu = sisa_jutaan % 100000


        # Ambil nilai puluhan_ribu dari sisa ratusan_ribu
        puluhan_ribu = sisa_ratusan_ribu // 10000
        sisa_puluhan_ribu = sisa_ratusan_ribu % 10000

        # Ambil nilai ribuan dari sisa puluhan_ribu
        ribuan = sisa_puluhan_ribu // 1000
        sisa_ribuan = sisa_puluhan_ribu % 1000

        # Ambil nilai ratusan dari sisa_ribuan
        ratusan = sisa_ribuan // 100
        sisa_ratusan = sisa_ribuan % 100

        # Ambil nilai puluhan dari sisa_ratusan
        puluhan = sisa_ratusan // 10
        satuan = sisa_ratusan % 10


        # 3. Tampilkan hasil sesuai format
        print(f"\nAnda memasukkan bilangan {angka_input} dimana;")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusan_ribu} merupakan ratusan ribu")
        print(f"{puluhan_ribu} merupakan puluhan ribu")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("Harap masukkan bilangan antara 0 sampai 9999999.")

except ValueError:
    print("Sorry input tidak valid! Harap masukkan angka.")
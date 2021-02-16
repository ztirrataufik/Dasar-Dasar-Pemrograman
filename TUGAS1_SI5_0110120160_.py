print("Fitur Input Nilai Mahasiswa")
nim = input("Masukan NIM : ")#Memasukan NIM dan disimpan dalam variabel nim.
kondisi = True
while kondisi: #looping/perulangan
    jmatkul = int(input("Masukan Jumlah Mata Kuliah Yang Diambil : "))#jumlah mata kuliah yang diambil, program akan melakukan perulangan untuk menerima data nilai mata kuliah yang diambil.
    index = 0 #index/iteration dipakai setelah mengisi jumlah matkul.
    totalsks = 0 #untuk menampung nilai total sks
    ip = 0 #untuk menampung nilai total index prestasi
    if jmatkul < 1 or jmatkul > 8: #validasi tidak boleh dibawah 1 atau diatas 8
        print("Jumlah Mata Kuliah Harus Antara 1 sampai 8")
    else :
        while index < jmatkul : #perulangan kedua ketika kondisi index lebih kecil dari jumlah matkul
            index = index + 1 #index akan bertambah ketika melakukan perulangan 
            print("Nilai Mata Kuliah : ", index) #mencetak nilai mata kuliah
            nama_matkul = input("Nama Mata Kuliah : ") #memasukan nama matkul
            beban_sks = int(input("Beban SKS Mata Kuliah : ")) #Memasukan Beban SKS Mata Kuliah
            nilai_kuis = eval(input("Nilai Kuis : ")) #Memasukan Nilai Kuis
            nilai_tugas1 = eval(input("Nilai Tugas 1 : ")) #Memasukan nilai tugas 1
            nilai_tugas2 = eval(input("Nilai Tugas 2 : ")) #Memasukam nilai tugas 2
            nilai_uts = eval(input("Nilai UTS : ")) #Memasukan Nilai UTS
            nilai_uas = eval(input("Nilai UAS : ")) #Memasukan Nilai UAS
            nmatkul = 0.15*nilai_kuis + 0.15*nilai_tugas1 + 0.20*nilai_tugas2 + 0.25*nilai_uts + 0.25*nilai_uas #Menjumlahkan bobot nilai tugas dikali nilai tugas lalu ditambah
            totalsks = totalsks + beban_sks #total sks di tambah beban sks
            if 85 <= nmatkul <= 100: #mencari grade
                nilai_huruf = "A"
                indeks_nilai = float(4.0) #index prestasi
            elif 70 <= nmatkul <= 85:
                nilai_huruf = "B"
                indeks_nilai = float(3.0)
            elif 55 <= nmatkul <= 70:
                nilai_huruf = "C"
                indeks_nilai = float(2.0)
            elif 40 <= nmatkul <= 55:
                nilai_huruf = "D"
                indeks_nilai = float(1.0)
            else :
                nilai_huruf = "E"
                indeks_nilai = float(0.0)
            print("Nilai Mata Kuliah", nama_matkul, ":", round(nmatkul, 2), "GRADE : ", nilai_huruf)
            ip = ip + (beban_sks * indeks_nilai) #menghitung total ip, beban sks dikali indeks nilai lalu ditambah dengan ip pada setiap perulangan
        kondisi = False #jika perulangan index tidak lebih kecil dari jumlah matkul, ubah kondisi menjadi False agar perulangan awal berhenti.
        ip_total = round(ip / totalsks)
        print("")
print("RANGKUMAN")
print("NIM : ", nim)
print("Total SKS : ", totalsks) #mencetak total sks

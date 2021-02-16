# Bagian ini adalah unit test.
# Unit test digunakan untuk melakukan pengujian
# otomatis terhadap program yang dibangun.
# Jangan lakukan perubahan apapun pada bagian ini.
# Unit test ini akan digunakan oleh dosen/asisten
# sebagai acuan dalam mengoreksi 
# hasil pekerjaan mahasiswa.
# Jika ingin mencoba menjalankan unit test ini,
# tekan Ctrl+Shift+S untuk membuka terminal shell
# di bagian kanan bawah layar.
# Ketik perintah pytest, lalu enter.
# Jika masih ada AssertionError, berarti fungsi yang
# dibuat belum benar.
# Jika tidak ada AssertionError dan hasil pengujian
# menunjukkan 100% sukses, berarti fungsi sudah benar.


import main

def hitung_kemunculan_1():
  assert main.hitung_kemunculan('abu abu merah jambu') == {'abu':2, 'merah':1, 'jambu':1}

def hitung_kemunculan_2():
  assert main.hitung_kemunculan('matahari') == {'matahari':1}

def hitung_kemunculan_3():
  assert main.hitung_kemunculan('jalan tol jalan jalan') == {'jalan':3, 'tol':1}

def test_urut_unik_1():
  assert main.urut_unik('abu abu merah jambu') == ['abu', 'jambu', 'merah']

def test_urut_unik_2():
  assert main.urut_unik('matahari') == ['matahari']

def test_urut_unik_3():
  assert main.urut_unik('jalan tol jalan jalan') == ['jalan', 'tol']

def test_read_1():
  assert main.read('data1.txt') == {'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}

def test_read_2():
  assert main.read('data2.txt') == {'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}

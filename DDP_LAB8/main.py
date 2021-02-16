# Nama: 
# NIM: 
# Kelas: 

def hitung_kemunculan(s):
  buah = s.split()#untuk mengubah type data string menjadi type data list
  res = {}#dictionary kosong untuk menampung sebuah data list yang berisi nama-nama buah
  for b in buah:#perulangan untuk mengeluarkan isi dari variabel buah
    res[b]=buah.count(b)#panggil variabel res kemudian masukan key dari variabel b untuk valuenya menggunakan count pada variabel buah
  return res#kembalikan nilai dari variabel res jika perulangan telah selesai

def urut_unik(s):
  buah = s.split()#untuk mengubah type data string menjadi type data list
  res = []#list kosong untuk menampung sebuah data list yang berisi nama-nama buah
  for b in buah:#perulangan untuk mengeluarkan isi dari variabel buah
    if b not in res:#jika value variabel b tidak ada pada list maka jalankan statment dibawah ini
      res.append(b)#panggil variabel res, lalu gabung dengan fungsi append untuk menambahkan value dari variabel b
  res.sort()#untuk menyortir value dari variabel res sesuai abjad
  return res#kembalikan nilai dari variabel res jika perulangan telah selesai

def read(filename):
  file = open(filename)
  dictionary = {}
  for data in file:
    data = data.split()
    dictionary[data[0]]= data[1]
  file.close()
  return dictionary





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = hitung_kemunculan("pisang jambu apel jambu pisang jeruk")
  print(f"hitung_kemunculan('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: {{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}})")
  print()
  r = urut_unik("pisang jambu apel jambu pisang jeruk")
  print(f"urut_unik('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: ['apel', 'jambu', 'jeruk', 'pisang'])")
  print()
  r = urut_unik('kecapi melon kecapi kecapi kecapi')
  print(f"urut_unik('kecapi melon kecapi kecapi kecapi') = {r} \n(solusi: ['kecapi', 'melon'])")
  print()
  r = read('data1.txt')
  print(f"read('data1.txt') = {r} \n(solusi: {{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}}")
  print()
  r = read('data2.txt')
  print(f"read('nilai2.txt') = {r} \n(solusi: {{'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}}")
  print()

if __name__ == '__main__':
  test()
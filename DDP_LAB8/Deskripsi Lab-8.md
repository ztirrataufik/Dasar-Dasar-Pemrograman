# Deskripsi Lab-8
Pada Lab-8, kalian diminta untuk membuat fungsi-fungsi yang dideskripsikan pada soal-soal di bawah. Kode fungsi tersebut dapat dituliskan dalam file main.py di tempat yang sudah disediakan.
Terdapat dua soal yang wajib dikerjakan (Soal 1 dan Soal 2) dan satu soal bonus (Soal 3) yang tidak wajib dikerjakan.
**Untuk setiap fungsi yang dibangun, berikan penjelasan mengenai alur jalannya fungsi. Tulis penjelasan tersebut dalam bentuk komentar pada fungsi.**


## Soal 1. Fungsi hitung_kemunculan()
Buatlah fungsi `hitung_kemunculan()` yang menerima parameter string `s` dan mengembalikan sebuah tipe data dictionary yang berisi daftar kata dan jumlah kemunculan kata tersebut dalam string `s`.
Asumsikan string `s` hanya terdiri dari sejumlah kata yang dipisahkan spasi. String `s` tidak mengandung tanda baca apapun selain spasi.


### Contoh 1.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> hitung_kemunculan('pisang jambu apel jambu pisang jeruk')
{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}
```

Penjelasan Contoh 1.1:
Daftar kata yang dikandung oleh string pada parameter pemanggilan fungsi tersebut adalah `pisang`, `jambu`, `apel`, dan `jeruk`.
Kata `pisang` muncul sebanyak 2 kali, kata `jambu` muncul sebanyak 2 kali, kata `apel` muncul sebanyak 1 kali, dan kata `jeruk` muncul sebanyak 1 kali.
Setiap kata tersebut menjadi `key` dari dictionary, dan jumlah kemunculan kata tersebut menjadi `value` dari key tersebut.


## Soal 2. Fungsi urut_unik()
Buatlah fungsi `urut_unik()` yang menerima parameter string `s` dan mengembalikan sebuah tipe data list yang berisi daftar kata dalam string `s` secara unik (tanpa duplikasi) dan terurut berdasarkan abjad.
Asumsikan string `s` hanya terdiri dari sejumlah kata dalam huruf kecil yang dipisahkan spasi. String `s` tidak mengandung tanda baca apapun selain spasi.


### Contoh 2.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> urut_unik('pisang jambu apel jambu pisang jeruk')
['apel', 'jambu', 'jeruk', 'pisang']
```

Penjelasan contoh 2.1:
Dalam string pada parameter pemanggilan fungsi tersebut, terdapat empat kata, yaitu `pisang`, `jambu`, `apel`, dan `jeruk`.
Setiap kata tersebut menjadi elemen pada list.
List tersebut diurutkan berdasarkan abjad, sehingga hasil akhirnya adalah `['apel', 'jambu', 'jeruk', 'pisang']`.


## [BONUS] Soal 3. Fungsi read()
Diberikan file `data1.txt` dan `data2.txt` yang berisi daftar nama benda dan kodenya.
Sebagai contoh, baris `101 Teddy-Bear` berisi kode `101` dan nama benda `Teddy-Bear`.


Buatlah fungsi `read()` yang menerima parameter string `filename` dan mengembalikan sebuah tipe data dictionary yang berisi pasangan kode dan nama benda yang terdapat di dalam file tersebut.
Catatan: semua key dan value pada dictionary dibuat dalam tipe data string


### Contoh 3.1
Contoh pemanggilan dan luaran fungsi:
```sh
>>> nilai_max('data1.txt')
{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}
```

Penjelasan contoh 3.1:
Pada file `data1.txt`, terdapat sepuluh baris data yang berisi pasangan kode dan nama benda.
Contoh kode antara lain 101, 102, dsb. Kode tersebut menjadi key pada dictionary.
Untuk setiap kode tersebut, nama benda yang berada di sebelahnya dijadikan value di dalam dictionary untuk key yang bersesuaian.


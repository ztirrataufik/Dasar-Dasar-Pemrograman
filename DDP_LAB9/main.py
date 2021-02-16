# Nama: 
# NIM: 
# Kelas: 

def sort_desc(arr):
  i = 0 #membuat varianbel/inisialisasi variabel i untuk mengunci dalam iterasi
  while i < len(arr)-1:#perulangan i dengan kondisi lebih kecil dari variabel array dikurangi 1
    j = 0#membuat variabel/inisialisasi varibel j untuk mengunci dalam iterasi
    while j < len(arr)-i-1:#perulangan j dengan kondisi lebih kecil dari variabel array dikurangi variabel i dikurangi 1
      if arr[j] < arr[j+1]:#kondisi ketika variabel array dengan posisi j lebih kecil dari array j + 1
        arr[j], arr[j+1] = arr[j+1], arr[j]#pertukaran antara variabel array j dengan variabel array j+1
      j += 1#digunakan agar perulangan dengan kondisi varibel j bisa menyeimbangkan nilai dari panjang variabel array
    i += 1#digunakan agar perulangan dengan kondisi variabel i bisa menyeimbangkan nilai dari panjang variabel array
  return arr#pengembalian nilai

#hasil diskusi dengan teman-teman




# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = sort_desc([2, 3, 1, 0, 4])
  print(f"sort_desc([2, 3, 1, 0, 4]) = {r} \n(solusi: [4, 3, 2, 1, 0]")
  print()
  r = sort_desc([1, 2, 3])
  print(f"sort_desc([1, 2, 3]) = {r} \n(solusi: [3, 2, 1]")
  print()

if __name__ == '__main__':
  test()
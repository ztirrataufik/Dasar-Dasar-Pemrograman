# Nama: Z Tirra Taufik
# NIM: 0110120160
# Kelas: SI-05

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self, head = None):
    self.head = head
  
  def add_last(self, new_data):
    if self.head is None:
      self.head = Node(new_data)
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = Node(new_data)
  
  def cetak(self):
    if self.head is None:
      print('List kosong')
    else:
      current = self.head
      while current is not None:
        print(current.data, end=' ')
        current = current.next
      print()

  def sum_odd(self):
    a = 0 #menginisialkan variabel a dengan value 0
    myNode = self.head #menginisialkan mynode dengan value self.head
    while myNode is not None: #perulangan untuk variabel myNode dengan kondisi jika myNode tidak None
      if myNode.data % 2 != 0: #percabangan ketika myNode.data di modulo % 2 dan mengembalikan sisa bukan 0, (otomatis angka tersebut ganjil)
        a += myNode.data #panggil variabel a lalu tambah dengan Mynode.data
      myNode = myNode.next #timpa variabel myNode dengan myNode.next agar bisa melanjutkan ke elemen berikutnya
    return a #mengembalikan nilai a
  
  def get_max(self):
    a = 0
    myNode = self.head
    if myNode is not None:
      while myNode:
        if a < myNode.data:
          a = myNode.data
        myNode = myNode.next
      return a
    else:
      return None





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  list1 = LinkedList()
  list1.add_last(1)
  list1.add_last(2)
  list1.add_last(3)
  list1.add_last(4)
  list1.add_last(5)
  print('list1 : ', end='')
  list1.cetak()
  r1 = list1.sum_odd()
  print(f"list1.sum_odd() = {r1} \t(solusi: 9)")
  r2 = list1.get_max()
  print(f"list1.get_max() = {r2} \t(solusi: 5)")
  print()

  list2 = LinkedList()
  list2.add_last(9)
  list2.add_last(9)
  list2.add_last(9)
  print('list2 : ', end='')
  list2.cetak()
  r1 = list2.sum_odd()
  print(f"list2.sum_odd() = {r1} \t(solusi: 27)")
  r2 = list2.get_max()
  print(f"list2.get_max() = {r2} \t(solusi: 9)")
  print()

  list3 = LinkedList()
  list3.add_last(6)
  list3.add_last(2)
  list3.add_last(8)
  list3.add_last(4)
  print('list3 : ', end='')
  list3.cetak()
  r1 = list3.sum_odd()
  print(f"list3.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list3.get_max()
  print(f"list3.get_max() = {r2} \t(solusi: 8)")
  print()

  list4 = LinkedList()
  print('list4 : ', end='')
  list4.cetak()
  r1 = list4.sum_odd()
  print(f"list4.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list4.get_max()
  print(f"list4.get_max() = {r2} \t(solusi: None)")
  print()

if __name__ == '__main__':
  test()
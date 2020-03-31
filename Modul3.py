print("NAMA : Sindhi")
print("NIM  : L200180084")
print("KELAS: D")
print("MODUL: 3"+"\n")

m1 = [[2,3],[4,5]]
m2 = [[10,20],[5,6]]
#------------------------------------NOMER 1A----------------------------------#
def cekMat(matrix):
    """memastikan type data Integer"""
    jum = len(matrix)
    hasil = ""
    for x in matrix:
        for i in x:
            assert isinstance(i, int),"Harus Integer"
        return True
    
#------------------------------------NOMER 1B----------------------------------#
def Ukuran(matrix):
    """Mengambil ukuran matriks"""
    return("Ukuran Matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))

#------------------------------------NOMER 1C----------------------------------#
def Jumlah(matrix1,matrix2):
    """Penjumlahan 2 Matrix"""
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            for y in range(0, len(matrix1[0])):
                print(matrix1[x][y] + matrix2[x][y],' '),
            print()
    else:
        print("Matriks Tidak Sesuai")
        
#------------------------------------NOMER 1D----------------------------------#
def Kali(matrix1,matrix2):
    """Perkalian 2 Matrix"""
    mat3 = []
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            row = []
            for y in range(0, len(matrix1[0])):
                total = 0
                for z in range(0, len(matrix1)):
                    total = total + (matrix1[x][z] * matrix2[z][y])
                row.append(total)
            mat3.append(row)

        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], ' ')
            print()
    else:
        print("Matriks Tidak Sesuai")
def determinan(matrix):
    """Menghitung Determinan Matrix"""
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

#------------------------------------CEK NOMER 1----------------------------------#
print("Nomer 1")
print(cekMat(m1))
print(Ukuran(m1))
Jumlah(m1,m2)
Kali(m1,m2)
print(determinan(m1))

#------------------------------------NOMER 2A----------------------------------#
def buatNol(m, n):
    """Menggunakan dua input"""
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

def buatNol2(m):
    """Menggunakan satu input"""
    n = m
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

#------------------------------------NOMER 2B----------------------------------#
def buatIdentitas(m):
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matrix)

#------------------------------------CEK NOMER 2----------------------------------#

print("Nomer 2")
buatNol(3,3)
buatNol2(3)
buatIdentitas(4)
print("\n")
#------------------------------------NOMER 3----------------------------------#
print("nomor 3")
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def MakeNode(list):
    a = Node(list[0])
    if len(list) > 1:
        b = a
        for i in range(1,len(list)):
            b.next = Node(list[i])
            b = b.next
    return a

def kunjungi(head):
    curNode = head
    while curNode != None:
        print(curNode.data)
        curNode = curNode.next

def cari(head, yang_dicari):
    temp = head
    while temp != None :
        if temp.data == yang_dicari:
            return temp
        temp = temp.next
    return Node(None)

def tambahDepan(head):
    temp = Node("tambah depan", head)
    return temp

def tambahAkhir(head):
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = Node("tambah akhir")
    return head

def tambah(head, posisi):
    """ Menambahkan simpul sebelum posisi """
    temp = head
    while temp != None:
        if temp.next.data == posisi:
            temp_belakang = temp.next
            temp.next = Node("tambah tengah", temp_belakang)
            return head
        temp = temp.next
    return None

def hapus(head, posisi):
    temp = head
    while temp != None:
        if temp.next.data == posisi:
            temp_belakang = temp.next.next
            temp.next = temp_belakang
            return head
        temp = temp.next
    return None

a = MakeNode(["Sindhi", "Ana", "Aulia", "sindhi", "aulia"])

print(a.data)
c = cari(a, "Aulia")
print(c.next.data)

print()
kunjungi(a)

print()
a = tambahDepan(a)
kunjungi(a)

print()
a = tambahAkhir(a)
kunjungi(a)

print()
a = tambah(a, "Aulia")
kunjungi(a)

print()
a = hapus(a, "Aulia")
kunjungi(a)
print("\n")
#------------------------------------NOMER 4-----------------------------------#
print("Nomor 4")
class DNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def massDNodeCreator(list):
    a = DNode(list[0])
    p = a
    for i in list[1:]:
        p.next = DNode(i)
        p.next.prev = p
        p = p.next
    return a

def tambahSimpulAwal(head, data):
    data = DNode(data)
    data.next = head
    data.next.prev = data
    return data

def tambahSimpulAkhir(head, data):
    data = DNode(data)
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = data
    return head

list = ["e", "f", "g", "h"]
a = massDNodeCreator(list)
print(a.next.next.next.prev.prev.data)

a = tambahSimpulAwal(a, "awal")
print(a.next.prev.data)

a = tambahSimpulAkhir(a, "akhir")
print(a.next.next.next.next.next.data)

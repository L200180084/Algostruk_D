## Menjumlahkan bilangan 1 sampai n
import time

## Cara pertama
def jumlahkan_cara_1(n):
    hasilnya=0
    for i in range (1,n+1):
        hasilnya+=i
    return hasilnya

#pengukuran kinerja
for i in range(5):              # mengulang lima kali
    awal = time.time()          #   menandai awal kerja
    h = jumlahkan_cara_1(1000000) #   menjumlah 1 sampai sejuta
    akhir = time.time()         #   menandai akhir kerja, lalu mencetak
    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h,akhir-awal))

## Cara kedua
import time

def jumlahkan_cara_2(n):
    return (n*(n+1))/2

#pengukuran kinerja
for i in range(5):              # mengulang lima kali
    awal = time.time()          #   menandai awal kerja
    h = jumlahkan_cara_2(1000000) #   menjumlah 1 sampai sejuta
    akhir = time.time()         #   menandai akhir kerja, lalu mencetak
    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h,akhir-awal))


## Kasus terburuk, rata-rata, dan terbaik
import time
import random

def InsertionSort(x):
    for i in range(1,len(x)):
        nilai = x[i]
        y = i
        while y >0 and nilai<x[y - 1]:
            x[y]=x[y-1]
            y -=1
        x[y]=nilai

print("======Average Case Scenario======")    
##average case
for i in range (5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = InsertionSort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))

print("======Worst Case Scenario======")    
for i in range (5):
    L = list(range(3000))
    L = L[::-1]         # Membalik rutan elemen dilist
    awal = time.time()
    U = InsertionSort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))

print("======Best Case Scenario======")    
for i in range (5):
    L = list(range(3000))
    awal = time.time()
    U = InsertionSort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))

## Operasi-operasi Dasar
x = 5
y = x
z = x + y * 8
d = x > 0 and x < 100
f = [3,2,4,5]
v = f[0:2]
print("x = ", x)
print("y = ", y)
print("z = ", z)
print("d = ", d)
print("f = ", f)
print("v = ", v)

## Kode yang mempunyai kompleksitas
count = 0
i = 32
while i >= 1 :
    count += 1
    i = i // 2
    print("i = ", i, " ", "count = ", count)

print(count)


## Analisis Perwaktusn Menggunakan timeit
from timeit import timeit
print(timeit('sqrt(2)', 'from math import sqrt', number=10000))

print(timeit('sqrt(2)', 'from math import sqrt', number=100000))

print(timeit('sqrt(2)', 'from math import sqrt', number=1000000))

print(timeit("1+2")) #waktu untuk menghitung 1+2, diulang 1 juta kali.

print(timeit("sin(pi/3)", setup='from math import sin, pi')) #sin(pi/3), diulang 1 juta kali.

print(timeit("sin(1.047)", setup='from math import sin')) #sin(1.047), diulang 1 juta kali.

import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:
def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

## Ini fungsi pengujinya:
def ujiKalangBersusuh(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 1000
LS = ujiKalangBersusuh(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya

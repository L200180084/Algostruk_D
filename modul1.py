import random

#Nomer 1
def cetakSiku(x) :
    for a in range(x) :
        print((a+1)*"*")

#Nomer 2
def gambarlahPersegiEmpat(a,b) :
    for i in range(a) :
        if ((i+1) == 1) :
            print(b*"@")
        elif ((i+1) == a) :
            print(b*"@")
        else :
            print("@"+" "*(b-2)+"@")

#Nomer 3
def jumlahHurufVokal(ch) :
    b = len(ch)
    a = 0
    for i in ch :
        if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            a += 1
    return b,a

def jumlahHurufKonsonan(ch) :
    b = len(ch)
    a = 0
    for i in ch :
        if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            a += 1
    return b,b-a

#Nomer 4
def rerata(x) :
    a = 0
    b = 0
    for i in x :
        a += 1
        b = b + i
        a = float(a)
        b = float(b)
    return(b/a)

#Nomer 5
def apakahPrima(a) :
    x = 0
    for i in range(a) :
        if a % (i+1) == 0 :
            x += 1
    if x == 2 :
        print("YA")
    else :
        print("TIDAK")

#Nomer 6
def cekPrima() :
    y = range(1001)
    for i in range(2,1001) :
        x = 0
        for j in range(i) :
            if i % (j+1) == 0 :
                x += 1
        if x == 2 :
            print(i)
#Nomer 7
def faktorPrima(x):
    listprima=[]
    prima=2
    while prima<=x:
        if x%prima==0:
            x/=prima
            listprima.append(prima)
        else:
            prima+=1
    return listprima
            
#Nomer 8
def apakahTerkandung(a,b) :
    if a in b :
        return True
    else :
        return False

#Nomer 9
def ums() :
    for i in range(101) :
        if (i+1) % 15 == 0 :
            print("Python UMS")
        elif (i+1) % 3 == 0 :
            print("Python")
        elif (i+1) % 5 == 0 :
            print("UMS")
        else :
            print(i+1)

#Nomer 10           
def selesaikanABC(a,b,c) :
    res = 0
    res = (b**2) - (4*a*c)

    if res == 0 :
        print("Determinannya nol. Persamaan mempunyai satu akar kembar.")
    elif res > 0 :
        print("Determinannya positif. Persamaan mempunyai akar real dan berlainan.")
    elif res < 0 :
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")

#Nomer 11
def apakahKabisat() :
    thn = int(input("Masukkan Tahun : "))
    if thn % 4 == 0 :
        if thn % 100 == 0 :
            if thn % 400 == 0 :
                print(True)
            else :
                print(False)
        else :
            print(True)
    else :
        print(False)

#Nomer 12
def tebak() :
    a = random.randrange(1,101)
    b = -1
    n = 0
    print("Permainan tebak angkat.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
    while a != b :
        n = n + 1
        b= int(input("Masukkan tebakan ke-"+str(n)+":> "))
        if b < a :
            print("Itu terlalu kecil. Coba lagi")
        elif b > a :
            print("Itu terlalu besar. Coba lagi")
        else :
            print("Ya. Anda benar.")
            break

#Nomer 13
def katakan(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = ""
    if x <= 0:
        hasil += 'Bilangan Haruslah Positif\ndan Bilangan Asli'
    elif x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += katakan(x-10) + " belas "
    elif x < 100:
        hasil += katakan(int(x/10)) + " puluh " + katakan(x%10)
    elif x < 200 :
        hasil += "seratus " + katakan(x-100)
    elif x < 1000 :
        hasil += katakan(int(x/100)) + " ratus " + katakan(x%100)
    elif x < 2000 :
        hasil += "seribu " + katakan(x-1000)
    elif x < 1000000 :
        hasil += katakan(int(x/1000)) + " ribu " + katakan(x%1000)
    elif x < 1000000000 :
        hasil += katakan(int(x/1000000)) + " juta " + katakan(x%1000000)
    elif x >= 1000000000 :
        hasil += katakan(int(x/1000000000)) + " milyar " + katakan(x%1000000000)
    return hasil

#Nomer 14           
def formatRupiah(a) :
    a = list(str(a))
    b = len(a)
    if b % 3 == 0 :
        b = int(b/3) - 1
    else :
        b = int(b/3)
    n = 0
    for i in range(b) :
        x = -3*(i+1)
        a.insert(int(x)+n,".")
        n = n - 1
    a = "".join(a)
    print("Rp "+a)
       

inp = input("Masukkan Kalimat : ")
inp2 = input("Masukkan Kata Yang Ingin Di Cari :")

spl = inp.lower().split()
spl2 = inp2.lower()

hasil = 0

try :
    for i in spl:
        if i == spl2:
            hasil += 1

except:
    print("ga ketemu")

        
print(hasil)
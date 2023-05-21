#Program Portal Parkir Otomatis
#Menerima masukan berupa slot, jenis kendaraan, pilihan tombol dari pengendara, dan mencetak waktu masuk, waktu keluar, dan tarif parkir yang harus dibayar

#KAMUS
# N, d, c : int
#T : array of integer
#U : array of integer
##lama : integer (Hasil konversi waktu masuk dalam detik)
#lama_1 : integer (Hasil konversi waktu keluar dalam detik)

#ALGORITMA
print("=======================")
print("Welcome to Portal Parkir Otomatis")
print("=======================")

jenis = input("Masukkan jenis kendaraan : ").upper()
d=0
N=int(input("Masukan jumlah kendaraan yang akan masuk : "))
import time

def waktumasuk():
  global hr,mn,sc
  b=time.localtime()
  hr = b.tm_hour
  mn = b.tm_min
  sc = b.tm_sec
  lama= hr*3600 + mn *60 + sc
  return(f'{hr}:{mn}:{sc}')


def waktukeluar():
  global hr_1,mn_1,sc_1
  b=time.localtime()
  hr_1 = b.tm_hour
  mn_1 = b.tm_min
  sc_1 = b.tm_sec
  lama_1 = hr_1*3600 + mn_1 *60 + sc_1
  return(f'{hr_1}:{mn_1}:{sc_1}')

def biayaparkirmobil(i):
  c=((W[i-1] - V[i-1])//3600)+1
  if(c <= 1) :
    return(4000)
  else :
    d = 4000+(c-1)*3000
    return(d)

def biayaparkirmotor(i):
  c=((W[i-1] - V[i-1])//3600)+1
  if(c <= 1) :
    return(3000)
  else :
    d = 3000+(c-1)*2000
    return(d)

T= [0 for i in range (N)]
U= [0 for i in range (N)]
V= [0 for i in range (N)]
W= [0 for i in range (N)]
if jenis == "MOBIL"  :
    for i in range (1, N+1) :
    # print(f'Parkiran mobil-{i}')
        print("Mobil ke " + str(i))
        print('Tekan Tombol hijau untuk mengeluarkan karcis dan tombol merah jika mengalamin kesulitan')
        a = input().upper()
        if a == "HIJAU" :
            T[i-1] = waktumasuk()
            lama= hr*3600 + mn *60 + sc
            V[i-1] = lama
            print("Waktu masuk mobil " + str(i) + " adalah " + str(T[i-1]))
        else : #jika tekan tombol merah
            print("Mohon tunggu sebentar.. petugas akan segera datang")

    print('Klik enter untuk keluar')
    b=input()
    kendaraan = 1
    while (kendaraan <= N) :
        i = int(input('No parkiran mobil : '))
        if T[i-1] == 0 : #jika klik tombol merah maka waktu masuk akan 0
            print("Anda mengalami kendala masuk ke dalam parkiran")
        else: #jika klik tombol hijau maka waktu masuk akan keluar
            U[i-1]=waktukeluar()
            lama_1 = hr_1*3600 + mn_1 *60 + sc_1
            W[i-1] = lama_1
            print("Waktu mobil " + str(i) + " masuk adalah " + str(T[i-1]))
            print("Waktu mobil " + str(i) + " keluar adalah " + str(U[i-1]))
            print(f'tarif : {biayaparkirmobil(i)}')
            print('Terima kasih selamat jalan')
        kendaraan += 1
elif jenis == "MOTOR" :
    for i in range (1, N+1) :
    # print(f'Parkiran mobil-{i}')
        print("Motor ke " + str(i))
        print('Tekan Tombol hijau untuk mengeluarkan karcis dan tombol merah jika mengalamin kesulitan')
        a = input().upper()
        if a == "HIJAU" :
            T[i-1] = waktumasuk()
            lama= hr*3600 + mn *60 + sc
            V[i-1] = lama
            print("Waktu masuk motor " + str(i) + " adalah " + str(T[i-1]))
        else : #jika tekan tombol merah
            print("Mohon tunggu sebentar.. petugas akan segera datang")

    print('Klik enter untuk keluar')
    b=input()
    kendaraan = 1
    while (kendaraan <= N) :
        i = int(input('No parkiran motor : '))
        if T[i-1] == 0 : #jika klik tombol merah maka waktu masuk akan 0
            print("Anda mengalami kendala masuk ke dalam parkiran")
        else: #jika klik tombol hijau maka waktu masuk akan keluar
            U[i-1]=waktukeluar()
            lama_1 = hr_1*3600 + mn_1 *60 + sc_1
            W[i-1] = lama_1
            print("Waktu motor " + str(i) + " masuk adalah " + str(T[i-1]))
            print("Waktu motor " + str(i) + " keluar adalah " + str(U[i-1]))
            print(f'tarif : {biayaparkirmotor(i)}')
            print('Terima kasih selamat jalan')
        kendaraan += 1
else :
    print("Masukkan jenis kendaraan Anda salah.")
import os
from time import sleep


aa='\033[1;37m'
os.system('cls' if os.name=='rf' else 'clear')
print('\033[1;31m\t\t╔═╗╔═╗╔═╗')
print('\033[1;37m\t\t╚═╗╚═╗║ ╦')
print('\033[1;31m\t\t╚═╝╚═╝╚═╝')
print('\x1b[5;37;41m\tsurat izin sekolah generator\x1b[0m')
Nama=input(aa+'\n[+]Nama kamu: ')
Kelas=str(input('[+]Kelas: '))
Sekolah=str(input('[+]Sekolah: '))
jurusan=str(input('[+]Jurusan: '))
Alasan=input('[+]Alasan: ')
letter='\t\t\t\tKepada Yth\n\t\t\t\tIbu/Bapak Guru\n\t\t\t\tWali kelas '+Kelas+'\n\t\t\t\t'+Sekolah+'\n\nDengan hormat,\nSaya orang tua siswa dari:\n\n     Nama   : '+Nama+'\n     Kelas  : '+Kelas+'\n    Jurusan : '+jurusan+'\n\nIngin memberitahukan bahwa anak saya tersebut\ntidak dapat hadir ke sekolah mengikut pelajaran\nseperti biasanya di karenakan '+Alasan+'.\n\n\t\t\t\tHormat Saya'
f=open('surat.txt','w')
f.write(letter)
f.close()
sleep(3)
print('[+]surat izin sakit telah dibuat')
print('[+]nama file (surat.txt)')

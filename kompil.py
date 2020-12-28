import os
os.system("clear")
print('kompilasi dalvik executable')
file=input('file : ')
try:
    os.system('ecj {}'.format(file))
    print('kompil untuk JVM berhasil')
except:
    print('file tidak ada')
os.system('sleep 1')
print('proses kompil untuk Dalvikvm')
os.system('sleep 2')
ubah=file.replace('java', 'dex')
ubahlg=file.replace('java', 'class')
try:
    os.system('dx --dex --output={} {}'.format(ubah,ubahlg))
    print('file berhasil di kompil')
except:
    print('file tidak ada')
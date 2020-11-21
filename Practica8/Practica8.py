from ftplib import FTP
import fnmatch
from ftplib import FTP
import os 
'''
FTP URL: ftp.dlptest.com
FTP User: dlpuser@dlptest.com
Password: eUj8GeW55SvYaswqUyDSm5v6N
'''

os.mkdir('Texto')
ftp = FTP()
ftp.connect('ftp.dlptest.com')
ftp.login('dlpuser@dlptest.com', 'eUj8GeW55SvYaswqUyDSm5v6N')

txts = ['txt','msg','README']
archivos = ftp.nlst()
print(archivos)
directorios=ftp.dir()

for archivo in archivos:
    for txt in txts:
        if fnmatch.fnmatch(archivo, '*.'+ txt):
            file = open(archivo + '.txt', 'wb')
            ftp.retrbinary('RETR' + archivo, file.write)
            file.close
            remitente= 'C:\Users\juced\Desktop\Practica8' + '"\"' +  archivo
            os.rename(remitente,'C:\Users\juced\Desktop\Practica8\Texto')


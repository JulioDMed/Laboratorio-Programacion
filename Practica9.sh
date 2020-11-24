#!/bin/bash
# -*- ENCODING: UTF-8 -*-
sudo apt-get install sendemail
sudo apt-get install libnet-ssleay-perl
echo "Escribe tu cuenta de gmail: "
read tugmail
echo "Escribe el asunto del correo: "
read asunto
echo "Escribe el cuerpo del correo: "
read cuerpo
echo "Escribe tu usuario: "
read usuario
echo "Escribe tu contraseña: "
read passw 

touch correos.txt
echo "Escribe los correos que deseas enviar y presiona Ctrl+D cuando acabes"
cat > correos.txt


i=0
while read line
do i=$(($i+1));
sendemail -f $tugmail -t $line -s smtp.gmail.com:587 -u $asunto -m $cuerpo -v -xu $usuario -xp $pass -o tls=yes
done < "correos.txt"
echo "Final line count is: $i";

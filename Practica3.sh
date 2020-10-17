#!/bin/bash 
function_name () {
	read -p "Ingresa un puerto: " valor 

	return $(($valor))
}

function_name 

# Comprobamos si está escuchando el puerto 80, típico de un Webserver
WS= netstat -an|grep $valor|grep "LISTEN"
# Si la cadena de texto está vacía 
if [ -z $WS ] 
then 
echo "No tenemos ningún servicio arrancado y escuchando por el puerto $valor." 
# De lo contrario else echo Tenemos un Webserver arrancado 
else
echo "Tenemos ningún servicio arrancado y escuchando por el puerto $valor."
fi

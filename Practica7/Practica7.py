import nmap 


def EscanearPuertos(rango,tuip):

    rango =(input("Ingrese el rango que quiere scanear: "))
    tuip= ''
    #Escanear puertos 
    nm = nmap.PortScanner(tuip, rango)
    results = nm.scan(tuip, rango)
    nm.scaninfo()
    nm.command_line()
    nm.all_hosts()
    return results


print("Ingresa el rango y tu IP: ")

scan = EscanearPuertos(rango,tuip)
try:
    print(scan)
except:
    print('Ingresa un valor ')
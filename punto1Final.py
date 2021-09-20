"""
1.1	Simular la administración en la asignación de memoria con particiones variables de DIFERENTES
tamaños para un sistema con 3 procesos P1, P2 y P3.   Se prevé asignar 150 b de memoria al núcleo
del Sistema Operativo. Los procesos tendrán los siguientes tamaños P1= 100 b, P2= 150 b, P3= 250 b.
Luego de la asignación deberá imprimirse la información contenida en una tabla de particiones.
La tabla de particiones contendrá la siguiente información (id Proceso, dirección de comienzo de
la partición asignada, tamaño de la partición).
"""
#aca creamos la particion
def Particion(nomb,cant):
    l=list()
    l=[None]*cant
    a=dict()
    a["nombre"] = nomb
    a["espacio"] = l
    a["libre"] = True
    return a

#funcion para crear las particiones en una lista y la devolverla
def CrearMemoria():
    m = list()  
    m.append(Particion("Sistema Operativo",150))
    m.append(Particion("Particion 1",150))
    m.append(Particion("Particion 2",200))
    m.append(Particion("Particion 3",300))
    return m

#aqui mostramos la memoria con un formato mas lindo a la vista
#solom sive para numeros multiplosde 10
def MostrarMemoriaActual(me):
    for j in range(len(me)):
        print("-------------------------------------------------------------------------------")
        print("********",me[j]["nombre"],"********")
        for t in range(len(me[j]["espacio"])//10):
            for i in range(10):
                print(me[j]["espacio"][t*10+i], end=" ")
            print()
    print("-------------------------------------------------------------------------------")
    print()

#resta funcion rellena la particion no importa cul sea con el dato, la cant de lugares
def RellenarParticion(part,desde,dato,cant):
    for i in range(desde,(cant+desde)):
        part[i]=dato

#devuelve la max cantidad de lugarases continuos de la memoria libre en el [0] 
#y el lugar donde empieza a estar libre esa maxima cantidad en el [1]
#  , pasando como parametro la lista de la particion
def MaximoLugarDisponible(part):
    c=0
    l=0
    b=True
    for i in range(len(part)):
        if part[i]==None:
            if b:
                l=i
                b=False
            c=c+1
        else:
            c=0
            b=True
    return c,l

def Proceso(nombre,tamaño):
    a=dict()
    a["nombre"] = nombre
    a["tamaño"] = tamaño
    a["usado"] = False
    a["id"] = id(a)
    a["idp"] = None
    a["tamp"] = None
    return a

def CrearProcesos():
    p=list()
    p.append(Proceso("P1",25))
    p.append(Proceso("P1'",75))
    p.append(Proceso("p2",150))
    p.append(Proceso("P3",250))
    
    return p

def IniciarSO(me):
    for i in range(len(me)):
        if me[i]["nombre"]=="Sistema Operativo":
          RellenarParticion(me[i]["espacio"],0,"SO",len(me[i]["espacio"]))


#Nombre del proceso-----id de proceso-----id de inicio de la particion asignada-----tamaño de la particon asignada
def MostrarTabla(pro):
    print("-------------------------------------------------------------------------------")
    print("-----------------------**********   TABLA  **********--------------------------")
    print("-------------------------------------------------------------------------------")
    print("|  N. del Proceso  |  id proceso  | id Ini. de la Part Asig. | tamaño de Part |")
    for n in range(len(pro)):
        print("|    ",pro[n]["nombre"],"    |   ",pro[n]["id"],"    |       ",pro[n]["idp"],"   |   ",pro[n]["tamp"],"  |")
    print("-------------------------------------------------------------------------------")





#                                    programa General
memori=CrearMemoria()
#ordenar las particiones de menor a mayor tamaño de memoria
#ordenan los areglos pero solo si estan bacios
memori= sorted(memori, key=lambda Tpart : Tpart["espacio"])
IniciarSO(memori)
MostrarMemoriaActual(memori)
procesos=CrearProcesos()

#Advertencia--> codigo denso...
for i in range(len(procesos)):
    for j in range(len(memori)):
        if procesos[i]["tamaño"]<=MaximoLugarDisponible(memori[j]["espacio"])[0] and memori[j]["libre"]:
            RellenarParticion(memori[j]["espacio"],MaximoLugarDisponible(memori[j]["espacio"])[1],procesos[i]["nombre"],procesos[i]["tamaño"])
            memori[j]["libre"]=False
            procesos[i]["idp"]=id(memori[j]["espacio"][0])
            procesos[i]["tamp"]=len(memori[j]["espacio"])
            procesos[i]["usado"]=True
            break            
    if not procesos[i]["usado"]:
        print("El proceso ", procesos[i]["nombre"]," debe esperar")
#fin de codigo denso

MostrarMemoriaActual(memori)
MostrarTabla(procesos)

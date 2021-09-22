"""
1.2	Modificar la propuesta anterior con la posibilidad de cargar N procesos y utilizar particiones 
fijas. El programa debe permitir ingresar nuevos procesos, mientras haya memoria libre para asignar, 
por cada proceso se debe ingresar o leer de un archivo el Id de proceso, tamaño del proceso, tiempo 
de arribo y tiempo de irrupción. La tabla de particiones impresa deberá contener (Id de partición, 
dirección de comienzo de partición, tamaño de la partición, id de proceso asignado a la partición, 
fragmentación interna). 
Mostrar la información anterior por cada proceso ingresado en la tabla de particiones.
"""
#tiempo de arriblo= ? --> es el momento en el que llega el proceso a la cola de procesos
#tiempo de irrupcion= es lo que dura el proceso
# 

def menu():
    pass

# op mostrar procesos
# op nuevo proceso
#       verificar que los datos del proceso no exedan o den error en el proceso
# op salir/comenzar proceso

#aca creamos la particion
def Particion(nomb,cant):
    l=list()
    l=[None]*cant
    a=dict()
    a["nombre"] = nomb
    a["espacio"] = l
    a["libre"] = True
    a["DuracionDePro"] = None
    return a

#funcion para crear las particiones en una lista y la devolverla
def CrearMemoria():
    m = list()  
    m.append(Particion("Sistema Operativo",150))
    m.append(Particion("Particion 1",150))
    m.append(Particion("Particion 2",200))
    m.append(Particion("Particion 3",300))
    #antes hacer lo demas que es mas necesarioa
    #primero definir el sistema operativo y luego las demas particiones
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
    a["tdarr"] = None
    a["tdirr"] = None
    return a

def MostarProcesos(listP):
    print("")
    print("PROCESOS")
    print("-------------------------------------------------------------------------------")
    print("| Nombre  | Tamaño | Usado |   id   |   idp  | tam. P | T. De Arr | T. De Irr |")
    print("-------------------------------------------------------------------------------")
    for i in range(len(listP)):
        print("|",listP[i]["nombre"],"|",listP[i]["tamaño"],"|",listP[i]["usado"],"|",listP[i]["id"],"|",listP[i]["idp"],"|",listP[i]["tamp"],"|",listP[i]["tdarr"],"|",listP[i]["tdirr"],"|")
        print("-------------------------------------------------------------------------------") 

def CrearProcesos():
    p=list()
    p.append(Proceso("P1",75))
    p[0]["tdarr"]=0
    p[0]["tdirr"]=2
    p.append(Proceso("P2",25))
    p[1]["tdarr"]=0
    p[1]["tdirr"]=3
    p.append(Proceso("p3",150))
    p[2]["tdarr"]=7
    p[2]["tdirr"]=6
    """ 
    p.append(Proceso("P4",250))
    p[3]["tdarr"]=2
    p[3]["tdirr"]=7
    p.append(Proceso("P5",250))
    p[4]["tdarr"]=3
    p[4]["tdirr"]=8
    """

    return p

def IniciarSO(me):
    ban=True
    for i in range(len(me)):
        if me[i]["nombre"]=="Sistema Operativo":
            RellenarParticion(me[i]["espacio"],0,"SO",len(me[i]["espacio"]))
            if ban:
                me[i]["libre"] = False
                ban=False

#Nombre del proceso-----id de proceso-----id de inicio de la particion asignada-----tamaño de la particon asignada
def MostrarTabla(pro):
    pass

def CargarProcesosPosibles(proc,memo,proYa,tg):
    proFalt=list()
    for i in range(len(proc)):
        for j in range(len(memo)):
            if proc[i]["tamaño"]<=len(memo[j]["espacio"]) and memo[j]["libre"]:
                memo[j]["DuracionDePro"]=TiempoDeIrrupcion(memo,proc[i],tg)
                RellenarParticion(memo[j]["espacio"],0,proc[i]["nombre"],proc[i]["tamaño"])
                memo[j]["libre"]=False
                proc[i]["idp"]=id(memo[j]["espacio"][0])
                proc[i]["tamp"]=len(memo[j]["espacio"])
                proc[i]["usado"]=True
                proYa.append(proc[i]) 
                break            
        if not proc[i]["usado"]:
            proFalt.append(proc[i]) #agrego el proceso que no fue cargado a la memoria
            print("El proceso ", proc[i]["nombre"]," debe esperar")
    return proFalt

def LiberarParticion(part):
    part["libre"]=True
    part["espacio"]=[None]*len(part["espacio"])
    part["DuracionDePro"] = None


def TiempoDeIrrupcion(memAc,Elproc,Tg):
    c=0
    ban=True
    for x in range(len(memAc)):
        if memAc[x]["DuracionDePro"]!=None:
             c= c + memAc[x]["DuracionDePro"]
             ban=False
    c=Elproc["tdirr"]+c
    if ban:
        c=Elproc["tdirr"]+Tg
    return c

def ExisteProcesoEnMemoria(mem):
    for x in range(len(mem)):
        if mem[x]["DuracionDePro"]!=None:
            return True
    return False


#                                    programa General
memori=CrearMemoria()
#ordenar las particiones de menor a mayor tamaño de memoria
#ordenan los areglos pero solo si estan bacios
memori= sorted(memori, key=lambda Tpart : Tpart["espacio"])
IniciarSO(memori)
#MostrarMemoriaActual(memori)
procesos=CrearProcesos()                #Todos los procesos            
colaDeProcesos=list()                   #lista de procesos listos para cargar
procesosCargados=list()                 #lista de procecos procesados xd
MostarProcesos(procesos)

t=0
while len(procesos)!=0 or ExisteProcesoEnMemoria(memori):
    a=list()
    cambioM=False
    print(f"Tiempo = - {t} -")
    
    for i in range(len(procesos)):
        if t == procesos[i]["tdarr"]:
            print("cargo el proceso", procesos[i]["nombre"] ," a la cola de procesos")
            colaDeProcesos.append(procesos[i])
            print("borramos el proceso", procesos[i]["nombre"] ," de procesos generales")
            a.append(i)
    a.sort(reverse=True)
    
    for i in a:
        del procesos[i] 
    
    #cargar en memoria
    for i in range(len(colaDeProcesos)):
        if colaDeProcesos!=[] and colaDeProcesos[i]["tdarr"] <= t:
            colaDeProcesos=CargarProcesosPosibles(colaDeProcesos,memori,procesosCargados,t)
            cambioM=True
        
    for i in range(len(memori)):
        if memori[i]["DuracionDePro"] == t:
            print("el proceso de la particion ", memori[i]["nombre"] ,"-Termino- sale de memoria")
            LiberarParticion(memori[i])
            cambioM=True
    
    if cambioM:
        MostrarMemoriaActual(memori) 
    t=t+1

    


print(colaDeProcesos)
print(a)
MostrarMemoriaActual(memori)
print(colaDeProcesos)
print(procesosCargados)
for i in memori:
    print(i["DuracionDePro"])
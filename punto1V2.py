"""
1.1	Simular la administración en la asignación de memoria con particiones variables de DIFERENTES
tamaños para un sistema con 3 procesos P1, P2 y P3.   Se prevé asignar 150 b de memoria al núcleo
del Sistema Operativo. Los procesos tendrán los siguientes tamaños P1= 100 b, P2= 150 b, P3= 250 b.
Luego de la asignación deberá imprimirse la información contenida en una tabla de particiones.
La tabla de particiones contendrá la siguiente información (id Proceso, dirección de comienzo de
la partición asignada, tamaño de la partición).
"""
def Particion(nomb,cant):
    l=list()
    l=[None]*cant
    a=dict()
    a["nombre"] = nomb
    a["espacio"]=l
    return a
#aca vamos a definir nuestra cantidad de memoria y hacer las particiones
def CrearMemoria():
    m = list()  
    m.append(Particion("SO",15))
    m.append(Particion("Part1",10))
    m.append(Particion("Part2",15))
    m.append(Particion("Part3",25))
    return m


#aqui generaremos ls particiones para
def GeneracionDeParticiones(memoriaLimpia):
    try:
        con=0
        for i in range(700):
            memoriaLimpia[i]["espacio"] = con
            con=con+1
            if i < 150:  #esto seri de 0..149
                memoriaLimpia[i]["particion"] = 0
            elif i < 250:   #150..249
                memoriaLimpia[i]["particion"] = 1
            elif i < 400:   #250..399
                memoriaLimpia[i]["particion"] = 2
            else:   #400..699
                memoriaLimpia[i]["particion"] = 3
    except:
        print("ERROR DE TAMAÑO:el tamaño de memoria no es 700")

def MostrarMemoriaActual(me):
    c=0
    for i in range(len(me)//10):

        if i==0:
            print("sistema operativo")
        if i==15:
            print("particion 1")
        if i == 25:
            print("particion 2")
        if i == 40:
            print("particion 3")

        for j in range(10):
            print(me[c]["espacio"], end=" ")
            c=c+1
        print()
    print("--------------------------------------------------------------------------------")
    print()



"""memoria = CrearMemoria(700)
GeneracionDeParticiones(memoria)
MostrarMemoriaActual(memoria)"""

memori=CrearMemoria()
print(memori)
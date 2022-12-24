'''
Computación 2
Sección: 03

  EQUIPO:
    Castillo, Diógenis C.I: 28.063.541
    Ferrer, Emanuel C.I: 30.027.439 
    Speranza, Paola C.I: 27.307.788

'''

# variables de entrada

band = 0
band1 = 0
band2 = 0
jm = 0
conte = 0
CantTotal = 0
acu = 0

# variables de salida

por: float
pro: float
mcant: int
mjug: str

# lectura de archivos

arch = open('torneo.txt','r')
arch1 = open('resultados5.txt', 'w')

contenido = arch.readlines()
n = int(contenido[0])# cantidad de elementos de la lista externa
linea = 1  # Posición del primer elemento de la lista externa


for i in range(n): # ciclo para la cantidad de integrantes por grupo (lista externa)
    # lectura del grupo
    listaext = contenido[linea].split(', ')
    linea += 1 
    nom_grupo = str(listaext[0])
    print('Nombre del grupo: ', nom_grupo)
    cant_integrantes =  int(listaext[1])
    print('Cantidad de Integrantes: ', cant_integrantes)
    m = int(listaext[2]) # cantidad de elementos de la lista interna


    for j in range(m): # ciclo para los datos del grupo (lista interna)
        listaint = contenido[linea].split(', ')
        linea += 1 
        Nom_jugador = str(listaint[0])
        print('Nombre del jugador: ', Nom_jugador)
        Edad = int(listaint[1])
        print('Edad: ', Edad)
        Cant_ene_ext = int(listaint[2])
        print('Cantidad de enemigos exterminados: ', Cant_ene_ext)
        
        CantTotal = CantTotal + Cant_ene_ext # Cantidad por grupo de enemigos eliminados
        
        if Cant_ene_ext > 5:
            conte = conte + 1 # Contador jugadores que exterminaron mas de 5
            acu = acu + Edad 
        
        if Edad < 23:
            jm = jm + 1  # Contador jugadores menores de 23
            
        if band == 0:
            mcant = Cant_ene_ext
            mjug = Nom_jugador
            band = 1
        
        if Cant_ene_ext <= mcant: # jugador con menos cantidad de enemigos eliminados en el grupo
            mcant = Cant_ene_ext
            mjug = Nom_jugador
    
    if band1 == 0:
        Mene = CantTotal
        NMene = nom_grupo
        band1 = 0
        
    if Mene <= CantTotal: #Nombre del grupo con mayor cantidad enemigos exterminados.
        Mene = CantTotal
        NMene = nom_grupo
        
    if band2 == 0: 
        mene = mcant
        mnombre = mjug
        band2 = 1
        
    if mene >= mcant: # jugador con menos cantidad de enemigos eliminados en toda la lista
        mene = mcant
        mnombre = mjug
        
    arch1.write(str(nom_grupo) + ', ' + str(cant_integrantes)  + ', ' + str(CantTotal) + ' \n')
    
    por = (jm / cant_integrantes) * 100
    print('Porcentaje de jugadores menores de 23 años: %.2f' % por, '%')
    pro = (acu / conte)       
    print('Edad Promedio de los jugadores que eliminaron a más de 5 enemigos: %.2f' % pro, 'años')
    
    # Para el siguiente grupo
    jm = 0
    CantTotal = 0
    conte = 0
    mcant = 0
    acu = 0

print('Nombre del grupo con mayor cantidad enemigos exterminados: ', nom_grupo)    
print('Nombre del jugador que extermino a la menor cantidad de enemigos: ', mnombre)
        

arch.close()
arch1.close()
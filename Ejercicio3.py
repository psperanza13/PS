'''
Computación 2
Sección: 03

  EQUIPO:
    Castillo, Diógenis C.I: 28.063.541
    Ferrer, Emanuel C.I: 30.027.439 
    Speranza, Paola C.I: 27.307.788

'''


def leerarch(registro):   # Subprograma de lectura de archivos
    linea = registro.split(',')
    print(linea)
    
    x1 = float(linea[0])
    y1 = float(linea[1])
    r1 = float(linea[2])
    x2 = float(linea[3])
    y2 = float(linea[4])
    r2 = float(linea[5])
    
    return x1, y1, r1, x2, y2, r2
    
def relacion(x1, y1, r1, x2, y2, r2): # Subprograma que me relaciona las datos de dos circunferencias
    C1 = [(0.0,0.0),0.0] # Circunferencia de mayor radio
    C2 = [(0.0,0.0),0.0] # Circunferencia de menor radio
    
    if r1 > r2:
        C1 = [(x1, y1), r1]
        C2 = [(x2, y2), r2]
        
    elif r1 < r2:
        C2 = [(x1, y1), r1]
        C1 = [(x2, y2), r2]
        
    else:
        C1 = [(x1, y1), r1]
        C2 = [(x2, y2), r2]
        
    return C1, C2
        
    
def dist(x1, y1, x2, y2): # Subprograma distancia entre dos circunferencias
    import math
    d: float
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1)** 2)
    
    return d

def tang(x1, y1, r1, x2, y2, r2): # Subprograma para tipo de forma tangencial
    
    C1, C2 = relacion(x1, y1, r1, x2, y2, r2) 
    d = dist(x1, y1, x2, y2)
    t: int
    
    if d == (r1 + r2) and d != 0:
        t = 1
        
    elif d == 0 and r1 == r2:
        t = 4
        
    elif d == (r1 - r2) and d != 0:
        t = 2
        
    elif d != (r1 + r2) or d != (r1 - r2):
        t = 3       
       
    return t
        
        
def imp(arch, C1, C2, t):  # Subprograma para impresión de un archivo
    arch.write(f'{C1} {C2} {t}\n')

def main(): # Programa principal
    
    # lectura de archivos
    
    arch = open('circunferencias.txt', 'r')
    arch1 = open('resultados6.txt', 'w')
    
    # variables de entrada
    
    band = 0
    d = 0.0
    mr = 0.0
    mmr = 0.0
    mc1 = [(0.0,0.0),0.0]

    
    for registro in arch:
       
        x1, y1, r1, x2, y2, r2 = leerarch(registro)
        
        C1, C2 = relacion(x1, y1, r1, x2, y2, r2)
        print(C1, C2)
        t = tang(x1, y1, r1, x2, y2, r2)
        imp(arch1, C1, C2, t)
        
        C1[0], C1[1] = C1 
        mr = C1[1] # asignar el radio de la circunferencia mayor a una variable
        
        if band == 0: 
            mmr = mr
            C1 = mc1
            band = 1
            
        elif mmr < mr: # Comparación de radios
            mmr = mr
            mc1 = C1
                           
    arch1.write('Circunferencia con mayor radio: ' + str(mc1))

    arch.close()
    arch1.close()
            
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











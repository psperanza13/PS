# medidas


desviacion = 0.0
neumedicion = 0.0
peso_ideal = 1545.5
munidad = 0
mmedicion = 0
moperador = 0
band = 0



arch = open('medi.txt','r')
arch2 = open('MedidasDesviadas.txt', 'w')
arch3 = open('MedidasAceptadas.txt', 'w')

N = arch.readline()

for registro in arch:
    linea = registro.split(',')
    print(linea)

    
    Numero_operador = linea[0]
    print('Número del Operador:', Numero_operador)
    Medicion = float(linea[1])
    print('Medición Registrada:', Medicion)
    unidad_medicion = linea[2].rstrip("\n")
    print('Unidad de Medición Utilizada:', unidad_medicion) 


    if unidad_medicion == ' l':
        neumedicion = float((Medicion * 0.4536) * 1000)
        print('%.2f' % neumedicion)

    if unidad_medicion == ' k':
        neumedicion = float(Medicion * 1000) 
        print('%.2f' % neumedicion)
        
    desviacion = ((peso_ideal - neumedicion) / peso_ideal) * 100
    print('%.2f' % desviacion)
    
    if band == 0:
        mpordesviacion = desviacion
        munidad = unidad_medicion
        moperador = Numero_operador
        mmedicion = Medicion
        band = 1
        
    if desviacion > mpordesviacion:
        mpordesviacion = desviacion
        munidad = unidad_medicion
        moperador = Numero_operador
        mmedicion = Medicion
       
   
    if desviacion < 5:
        arch3.write(Numero_operador + ', ' + str(neumedicion) + 'g, ' + str(desviacion) + '% \n')
        print('Medida Aceptada: ', Numero_operador, ', ', neumedicion, ' g')
    
    else:
        arch2.write(Numero_operador + ', ' + str(neumedicion) + 'g, ' + str(neumedicion) + '% \n')
        print('Medida no Aceptada: ', Numero_operador, ', ', neumedicion, ' g')
                

arch.close()
arch2.close()
arch3.close()
    

print('Mayor porcentaje de desviacion: ', moperador, ', ', mmedicion, ', ', munidad)   

 

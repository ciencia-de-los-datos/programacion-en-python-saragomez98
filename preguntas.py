"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
    suma=0
    for num in columns:
        suma += int(num[1]) 
    return suma
  

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    from operator import itemgetter

    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        column1=[row[0]for row in columns]
    result=dict()
    for letra in column1:
        if letra in result.keys():
            result [letra]=result[letra]+1
        else:
            result[letra]=1
    tuplas=[(key,value) for key,value in result.items()]
    tuplas=sorted(tuplas,key=itemgetter(0))
    
    return tuplas
    


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    from multiprocessing import cpu_count
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        column1=[row[0]for row in columns]
        column2=[row[1] for row in columns]
        lista=list(zip(column1,column2))
    
    count_list = []
    letter_list=['A','B','C','D','E']
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    #count_list = []

    for i in range(len(lista)):
        if lista[i][0]  =='A':
            a_count += int(lista[i][1])
        elif lista[i][0] == 'B':
            b_count += int(lista[i][1])
        elif lista[i][0] == 'C':
            c_count += int(lista[i][1])
        elif lista[i][0] == 'D':
            d_count += int(lista[i][1])
        elif lista[i][0] == 'E':
            e_count += int(lista[i][1])
    
    count_list =[a_count,b_count,c_count,d_count,e_count]
    lista_final=list(zip(letter_list,count_list))
    print(lista_final)
    return lista_final


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        column1=[row[2]for row in columns]

    fecha= [z.split("-") for z in column1]
    mes=[row[1] for row in fecha]
 
    result=dict()
    for dato in mes:
        if dato in result.keys():
            result [dato]=result[dato]+1
        else:
            result[dato]=1
    
    tuplas=[(key,value) for key,value in result.items()]
    tuplas=sorted(tuplas,key=itemgetter(0))
    return tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        column1=[row[0:3] for row in columns]
    letras=sorted(set([x[0] for x in column1]))
    def valores(letra,column2):
        column2=[int(x[1]) for x in column1 if letra==x[0]]
        return column2
    
    result05=[((x,max(valores(x,column1)),min(valores(x,column1)))) for x in letras]
    return result05

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    from operator import itemgetter

    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
   
    listas=[row[4].split(",") for row in columns]

    result=[]
    for x in listas:
        for i in x:
            key=i[0:3]
            value=i[4:6]
            tupla=(str(key),int(value))
            result.append(tupla)
    result2={}
    for letra,valor in result:
        valor=int(valor)
        if letra in result2.keys():
            result2[letra].append(valor)
        else:
            result2[letra]=[valor]

    result06=[(key,min(value),max(value)) for key,value in result2.items()]
    result06=sorted(result06,key=itemgetter(0))

  
    return result06


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)

    result=[]
    for x in columns:
        key=x[0]
        value=x[1]
        tupla=(str(key),int(value))
        result.append(tupla)
    
    result2={}
    for letra,valor in result:
        valor=int(valor)
        if valor in result2.keys():
            result2[valor].append(letra)
        else:
            result2[valor]=[letra]
 
    result07=[(int(key),value) for key, value in result2.items()]
    result07=sorted(result07,key=itemgetter(0))

    return result07
    

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)

    result=[]
    for x in columns:
        key=x[0]
        value=x[1]
        tupla=(str(key),int(value))
        result.append(tupla)
   
    result2={}
    for letra,valor in result:
        valor=int(valor)
        if valor in result2.keys():
            result2[valor].append(letra)
        else:
            result2[valor]=[letra]
  
    result08=[(int(key),sorted(list(set(value)))) for key, value in result2.items()]
    result08=sorted(result08,key=itemgetter(0))
  
    return result08


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
  
    listas=[row[4].split(",") for row in columns]
   
    result=[]
    for x in listas:
        for i in x:
            key=i[0:3]
            value=i[4:6]
            tupla=(str(key),int(value))
            result.append(tupla)
 
    result2={}
    for letra,valor in result:
        valor=int(valor)
        if letra in result2.keys():
            result2[letra].append(valor)
        else:
            result2[letra]=[valor]
 
    result09=[(key,len(value)) for key,value in result2.items()]
    result09=sorted(result09,key=itemgetter(0))
    result09=dict(result09)

    return result09
  
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)

    result=[]
    for x in columns:
        letra=x[0]
        value1=x[3].split(',')
        value2=x[4].split(',')
        tupla=(letra,len(value1),len(value2))
        result.append(tupla)

    return result

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        lista= sorted([x[3] for x in columns])
        lista=[x.split(',') for x in lista]
        lista=sorted(set([x[y] for x in lista for y in range(len(x))]))

    result={}
    for x in lista:
        for y in columns:
            if x in y[3] and x not in result.keys():
                result[x]=int(y[1])
            elif x in y[3]:
                result[x]+=int(y[1])
    
    return result
    
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    from operator import itemgetter
    with open("data.csv",newline='') as file:
        data=csv.reader(file, delimiter='\t')
        columns= list(data)
        column1=sorted(set([row[0] for row in columns]))
  
    result12={}
    for letra in column1:
        for num in columns:
            if letra==num[0] and letra not in result12.keys():
                result12 [letra]=sum([int(i[4:]) for i in num[4].split(',')])
            elif letra==num[0]:
                result12[letra]+=sum([int(i[4:]) for i in num[4].split(',')])
  

    return result12

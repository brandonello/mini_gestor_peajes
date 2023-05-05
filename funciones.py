import pickle
import random
import os.path
import registro as re
'''
De cada Cobro, se tiene un número identificatorio,
  el nombre del puesto que hizo el cobro (una cadena para describirlo, terminada en punto. Por ejemplo:
   “Autopista Carlos Paz.”, “Córdoba acceso norte.”, etc), el monto cobrado, el domino o patente del auto al
    que se le cobró (una cadena), y la hora en que se le cobró (para simplificar, un número entero entre 0 y 23).

1. Generar un arreglo de registros que contenga los datos de todos los cobros que la empresa realizó.
 Puede generarlo en forma manual o aleatoria. No se exige que el arreglo se genere en forma ordenada.
'''

NOMBRES = ('Translasierras.', 'Paso Del Sur.', 'Sierras De Córdoba.', 'Norte Cordobés.', 'Córdoba acceso norte.',
           'Peaje del Centro.', 'Ruta de Nuevo Orizonte.', 'Peaje de Río Lindo.', 'Autopista Carlos Paz.')


ABC = ('a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x'
       , 'y', 'z')

def validar_peaje(nom_ingresado):
    nom_ingresado = nom_ingresado.lower()
    for nombre in NOMBRES:
        nombre = nombre[:-1]
        if nombre.lower() == nom_ingresado:
            return True
    return False

def menu():
    print(chr(27) + '[0;36m' + '-' * 12 + 'GESTOR DE PEAJES' + '-' * 12 + chr(27) + '[0m')
    print('1) Generar registros\n2) Mostrar registros\n3) Mostrar listado por id\n4) Determinar montos nocturnos\n'
          '5) Generar archivo cobros desde un puesto\n6) Mostrar archivo generado en op 5\n'
          '7) Informar peaje que cobro\n8) Cuántas mayúsculas en cadena')

def generar_registro(vec_cobros):
    for i in range(1000):
        id = random.randint(100000, 999999)
        nombre = random.choice(NOMBRES)
        monto = random.choice((70, 100, 150, 220, 350, 600))
        patente = random.choice(ABC).upper() + random.choice(ABC).upper() + random.choice(ABC).upper() +\
        str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        hora = random.randint(0, 23)
        cobro = re.Cobro(id, nombre, monto, patente, hora)
        add_in_order(vec_cobros, cobro)
    print("Registros generados correctamente")


def add_in_order(vec_cobros, objeto):
    n = len(vec_cobros)
    pos = n
    izq, der = 0, n -1

    while izq <= der:
        c = (izq + der) // 2

        if objeto.id == vec_cobros[c].id:
            pos = c
            break
        if objeto.id < vec_cobros[c].id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec_cobros[pos:pos] = [objeto]


def montos_acumulados(vec_cobros, nombre_peaje):
    vec_casillas = [0] * 24
    horas_noche = (20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6)


    for cobro in vec_cobros:
        if cobro.nombre.lower() == nombre_peaje and cobro.monto != 0 and cobro.hora in horas_noche:
            casilla = random.randint(0, 23)
            vec_casillas[casilla] += cobro.monto
    return vec_casillas


def monstrar_montos(vec_cobros, men):
    for cobro in vec_cobros:
        if cobro.monto >= men:
            print(cobro)


def busqueda_bin_num_id(vec_cobros, num_id):
    n = len(vec_cobros)
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if num_id == vec_cobros[c].id:
            return c

        if num_id < vec_cobros[c].id:
            der = c - 1

        else:
            izq = c + 1

    return -1


def archivo_cobros_xid(vec_cobros, nom_peaje):
    fd = 'CobrosXid.pydb'
    m = open(fd, 'wb')
    for cobro in vec_cobros:
        if cobro.nombre == nom_peaje:
            pickle.dump(cobro, m)
    m.close()
    print('El archivo', fd, 'se ha generado con éxito.')
    return fd

def mostar_archivo(archivo):

    if os.path.exists(archivo):
        size = os.path.getsize(archivo)
        m = open(archivo, 'rb')
        while m.tell() < size:
            cobro = pickle.load(m)
            print(cobro)
        m.close()
    else:
        print('El archivo no existe o no se ha cargado aún...')
        print('Utilice la opción 5 del menú')


def cobro_peaje(vec_cobros, p, h):
    for cobro in vec_cobros:
        if cobro.patente == p and cobro.hora == h:
            return cobro.nombre
    return 'No existe ese cobro...'


'''
8. Tome la cadena retornada en el punto 7 anterior, y determine cuántas palabras de esa cadena contienen al menos
 una letra mayúscula. Puede considerar que la cadena termina siempre con un punto, y que las palabras se separan entre
  ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada
   vuelta del ciclo que itere sobre ella.
'''

def mayus_en_palabras(cadena):
    cmayus = 0
    newword_ok = True
    for caracter in cadena:
        if caracter in '. ':
            newword_ok = True
        else:
            if 'A' <= caracter <= 'Z':
                if newword_ok:
                    cmayus += 1
                    newword_ok = False
    return cmayus



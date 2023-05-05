import funciones as fun

'''
Una empresa concesionaria de cabinas de peaje necesita un programa que le permita llevar estadísticas de las operatorias
 de los diferentes cobros realizados en sus puestos de peaje. De cada Cobro, se tiene un número identificatorio,
  el nombre del puesto que hizo el cobro (una cadena para describirlo, terminada en punto. Por ejemplo:
   “Autopista Carlos Paz.”, “Córdoba acceso norte.”, etc), el monto cobrado, el domino o patente del auto al
    que se le cobró (una cadena), y la hora en que se le cobró (para simplificar, un número entero entre 0 y 23).

En base a lo anterior, realizar un programa completo que a través de un menú de opciones y aplicando las
 validaciones que usted considere necesarias, realice los siguientes puntos:


1. Generar un arreglo de registros que contenga los datos de todos los cobros que la empresa realizó.
 Puede generarlo en forma manual o aleatoria. No se exige que el arreglo se genere en forma ordenada.

2. Muestre el arreglo generado, a razón de un registro por línea en la consola de salida.

3. Muestre un listado ordenado por número de identificación, de menor a mayor, pero que sólo contenga
 los datos de los registros cuyo importe pagado sea menor a un valor m que se pasa como parámetro.

4. Determine el monto acumulado que se cobró durante cada una de las 24 horas del día en las diferentes casillas
 de peaje (un total de 24 acumuladores). Pero muestre sólo los resultados que sean diferentes de 0 y que correspondan
  a horas nocturnas (horas entre las 20 y las 23, y entre las 0 y las 6).

5. Genere un archivo binario con todos los registros de cobros que se hicieron desde un puesto de cobro cuyo número
 de identificación id se pasa como parámetro.

6. Muestre el archivo generado en el punto 5, a razón de un registro por línea en la pantalla.

7. Informar si se le ha cobrado un peaje a un auto cuya patente es un valor p, a una determinada hora h,
 siendo p y h dos valores pasados como parámetro. Si existe ese cobro, retorne el nombre del puesto que hizo el cobro,
  y muéstre ese nombre en pantalla. Si no existiera tal cobro, informar con un mensaje.

8. Tome la cadena retornada en el punto 7 anterior, y determine cuántas palabras de esa cadena contienen al menos
 una letra mayúscula. Puede considerar que la cadena termina siempre con un punto, y que las palabras se separan entre
  ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada
   vuelta del ciclo que itere sobre ella.

'''


def main():
    op = -1
    vec_cobros = []
    fd = ''
    cadena_peaje = ''
    while op != 0:
        fun.menu()
        op = int(input('Ingrese un opción del menú: '))
        if op == 1:
            fun.generar_registro(vec_cobros)
        elif len(vec_cobros) == 0:
            print('Primero debe usar la opción 1 para cargar cobros!')
            continue

        elif op == 1:
            fun.generar_registro(vec_cobros)


        elif op == 2:
            for cobro in vec_cobros:
                print(cobro)

        elif op == 3:
            men = int(input('Ingrese el mínimo monto de cobro para mostrar cobros: '))
            fun.monstrar_montos(vec_cobros, men)

        elif op == 4:
            nombre_peaje = input('Ingrese el nombre del peaje: ')
            existe = fun.validar_peaje(nombre_peaje)
            if existe:
                nombre_peaje = nombre_peaje + '.'
                vec_casillas = fun.montos_acumulados(vec_cobros, nombre_peaje)
                for i in range(len(vec_casillas)):
                    print('La casilla número ' + str(i + 1) + ' acumuló $' + str(vec_casillas[i]))
            else:
                print('El nombre del peaje ingresado no existe...')
        elif op == 5:
            num_id = int(input('Ingrese el número id del cobro: '))
            indice = fun.busqueda_bin_num_id(vec_cobros, num_id)
            if indice == -1:
                print('El id de cobro no se ha encontrado...')
            else:
                nom_peaje = vec_cobros[indice].nombre
                fd = fun.archivo_cobros_xid(vec_cobros, nom_peaje)

        elif op == 6:

            fun.mostar_archivo(fd)

        elif op == 7:
            p = input('Ingrese la patente del auto al que se le cobró: ')
            p = p.upper()
            h = int(input('Ingrese la hora en un sólo número de formato 24h: '))
            nom = fun.cobro_peaje(vec_cobros, p, h)
            print(nom)
            cadena_peaje = nom

        elif op == 8:

            cant_pal_mayus = fun.mayus_en_palabras(cadena_peaje)
            print('La cantidad de palabras con al menos una mayúscula en la cadena es', cant_pal_mayus)

        elif op == 0:
            print('Hasta luego...')
            exit(-1)
        else:
            print('Debe ingresar una opción válida!')




if __name__ == '__main__':
    main()

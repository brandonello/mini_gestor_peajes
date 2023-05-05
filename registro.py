class Cobro:
    def __init__(self, id, nombre, monto, patente, hora):
        self.id = id
        self.nombre = nombre
        self.monto = monto
        self.patente = patente
        self.hora = hora

    def __str__(self):
        return 'ID: {:<10} | Nombre: {:<30} | Monto: ${:<10} | Patente: {:<8} | Hora: {}'\
            .format(self.id, self.nombre, self.monto, self.patente, self.hora)

class Tarjeta:
    def __init__(self, numero, id, nombre, codigo, vencimiento):
        self.numero= numero
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.vencimiento = vencimiento

    def __str__(self):
        return chr(27) + '[0;36m' + 'Código {:<10}'.format(self.codigo) + chr(27) + '[0m'


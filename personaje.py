class IOrigen:
    def accion():
        pass 

class Tanque(IOrigen):
    def accion(self):
        print('Se mueve 4 casillas y realiza ataque giratorio')

class Mago(IOrigen):
    def accion(self):
        print('Se mueve 3 casillas y lanza una bola de fuego')

class Necromante(IOrigen):
    def accion(self):
        print('Se mueve 2 casillas e invoca 1 esqueleto')

class Luchador(IOrigen):
    def accion(self):
        print('Se mueve 6 casillas y lanza una estocada')

class Juego:
    def __init__(self,personaje : IOrigen):
        super().__init__()
        self.personaje = personaje
    
    def moverse(self):
        self.personaje.accion()

class Personaje(Juego):
    def __init__(self, personaje: IOrigen):
        super().__init__(personaje)

if __name__ == '__main__':
    tanque,mago,necromante,luchador = Tanque(),Mago(),Necromante(),Luchador()
    opcion = int(input('Seccione para elegir clase \n'+
        '1. Tanque\n2. Mago\n3. Necromante\n4. Luchador\n'
    ))
    if opcion == 1:
        Personaje(tanque).moverse()
    elif opcion == 2:
        Personaje(mago).moverse()
    elif opcion == 3:
        Personaje(necromante).moverse()
    elif opcion == 4:
        Personaje(luchador).moverse()
    else:
        print('Elija bien pelao')
   
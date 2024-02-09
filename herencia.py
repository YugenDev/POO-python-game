class Personaje:
  nombre = "default"
  fuerza = 0
  inteligencia = 0
  defensa = 0
  vida = 0

  def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida

  def atributos(self):
    print("°Nombre:", self.nombre)
    print("°Fuerza:", self.fuerza)
    print("°Inteligencia:", self.inteligencia)
    print("°Defensa:", self.defensa)
    print("°Vida:", self.vida)

  def subir_nivel_de_atributos(self, fuerza, inteligencia, defensa):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa

  def esta_vivo(self):
    return self.vida > 0

  def morir(self):
    self.vida = 0
    print(f"El personaje *{self.nombre}* ha muerto")

  def daño(self, enemigo):
    return self.fuerza - enemigo.defensa

  def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
    if enemigo.esta_vivo():
      print("La vida de", enemigo.nombre, "es", enemigo.vida)
    else:
      enemigo.morir()


#empezamos a aplicar la herencia, estamos creando una clase nueva a partir del molde que ya tenemos, para decirle cual es la clsa de la cual va a heredar sus atributos y metodos se lo especificamos en el parentesis, así guerrero ya sabe cual es su clase padre de la cual hereda sus atributos y metodos.
class Guerrero(Personaje):

  #ahora vamos a hacer que nuestra clase guerrero tenga una caracteristica nueva, que es el arma que tiene, para esto vamos a agregar un nuevo atributo a nuestra clase utilizando el metodo __init__, en este caso le añadimos el atributo espada que será un bonus de daño.
  def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
    Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
    self.espada = espada

  #en esta funcion le damos la opción al usuario de que escoja cuanto bono de daño quiere según el arma que escoja
  def cambiar_arma(self):
    opcion = int(input("\x1b[1;33m"+"Elige un arma (1). Phantom, 8 de daño, (2). Vandal, 10 de año. --> "+"\x1b[0m "))
    if opcion == 1:
      self.espada = 8
    elif opcion == 2:
      self.espada = 10
    else:
      print("*****************************")
      print("\x1b[1;33m"+"ESA OPCIÓN NO EXISTE ESTUPIDO"+"\x1b[0m")
      print("*****************************")

  #Aqui simplemente modificamos la función atributos que ya teniamos antes para que también muestre el bono de daño que hace por el arma
  def atributos(self):
    Personaje.atributos(self)
    print("°Bono de daño por arma:", "\x1b[1;33m"+f"{self.espada}"+"\x1b[0m")

  #En esta función es donde aplicamos el bono de daño que causa la espada con la formula de fuerza * daño de arma - defensa del enemigo
  def daño(self, enemigo):
    return self.fuerza*self.espada - enemigo.defensa

#creacion de la Mago, el pirobo tiene un libro con el q hace chimbadas ahi raras
class Mago(Personaje):

  def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida)
      self.libro = libro
  
  def atributos(self):
      super().atributos()
      print("·Libro:", self.libro)
  
  def daño(self, enemigo):
      return self.inteligencia*self.libro - enemigo.defensa


#AHORA SI EL HIJUEPUTA COMBATEEEEEEE, función para combatir jiji jaja
def combate(jugador_1, jugador_2):
  turno = 0
  while jugador_1.esta_vivo() and jugador_2.esta_vivo():
      print("\nTurno", turno)
      print(">>> Acción de ", jugador_1.nombre,":", sep="")
      jugador_1.atacar(jugador_2)
      print(">>> Acción de ", jugador_2.nombre,":", sep="")
      jugador_2.atacar(jugador_1)
      turno = turno + 1
  if jugador_1.esta_vivo():
      print("\nHa ganado", jugador_1.nombre)
  elif jugador_2.esta_vivo():
      print("\nHa ganado", jugador_2.nombre)
  else:
      print("\nEmpate")

#se crean las instancias de las clases que van a pelear
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

#se muestran los atributos de los personajes/clases
personaje_1.atributos()
personaje_2.atributos()      

#se llama a la función de combate para que ahora si empiecen los guamasos
combate(personaje_1, personaje_2)
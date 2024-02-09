#Aqui hacemos la clase personaje, las clases son como plantillas para crear entidades, son como moldes para pastel, y las cosas que tiene dentro como los atributos/variables son los ingredientes y las acciones para hacer ese pastel son los metodos o funciones (def).

class Personaje:
  nombre = "default"
  fuerza = 0
  inteligencia = 0
  defensa = 0
  vida = 0

  #Aqui creamos el constructor de la clase, el constructor es una funcion que se ejecuta cuando le quieres medificar el valor a esas variables/atributos que creamos antes en la clase.
  def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida

  #aqui creamos el metodo atibutos, esto es es como una funcion dentro de la clase que sirve para mostrar los atributos mediante los print.
  def atributos(self):
    print("°Nombre:", self.nombre)
    print("°Fuerza:", self.fuerza)
    print("°Inteligencia:", self.inteligencia)
    print("°Defensa:", self.defensa)
    print("°Vida:", self.vida)

  #este es el metodo que nos sirve para subir de nivel los atributos del personaje, esto se hace haciendo referencia al atributo que queremos subir y le sumamos un valor, ese valor se lo daremos despues cuando estemos llamando la función por fuera de la clase.
  def subir_nivel_de_atributos(self, fuerza, inteligencia, defensa):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa

  #Este metodo nos sirve para verificar si el personaje esta vivo, si su vida es mayor a 0 quiere decir que sigue vivo
  def esta_vivo(self):
    return self.vida > 0
    
  #Este metodo ejecuta la muerte del personaje
  def morir(self):
    self.vida = 0
    #la f al principio de la función print es para que se pueda llamar a una variable dentro del texto utilizando {}.
    print(f"El personaje *{self.nombre}* ha muerto")

  #Este metodo es el que define como funciona el daño, en este caso el daño se calcula con la fuerza del personaje la cual se le resta el valor que tenga la defensa de enemigo, por ejemplo si tu fuerza es de 5 y la defensa de tu enemigo es de 3, el daño seria 2.
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

# AQUI es donde le estamos asignando los valores a los atributos de la clase personaje, esto es lo que se llama instanciar una clase, que basicamente es crear y trabajar con una representación de la entidad que creamos antes, aqui le damos sus valores a los atributos en orden.
mi_personaje = Personaje("urato", 10, 1, 6, 100)
#Aca volvemos a hacer una instancia de la clase personaje, pero esta vez para representar a un enemigo 
mi_enemigo = Personaje("programacion", 7, 10, 5, 100)

#Aqui simplemente estamos mostrando por consola los atributos del personaje y sus respectvos valores antes y despues de utilizar la función subir_nivel_de_atributos.
print("El personaje se llama:" , mi_personaje.nombre)
print("Tiene una fuerza de:" , mi_personaje.fuerza)
print("Tiene una inteligencia de:" , mi_personaje.inteligencia)
print("Tiene una defensa de:" , mi_personaje.defensa)
print("\x1b[1;33m"+"Antes de subir de niveles con la funcion"+"\x1b[0m")
mi_personaje.atributos()
print("\x1b[1;33m"+"despues de subir de niveles con la def subir_nivel"+"\x1b[0m")
#aca se le suman los valores a los atributos del personaje mediante el llamado de la funcion subir_nivel_de_atributos.
mi_personaje.subir_nivel_de_atributos(1,1,1)
mi_personaje.atributos()

#A partir de aca empieza la pelea
print("\x1b[1;33m"+"******Pelea******"+"\x1b[0m")
print("(como abajo volvemos a instanciar a los personajes ya la def de subir nivel no se aplica pq reescribmos los datos de los personajes a estos de abajo)")
mi_personaje = Personaje("urato", 10, 1, 6, 100)
mi_enemigo = Personaje("programacion", 7, 10, 5, 100)

mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
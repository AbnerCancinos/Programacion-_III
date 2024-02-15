
from graphviz import Digraph   # Utilizaremos esto para poder tbajar con graphviz 


class Nodo(object):     #Clase que hereda de objeto 
    def __init__(self, datos = None, Nombre = None, apellido = None, siguiente =None, anterior = None):  # Estos son los componentes que contiene un nodo 
        self.datos = datos
        self.Nombre = Nombre
        self.apellido= apellido
        self.siguiente =siguiente
        self.anterior=anterior

class Lista (object):   #Estos componentes definene a las listas para el inicio y el anterior
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def insertarInicio(self, datos, nombre, apellido  ):    #metodo que recibe como parametro un datos de la funcion Menu 
        nodo = Nodo(datos, nombre, apellido)      #Instanciamos la clase nodo 
        if self.cabeza is None: #condicion para evaluar si ya hay datos dentro de la lista 
            self.cabeza = nodo
            self.cola = nodo
            print(f"\nSE ALMACENO CON EXITO LOS VALOR")
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo # aqui se define que el elemento del nuevo nodo, el anteior apuntara al nodo que almacenamos de primero 
            self.cabeza = nodo
            print(f"\nSE ALMACENO CON EXITO LOS VALOR ")

    def insertarFinal(self, datos, nombre, apellido): # Corregido para recibir tres argumentos
        nodo = Nodo(datos, nombre, apellido)
        if self.cola is None:
            self.cabeza = nodo
            self.cola = nodo
            print("\nSE ALMACENO CON EXITO LOS VALORES ")
        else:
            self.cola.siguiente = nodo
            nodo.anterior = self.cola 
            self.cola = nodo
            print("\nSE ALMACENO CON EXITO LOS VALORES ")

    def mostrarDatos(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print("\nNo. Carnet:", nodo_actual.datos)
            print("Nombre:", nodo_actual.Nombre)
            print("Apellido:", nodo_actual.apellido)
            print("-------------------------------")
            nodo_actual = nodo_actual.siguiente #despues de mostrar el dato que el nodo_actual apunte al siguiente 

    def eliminar(self, dato):# para eliminarlos solo utilizaremos el No. de carnet
        nodo_actual = self.cabeza #variable auxiliar 
        while nodo_actual is not None:
            if nodo_actual.datos == dato: #aqui comprobamos si la informacion es igual 
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente #ctualizacion de los enlaces 
                else:
                    self.cabeza = nodo_actual.siguiente #en caso si el nodo a eliminar es la cabeza
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior #la misma logica de actulizacion de enlaces 
                else:
                    self.cola = nodo_actual.anterior#en caso si el nodo a eliminar es la cabeza
                return True  # Indica que se encontró y eliminó el nodo
            nodo_actual = nodo_actual.siguiente
        return False  # Indica que no se encontró el dato en ningún nodo


    def graficar(self):

        diagrama = Digraph(comment='Lista Doblemente Enlazada') #se crea un objeto de diagrapvia llamado diagrama 
        nodo_actual = self.cabeza #utilizaremos una variable auxiliar para iterar y no cambiar la posicion de la cabeza 
        while nodo_actual is not None:
            #esto es direccion de la memoria y en donde lo almacenara 
            diagrama.node(str(id(nodo_actual)), str(nodo_actual.datos))
            if nodo_actual.siguiente is not None: #comprobar si un doto tiene conexcion para enlazarlos 
                diagrama.edge(str(id(nodo_actual)), str(id(nodo_actual.siguiente)), label="sigui", minlen="2", constraint="true", penwidth="2")
            if nodo_actual.anterior is not None:
                diagrama.edge(str(id(nodo_actual)), str(id(nodo_actual.anterior)), label="ante", minlen="2", constraint="true", penwidth="2")
            nodo_actual = nodo_actual.siguiente
        diagrama.render('Listas Enlazadas/IMG/imagenes', format='png', cleanup=True) #en esta seccion recordemos que ya se esta ejecutando de la carpeta de Listad Enlazadas entonces solo necesitaremos colocar la carpeta en donde se almacenara 

def Menu():
    lista = Lista()
    while True:
        print("\nMenu:")
        print("1. Añadir Elemento al inicio")
        print("2. Añadir Elemento al Final")
        print("3. Eliminar por valor")
        print("4. Mostrar valores")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            elemento = input("Ingrese el No. de Carnet: ")
            elemento2 = input("Ingrese el Nombre: ")
            elemento3 = input("Ingrese el Apellido: ")
            lista.insertarInicio(elemento, elemento2, elemento3)
            lista.graficar()
        elif opcion == "2":
            elemento = input("Introduce el No. de Carnet: ")
            elemento2 = input("Ingrese el Nombre: ")
            elemento3 = input("Ingrese el Apellido: ")
            lista.insertarFinal(elemento, elemento2, elemento3) 
            lista.graficar()
        elif opcion == "3":
            valor = input("Introduce el NUMERO DE CARNET CORREO PARA ELIMINAR EL NODO: ")
            lista.eliminar(valor)
            print(f"\nSE ELIMINO CON EXITO LOS VALORES ")
            lista.graficar()
        elif opcion == "4":
            lista.mostrarDatos()
        elif opcion == "5":
            print("Saliendo del programa.... ") 
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__": #esto es para que el script de python el menu sea el principal 
    Menu()

            



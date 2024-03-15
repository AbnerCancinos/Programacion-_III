import os
import graphviz

class Nodo:
    #Elemetos que tendra el nodo
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BuscarResultado:
    #Nos ayudara para evaluar el tipo de nodo, hoja, raiz o padre
    def __init__(self, value, node_type):
        self.value = value
        self.node_type = node_type  

class ArbolBinario:
    def __init__(self):
        #La raiz que tendra el arbol
        self.root = None

    def insert(self, value):
        try:
            value = int(value)  #Caso base para saber si es raiz, en caso de no tener valores 
            if not self.root:
                self.root = Nodo(value)
            else:
                self.insert2(self.root, value)
                self.visualize_tree()   # metodo que tiene con graphviz
        except ValueError:
            print("Error: Ingrese un número entero válido")

    def insert2(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Nodo(value)
            else:
                self.insert2(node.left, value)  #Recursividad para que recorra todo el lado izquierdo 
        elif value > node.value:
            if node.right is None:
                node.right = Nodo(value)
            else:
                self.insert2(node.right, value) #Recursividad para que recorra todo el lado derecho 


    def visualize_tree(self):
        dot = graphviz.Digraph()    #para poder trabajar con graphviz
        self._visualize_tree_recursive(self.root, dot)
        #Direccion por donde se guardara la imagen de graphviz
        dot.render('Arboles_binarios/IMG/imagenes', format='png', cleanup=True)

    def _visualize_tree_recursive(self, node, dot):
        if node:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._visualize_tree_recursive(node.left, dot)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._visualize_tree_recursive(node.right, dot)

     # Nuevo Método: Recorrido in-orden
    def in_order_traversal(self):
        self._in_order_traversal_recursive(self.root)
        print()

    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.value, end=" ") #  el end solo funciona para que no tener el espacio entre cada valor 
            self._in_order_traversal_recursive(node.right)

    # Nuevo Método: Recorrido post-orden
    def post_order_traversal(self):
        self._post_order_traversal_recursive(self.root)
        print()

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.value, end=" ")

    # Nuevo Método: Recorrido pre-orden
    def pre_order_traversal(self):
        self._pre_order_traversal_recursive(self.root)
        print()

    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def metodo_buscar(self, value):
        result = self.metodo_buscar2(self.root, value)
        if result:
            return result
        else:
            return None

    def metodo_buscar2(self, node, value):
        if node is None:
            return None
        elif value == node.value:   # si el valor que enviamos como parametro es igual a la raiz devueve la raiz 
            if node == self.root:
                return BuscarResultado(value, "RAIZ")
            elif node.left or node.right:
                if node.left and node.right:    #condicion para asignarle un hijo o los dos hijos que tiene el padre 
                    return BuscarResultado(value, "CON_HIJOS")
                else:
                    return BuscarResultado(value, "HIJO")
            else:
                return BuscarResultado(value, "HOJA")
        elif value < node.value:
            return self.metodo_buscar2(node.left, value)    #metodo recursivo siempre para recorrer el lado izquierdo 
        else:
            return self.metodo_buscar2(node.right, value)       #metodo recursivo siempre para recorrer el lado derecho  
        

    def delete(self, value):
        if self.metodo_buscar(value):    #para eliminar de primero debemos de buscar el valor 
            self.root = self._delete_recursive(self.root, value)
            self.visualize_tree()
            print(f"Nodo con valor {value} eliminado correctamente.")
        else:
            print(f"No se Encontro el nodo con valor {value} en el árbol.")

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value) #recursividad para recorrer todo el lado izquierdo  
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)  #recursividad para recorrer todo el lado derecho  
        else:
            if node.left is None:   #en todo caso que el nodo tenga hijos 
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)
        return node

    def _find_min(self, node):  #Este metodo encuentra el nodo con valor minimo
        while node.left is not None: #reemplazando hacia la izquierda hasta encontrar un nodo hijo
            node = node.left
        return node
    
    def metodo_arhivo(tree):
        filename = input ("Ingrese la Ruta del Archivo: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip() #Estos el .strip y .isdigit es para leer el archivo por los espacio o lineas
                    if line.isdigit():
                        value = int(line)
                        tree.insert(value)
                    else:
                        print(f"Datos cargados correctamente desde el archivo.")
        except FileNotFoundError:   # Esta se utiliza en caso que no se encuentre el archivo 
            print("El archivo especificado no se encuentra.")
        except ValueError: # en todo caso si el valor del archivo como contiene numero 
            print("Error al convertir los datos del archivo a números enteros.")

def main():
    Arbol = ArbolBinario()
    while True:
        print("\n----- MENU -----")
        print("1. Insertar un valor")
        print("2. Mostrar Recorrido in-orden")
        print("3. Mostrar Recorrido post-orden")
        print("4. Mostrar Recorrido pre-orden")
        print("5. Buscar un valor")
        print("6. Eliminar un valor")
        print("7. Cargar archivo con datos binario")
        print("8. Salir del programa")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            datos = input("Ingrese el valor que desea insertar: ")
            try:
                value = int(datos) #El valor que almacenamos lo guarda como entero 
                Arbol.insert(value)
            except ValueError:
                print("Error: Ingrese un número entero válido")
            Arbol.visualize_tree()
        elif opcion == '2':
            print("Recorrido in-orden:")
            Arbol.in_order_traversal()
        elif opcion == '3':
            print("Recorrido post-orden:")
            Arbol.post_order_traversal()
        elif opcion == '4':
            print("Recorrido pre-orden:")
            Arbol.pre_order_traversal()
        elif opcion == '5':
            datos = int(input("Ingrese el valor que desea buscar: "))
            resultado = Arbol.metodo_buscar(datos)
            if resultado:
                print(f"El valor {resultado.value} se encuentra en un nodo de tipo {resultado.node_type}.")
            else:
                print(f"El valor {resultado} no se encuentra en el árbol.")
                Arbol.pre_order_traversal()
        elif opcion == '6':
            value = int(input("Ingrese el valor que desea eliminar: "))
            Arbol.delete(value)
        elif opcion == '7':
            Arbol.metodo_arhivo()
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()




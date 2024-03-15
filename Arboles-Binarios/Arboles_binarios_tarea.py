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







# from graphviz import Digraph   # Utilizaremos esto para poder tbajar con graphviz 
# import os

# class NodoA:
#     def __init__(self, valor):
#         self.valor = valor
#         self.izq = None
#         self.dere = None

# class ABB: 
#     def __init__(self):
#         self.raiz = None
#         self.graph = Digraph(comment='Árbol Binario')


#     def insert(self, valor): 
#         if self.raiz is None:
#             self.raiz = NodoA(valor)
#         else:
#             self.insert2(valor, self.raiz)
#         self.mostrar()

#     def insert2(self, valor, nodo):
#         if int(valor) < int(nodo.valor):
#             if nodo.izq is None:
#                 nodo.izq = NodoA(valor)
#             else:
#                 self.insert2(valor, nodo.izq)
#         elif int(valor) > int(nodo.valor):
#             if nodo.dere is None:
#                 nodo.dere = NodoA(valor)
#             else:
#                 self.insert2(valor, nodo.dere)

#     def buscar(self, valor):
#         encontrado = self.buscar2(valor, self.raiz)
#         if encontrado:
#             print(f"El valor {valor} se encontró en el árbol.")
#         else:
#             print(f"El valor {valor} no se encontró en el árbol.")

#     def buscar2(self, valor, nodo):
#         if nodo is None:
#             return False
            
#         if nodo.valor == valor:
#             return True
            
#         encontrado_izq = self.buscar2(valor, nodo.izq)
#         encontrado_dere = self.buscar2(valor, nodo.dere)
        
#         return encontrado_izq or encontrado_dere


#     def inorder(self, nodo):
#         if nodo != None:
#             self.inorder(nodo.izq)
#             print(nodo.valor)
#             self.inorder(nodo.dere)

#     def postorden(self, nodo):
#         if nodo != None:
#             self.postorden(nodo.izq)
#             self.postorden(nodo.dere)
#             print(nodo.valor) # practicamente es la raiz 

#     def preorden(self, nodo):
#         if nodo != None:
#             print(nodo.valor)
#             self.preorden(nodo.izq)
#             self.preorden(nodo.dere)

#     def archvivos(self, ruta):
#         if os.path.exists(ruta) and os.path.splitext(ruta)[1] == '.txt':
#             with open(ruta, "r") as archivo:
#                 contenido = archivo.read()
#                 # Separar los valores por espacios o por líneas
#                 valores = contenido.split() if ' ' in contenido else contenido.splitlines()
#                 if self.raiz is not None:
#                     eliminar_todo = input("El árbol binario ya contiene datos. Para ingresar debe de eliminar los anteriores (s/n): ")
#                     if eliminar_todo.lower() == 's':
#                         self.raiz = None
#                         print("Se han eliminado todos los datos del árbol binario.")
#                     else:
#                         print("No se han insertado los nuevos datos en el árbol binario.")
#                         return
#                 for valor in valores:
#                     try:
#                         entero = int(valor)
#                         self.insert(entero)
#                     except ValueError:
#                         print(f"El valor '{valor}' no es un entero y no se ha insertado en el árbol.")
#         else:
#             print("La ruta no es válida o no es un  archivo de texto.")


#     def _eliminar(self, nodo, valor):
#         if nodo is None:
#             return None
#         if valor < nodo.valor:
#             nodo.izq = self._eliminar(nodo.izq, valor)
#         elif valor > nodo.valor:
#             nodo.dere = self._eliminar(nodo.dere, valor)
#         else:
#             if nodo.izq is None:
#                 return nodo.dere
#             elif nodo.dere is None:
#                 return nodo.izq
#             else:
#                 temp = nodo.dere
#                 while temp.izq:
#                     temp = temp.izq
#                 nodo.valor = temp.valor
#                 nodo.dere = self._eliminar(nodo.dere, temp.valor)

#         # Eliminar conexiones en el grafo de Graphviz
#         self.graph.node(str(valor), style='invisible')  # Ocultar el nodo eliminado
#         return nodo

#     def eliminar_conexiones(self, nodo, valor):
#         if nodo is None:
#             return
#         if nodo.izq and nodo.izq.valor == valor:
#             nodo.izq = None
#         elif nodo.dere and nodo.dere.valor == valor:
#             nodo.dere = None
#         else:
#             self.eliminar_conexiones(nodo.izq, valor)
#             self.eliminar_conexiones(nodo.dere, valor)

#     def mostrar(self):
#         self.graph.attr(rankdir='TB')  # Orientación de arriba hacia abajo
#         self.graph.attr('node', shape='circle')  # Forma de los nodos
#         self.graph.attr('node', width='0.5')  # Ancho de los nodos
#         self.graph.attr('node', style='filled')  # Estilo de los nodos
#         self.graph.attr('graph', nodesep='1')  # Separación entre nodos
#         self.graph.attr('graph', ranksep='1')
#         self._mostrar_arbol(self.raiz)
#         self.graph.render('Arboles_binarios/IMG/imagenes', format='png', cleanup=True)

#     def _mostrar_arbol(self, nodo):
#         if nodo is not None:
#             if nodo.izq is not None:
#                 self.graph.edge(str(nodo.valor), str(nodo.izq.valor))
#             if nodo.dere is not None:
#                 self.graph.edge(str(nodo.valor), str(nodo.dere.valor))
#             self._mostrar_arbol(nodo.izq)
#             self._mostrar_arbol(nodo.dere)




# def menu():
#     arbolBinario = ABB()
#     while True: #bucle que se repetira hasta que seleccione la opcion 8 
#         print("\n-----CONTENIDO DEL MENU-------")
#         print("1. Insertar un valor")
#         print("2. Mostrar Recorrido in-orden")
#         print("3. Mostrar Recorrido post-orden")
#         print("4. Mostrar Recorrido pre-orden")
#         print("5. Buscar un valor")
#         print("6. Eliminar un valor")
#         print("7. Cargar archivo con datos binario")
#         print("8. Salir del programa")
#         option = input("Seleccione la opción que desee: ")
        
#         if option == "1":
#             valor = input("Ingrese un valor para insertar en el árbol: ")
#             arbolBinario.insert(valor)
#         elif option == "2":
#             print("Recorrido in-orden:")
#             # le enviamos como parametro la raiz inicial del arbol 
#             arbolBinario.inorder(arbolBinario.raiz)
#         elif option == "3":
#             print("Recorrido post-orden:")
#             arbolBinario.postorden(arbolBinario.raiz)
#         elif option == "4":
#             print("Recorrido pre-orden:")
#             arbolBinario.preorden(arbolBinario.raiz)
#         elif option == "5":
#             respuesta = input("Ingrese el valor que desea buscar")
#             arbolBinario.buscar(respuesta)
#         elif option == "6":
#             respuesta = input("Ingrese el valor que desea Eliminar")
#             arbolBinario._eliminar(arbolBinario.raiz, respuesta)
#         elif option == "7":
#             respuesta = input("Ingrese la ruta del archivo")
#             arbolBinario.archvivos(respuesta)
#         elif option == "8":
#             print("Saliendo del programa....")
#             break
#         else:
#             print("Ingrese una opción dentro del rango")


# if __name__ == "__main__": #esto es para que el script de python el menu sea el principal 
#     menu()
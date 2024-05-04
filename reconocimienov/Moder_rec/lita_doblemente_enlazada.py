class Nodo:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        
    def es_vacio(self):
        return self.cabeza is None
    
    def insertar(self, data):
        nuevo_nodo = Nodo(data)
        if self.es_vacio():
            self.cabeza = self.ultimo = nuevo_nodo
        else:
            self.ultimo.next = nuevo_nodo
            nuevo_nodo.prev = self.ultimo
            self.ultimo = nuevo_nodo
            
    def mostrar(self):
        nodo = self.cabeza
        while nodo:
            print(nodo.data, end = " <-> " if nodo.next else "")
            nodo = nodo.next
        print()
        
    def delete(self, data):
        if self.es_vacio():
            return
        
        current_node = self.cabeza
        
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.cabeza = current_node.next
                
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.ultimo = current_node.prev

                return
            
            current_node = current_node.next

# Uso de la lista doblemente enlazada
lista = ListaDoblementeEnlazada()
for i in range(1, 6):
    lista.insertar(i)

print("Antes de eliminar:")
lista.mostrar()

lista.delete(5)
print("\nLuego de eliminar:")
lista.mostrar()

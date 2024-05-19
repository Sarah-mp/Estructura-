from modelo import clf

class Nodo:
    def __init__(self, modelo, correo=None, es_spam=None):
        self.modelo = modelo #Guarda el modelo de clasificación en la instancia del no
        self.correo = correo # Almacena el correo electrónico en el nodo.
        self.es_spam = es_spam #  Almacena la clasificación del correo (spam o no).
        self.izquiero = None
        self.derecha = None


class ArbolSpam:
    izquierda = None # Inicializa el hijo izquierdo del nodo.
    derecha = None # Inicializa el hijo derecho del nodo.
    modelo = None
    def __init__(self, raiz=None):
        self.raiz = raiz
        
    def evaluar_correo(self, correo):
        # Usar el modelo para predecir si el correo es spam o no
       
        prediccion = self.modelo.predict([correo])[0] # devuelve una lista, obtiene el resultado para el correo dado.
        return prediccion  
    
    def _insertar(self, valor, nodo):
        if valor < nodo.es_spam:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)

    def insertar(self, correo):  #  Define cómo insertar un nuevo correo en el árbol.
        #  Si el nodo actual no tiene correo, lo asigna y evalúa si es spam.
        self.correo = correo # Asigna el correo al nodo.
        self.es_spam = self.evaluar_correo(correo)  #Evalúa el correo y almacena el resultado.
        nodo = Nodo(self.modelo, correo, self.es_spam) 
        print("="*50)
        print(correo)
        self._insertar(self.es_spam, nodo)
        
    """
    def insertar_copia(self, correo):  #  Define cómo insertar un nuevo correo en el árbol.
        if self.correo is None: #  Si el nodo actual no tiene correo, lo asigna y evalúa si es spam.
            self.correo = correo # Asigna el correo al nodo.
            self.es_spam = self.evaluar_correo(correo)  #Evalúa el correo y almacena el resultado.
        else:
            
            print("="*50)
            print(correo)
            if self.es_spam == 1:  # Si el correo en el nodo es spam, intenta insertar el nuevo correo en el subárbol derecho.
                if self.derecha is None: # Si no hay hijo derecho, crea un nuevo nodo.
                    self.derecha = Nodo(self.modelo) 
                self.derecha.insertar(correo)  #  Inserta el correo en el subárbol derecho.
            else:
                # Si el correo no es spam, sigue un proceso similar para el subárbol izquierdo.
                if self.izquierda is None:
                    self.izquierda = Nodo(self.modelo)
                self.izquierda.insertar(correo)
    """
    def imprimir(self):  # Define cómo imprimir todos los correos en el árbol.
        if self.izquierda:  # Si hay un subárbol izquierdo, lo imprime primero (recorrido inorden
            self.izquierda.imprimir()
        print('Correo:', self.correo, '| Es spam:', 'Sí' if self.es_spam else 'No') # Imprime la información del correo en el nodo actual.
        if self.derecha:
            self.derecha.imprimir()  # Luego, imprime el subárbol derecho.


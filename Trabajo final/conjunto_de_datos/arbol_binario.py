from modelo import clf

class Nodo:
    def __init__(self, modelo, correo=None, es_spam=None):
        self.modelo = modelo #Guarda el modelo de clasificación en la instancia del no
        self.correo = correo # Almacena el correo electrónico en el nodo.
        self.es_spam = es_spam #  Almacena la clasificación del correo (spam o no).
        self.izquierda = None # Inicializa el hijo izquierdo del nodo.
        self.derecha = None # Inicializa el hijo derecho del nodo.

    def evaluar_correo(self, correo):
        # Usar el modelo para predecir si el correo es spam o no
       
        prediccion = self.modelo.predict([correo])[0] # devuelve una lista, obtiene el resultado para el correo dado.
        return prediccion  

    def insertar(self, correo):  #  Define cómo insertar un nuevo correo en el árbol.
        if self.correo is None: #  Si el nodo actual no tiene correo, lo asigna y evalúa si es spam.
            self.correo = correo # Asigna el correo al nodo.
            self.es_spam = self.evaluar_correo(correo)  #Evalúa el correo y almacena el resultado.
        else:
           
            if self.es_spam == 1:  # Si el correo en el nodo es spam, intenta insertar el nuevo correo en el subárbol derecho.
                if self.derecha is None: # Si no hay hijo derecho, crea un nuevo nodo.
                    self.derecha = Nodo(self.modelo) 
                self.derecha.insertar(correo)  #  Inserta el correo en el subárbol derecho.
            else:
                # Si el correo no es spam, sigue un proceso similar para el subárbol izquierdo.
                if self.izquierda is None:
                    self.izquierda = Nodo(self.modelo)
                self.izquierda.insertar(correo)

    def imprimir(self):  # Define cómo imprimir todos los correos en el árbol.
        if self.izquierda:  # Si hay un subárbol izquierdo, lo imprime primero (recorrido inorden
            self.izquierda.imprimir()
        print('Correo:', self.correo, '| Es spam:', 'Sí' if self.es_spam else 'No') # Imprime la información del correo en el nodo actual.
        if self.derecha:
            self.derecha.imprimir()  # Luego, imprime el subárbol derecho.


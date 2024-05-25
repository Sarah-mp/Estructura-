class Nodo:
    def __init__(self, modelo, correo=None, es_spam=None):
        # Inicializa un nodo con un modelo de clasificación, un correo opcional, y su etiqueta (spam o no spam).
        self.modelo = modelo
        self.correo = correo
        self.es_spam = es_spam
        self.izquierdo = None  # Inicializa el nodo hijo izquierdo como None.
        self.derecho = None    # Inicializa el nodo hijo derecho como None.

    def insertar(self, correo):
        # Usa el modelo del nodo para predecir si el correo dado es spam. predict devuelve un array, [0] toma el primer elemento.
        es_spam = self.modelo.predict([correo])
        if es_spam == 0:  # Si el correo no es spam
            if self.izquierdo is None:
                # Si no hay nodo izquierdo, crea uno nuevo con el correo como no spam.
                self.izquierdo = Nodo(self.modelo, correo, es_spam)
            else:
                # Si hay un nodo izquierdo, inserta recursivamente el correo en el subárbol izquierdo.
                self.izquierdo.insertar(correo)
        else:  # Si el correo es spam
            if self.derecho is None:
                # Si no hay nodo derecho, crea uno nuevo con el correo como spam.
                self.derecho = Nodo(self.modelo, correo, es_spam)
            else:
                # Si hay un nodo derecho, inserta recursivamente el correo en el subárbol derecho.
                self.derecho.insertar(correo)

    def imprimir(self):
        # Imprime primero el subárbol izquierdo (recursivamente), si existe.
        if self.izquierdo:
            self.izquierdo.imprimir()
        # Imprime la información del nodo actual.
        print('Correo:', self.correo, '| Es spam:', 'Sí' if self.es_spam else 'No')
        # Imprime después el subárbol derecho (recursivamente), si existe.
        if self.derecho:
            self.derecho.imprimir()


class ArbolSpam:
    def __init__(self, modelo):
        # Inicializa el árbol con una raíz que inicialmente es None y un modelo de clasificación.
        self.raiz = None
        self.modelo = modelo

    def clasificar(self, correo):
        # Usa el modelo para predecir si el correo dado es spam. predict devuelve un array, [0] toma el primer elemento.
        es_spam = self.modelo.predict([correo])
        if self.raiz is None:
            # Si el árbol está vacío, establece la raíz con el nuevo nodo.
            self.raiz = Nodo(self.modelo, correo, es_spam)
        else:
            # Si el árbol no está vacío, inserta el correo en el árbol usando el método insertar del nodo raíz.
            self.raiz.insertar(correo)

    def imprimir(self):
        # Si la raíz no es None, llama al método imprimir del nodo raíz para imprimir todo el árbol.
        if self.raiz is not None:
            self.raiz.imprimir()


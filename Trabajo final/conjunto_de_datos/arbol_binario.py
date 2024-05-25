class Nodo:
    def __init__(self, modelo, correo=None, es_spam=None):
        self.modelo = modelo
        self.correo = correo
        self.es_spam = es_spam
        self.izquierdo = None
        self.derecho = None

    def insertar(self, correo):
        # Evaluar el correo usando el modelo del nodo
        es_spam = self.modelo.predict([correo])
        if es_spam == 0:  # No es spam
            if self.izquierdo is None:
                self.izquierdo = Nodo(self.modelo, correo, es_spam)
            else:
                self.izquierdo.insertar(correo)
        else:  # Es spam
            if self.derecho is None:
                self.derecho = Nodo(self.modelo, correo, es_spam)
            else:
                self.derecho.insertar(correo)

    def imprimir(self):
        if self.izquierdo:
            self.izquierdo.imprimir()
        print('Correo:', self.correo, '| Es spam:', 'Sí' if self.es_spam else 'No')
        if self.derecho:
            self.derecho.imprimir()

class ArbolSpam:
    def __init__(self, modelo):
        self.raiz = None
        self.modelo = modelo

    def clasificar(self, correo):
        es_spam = self.modelo.predict([correo])
        if self.raiz is None:
            self.raiz = Nodo(self.modelo, correo, es_spam)
        else:
            self.raiz.insertar(correo)

    def imprimir(self):
        if self.raiz is not None:
            self.raiz.imprimir()

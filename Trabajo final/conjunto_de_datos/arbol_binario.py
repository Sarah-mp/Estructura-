from modelo import clf

class Nodo:
    def __init__(self, modelo, correo=None, es_spam=None):
        self.modelo = modelo
        self.correo = correo
        self.es_spam = es_spam
        self.izquierda = None
        self.derecha = None

    def evaluar_correo(self, correo):
        # Usar el modelo para predecir si el correo es spam o no
       
        prediccion = self.modelo.predict([correo])[0]
        return prediccion  

    def insertar(self, correo):
        if self.correo is None:
            self.correo = correo
            self.es_spam = self.evaluar_correo(correo)
        else:
            # Inserta el correo en el subárbol adecuado basado en la predicción
            if self.es_spam == 1:  # Si el correo actual en el nodo es spam
                if self.derecha is None:
                    self.derecha = Nodo(self.modelo)
                self.derecha.insertar(correo)
            else:
                if self.izquierda is None:
                    self.izquierda = Nodo(self.modelo)
                self.izquierda.insertar(correo)

    def imprimir(self):
        if self.izquierda:
            self.izquierda.imprimir()
        print('Correo:', self.correo, '| Es spam:', 'Sí' if self.es_spam else 'No')
        if self.derecha:
            self.derecha.imprimir()


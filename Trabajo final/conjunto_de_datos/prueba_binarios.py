import sys
sys.setrecursionlimit(10000)
import pandas as pd
from modelo import clf
from arbol_binario import Nodo 

df = pd.read_csv('spam.csv')
 #Supongamos que estos son ejemplos de correos para probar
correos_de_prueba = [
    "Congratulations! you've won a $1000 Walmart gift card. Go to http://example.com to claim now.",
    "Hi, I hope you are doing well. We have a meeting scheduled for 3 PM today.",
    "Urgent: Your account has been breached. Immediate action required!",
    "Hello, don't forget the book club meeting tomorrow morning.",
    "Earn money fast! Guaranteed high returns with minimal investment. Click here!"
]
correos_de_prueba = list (df["Message"])


# Crear una instancia de la raíz del árbol pasando el modelo entrenado
raiz = Nodo(clf)

# Insertar cada correo en el árbol y evaluar si es spam o no
for correo in correos_de_prueba:
    raiz.insertar(correo)

# Imprimir la estructura del árbol y la clasificación de cada correo
raiz.imprimir()

import sys  # proporciona acceso a algunas variables y funciones 
sys.setrecursionlimit(10000)  # aumenta el límite de recursión predeterminado del intérprete de Python 
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

correos_de_prueba = list (df["Message"]) # todos los correos del archivo CSV se utilizan para las pruebas.


# Se pasa el modelo de clasificación clf a este nodo, el cual se usará para evaluar si cada correo es spam o no.
raiz = Nodo(clf)

# Insertar cada correo en el árbol y evaluar si es spam o no
for correo in correos_de_prueba: #  Itera sobre cada correo en la lista 
    raiz.insertar(correo) # determina dónde colocar el correo en el árbol (en el subárbol izquierdo o derecho) basándose en si es clasificado como spam o no.

## imprimir todos los correos y su clasificación 
raiz.imprimir()  

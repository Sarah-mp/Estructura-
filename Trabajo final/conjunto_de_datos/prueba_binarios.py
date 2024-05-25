import sys  # proporciona acceso a algunas variables y funciones

sys.setrecursionlimit(10000)  # aumenta el límite de recursión predeterminado del intérprete de Python 
import pandas as pd

from arbol_binario import ArbolSpam
from modelo import spamClassifier

 #Supongamos que estos son ejemplos de correos para probar
correos_de_prueba = [
    "ESTE ES UN MENSAJE ES DE YA SABEMOS QUE, PORQUE SIGUE LA MISMAS REGLAS QUE LA DATA DE ENTRENO DEL MODELO, DINERO Y MAYUSCULAS Y NUMEROS $20,000. Y LINKS https://www.linkedin.com/pulse/2023-10-spam-text-examples-zhanna-sedrakyan/",
    "You received 3.41 Bitcoin (BTC). To confirm your transaction, visit [link] NOW.",
    "Hi, this is Cynde from HR. We have a couple question regarding your application. Please call [number] to schedule a interview.",
    "Your niece has been arrested and needs $7,500.",
    "r/Colombia · Posted by u/Wrong_AnswersOnly 5h ago Búsqueda del tesoro en Colombia: ¿podrían encontrar a un colombiano de entre 15 y 20 años sin este corte de cabello?",
    "BB/LIVELO Caro Sr(a) seus pontos estão prestes a expirar. Notificação 9582777074871504- Para mais informações, acesse o anexo.",
    # "Hola sara, tengo unas malas noticias con su compañero sergio. este muchacho no da pie con bola"
    # "Congratulations! you've won a $1000 Walmart gift card. Go to http://example.com to claim now.",
    # "Hi, I hope you are doing well. We have a meeting scheduled for 3 PM today.",
    # "Urgent: Your account has been breached. Immediate action required!",
    # "Hello, don't forget the book club meeting tomorrow morning.",
    # "Earn money fast! Guaranteed high returns with minimal investment. Click here!"
    # "hjbshsaksjskddksjkbjmbssjkbdjsasbjhsbdx",
    
]

# Se pasa el modelo de clasificación clf a este nodo, el cual se usará para evaluar si cada correo es spam o no.
raiz = ArbolSpam(spamClassifier)

# Insertar cada correo en el árbol y evaluar si es spam o no
for correo in correos_de_prueba: #  Itera sobre cada correo en la lista 
    raiz.clasificar(correo) # determina dónde colocar el correo en el árbol (en el subárbol izquierdo o derecho) basándose en si es clasificado como spam o no.

## imprimir todos los correos y su clasificación 
raiz.imprimir()  

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


class SpamClassifier:
    def __init__(self, model):
        """
        Inicializa la clase con un modelo ya entrenado.
        """
        self.model = model

    def predict(self, message):
        """
        Predecir si un mensaje es spam o no.
        
        Args:
        message (str): El mensaje a evaluar.
        
        Returns:
        str: 'spam' si el mensaje es considerado spam, 'ham' si no lo es.
        """
        if pd.isna(message):
            message = ''  # Asegurarse de que no hay NaN
        prediction = self.model.predict(message)[0]
        return prediction

# Cargar datos
trainData = pd.read_csv('spamTrain.csv')
testData = pd.read_csv('spamTest.csv')
testDataEval = pd.read_csv('spamTestEval.csv')

# Asegurar que no hay valores NaN en las columnas de mensajes
trainData['message'].fillna('', inplace=True)  # Reemplazar NaN por cadenas vacías
testData['message'].fillna('', inplace=True)

# Convertir la categoría de los mensajes ('ham' o 'spam') en una etiqueta numérica para el conjunto de entrenamiento
trainData['etiqueta'] = trainData['category'].map({'ham': 0, 'spam': 1})

# Configurar el pipeline para el vectorizador y el clasificador
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

# Preparar datos de entrenamiento
X_train = trainData['message']
y_train = trainData['etiqueta']

# Entrenar el modelo
clf.fit(X_train, y_train)

# Preparar datos de prueba
X_test = testData['message']
# Asumiendo que testDataEval contiene las etiquetas verdaderas
y_test = testDataEval['category'].map({'ham': 0, 'spam': 1})

# Realizar predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

spamClassifier = SpamClassifier(clf)
# Calcular la precisión y generar el informe de clasificación usando el conjunto de evaluación
# print("Evaluación de la precisión sobre el conjunto de prueba:")
# print(classification_report(y_test, y_pred))
# print("Matriz de Confusión:")
# print(confusion_matrix(y_test, y_pred))

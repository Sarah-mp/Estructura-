from data import df  # Asegúrate de que data.py esté en el mismo directorio
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix


# Inicializamos el vectorizador TF-IDF
tfidf_vectorizador = TfidfVectorizer()

# Aplicamos la vectorización a la columna 'Message' del DataFrame
X = tfidf_vectorizador.fit_transform(df['Message'])

# Obtenemos las etiquetas correspondientes a cada correo de la columna 'etiqueta'
y = df['etiqueta']

# Dividir los datos en un conjunto de entrenamiento y un conjunto de prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el clasificador Naive Bayes
modelo_nb = MultinomialNB()

# Entrenar el modelo con los datos de entrenamiento
modelo_nb.fit(X_entrenamiento, y_entrenamiento)

# Realizar predicciones sobre el conjunto de prueba
y_prediccion = modelo_nb.predict(X_prueba)

# Imprimir un informe con las principales métricas de clasificación
print(classification_report(y_prueba, y_prediccion))

# Imprimir la matriz de confusión
print(confusion_matrix(y_prueba, y_prediccion))


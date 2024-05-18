import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Cargar datos
df = pd.read_csv('spam.csv')

# Se crea una nueva columna etiqueta que convierte la categoría de los mensajes ('ham' o 'spam') 
df['etiqueta'] = df['Category'].map({'ham': 0, 'spam': 1})
df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

#muestra las primeras filas del DataFrame 
print(df.head())

#muestran información sobre las columnas y el DataFrame 
print(df.columns)
print(df.info())

#transforma los textos a vectores numéricos y luego aplica el clasificador MultinomialNB.
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

# X la columna de mensajes, y columna de etiquetas numéricas
X = df['Message']
y = df['etiqueta']

# Dividir los datos en un conjunto de entrenamiento y un conjunto de prueba
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo usando el pipeline
clf.fit(X_train,y_train)

# Realizar predicciones sobre el conjunto de prueba
y_prediccion = clf.predict(X_train)

# Imprimir un informe con las principales métricas de clasificación
print(classification_report(y_train, y_prediccion))

# Imprimir la matriz de confusión
print(confusion_matrix(y_train, y_prediccion))

emails = [
    "Sounds great! Are you home now?",
    "Will u meet ur dream partner soon? Is ur career off 2 a flying start? 2 find out free, txt HORO followed by ur star sign, e.g. HORO ARIES"
]

email_predicciones = clf.predict(emails)
print(email_predicciones)

precision = clf.score(X_test,y_test)
print(f"La precisión del modelo es: {precision}")

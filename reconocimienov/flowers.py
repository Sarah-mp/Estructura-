from reconocimienov.modelos.Model import Model

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
model_name = "flower_photos"

flowers_model = Model(model_name=model_name,dataset_url = dataset_url)
flowers_model.compile()
flowers_model.train()
flowers_model.save()
# Emotion Classifier

### Tools used

This was built with PyTorch for the Machine Learning part and Flask as a Webserver. For containerization and easy deployment use Docker. The dataset used for model training is the Aff-Wild2


### Deploying the Model

Commands to launch the container:
```bash
#step 1
docker build -t emotion-classification:1.0.0 .

#step 2
docker container run -d -p 5000:5000 emotion-classification:1.0.0
```

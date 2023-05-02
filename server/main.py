from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from fastai.vision.all import *
from torchvision import transforms
from PIL import Image

#Labeling function required for load_learner to work
def GetLabel(fileName):
  return fileName.split('_')[0]

idx_to_class = {0: 'ANGRER', 1: 'DISGUST', 2: 'FEAR', 3: 'HAPPINESS', 4: 'SADNESS', 5: 'SURPRISE'}

model = torch.load('server/lsdModel5_eff_68_5.pt') #Import Model
model.eval()
preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

app = Flask(__name__)
cors = CORS(app) #Request will get blocked otherwise on Localhost

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    img = Image.open(request.files['file'])
    
    image_tensor = preprocess(img).unsqueeze(0)
    #print(image_tensor)
    output = model(image_tensor)
    print(output.data.cpu().numpy())
    label = idx_to_class.get(output.data.cpu().numpy().argmax())

    return f'{label}'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)




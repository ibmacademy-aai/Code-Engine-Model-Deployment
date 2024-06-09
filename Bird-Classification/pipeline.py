import onnxruntime as ort
import numpy as np
from PIL import Image
from torchvision import transforms
import json

class ONNXPipeline:
    def __init__(self, model_path):
        self.session = ort.InferenceSession(model_path)
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(260),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.47853944, 0.4732864, 0.47434163]),
        ])

    def preprocess_image(self, image):
        input_image = image.convert("RGB")
        img_tensor = self.preprocess(input_image)
        img_tensor = img_tensor.unsqueeze(0)  # Batch dimension
        return img_tensor.numpy()

    def predict(self, image, select_top=5) :
        # load the config file to extract label from id
        with open("./model/config.json") as f:
            config = json.load(f)
            id2label = lambda x: config["id2label"][str(x)]
        
        # load and predict the model
        img_tensor = self.preprocess_image(image)
        inputs = {self.session.get_inputs()[0].name: img_tensor}
        outputs = self.session.run(None, inputs)
        
        # process outputs by selecting few top scores then mapping them with the corresponding labels
        top = np.argsort(outputs[0].flatten())[-1:-(select_top+1):-1] # sorting index by score from lowest to highest, and slice the few last index (highest scores)  
        score = outputs[0][0][top].astype(float)
        score = (score-min(score))/(max(score)-min(score)) # normalize score range beteween 0 and 1
        result = [{'score': score[i], "label": id2label(top[i])} for i in range(select_top)]
        return result
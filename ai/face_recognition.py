import face_recognition
from PIL import Image
import os
import pickle
from PIL import Image
import numpy as np
from typing import List
import onnxruntime as ort
from insightface.app import FaceAnalysis
import shutil

class Model():
    def __init__(self) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'model.pkl')
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)
        self.app = FaceAnalysis(name="buffalo_l",providers=['CUDAExecutionProvider'])
        self.app.prepare(ctx_id=0, det_size=(256, 256))

    def predict_face(self, file_path):
        image = Image.open(file_path)        
        img_arr = np.array(image)  
        im = Image.fromarray((img_arr))
        required_size=(256, 256)
        im = im.resize(required_size)
        rgb_arr = np.array(im.convert('RGB'))   
        emb_res = self.app.get(rgb_arr)
        try:
            face_array = emb_res[0].embedding
            face_array = face_array.reshape(1, -1)
        except:
            print('no embedding found for this image')
            return None
        distances, indices = self.model.kneighbors(face_array)

        # Check if the distance to the nearest neighbor is below the threshold
        threshold = 30 # You might need to adjust this
        if distances[0][0] < threshold:
            predict = self.model.predict(face_array)
        else:
            return None
        
        return predict[0]

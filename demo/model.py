import numpy as np
import pandas as pd
import os
import time

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.layers import GlobalAveragePooling2D, Dense, Dropout,Activation,Flatten
from keras.callbacks import ModelCheckpoint

from keras.applications.vgg16 import preprocess_input
from keras.layers import Input
from keras.models import Model, load_model
from keras.utils import np_utils
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from typing import Any, Dict, List, Optional, Pattern, Set, Tuple
from io import BytesIO

import urllib.parse

PATH_MODEL = 'models/m-b.h5'

def predict(img_path):
    model = load_model(PATH_MODEL)
    img_path = urllib.parse.unquote(img_path)
    img_list = []    

    with urllib.request.urlopen(img_path) as url:
        try:
            img = image.load_img(
                BytesIO(url.read()), 
                target_size=(224, 224)
            )
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            x = x.astype('float32')
        except OSError as e:
            pass
        
        # Impressionism         Impressionism           10643
        # Realism               Realism                 10523
        # Romanticism           Romanticism              9285
        # Expressionism         Expressionism            7013
        # Post-Impressionism    Post-Impressionism       5778
        # Art Nouveau (Modern)  Art Nouveau (Modern)     4899
        # Baroque               Baroque                  4400
        # Surrealism            Surrealism               4167
        # Symbolism             Symbolism                3476
        # Rococo                Rococo                   2733
        if x.any():
            res = model.predict(
                x
            ).tolist()[0]
            
            style_codes = {
                0: "Impressionism",
                1: "Realism",
                2: "Romanticism",
                3: "Expressionism",
                4: "Post-Impressionism",
                5: "Art Nouveau (Modern)",
                6: "Baroque",
                7: "Surrealism",
                8: "Symbolism",
                9: "Rococo",
            }
            print("res", res)
            return style_codes[
                res.index(max(res))
            ]

    return "No result"
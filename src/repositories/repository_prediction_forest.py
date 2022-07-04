import ast
import json

import requests
from requests_oauthlib import OAuth1
from src.config.settings import Setting


import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np
import joblib
import os


path_base = os.path.dirname(os.path.realpath(__file__))

class RandomForest:

    def __init__(self):
        self.data_origin = pd.read_csv(Setting.DATA_RANDOM_FOREST)
        self.model_classifer_path = Setting.MODEL_RANDOM_FOREST

        try:
            self.model = joblib.load(self.model_classifer_path)

        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_classifier_path)


    def _cleaning_BD(self):
        bd_model = self.data_origin
        bd_model_duplicates = bd_model.drop_duplicates()
        bd_model_no_null = bd_model_duplicates.drop(columns=['Concentración_x', 'index', 'UP'], axis=1)

        bd_fair = bd_model_no_null.drop(columns=['Key_fecha', 'variable_fecha', 'Número de lote_x', 'Fecha inicio estudio'],
                             axis=1)
        df_no_null['description'] = df_no_null['Descripción_x'].str.split(' ').apply(lambda x: x[0])


    def _train_model(self):
        pass

    def _prediction(self):
        pass

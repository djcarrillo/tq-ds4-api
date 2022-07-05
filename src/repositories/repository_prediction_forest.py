import ast
import json
import os
import math
import joblib
import requests
import numpy as np
import pandas as pd
from sklearn import preprocessing
from config.settings import Setting
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


le = preprocessing.LabelEncoder()
path_base = os.path.dirname(os.path.realpath(__file__))


class RandomForest:

    def __init__(self):
        self.data_origin = pd.read_csv(Setting.DATA_RANDOM_FOREST, sep=';')
        self.model_classifer_path = Setting.MODEL_RANDOM_FOREST

        try:
            self.model = joblib.load(self.model_classifer_path)

        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_classifer_path)

    def cleaninBD(self):

        np.random.seed(1997)
        bd_model = self.data_origin
        bd_model_duplicates = bd_model.drop_duplicates()
        bd_fair = bd_model_duplicates.drop(
            columns=['Key_fecha', 'variable_fecha', 'Número de lote_x', 'Fecha inicio estudio', 'Concentración_x', 'index', 'UP'],
            axis=1)
        bd_fair['description'] = bd_fair['Descripción_x'].str.split(' ').apply(lambda x: x[0])
        categorical_cols = [cname for cname in bd_fair.columns if bd_fair[cname].dtype == "object"]
        # Columnas Numericas
        int_cols = [cname for cname in bd_fair.columns if bd_fair[cname].dtype == "int"]
        float_cols = [cname for cname in bd_fair.columns if bd_fair[cname].dtype == "float64"]
        # Columna target
        target_col = ['ATC']
        numb_cols = float_cols + int_cols
        all_cols = float_cols + int_cols + target_col

        df_final = bd_fair[all_cols].copy()
        df_final = df_final.fillna(0)
        df_final = df_final.replace(np.nan, 0)
        df_final = df_final[df_final['ATC'] != 0]

        df_final.reset_index(drop=True, inplace=True)
        df_final.replace([np.inf, -np.inf], 0, inplace=True)

        # Normalizar la data numerica
        scaler = MinMaxScaler()
        df_final[numb_cols] = scaler.fit_transform(df_final[numb_cols])
        df_final = df_final.loc[(df_final != 0).any(axis=1)]
        return df_final, numb_cols, target_col



        #mse = mean_squared_error(y_test, y_pred)
        #rmse = math.sqrt(mse)
        #mae = mean_absolute_error(y_test, y_pred)
        #rsquared = r2_score(y_test, y_pred)
        #max_error = max_error(y_test, y_pred)


    def _train_model(self):

        df_final, numb_cols, target_col = self.cleaninBD()
        df_final.to_csv(f'{path_base}/../enums/random_forest/data_training/df_final.csv')
        le.fit(df_final.ATC)

        # Prepare X and y
        X = df_final[numb_cols]
        y = le.transform(df_final[target_col])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)
        regressor = RandomForestRegressor(n_estimators=20, random_state=0)
        regressor.fit(X_train, y_train)
        #y_pred = regressor.predict(X_test)

        return regressor


    def _prediction(self, medication_study):

        # Normalizar la data numerica
        scaler = MinMaxScaler()
        df_final = scaler.fit_transform([np.array(medication_study)])
        result = self.model.predict(df_final)

        le = preprocessing.LabelEncoder()
        df_final = pd.read_csv(f'{path_base}/../enums/random_forest/data_training/df_final.csv')
        le.fit(df_final.ATC)

        return le.inverse_transform([int(result[0])])

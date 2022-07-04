import os
import joblib
import numpy  as np
import pandas as pd
import statsmodels.api as sm

from src.config.settings import Setting


path_base = os.path.dirname(os.path.realpath(__file__))

class LogitModel:

    def __init__(self):
        self.data_origin = pd.read_csv(Setting.DATA_RANDOM_FOREST, sep=';')
        self.model_classifer_path = Setting.MODEL_LOGIT

        try:
            self.model = joblib.load(self.model_classifer_path)

        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_classifier_path)


    def _cleaning_BD(self):
        df = self.data_origin
        df["ATC"].astype("category").dtypes 
        # Define dummy varables for the model 
        df["Pass"] = pd.get_dummies(df["Dentro_Rango"], drop_first = True) # Pass dummy 
        df["Intercept"] = 1 
        ATC = pd.get_dummies(df["ATC"], drop_first = True) # Dummies for the categories 
        df = pd.concat([df, ATC], axis=1) 
        return df 
        
    def model_0(self): # Define model for period 0 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 0"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 0"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_3(self): # Define model for period 3 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 3"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 3"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_6(self): # Define model for period 6 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 6"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 6"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_9(self): # Define model for period 9 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 9"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 9"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_12(self): # Define model for period 12 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 12"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 12"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_18(self): # Define model for period 18 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 18"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 18"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_24(self): 
        df = self._cleaning_BD # Define model for period 24 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 24"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 24"]) 
        model_res = model.fit() 
        return model_res 
    
    def model_36(self): # Define model for period 36 
        df = self._cleaning_BD 
        model = sm.Logit(df["Pass"][df["variable_resultado"] == "mes 36"], 
                 df[["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]][df["variable_resultado"] == "mes 36"]) 
        model_res = model.fit() 
        return model_res

    def _train_model(self):
         self.model_0=self.model_0()
         self.model_3=self.model_3()
         self.model_6=self.model_6()
         self.model_9=self.model_9()
         self.model_12=self.model_12()
         self.model_18=self.model_18()
         self.model_24=self.model_24()
         self.model_36=self.model_36()

    def _prediction(self, mes, ATC): 
        ex = pd.DataFrame(np.array([(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)]), 
                  columns=["Intercept", "B", "C", "D", "H", "J", "M", "N", "P", "R"]) 
        if ATC != "A":
            ex[ATC] = 1 
        
        if mes in [0, 3, 6, 9, 12, 18, 24, 36]: 

            if mes == 0:
                Prob = self.model_0.predict(ex)
            if mes == 3:
                Prob = self.model_3.predict(ex)
            if mes == 6:
                Prob = self.model_6.predict(ex)
            if mes == 9:
                Prob = self.model_9.predict(ex)
            if mes == 12:
                Prob = self.model_12.predict(ex)
            if mes == 18:
                Prob = self.model_18.predict(ex)
            if mes == 24:
                Prob = self.model_24.predict(ex)
            if mes == 36:
                Prob = self.model_36.predict(ex)

        else: 
            return f'Error for input parameter: {mes} is not a valid option'
        
        return Prob > 0.7

#! /usr/bin/env python
# encoding: latin1
import pickle
import pandas as pd
import io
import csv
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
def main():
    #uploaded=files.upload()
    sample_df = pd.read_csv('ESCEQ/Reportes/VariablesEquinasv5.csv', encoding='latin-1',sep=';')
    #sample_df.head()
    x_multiple= sample_df.iloc[:,:-1]
    y_multiple=sample_df.iloc[:,-1]
    #x_multiple.head()

    #separar los datos de "train" entrenamiento y prueba para probar el algoritmo test
    X_train, X_test, y_train , y_test =train_test_split(x_multiple,y_multiple,test_size=0.3,random_state=1)


    #definir el algoritmo a utilizar
    model_multiple = linear_model.LinearRegression()
    #entreno el modelo
    model_multiple.fit(X_train,y_train)
    #realizo una prediccion
    y_preds_multiple=model_multiple.predict(X_test)
    #comp= pd.DataFrame({'real': y_test,'preds':y_preds_multiple})
    #print(comp.head(10))
    nombre_archivo='ESCEQ/Reportes/modelo_pickle.pickle'
    #with open (nombre_archivo,'wb') as f:
       #pickle.dump(nombre_archivo, f)
    pickle.dump(model_multiple, open(nombre_archivo, 'wb'))
        #pickle.dump(file(nombre_archivo),f)

if __name__ == "__main__":
    main()

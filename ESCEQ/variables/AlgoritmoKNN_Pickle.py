def handle_uploaded_file(f):
    import pickle
    import pandas as pd
    import io
    import csv
    import numpy as np
    #import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsRegressor
    from os import remove
    from os import path
    from sklearn.preprocessing import StandardScaler
    
    try:        
        if path.exists('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv'):
            remove('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv')
        
        with open('ESCEQ/variables/Reportes/archivo/'+f.name , 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        #uploaded=files.upload()
        sample_df = pd.read_csv('ESCEQ/variables/Reportes/archivo/'+f.name, encoding='latin-1',sep=';')
            #sample_df.head()
        x_knn= sample_df.iloc[:,:-1]
        y_knn=sample_df.iloc[:,-1]
            #x_multiple.head()
        scaler = StandardScaler()
        x_knn[['Grado de claudicacion','Grano','Forraje','Veces al dia','Horarios','Tiempo Hora',
        'Tiempo Minutos','Tiempo Trabajohoras','Tiempo TrabajoDiaria','Tiempo Trabajo Semanal',
        'Tiempo Horas','Tiempo Minutos']]=scaler.fit_transform(x_knn[['Grado de claudicacion','Grano','Forraje','Veces al dia','Horarios','Tiempo Hora','Tiempo Minutos','Tiempo Trabajohoras','Tiempo TrabajoDiaria','Tiempo Trabajo Semanal','Tiempo Horas','Tiempo Minutos']])

        #separar los datos de "train" entrenamiento y prueba para probar el algoritmo test
        X_train, X_test, y_train , y_test =train_test_split(x_knn,y_knn,test_size=0.3,random_state=1)
            

            #definir el algoritmo a utilizar
        KNN= KNeighborsRegressor(n_neighbors=3,metric = 'minkowski', p = 1)
            #entreno el modelo
        KNN.fit(X_train,y_train)
            #realizo una prediccion
        y_pred = KNN.predict(X_test)
            #comp= pd.DataFrame({'real': y_test,'preds':y_preds_multiple})
            #print(comp.head(10))
        
        nombre_archivo='ESCEQ/variables/modeloKNN_pickle.pickle'
        if path.exists(nombre_archivo):
            remove(nombre_archivo)
            #with open (nombre_archivo,'wb') as f:
            #pickle.dump(nombre_archivo, f)
        pickle.dump(KNN, open(nombre_archivo, 'wb'))
                #pickle.dump(file(nombre_archivo),f)
        return 0
    except:
        return 1


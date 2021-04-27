def calcular_valor_k():
    import pandas as pd
    import io
    import csv
    import numpy as np
    #import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsRegressor
    
    
        
    #uploaded=files.upload()
    sample_df = pd.read_csv('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv', encoding='latin-1',sep=';')
        #sample_df.head()
    x_knn= sample_df.iloc[:,:-1]
    y_knn=sample_df.iloc[:,-1]
        #x_multiple.head()

        #separar los datos de "train" entrenamiento y prueba para probar el algoritmo test
    X_train, X_test, y_train , y_test =train_test_split(x_knn,y_knn,test_size=0.3,random_state=1)
    k_range = range(x_knn.shape[0])
    scores = []
    for k in k_range:
        knn = KNeighborsRegressor(n_neighbors = k)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    plt.figure()
    plt.xlabel('k')
    plt.ylabel('accuracy')
    plt.scatter(k_range, scores)
    plt.show()


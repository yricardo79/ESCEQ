import os
from datetime import datetime
from os import path
from os import remove

import MySQLdb
import django_excel as excel
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView
# import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

from ESCEQ.variables.forms import VarsForm
from registro.models import Variables, Equino
from .AlgoritmoKNN_Pickle import handle_uploaded_file
from .invocar_modelo import predecir_puntaje
from sklearn.preprocessing import StandardScaler

class CrearVars(CreateView):
    model = Variables
    template_name = 'calcular-vars.html'
    form_class = VarsForm
    success_url = reverse_lazy('calcular-vars')

def validar_extension (ext):
    if ext == '.csv':
        return 'Correcto'
    else:
        return 'Incorrecto'

def list(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            extension = os.path.splitext(str(request.FILES['myfile']))[1]
            valida_ext = validar_extension(extension)
            # return HttpResponse(myfile)
            # partes_archivo=myfile.split('.')
            #if extension == '.csv':
            if valida_ext == 'Correcto': 
                resultado = handle_uploaded_file(myfile)
                if resultado == 0:
                    if path.exists('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv'):
                        remove('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv')
                    os.rename('ESCEQ/variables/Reportes/archivo/' + str(myfile),
                              'ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv')
                    return render(request, 'cargue-archivo.html', {'mensaje': "Archivo pickle creado correctamente!!"})
                else:
                    return render(request, 'cargue-archivo.html',
                                  {'mensaje': "Archivo pickle No creado correctamente!!"})
            else:
                return render(request, 'cargue-archivo.html', {'mensaje': "La extension del archivo debe ser (csv)"})
        template = loader.get_template('cargue-archivo.html')
        return render(request, 'cargue-archivo.html')
    except:
        return render(request, 'puntajepredecido.html', {'mensaje': "Ocurrio un error al procesar el archivo"})


def predecir(request):
    try:
        if request.method == "POST":
            chip = int(request.POST['chip'])
            claudicacion = int(request.POST['claudicacion'])
            grado_claudi = int(request.POST['grado_claudi'])
            presencia_sangre = int(request.POST['presencia_sangre'])
            olleres = int(request.POST['olleres'])
            boca = int(request.POST['boca'])
            heridas_sangrantes = int(request.POST['heridas_sangrantes'])
            evidencia_fat_sud = int(request.POST['evidencia_fat_sud'])
            grano = float(request.POST['grano'])
            forraje = float(request.POST['forraje'])
            suplemento = int(request.POST['suplemento'])
            sup_oral = int(request.POST['sup_oral'])
            sup_intravenoso = int(request.POST['sup_intravenoso'])
            dieta_veces_dia = float(request.POST['dieta_veces_dia'])
            dieta_horarios = float(request.POST['dieta_horarios'])
            calentamiento_previo = int(request.POST['calentamiento_previo'])
            hora_calentamiento = float(request.POST['hora_calentamiento'])
            minuto_calentamiento = float(request.POST['minuto_calentamiento'])
            trabajo_cantidad_horas = float(request.POST['trabajo_cantidad_horas'])
            trabajo_cantidad_diaria = float(request.POST['trabajo_cantidad_diaria'])
            trabajo_cantidad_semanal = float(request.POST['trabajo_cantidad_semanal'])
            trabajo_potrero = int(request.POST['trabajo_potrero'])
            trabajo_caminador = int(request.POST['trabajo_caminador'])
            tiempo_pot_cam_horas = float(request.POST['tiempo_pot_cam_horas'])
            tiempo_pot_cam_mins = float(request.POST['tiempo_pot_cam_mins'])
            puntaje = predecir_puntaje(claudicacion, grado_claudi, presencia_sangre, olleres, boca, heridas_sangrantes,
                                       evidencia_fat_sud, grano, forraje, suplemento, sup_oral, sup_intravenoso,
                                       dieta_veces_dia,
                                       dieta_horarios, calentamiento_previo, hora_calentamiento, minuto_calentamiento,
                                       trabajo_cantidad_horas, trabajo_cantidad_diaria, trabajo_cantidad_semanal,
                                       trabajo_potrero,
                                       trabajo_caminador, tiempo_pot_cam_horas, tiempo_pot_cam_mins)
            today = datetime.now()
            fecha_registro = today.strftime("%Y-%m-%d")
            conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="esceq")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO variables (chip_id,fecha_registro,claudicacion,grado_claudi,presencia_sangre,olleres,boca,heridas_sangrantes,evidencia_fat_sud,grano,forraje,suplemento,sup_oral,sup_intravenoso,dieta_veces_dia,dieta_horarios,calentamiento_previo,hora_calentamiento,minuto_calentamiento,trabajo_cantidad_horas,trabajo_cantidad_diaria,trabajo_cantidad_semanal,trabajo_potrero,trabajo_caminador,tiempo_pot_cam_horas,tiempo_pot_cam_mins,puntaje) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (chip, fecha_registro, claudicacion, grado_claudi, presencia_sangre, olleres, boca, heridas_sangrantes,
                 evidencia_fat_sud, grano, forraje, suplemento, sup_oral, sup_intravenoso, dieta_veces_dia,
                 dieta_horarios, calentamiento_previo, hora_calentamiento, minuto_calentamiento, trabajo_cantidad_horas,
                 trabajo_cantidad_diaria, trabajo_cantidad_semanal, trabajo_potrero, trabajo_caminador,
                 tiempo_pot_cam_horas, tiempo_pot_cam_mins, puntaje))
            conn.commit()
            cursor.close()
            conn.close()

            if puntaje == -1:
                return render(request, 'puntajepredecido.html', {'mensaje': "Error en la Predicción"})
            else:
                return render(request, 'puntajepredecido.html', {
                    'mensaje': "De acuerdo a las variables registradas el puntaje predictivo es " + str(puntaje)})
        else:
            miFormulario = VarsForm()
            return render(request, "calcular-vars.html", {"form": miFormulario})
    except:
        return render(request, 'capturaExcepciones.html', {'mensaje': "No se grabo las variables"})


def exportar(request):
    export = []
    # encabezados
    export.append([
        'Claudicaciones',
        'Grado de claudicacion',
        'Presencia Sangre',
        'olleres',
        'Boca',
        'Heridas Sangrantes',
        'Fatiga Sudoracion',
        'Grano',
        'Forraje',
        'Suplemento',
        'Via Oral',
        'Via Intravenosa',
        'Veces al dia',
        'Horarios',
        'Calentamiento Previo',
        'Tiempo Hora',
        'Tiempo Minutos',
        'Tiempo Trabajohoras',
        'Tiempo TrabajoDiaria',
        'Tiempo Trabajo Semanal',
        'Tiempo Horas',
        'Tiempo Minutos',
        'Potrero',
        'Caminador',
        'Puntaje'
    ])

    queryset = Variables.objects.all()
    for querysets in queryset:
        export.append([
            querysets.claudicacion, querysets.grado_claudi, querysets.presencia_sangre, querysets.olleres,
            querysets.boca, querysets.heridas_sangrantes, querysets.evidencia_fat_sud, querysets.grano,
            querysets.forraje, querysets.suplemento, querysets.sup_oral, querysets.sup_intravenoso,
            querysets.dieta_veces_dia, querysets.dieta_horarios, querysets.calentamiento_previo,
            querysets.hora_calentamiento, querysets.minuto_calentamiento, querysets.trabajo_cantidad_horas,
            querysets.trabajo_cantidad_diaria, querysets.trabajo_cantidad_semanal, querysets.tiempo_pot_cam_horas,
            querysets.tiempo_pot_cam_mins, querysets.trabajo_potrero, querysets.trabajo_caminador, querysets.puntaje,
        ])

    # Obtener fecha
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "csv", delimiter=";", file_name="VariablesEquinas-" + strToday + ".csv")


def graficaEntrenamiento(request):
    try:
        sample_df = pd.read_csv('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv', encoding='latin-1', sep=';')

        X = sample_df.iloc[:, :-1]
        Y = sample_df.iloc[:, -1]

        eje_x = range(X.shape[0])
        eje_y = Y
        # Creamos una figura y le dibujamos el gráfico
        fig, ax = plt.subplots()        
        ax.plot(eje_x, eje_y, '-', label="yellow Bar", color='y')
        # fig.set_size_inches(15,7)
        ax.set_xlabel("Eje X-(Cantidad Caballos)")
        ax.set_ylabel("Eje Y-(Puntaje)")
        ax.set_title("Gráfico Variables (Cantidad de Caballos) - Puntaje")
        # Creamos los ejes
        # canvas=FigureCanvas(fig)
        ax.set_facecolor('#713404')
        # plt.bar(eje_x, eje_y,label="Blue Bar", color='g')
        # plt.bar(eje_x, eje_y)
        # plt.savefig('barras_simple.png')
        # tamano
        fig.set_size_inches(11, 4)
        # Finalmente mostramos la grafica con el metodo show()
        plt.show()

        return render(request, 'mostrargraficaEntrenamiento.html')
    except:
        return render(request, 'capturaExcepciones.html',
                      {'mensaje': "Ocurrio un error al generar el Gráfico entrenamiento"})


def graficaEquinosPuntaje(request):
    try:
        conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="esceq")
        chip = int(request.POST['chipequino'])
        cursor = conn.cursor()
        
        cursor.execute("SELECT count(chip_id) FROM variables WHERE chip_id = '%i'" % chip)
        result=cursor.fetchone()
        count=result[0]
        #chip=234565
        if count > 0:
            cursor.execute(
                "SELECT fecha_registro,puntaje FROM variables WHERE chip_id = '%i'" % chip + "order by fecha_registro")  # Ejecutar una consulta
            # cursor.execute("SELECT fecha_registro,puntaje FROM registro_variables")
            datos = cursor.fetchall()

            fecha = []
            puntaje = []

            for row in datos:
                fecha.append(row[0])
                puntaje.append(row[1])

            # Creamos una figura y le dibujamos el gráfico
            fig, ax = plt.subplots()
            # plt.xticks(mapeado, fecha)  # Mapeamos los valores horizontales
            ax.set_xlabel("Eje X-Fecha Registro")
            ax.set_ylabel("Eje Y-Puntaje")
            ax.set_title("Gráfico Fecha vs Puntaje Para el Equino Chip: " + str(chip))
            # Creamos los ejes
            ax.set_facecolor('#3FBF9D')
            # canvas=FigureCanvas(fig)
            eje_x = range(len(fecha))
            plt.bar(eje_x, puntaje, color=['blue','red','green','gold','brown'],width=0.1)
            ax.set_xticks(eje_x)
            ax.set_xticklabels(fecha)
            # label="Green Bar", color='g'
            # plt.savefig('barras_simple.png')
            # tamano
            fig.set_size_inches(11, 4)
            # Finalmente mostramos la grafica con el metodo show()
            cursor.close()
            conn.close()
            plt.show()

            return render(request, 'mostrargraficaEquinos.html')
        else:            
            return render(request,'mostrargraficaEquinos.html',{'mensaje': "El Chip ingresado No se encuentra registrado."})
    except:
        cursor.close()
        conn.close()
        return render(request, 'capturaExcepciones.html',
                      {'mensaje': "Ocurrio un error al generar el Gráfico de puntaje para el equino"})


def graficaMaxPuntajes(request):
    try:
        conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="esceq")
        
        cursor = conn.cursor()
        cursor.execute(
            "SELECT   chip_id, max(puntaje) FROM variables GROUP BY chip_id  order by chip_id asc LIMIT 5")  # Ejecutar una consulta
        # cursor.execute("SELECT fecha_registro,puntaje FROM registro_variables")
        datos = cursor.fetchall()

        Chip = []
        puntaje = []

        for row in datos:
            Chip.append(row[0])
            puntaje.append(row[1])

        # Creamos una figura y le dibujamos el gráfico
        fig, ax = plt.subplots()
        ax.set_xlabel("Eje X-Chip Equino")
        ax.set_ylabel("Eje Y-Puntaje")
        ax.set_title("Gráfico Cino Mejores Puntajes por Equino")
        # Creamos los ejes
        # canvas=FigureCanvas(fig)
        
        x = range(len(Chip))
        plt.bar(x, puntaje,color=['blue','red','green','gray','brown'],width=0.1)
        ax.set_xticks(x)
        ax.set_xticklabels(Chip)
        ax.set_facecolor('#3FBF9D')
        # label="Green Bar", color='g'
        # tamano
        fig.set_size_inches(11, 4)
        # Finalmente mostramos la grafica con el metodo show()
        cursor.close()
        conn.close()
        plt.show()

        return render(request, 'mostrargraficaMayorP.html')
    except:
        cursor.close()
        conn.close()
        return render(request, 'capturaExcepciones.html',{'mensaje': "Ocurrio un error al generar el Gráfico Cinco Mejores Puntajes por Equino"})


def graficaKNN(request):
    #try:
        # uploaded=files.upload()
        sample_df = pd.read_csv('ESCEQ/variables/Reportes/archivo/VariablesEquinas.csv', encoding='latin-1', sep=';')
        # sample_df.head()
        x_knn = sample_df.iloc[:, :-1]
        y_knn = sample_df.iloc[:, -1]
        # x_multiple.head()
        scaler = StandardScaler()
        x_knn[['Grado de claudicacion','Grano','Forraje','Veces al dia','Horarios','Tiempo Hora',
        'Tiempo Minutos','Tiempo Trabajohoras','Tiempo TrabajoDiaria','Tiempo Trabajo Semanal',
        'Tiempo Horas','Tiempo Minutos']]=scaler.fit_transform(x_knn[['Grado de claudicacion','Grano','Forraje','Veces al dia','Horarios','Tiempo Hora','Tiempo Minutos','Tiempo Trabajohoras','Tiempo TrabajoDiaria','Tiempo Trabajo Semanal','Tiempo Horas','Tiempo Minutos']])

        # separar los datos de "train" entrenamiento y prueba para probar el algoritmo test
        X_train, X_test, y_train, y_test = train_test_split(x_knn, y_knn, test_size=0.3, random_state=1)
        k_range = range(1, 20)
        errortest = []
        errortrain = []
        for k in k_range:
            knn = KNeighborsRegressor(n_neighbors=k)
            knn.fit(X_train, y_train)
            predit_i = knn.predict(X_test)
            # error.append(np.mean(predit_i!=y_test))
            errortest.append(knn.score(X_test, y_test))
            errortrain.append(knn.score(X_train, y_train))
        # plt.figure()
        # plt.xlabel('k')
        # plt.ylabel('accuracy')
        # plt.scatter(k_range, scores)
        # plt.xticks([0,5,10,15,20,25,30])
        # plt.show()
        
        plt.figure(figsize=(10, 6))
        plt.plot(k_range, errortest, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
        plt.plot(k_range, errortrain, color='green', linestyle='dashed', marker='o', markerfacecolor='red',
                 markersize=10)
        plt.title('Error Rate K Value Test y Train')
        plt.xlabel('K Value')
        plt.ylabel('accuracy')
        
        plt.show()
        return render(request, 'mostrarKNN.html')
    #except:
        #return render(request, 'capturaExcepciones.html',
                      #{'mensaje': "Ocurrio un error al generar el Gráfico del Modelo"})

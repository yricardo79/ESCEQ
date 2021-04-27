def predecir_puntaje(claudicacion,grado_claudi,presencia_sangre,olleres,boca,heridas_sangrantes,
                                evidencia_fat_sud,grano,forraje,suplemento,sup_oral,sup_intravenoso,dieta_veces_dia,
                                dieta_horarios,calentamiento_previo,hora_calentamiento,minuto_calentamiento,
                                trabajo_cantidad_horas,trabajo_cantidad_diaria,trabajo_cantidad_semanal,trabajo_potrero,
                                trabajo_caminador,tiempo_pot_cam_horas,tiempo_pot_cam_mins):    
    import pickle
    from numpy import array

    try:
        #nombre_archivo='ESCEQ/Reportes/modelo_pickle.pickle'
        #nombre_archivo='ESCEQ/Reportes/modeloArboles_pickle.pickle'
        nombre_archivo='ESCEQ/variables/modeloKNN_pickle.pickle'
        #nombre_archivo='ESCEQ/Reportes/modeloMVS_pickle.pickle'
        #nombre_archivo='ESCEQ/Reportes/modeloNaiverBayer_pickle.pickle'
        X_new = array([[claudicacion,grado_claudi,presencia_sangre,olleres,boca,heridas_sangrantes,evidencia_fat_sud,grano,forraje,suplemento,sup_oral,sup_intravenoso,dieta_veces_dia,dieta_horarios,calentamiento_previo,hora_calentamiento,minuto_calentamiento,trabajo_cantidad_horas,trabajo_cantidad_diaria,trabajo_cantidad_semanal,trabajo_potrero,trabajo_caminador,tiempo_pot_cam_horas,tiempo_pot_cam_mins]])
        with open (nombre_archivo,'rb') as f:
            mp = pickle.load(f)
            #hacer nuevos pronosticos        
            puntaje=mp.predict(X_new) 
        return (round(puntaje[0],2))        
    except:
        return 0

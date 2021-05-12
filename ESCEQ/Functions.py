def validar_extension(ext):
    if ext == '.csv':
        return 'Correcto'
    else:
        return 'Incorrecto'

def bus_ser_equ2(txt_caballo):
    # ctrl info form
    if txt_caballo !="":
        # mensaje = "Caballo búscado. %r" %request.GET["txt_caballo"]
        texto_caballo = txt_caballo
        if len(texto_caballo) > 20:
            return False
        else:
            return True
    else:
        return False
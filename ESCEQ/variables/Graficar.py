def plotgrafica(request):


sample_df = pd.read_csv('ESCEQ/variables/Reportes/archivo/'+f.name, encoding='latin-1',sep=';')

X= sample_df.iloc[:,:-1]
Y=sample_df.iloc[:,-1]

# Creamos una figura y le dibujamos el gr�fico
f = plt.figure()

# Creamos los ejes
axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
axes.plot(X, Y)
axes.set_xlabel("Eje X")
axes.set_ylabel("Eje Y")
axes.set_title("Gr�fico")

# Como enviaremos la imagen en bytes la guardaremos en un buffer
buf = io.BytesIO()
canvas = FigureCanvasAgg(f)
canvas.print_png(buf)


# Creamos la respuesta enviando los bytes en tipo imagen png
response = HttpResponse(buf.getvalue(), content_type='image/png')

# Limpiamos la figura para liberar memoria
f.clear()

# A�adimos la cabecera de longitud de fichero para m�s estabilidad
response['Content-Length'] = str(len(response.content))

# Devolvemos la response
return response
#eje_x = list(range(X.shape[0]))
#eje_y = Y
#fig,ax =plt.subplots()
#ax.plot(eje_x,eje_y,'-')
#fig.set_size_inches(15,7)

#plt.show()
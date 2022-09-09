from PIL import Image
image = Image.open('youtube2.png')
image.thumbnail((220, 220))
image.save('youtube.png')

image = Image.open('salir2.png')
image.thumbnail((220, 220))
image.save('salir.png')

image = Image.open('googlemaps2.png')
image.thumbnail((220, 220))
image.save('googlemaps.png')

image = Image.open('reporte_recopilación2.png')
image.thumbnail((220, 220))
image.save('reporte_recopilacion.png')

image = Image.open('reporte_exporacion2.png')
image.thumbnail((220, 220))
image.save('reporte_exploracion.png')

image = Image.open('contraseña2.png')
image.thumbnail((220, 220))
image.save('contraseña.png')

image = Image.open('formulario2.png')
image.thumbnail((220, 220))
image.save('formulario.png')
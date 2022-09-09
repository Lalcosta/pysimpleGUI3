
#Helio Cisneros

import PySimpleGUI as sg
import pandas as pd
import webbrowser

print=sg.Print

def formulario():
    texto_hospitalizado = sg.Text(("Hospitalizado:"), font = ("Helvetica", 20))
    opciones_Hospitalizado = ("Si", "No", )
    hospitalizado = sg.Combo(opciones_Hospitalizado, key = "INPUT_hospitalizado")
    texto_resultados = sg.Text("resultado de la prueba :", font = ("Helvetica", 20))
    resultado_opciones = ("Negativo", "Positivo", "no identificado", )
    resultado = sg.Combo(resultado_opciones, key = "INPUT_resultados")
    texto_sintomas = sg.Text("Sintomas de la vacuna ", font = ("Helvetica", 20))
    sintomas = ( "dolor de cabeza" , "cansancio" , "fiebre" , "dolor de cabeza")
    sintomas = sg.Combo (sintomas, key = "INPUT_sintomas")
    texto_edo = sg.Text("Estado de origen", font = ("Helvetica", 20))
    edos = ('Aguascalientes','Baja California Sur','Baja California','Campeche','Coahuila de Zaragoza','Colima',
        'Chiapas','Chihuahua','Ciudad de M','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco',
        'Mexico','Michoacan','Morelos','Nayarit','NueveLeon','Oaxaca','Puebla','Queretaro',
        'Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz de Ignacio de la Llave',
        'Yucatan','Zacatecas','Otro País... ')
    estados = sg.Combo(edos, key = 'INPUT_estado', font = ('Helvetica', 20), text_color = "#369898")
    texto_edad = sg.Text("Ingresa la edad:", font = ("Helvetica", 20))
    edad = sg.Spin(tuple(range(1,125),), key ="INPUT_edad", font = ("Helvetica", 20) )
    texto_AumentoCasos = sg.Text("Estan aumentando los casos?:",font = ("Helvetica", 20))
    opciones_AumentoCasos = ("Si" , "No", "Se quedan consistentes")
    AumentoCasos = sg.Combo (opciones_AumentoCasos, key = "INPUT_AumentoCasos")
    btn_menu=sg.Button("REGRESAR AL MENU",key="BTN_MENU")
    btn_registrar=sg.Button("Registrar datos",key="BTN_REGISTRO")
    layout = [[texto_hospitalizado, hospitalizado],
              [texto_edad, edad],
              [texto_edo,estados],
              [texto_sintomas,sintomas],
              [texto_resultados,resultado],
              [texto_AumentoCasos,AumentoCasos],
              [btn_menu,btn_registrar]]
    frame_formulario=sg.Frame("Formulario",layout,font = ("Helvetica", 25), key = "FRAME_FORMULARIO", visible = False)
    return frame_formulario
    
def menu():
    
    b1 = sg.Button( key = "BTN_FORMULARIO", image_filename = "formulario.png") 
    b2 = sg.Button( key = "BTN_REPORTE_REC", image_filename = "reporte_recopilacion.png") 
    b3 = sg.Button( key = "BTN_REPORTE_EXP",image_filename = "reporte_exploracion.png")
    b4 = sg.Button( key = "BTN_GOOGLE", image_filename = "googlemaps.png")
    b5 = sg.Button( key = "BTN_YT", image_filename = "youtube.png") 
    b6= sg.Button( key = "BTN_SALIR", image_filename = "salir.png")
    
    #Layout del menú
    layout_menu = [ [b1],
                   [b2 ,b3] ,
                [b4, b5,b6]]
    #Frame del menú
    frame_menu = sg.Frame("Menu", layout_menu, key = "FRAME_MENU", visible = False)
    return frame_menu

def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña ", font = ("Helvetica", 25))
    
    password = sg.Input(password_char = "*" , font = ("Helvetica", 25), key = 'INP_PASSWORD', text_color = "black")
    
    b1 = sg.Button("Validar Ingreso", font = ("Helvetica", 25), key = 'BTN_PASSWORD')
    imagen = sg.Image(filename = 'contraseña.png')
    
    layout =  [[texto_password, password],
               [b1],
               [imagen]]
                         
    #crear el frame - ventana para ingresar los datos del password
    frame_password = sg.Frame("Validar Ingreso", layout, font = ("Helvetica", 25), key = "FRAME_PASSWORD", visible = True)
                         
    return frame_password         

sg.theme("LightBrown13")

contraseña=validar_ingreso()
opciones=menu()
forms=formulario()

layout=[[forms,opciones],
        [contraseña]]

window = sg.Window('Helio Cisneros', layout,size=(800,800))

while True:
    event, values=window.read()
    if event ==sg.WIN_CLOSED:
        break
    
    elif event=="BTN_PASSWORD":
                password=values["INP_PASSWORD"]
                
                if password=="Helio":
                        sg.popup("Contraseña correcta")
                        window["FRAME_PASSWORD"].update(visible=False)
                        window["FRAME_MENU"].update(visible=True)
                        
                else:
                        sg.popup("Contraseña incorrecta")
                        
    elif event=="BTN_FORMULARIO":
                window["FRAME_FORMULARIO"].update(visible=True)
                window["FRAME_MENU"].update(visible=False)
    
    elif event =="BTN_REPORTE_EXP":
        datos=pd.read_csv("covid.csv")
        print("Total de  casos acumulados:",datos["Casos acumulados"].sum())
        print("Total de  muertes acumuladas:",datos["Muertes acumuladas"].sum())
        print("Nuevos casos por estado")
        for i in range(len(datos["Estado"])):
            print(datos["Estado"][i],":",datos["Nuevos casos"][i])
    
    elif event=="BTN_REPORTE_REC":
                datos=pd.read_csv("recopilacion.csv")
                print("Personas hospitalizadas:")
                print(datos['Hospitalizado'].value_counts())
                print("Conteo por edad:")
                print(datos['Edad'].value_counts())
                print("Sintomas más frecuentes:")
                print(datos['Sintomas'].value_counts(sort=True))
                print("Resultados positivos vs negativos:")
                print(datos["Resultado"].value_counts())
    
                
    elif event == "BTN_REGISTRO":
        with open("recopilacion.csv","a") as archivo:
                        hospitalizado=values["INPUT_hospitalizado"]
                        edad=values["INPUT_edad"]
                        estado=values["INPUT_estado"]
                        sintomas=values["INPUT_sintomas"]
                        resultado=values["INPUT_resultados"]
                        aumento=values["INPUT_AumentoCasos"]
                    
                        #Creamos el string para enviar los datos
                        row=hospitalizado + "," + str(edad) + "," + estado + "," + sintomas + "," + resultado + "," + aumento  + "\n"
                        #Escribimos los datos en la base
                        archivo.write(row)
    elif event =="BTN_MENU":
        window["FRAME_MENU"].update(visible=True)
        window["FRAME_FORMULARIO"].update(visible=False)
    
    elif event == "BTN_YT":
        webbrowser.open("https://www.youtube.com/watch?v=yBXj6X8qMpI")
        
    elif event=="BTN_GOOGLE":
        webbrowser.open("https://www.google.com/maps/search/Centro+de+salud/@19.3258096,-99.1719434,11z")
    
    elif event=="BTN_SALIR":
        break
    

window.close()
        
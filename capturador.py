import pyautogui
import threading
import time
tiempoEntreCapura= int( input( "Introduce el tiempo entre cada captura(segundos): "))
cantidadMaximaDeCapturas= int( input("Introduce la cantidad maxima de capturas: "))

# Tarea a ejecutarse cada determinado tiempo.

def timer():
    cantidadCapturas= 0
    while cantidadCapturas < cantidadMaximaDeCapturas :
        imagen = pyautogui.screenshot()
        imagen.save( r"C:\\Users\\marti\\Desktop\\capturasDelPrograma\\screen_{}.png".format(cantidadCapturas))
        cantidadCapturas = cantidadCapturas + 1
        time.sleep(tiempoEntreCapura)   # tiempo de espera entre cada captura.

# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()

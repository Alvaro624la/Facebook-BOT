from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time 
# alternativa para el módulo time: 'from time import sleep' y luego usar solo 'sleep()' o solo 'localtime()'

# MODULOS PROPIOS
from locators import LocatorsClass as loc


### CREDENCIALES:
def ask_user_email(user_email=None):
    try:
        # Si el usuario ha introducido el user_email, devuelvelo. Si no, preguntale.
        if user_email:
            return user_email
        else:
            user_email = input('Introduce tu email de Facebook: ')
            ask_if_secure_email = input('¿Estas seguro de que está correctamente escrito? (s/n): ')
            if ask_if_secure_email.lower() not in ['y', 'yes', 's', 'si']:
                ask_user_email()
            else:
                return user_email
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y contraseña de Facebook del usuario mediante preguntas --> {err}')

def ask_user_password(user_password=None):
    try:
        # Si el usuario ha introducido el user_password, devuelvelo. Si no, preguntale.
        if user_password:
            return user_password
        else:
            user_password = input('Ahora introduce tu contraseña de Facebook: ')
            ask_if_secure_pass = input('¿La contraseña también está correctamente escrita? (s/n): ')
            if ask_if_secure_pass.lower() not in ['y', 'yes', 's', 'si']:
                ask_user_password()
            else:
                return user_password
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y contraseña de Facebook del usuario mediante preguntas --> {err}')


### DRIVER CONFIG:
# Configurar las opciones del navegador para desactivar las notificaciones de forma predeterminada
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver_path = './chromedriver-win64/chromedriver.exe'
# se crea una instancia del webdrive chrome
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

def open_url_after_driver_config():
    # abrimos la url y se espera a que esté completamente cargada con el metodo get de driver
    driver.get("https://www.facebook.com/")

### VERIFICACION TITULO PAGINA:
def verify_page_title():
    try:
        # verificamos si el titulo de la página del driver es Facebook. Si no es, lanza error.
        assert "Facebook" in driver.title
    except AssertionError as err:
        print(f'Error de tipo AssertionError. El título de la página no coincide con la página cargada --> {err}\n\nCerrando en 5 segundos')
        time.sleep(5)
        driver.close()

### COOKIES:
def cookies():
    # Apaño temporal para que cargue bien la ventana de cookies y no ejecute el btn_cookies antes de tiempo causando un error ----------------------------------------------
    time.sleep(1) #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # detectamos si existe un boton de cookies, y las rechazamos. Si este no existe, seguimos
    # Usar *loc.COOKIES permite desempaquetar la tupla
    btn_cookies = driver.find_element(*loc.COOKIES)
    if btn_cookies:
        print('Rechazando cookies opcionales')
        btn_cookies.click()
    else:
        print('Configuración de cookies ya definida. Continuando...')

### INICIAR SESION
intentos_inicio_sesion = 0
def facebook_login():
    global intentos_inicio_sesion
    if intentos_inicio_sesion >= 3:
        print(f'Has intentado iniciar sesion {intentos_inicio_sesion} veces.\nExiste algún problema externo a este BOT de Facebook que impide iniciar sesion correctamente.\nCompruebe el error que le muestra la página de Facebook e intente arreglarlo para volver a intentar entrar. Cerrando en 15 segundos')
        time.sleep(15)
        driver.close()
    try:
        usuario_inicio_sesion = driver.find_element(*loc.LOGIN_EMAIL)
        usuario_inicio_sesion.clear()
        usuario_inicio_sesion.send_keys(user_email)
        contraseña_inicio_sesion = driver.find_element(*loc.LOGIN_PASS)
        contraseña_inicio_sesion.clear()
        contraseña_inicio_sesion.send_keys(user_password)
        btn_inicio_sesion = driver.find_element(*loc.LOGIN_BTN)
        btn_inicio_sesion.click()
        print('Iniciando sesión...')
        intentos_inicio_sesion += 1
    except:
        # Sesion ya iniciada, porque no encuentra los campos de inicio de sesion email, pass y login
        print('Iniciando sesión...')

    # Comprobación del correcto iniciado sesión (usando try except de manera inversa)
    try:            
        try:
            # Localizamos y clicamos en btn: ¿Has olvidado la contraseña?
            btn_olvidado_contraseña = WebDriverWait(driver, 5).until(EC.presence_of_element_located(loc.LOGIN_FORGOTTEN_PASS_LINK))
            btn_olvidado_contraseña.click()
            ask_user_password()
            driver.find_element(By.ID, "pass").clear()
            driver.find_element(By.ID, "pass").send_keys(user_password)
            driver.find_element(By.XPATH, "//button[@name='login']").click()
        except:
            # Detectar algún mensaje de error en el inicio de sesión
            WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.LOGIN_ERR_MSG))
            print('Error al iniciar sesión. Introduzca los credenciales de nuevo.')
            ask_user_email()
            ask_user_password()
            facebook_login()
    except:
        # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito.
        WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.GROUPS_BTN))


### IR A TUS GRUPOS
def ir_a_grupos():
    print('Sesión iniciada con éxito')
    try:
        # busco el enlace a grupos y le doy click
        btn_grupos = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.GROUPS_BTN))
        print('Dirigiendome a grupos')
        btn_grupos.click()
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al buscar el enlace a grupos --> {err}')
        print('Yendo a grupos través de URL específica .../groups/feed/')
        driver.get("https://www.facebook.com/groups/feed/")

#########################################################################################
################################ OBTENER LINKS DE GRUPOS ################################

def obtener_links_grupos():
    #########################################################################################
    ############# EN CASO DE NO ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ########################

    # Encontrar todos los enlaces de grupos en la url actual, que no tengan el panel principal role"main" como elemento padre (para no obtener links de grupos sugeridos)
    # all_links = driver.find_elements(By.XPATH, '//a[not(ancestor::div[@role="main"])]')

    #########################################################################################
    #################### ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ###############################
    driver.get("https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="main"]')))
    # Buscar todos los links dentro del panel principal --> div con role="main"
    all_links = driver.find_elements(By.XPATH, '//div[@role="main"]//a')
    #########################################################################################

    # Declaramos la variable donde definiremos el array de tipo set que usaremos para almacenar todos los links que sean de grupos
    arr_links_grupos_obtenidos = set([])

    print('Buscando grupos')
    for i in range(len(all_links)):
        link = all_links[i]
        link_regex = re.search(r"https://www.facebook.com/groups/\d+", link.get_attribute("href"))
        try:
            if link_regex : arr_links_grupos_obtenidos.add(link_regex.group())
        except Exception as err:
            print(f'Ha habido un error de tipo "{type(err).__name__}" obteniendo los links de los grupos --> {err}')
    print(f'{"-"*30}\nEnlaces obtenidos: {len(arr_links_grupos_obtenidos)} enlaces de grupo')
    print(arr_links_grupos_obtenidos)
    return arr_links_grupos_obtenidos

################################ OBTENER LINKS DE GRUPOS ################################
#########################################################################################

# Variables de fecha. Siempre pueden ser útiles.
actual_year = time.localtime().tm_year
actual_month = time.localtime().tm_mon
actual_day = time.localtime().tm_mday
actual_hour = time.localtime().tm_hour
actual_min = time.localtime().tm_min
actual_sec = time.localtime().tm_sec

# Porcentaje de completado del script entero. Regla de tres calculando todos los links como el 100%.
# arr_links_grupos_obtenidos = obtener_links_grupos()
porcentaje_completado = 0
def informe_porcenataje_completado():
    porcentaje_unico_link = (1 * 100) / len(arr_links_grupos_obtenidos)
    # /3 porque son 3 los procesos para publicar: abrir cuadro/escribir/btn publicar, y quiero que en cada uno informe del porcentaje
    global porcentaje_completado 
    porcentaje_completado += porcentaje_unico_link/3
    print(f'{int(round(porcentaje_completado, 0))}% completado')

######################################################################################################
################################# EL USUARIO ESCRIBE EL POST DESEADO #################################

def crear_post():
    # Avisar al usuario de escribir el post por consola
    info_to_user_message = "Por favor, escribe el post en la consola/terminal abierta del principio"
    info_to_user_div = f"var mensaje = document.createElement('div'); mensaje.textContent = '{info_to_user_message}'; mensaje.style.cssText = 'font-size: 1.2em; position: fixed; top: 15px; left: 15px; padding: 20px; background-color: yellow; border-radius: 5px; z-index: 9999'; document.body.appendChild(mensaje);"
    driver.execute_script(info_to_user_div)

    print("Escribe aquí tu post línea por línea (presiona Enter dos veces para terminar):\n")
    lineas = []
    while True:
        linea = input()
        # Si en linea hay contenido, es True. Si es "", es False y termina el bucle
        if linea:
            lineas.append(linea)
        else:
            break
    post = "\n".join(lineas)
    
    if post.strip() == '':
        print('Error: Sin contenido. Por favor, escribe o introduce contenido para generar el post.')
        crear_post()
    else:
        # El usuario revisa su post y confirma para proceder a compartir, si no, vuelve a escribir el post de nuevo
        print("\nTu post será el siguiente:")
        print(post)
        ask_if_secure_post = input('Estas seguro de querer publicarlo en todos los grupos (s/n): ')
        if ask_if_secure_post.lower() not in ['y', 'yes', 's', 'si'] : crear_post()

        return post


################################# EL USUARIO ESCRIBE EL POST DESEADO #################################
######################################################################################################

##########################################################################################
################################# ABRIR LINKS Y PUBLICAR #################################

# Manejo la alerta que a veces aparece inesperadamente durante la ejecución del script y está fuera de nuestro control.
def dismiss_alert():
    try:
        alert = driver.switch_to.alert
        alert.dismiss()  # O bien alert.accept() para rechazarla
        print("Alerta manejada")
    except:
        print("No se encontró ninguna alerta. Continuando...")

# Recorremos el array con todos los links de grupos y publicamos en cada uno
def publicar_en_cada_grupo():
    for link in arr_links_grupos_obtenidos:
        
        dismiss_alert()
        try:
            driver.get(link)
            # Espera a que cargue el escribe algo box y localizamos el elemento para clicarlo posteriormente
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            escribe_algo_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.GROUP_WRITE_STG_LINEBOX))
            escribe_algo_box.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 1 de tipo {type(err).__name__} - Encontrar cuadro de dialogo para escribir --> {err}')
        
        dismiss_alert()
        try:
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            crea_una_publicacion_publica = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.POST_WRITE_BOX))
            crea_una_publicacion_publica.send_keys(contenido_publicacion)
            try:
                # Si sale un cuadro de texto sobre "Información adicional sobre este contenido" le damos a "Compartir de todas formas"
                popup_adicional_al_pegar_link = WebDriverWait(driver, 3).until(EC.presence_of_element_located(loc.WARNING_LINK_POPUP))
                popup_adicional_al_pegar_link.click()
            except:
                print('No ha aparecido ningún problema con agregar el link en la publicación. Continuando...')
            # Tiempo de espera para que la miniatura del posible link de la publicación se cargue correctamente (tiempo de espera estimado, a ojimetro)
            time.sleep(2)
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 2 de tipo {type(err).__name__} - Escribir en el recuadro --> {err}')

        dismiss_alert()
        try:
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            btn_publicar = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.POST_BTN))
            btn_publicar.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 3 de tipo {type(err).__name__} - Click en el boton Publicar --> {err}')
            
        # Esperar a que el boton de Publicar desaparezca
        btn_publicar = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(loc.POST_BTN))
        
        #Se vuelve a ejecutar el bucle for, hasta que no queden mas links en el arr --> arr_links_grupos_obtenidos

################################# ABRIR LINKS Y PUBLICAR #################################
##########################################################################################

def mensage_final_cerrar_bot():
    informe_porcenataje_completado()
    print('Contenido publicado en todos los grupos')

    print(f'Cerrando en 10 segundos.\n{"-"*30}\nAlvaro624la te agradece haber utilizado su herramienta y espera que te haya sido útil ;D')
    print("                       _            ")
    print("                      (_)           ")
    print("   __ _ _ __ __ _  ___ _  __ _ ___  ")
    print("  / _` | '__/ _` |/ __| |/ _` / __| ")
    print(" | (_| | | | (_| | (__| | (_| \__ \ ")
    print("  \__, |_|  \__,_|\___|_|\__,_|___/ ")
    print("   __/ |                            ")
    print("  |___/   ")
    time.sleep(7)
    print('Cerrando en 3 segundos')
    time.sleep(1)
    print('Cerrando en 2 segundos')
    time.sleep(1)
    print('Cerrando en 1 segundo')
    time.sleep(1)
    driver.close()

############################################################################
################################# FUNCIONES ################################
############################################################################
open_url_after_driver_config()
verify_page_title()
cookies()
###################### Iniciar sesión automáticamente ######################
# Para iniciar sesión automáticamente, puedes añadir tus datos entre comillas (simples o dobles) así: 
##### ...ask_user_email('aquí_tu_email')
##### ...ask_user_password('aquí_tu_contraseña')
# aquí debajo:
user_email = ask_user_email()
user_password = ask_user_password()
############################################################################
facebook_login()
ir_a_grupos()
arr_links_grupos_obtenidos = obtener_links_grupos()
contenido_publicacion = crear_post()
publicar_en_cada_grupo()
mensage_final_cerrar_bot()
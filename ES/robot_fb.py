from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time 
# alternativa para el módulo time: 'from time import sleep' y luego usar solo 'sleep()' o solo 'localtime()'

# DRIVER MANAGER https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-chrome 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# MODULOS PROPIOS
from locators import LocatorsClass as loc
from pop_ups import PopUpsClass as pop_up

# Traducciones para IDIOMA
def language_set_function():
    # JS
    global t_ask_credentials_user
    global t_ask_credentials_password
    global t_ask_credentials_accept
    global t_ask_group_selection_accept
    global t_create_post_publicar
    # PY
    global t_ask_credentials_info_to_user_message
    global t_ask_credentials_esperando_a_obtener_credenciales
    global t_cookies_rechazando_cookies_opcionales 
    global t_cookies_config_cookies_definida_continuando 
    global t_facebook_login_intentos_inicio_sesion_msg 
    global t_facebook_login_iniciando_sesion 
    global t_facebook_login_info_to_user_message
    global t_ir_a_grupos_sesion_iniciada_exitosamente
    global t_ir_a_grupos_dirigiendome_a_grupos
    global t_ir_a_grupos_dirigiendome_a_grupos_via_URL
    global t_obtener_obj_grupos_grupo_obtenido
    global t_obtener_obj_grupos_procesando
    global t_obtener_obj_grupos_link_ya_existente
    global t_js_function_info_to_user_message
    global t_esperar_hasta_cliente_selecciona_grupos_msg
    global t_informe_porcenataje_completado_msg
    global t_crear_post_info_to_user_message
    global t_crear_post_esperando_a_crear_post_para_publicar
    global t_dismiss_alert_alerta_manejada
    global t_dismiss_alert_ninguna_alerta_encontrada
    global t_publicar_en_cada_grupo_sin_problemas_al_agregar_link
    global t_mensage_final_cerrar_bot_contenido_publicado_en_todos_grupos
    global t_mensage_final_cerrar_bot_cerrando_en_10s_y_agradecimiento
    global t_mensage_final_cerrar_bot_cerrando_en_3s
    global t_mensage_final_cerrar_bot_cerrando_en_2s
    global t_mensage_final_cerrar_bot_cerrando_en_1s

    if(language_set == 'ES'):
        # JS
        t_ask_credentials_user = "Usuario / Email"
        t_ask_credentials_password = "Contraseña"
        t_ask_credentials_accept = "Aceptar"
        t_ask_group_selection_accept = "Aceptar"
        t_create_post_publicar = "Publicar"
        # PY
        t_ask_credentials_info_to_user_message = "Por favor, introduzca los credenciales para que el BOT pueda operar y ver sus grupos"
        t_ask_credentials_esperando_a_obtener_credenciales = 'Esperando para obtener las credenciales...'
        t_cookies_rechazando_cookies_opcionales = 'Rechazando cookies opcionales'
        t_cookies_config_cookies_definida_continuando = 'Configuración de cookies ya definida. Continuando...'
        t_facebook_login_intentos_inicio_sesion_msg = 'veces has intentado iniciar sesion.\nExiste algún problema externo a este BOT de Facebook que impide iniciar sesion correctamente.\nCompruebe el error que le muestra la página de Facebook e intente arreglarlo para volver a intentar entrar. Cerrando en 15 segundos'
        t_facebook_login_iniciando_sesion = 'Iniciando sesión...'
        t_facebook_login_info_to_user_message = 'Error al iniciar sesión. Siga los pasos que Facebook le marca, para iniciar sesión por completo'
        t_ir_a_grupos_sesion_iniciada_exitosamente = 'Sesión iniciada con éxito'
        t_ir_a_grupos_dirigiendome_a_grupos = 'Dirigiendome a grupos'
        t_ir_a_grupos_dirigiendome_a_grupos_via_URL = 'Yendo a grupos través de URL específica .../groups/feed/'
        t_obtener_obj_grupos_grupo_obtenido = 'Obtención de links: grupo obtenido'
        t_obtener_obj_grupos_procesando = 'Obtención de links: procesando...'
        t_obtener_obj_grupos_link_ya_existente = 'Obtención de links: link ya existente'
        t_js_function_info_to_user_message = 'Por favor, selecciona los grupos donde deseas compartir'
        t_esperar_hasta_cliente_selecciona_grupos_msg = 'Esperando a aceptar la selección de grupos donde compartir...'
        t_informe_porcenataje_completado_msg = '% completado'
        t_crear_post_info_to_user_message = 'Escribe aquí lo que quieres publicar y clica en Publicar cuando estés seguro y quieras compartirlo en todos los grupos anteriormente seleccionados'
        t_crear_post_esperando_a_crear_post_para_publicar = 'Esperando para crear el post para publicar...'
        t_dismiss_alert_alerta_manejada = 'Alerta manejada'
        t_dismiss_alert_ninguna_alerta_encontrada = 'No se encontró ninguna alerta. Continuando...'
        t_publicar_en_cada_grupo_sin_problemas_al_agregar_link = 'No ha aparecido ningún problema con agregar el link en la publicación. Continuando...'
        t_mensage_final_cerrar_bot_contenido_publicado_en_todos_grupos = 'Contenido publicado en todos los grupos'
        t_mensage_final_cerrar_bot_cerrando_en_10s_y_agradecimiento = f'Cerrando en 10 segundos.\n{"-"*30}\nAlvaro624la te agradece haber utilizado su herramienta y espera que te haya sido útil ;D'
        t_mensage_final_cerrar_bot_cerrando_en_3s = 'Cerrando en 3 segundos'
        t_mensage_final_cerrar_bot_cerrando_en_2s = 'Cerrando en 2 segundos'
        t_mensage_final_cerrar_bot_cerrando_en_1s = 'Cerrando en 1 segundo'
    else:
        # JS
        t_ask_credentials_user = "User / Email"
        t_ask_credentials_password = "Password"
        t_ask_credentials_accept = "Accept"
        t_ask_group_selection_accept = "Accept"
        t_create_post_publicar = "Post"
        # PY
        t_ask_credentials_info_to_user_message = "Please enter the credentials so that the BOT can operate and view your groups"
        t_ask_credentials_esperando_a_obtener_credenciales = 'Waiting to get the credentials...'
        t_cookies_rechazando_cookies_opcionales = 'Rejecting optional cookies'
        t_cookies_config_cookies_definida_continuando = 'Cookie configuration already defined. Continuing...'
        t_facebook_login_intentos_inicio_sesion_msg = 'times you have tried to log in.\nThere is some problem external to this Facebook BOT that prevents you from logging in correctly.\nCheck the error that the Facebook page shows you and try to fix it to try to log in again. Closing in 15 seconds'
        t_facebook_login_iniciando_sesion = 'Logging in...'
        t_facebook_login_info_to_user_message = 'Failed to login. Follow the steps that Facebook shows you to log in completely'
        t_ir_a_grupos_sesion_iniciada_exitosamente = 'Session started successfully'
        t_ir_a_grupos_dirigiendome_a_grupos = 'Addressing me to groups'
        t_ir_a_grupos_dirigiendome_a_grupos_via_URL = 'Going to groups via specific URL .../groups/feed/'
        t_obtener_obj_grupos_grupo_obtenido = 'Obtaining links: group obtained'
        t_obtener_obj_grupos_procesando = 'Obtaining links: processing...'
        t_obtener_obj_grupos_link_ya_existente = 'Obtaining links: already existing link'
        t_js_function_info_to_user_message = 'Please select the groups where you want to share'
        t_esperar_hasta_cliente_selecciona_grupos_msg = 'Waiting to accept the selection of groups to share...'
        t_informe_porcenataje_completado_msg = '% completed'
        t_crear_post_info_to_user_message = 'Write here what you want to publish and click on Publish when you are sure and want to share it in all the previously selected groups'
        t_crear_post_esperando_a_crear_post_para_publicar = 'Waiting to create the post to publish...'
        t_dismiss_alert_alerta_manejada = 'Alert handled'
        t_dismiss_alert_ninguna_alerta_encontrada = 'No alert was found. Continuing...'
        t_publicar_en_cada_grupo_sin_problemas_al_agregar_link = 'There has been no problem with adding the link in the publication. Continuing...'
        t_mensage_final_cerrar_bot_contenido_publicado_en_todos_grupos = 'Content posted in all groups'
        t_mensage_final_cerrar_bot_cerrando_en_10s_y_agradecimiento = f'Closing in 10 seconds.\n{"-"*30}\nAlvaro624la thanks you for using his tool and hopes it has been useful to you ;D'
        t_mensage_final_cerrar_bot_cerrando_en_3s = 'Closing in 3 seconds'
        t_mensage_final_cerrar_bot_cerrando_en_2s = 'Closing in 2 seconds'
        t_mensage_final_cerrar_bot_cerrando_en_1s = 'Closing in 1 second'

### IDIOMA:
def ask_language(language=None):
    global language_set
    try:
        if language:
            # return language
            language_set = language
        else:
            # Ventana emergente para que el cliente introduzca los credenciales
            info_to_user_message = 'Selecciona el idioma / Select the language'
            info_to_user_div = pop_up.LANGUAGE(info_to_user_message)
            driver.execute_script(info_to_user_div)

            html_oculto_language_selected = driver.find_element(By.ID, "language_selected")
            while html_oculto_language_selected.get_attribute("innerHTML") != 'True':
                time.sleep(1)
                print('Esperando para seleccionar el idioma... / Waiting to select the language...')
            # Cuando el idioma se ha seleccionado, obtenemos su valor
            html_input_language_email = driver.find_element(By.ID, "language_final_selected_name")
            language = html_input_language_email.get_attribute("innerHTML")
            # return language
            language_set = language
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y la contraseña de Facebook del usuario mediante preguntas --> {err}')

### CREDENCIALES:
def ask_credentials(user_email=None, user_password=None):
    try:
        if user_email and user_password:
            return user_email, user_password
        else:
            # Ventana emergente para que el cliente introduzca los credenciales
            info_to_user_message = t_ask_credentials_info_to_user_message
            info_to_user_div = pop_up.CREDENTIALS(info_to_user_message, t_ask_credentials_user, t_ask_credentials_password, t_ask_credentials_accept)
            driver.execute_script(info_to_user_div)

            html_oculto_credenciales_introducidos = driver.find_element(By.ID, "credenciales_introducidos")
            while html_oculto_credenciales_introducidos.get_attribute("innerHTML") != 'True':
                time.sleep(1)
                print(t_ask_credentials_esperando_a_obtener_credenciales)

            html_input_user_email = driver.find_element(By.ID, "credentials_name_input")
            html_input_user_password = driver.find_element(By.ID, "credentials_password_input")
            user_email = html_input_user_email.get_attribute("value")
            user_password = html_input_user_password.get_attribute("value")
            return user_email, user_password
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y la contraseña de Facebook del usuario mediante preguntas --> {err}')


### DRIVER CONFIG:
# Configurar las opciones del navegador para desactivar las notificaciones de forma predeterminada
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# se crea una instancia del webdrive chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def open_url_after_driver_config():
    # abrimos la url y se espera a que esté completamente cargada con el metodo get de driver
    driver.get("https://www.facebook.com/")

### VERIFICACION TITULO PAGINA:
def verify_page_title():
    try:
        # tiempo manual preventivo para que no lance el error assert cuando aún no ha cargado la página ni el title
        time.sleep(1)
        # verificamos si el titulo de la página del driver es Facebook. Si no es, lanza error.
        assert "Facebook" in driver.title
    except AssertionError as err:
        print(f'Error de tipo AssertionError. El título de la página no coincide con la página cargada --> {err}\n\nCerrando en 5 segundos')
        time.sleep(5)
        driver.close()

### COOKIES:
def cookies():
    # detectamos si existe un boton de cookies, y las rechazamos. Si este no existe, seguimos
    # Usar *loc.COOKIES permite desempaquetar la tupla
    try:
        WebDriverWait(driver, 5).until(EC.any_of(
            EC.presence_of_element_located((loc.COOKIES_ES)),
            EC.presence_of_element_located((loc.COOKIES_CA)),
            EC.presence_of_element_located((loc.COOKIES_EN))
        ))
        btn_cookies = WebDriverWait(driver, 5).until(EC.any_of(
            EC.element_to_be_clickable((loc.COOKIES_ES)),
            EC.element_to_be_clickable((loc.COOKIES_CA)),
            EC.element_to_be_clickable((loc.COOKIES_EN))
        ))
        btn_cookies.click()
        print(t_cookies_rechazando_cookies_opcionales)
    except Exception:
        print(t_cookies_config_cookies_definida_continuando)

### INICIAR SESION
intentos_inicio_sesion = 0
def facebook_login():
    global intentos_inicio_sesion
    if intentos_inicio_sesion >= 3:
        print({intentos_inicio_sesion} + " " + {t_intentos_inicio_sesion_msg})
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
        print(t_facebook_login_iniciando_sesion)
        intentos_inicio_sesion += 1
    except:
        # Sesion ya iniciada, porque no encuentra los campos de inicio de sesion email, pass y login
        print(t_facebook_login_iniciando_sesion)

    # Comprobación del correcto iniciado sesión (usando try except de manera inversa)
    try:            
        try:
            WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.LOGIN_ERR_MSG_1))
            # info_to_user_message = "Error al iniciar sesión. Siga los pasos que Facebook le marca, para iniciar sesión por completo"
            info_to_user_div = pop_up.QUICK_MESSAGE(t_facebook_login_info_to_user_message)
            driver.execute_script(info_to_user_div)
            # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito. Pongo 999 de espera por si la cuenta tiene verificacion en dos pasos con el movil para dar tiempo a completarla y entrar en facebook, y seguir el proceso
            WebDriverWait(driver, 60).until(EC.presence_of_element_located(loc.GROUPS_BTN))
        except:
            WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.LOGIN_ERR_MSG_2))
            # info_to_user_message = "Error al iniciar sesión. Siga los pasos que Facebook le marca, para iniciar sesión por completo"
            info_to_user_div = pop_up.QUICK_MESSAGE(t_facebook_login_info_to_user_message)
            driver.execute_script(info_to_user_div)
            # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito. Pongo 999 de espera por si la cuenta tiene verificacion en dos pasos con el movil para dar tiempo a completarla y entrar en facebook, y seguir el proceso
            WebDriverWait(driver, 60).until(EC.presence_of_element_located(loc.GROUPS_BTN))
    except:
        # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito. Pongo 999 de espera por si la cuenta tiene verificacion en dos pasos con el movil para dar tiempo a completarla y entrar en facebook, y seguir el proceso
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(loc.GROUPS_BTN))

### IR A TUS GRUPOS
def ir_a_grupos():
    print(t_ir_a_grupos_sesion_iniciada_exitosamente)
    try:
        # busco el enlace a grupos y le doy click
        btn_grupos = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.GROUPS_BTN))
        print(t_ir_a_grupos_dirigiendome_a_grupos)
        btn_grupos.click()
    except Exception as err:
        # print(f'Error de tipo "{type(err).__name__}" al buscar el enlace a grupos --> {err}')
        print(t_ir_a_grupos_dirigiendome_a_grupos_via_URL)
        driver.get("https://www.facebook.com/groups/feed/")

#########################################################################################
################################ OBTENER LINKS DE GRUPOS ################################

def obtener_obj_grupos():
    #########################################################################################
    ############# EN CASO DE NO ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ########################

    # Encontrar todos los enlaces de grupos en la url actual, que no tengan el panel principal role"main" como elemento padre (para no obtener links de grupos sugeridos)
    # all_a_tags = driver.find_elements(By.XPATH, '//a[not(ancestor::div[@role="main"])]')

    #########################################################################################
    #################### ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ###############################
    driver.get("https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="main"]')))

    arr_obj_grupos_obtenidos = []
    
    # bajar pagina hasta abajo para cargar todos los grupos 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Esperar un momento para que la página cargue completamente
    time.sleep(3)
    # bajar página de nuevo por si acaso
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # dentro de --> 
    panel_central = WebDriverWait(driver, 10).until(EC.any_of(
        EC.presence_of_element_located((By.XPATH, '//div[@role="main" and @aria-label="Preview of a group"]')),
        EC.presence_of_element_located((By.XPATH, '//div[@role="main" and @aria-label="Vista previa de un grupo"]'))
    ))
    # print('panel central: ')
    print(panel_central)
    # de cada padre --> role="listitem": 
    list_item = panel_central.find_elements(By.XPATH, '//div[@role="listitem"]') # por si sirve, también tiene --> style="max-width: 600px; min-width: 320px;"
    # print('COMP0: list_item length: ')
    print(len(list_item))
    array_existe_link = []
    grupo_index = -1
    for grupo in list_item:
        try:
            # el tag --> 
            a_tag = WebDriverWait(grupo, 0).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
            # el link dentro del tag-->
            link_regex = re.search(r"https://www.facebook.com/groups/\d+", a_tag.get_attribute("href"))
            link = link_regex.group()

            if link not in array_existe_link:
                # añadelo para la siguiente comprobación
                array_existe_link.append(link)

                grupo_index += 1
                # la img --> 
                img_tag = WebDriverWait(grupo, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'image')))
                img_url = img_tag.get_attribute("xlink:href")

                # el titulo --> 
                title_tag = WebDriverWait(grupo, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'svg')))
                title = title_tag.get_attribute("aria-label")

                # crea un nuevo obj
                new_obj = {
                    'index': 0,
                    'link': '',
                    'img_url': '',
                    'title': ''
                }
                # asigna valores al obj
                new_obj['index'] = grupo_index
                new_obj['link'] = link
                new_obj['img_url'] = img_url
                new_obj['title'] = title
                arr_obj_grupos_obtenidos.append(new_obj)

                # print('arr_obj_grupos_obtenidos-------------------------------------------------------------------------------------')
                # print(len(arr_obj_grupos_obtenidos))
                print(t_obtener_obj_grupos_grupo_obtenido)
        except Exception as err:
            print(t_obtener_obj_grupos_procesando)

            # print('a_tag: ')
            # print(err)
        print(t_obtener_obj_grupos_link_ya_existente)
    return arr_obj_grupos_obtenidos

def js_function():
    # Elegir grupos donde publicar (internamente: agregar o quitar links de los grupos del array --> arr_links_grupos_obtenidos y agregarlos al arr final de links --> arr_links_grupos_seleccionados)
    # arr_obj_prueba = ['https://www.facebook.com/groups/740970037910764', 'https://www.facebook.com/groups/867005741560869']
    # arr_obj_grupos_obtenidos_ej = [{'index': 0, 'link': 'https://www.facebook.com/groups/1113068039716987', 'img_url': 'https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/429679221_2579686565547152_5684308905641758804_n.jpg?stp=cp0_dst-jpg_s110x80&_nc_cat=103&ccb=1-7&_nc_sid=aae68a&_nc_ohc=mgnzalFHSQkAX9lcfZY&_nc_ht=scontent-mad1-1.xx&oh=00_AfDGcA6adJsCdZYMLOWO1fj5DIH7wZhnJA0_6woVj8y7nw&oe=65E94F31', 'title': 'pruebas alvaro 2'}, {'index': 1, 'link': 'https://www.facebook.com/groups/1478094899435458', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'Pruebas alvaro'}, {'index': 2, 'link': 'https://www.facebook.com/groups/867005741560869', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'pruebas 2'}, {'index': 3, 'link': 'https://www.facebook.com/groups/740970037910764', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'pruebas 1'}]
    info_to_user_message = t_js_function_info_to_user_message
    info_to_user_div = pop_up.GROUP_SELECTION(info_to_user_message, arr_obj_grupos_obtenidos, t_ask_group_selection_accept)
    driver.execute_script(info_to_user_div)

def esperar_hasta_cliente_selecciona_grupos():
    div_ids_oc_sel = driver.find_element(By.ID, "ids_ocultos_seleccionados")
    while div_ids_oc_sel.get_attribute("innerHTML") != 'True':
        time.sleep(1)
        print(t_esperar_hasta_cliente_selecciona_grupos_msg)

def finds_links_with_ids_ocultos_arr():
    ids_ocultos = driver.find_element(By.ID, "ids_ocultos")
    ids_ocultos_innerHTML = ids_ocultos.get_attribute("innerHTML")
    arr_indices_ocultos_seleccionados = ids_ocultos_innerHTML.split(',')
    arr_final_links = []

    for indice_oculto in arr_indices_ocultos_seleccionados:
        try:
            # Convertimos el índice a entero para usarlo como índice en arr_obj_grupos_obtenidos
            indice_oculto = int(indice_oculto.strip())
            if arr_obj_grupos_obtenidos[indice_oculto]['link']:
                arr_final_links.append(arr_obj_grupos_obtenidos[indice_oculto]['link'])
        except Exception as err:
            print(f"Error al obtener el enlace del grupo con índice {indice_oculto}: {err}")

    print(arr_final_links)
    return arr_final_links
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
porcentaje_completado = 0
def informe_porcenataje_completado():
    porcentaje_unico_link = (1 * 100) / len(arr_links_grupos_obtenidos)
    # /3 porque son 3 los procesos para publicar: abrir cuadro/escribir/btn publicar, y quiero que en cada uno informe del porcentaje
    global porcentaje_completado 
    porcentaje_completado += porcentaje_unico_link/3
    print(f'{int(round(porcentaje_completado, 0))}{t_informe_porcenataje_completado_msg}')

######################################################################################################
################################# EL USUARIO ESCRIBE EL POST DESEADO #################################

def crear_post():
    # Ventana emergente para que el cliente cree el post
    # info_to_user_message = "Escribe aquí lo que quieres publicar y clica en Publicar cuando estés seguro y quieras compartirlo en todos los grupos anteriormente seleccionados"
    info_to_user_div = pop_up.CREATE_POST(t_crear_post_info_to_user_message, t_create_post_publicar)
    driver.execute_script(info_to_user_div)

    post_creado = driver.find_element(By.ID, "post_creado")
    while post_creado.get_attribute("innerHTML") != 'True':
        time.sleep(1)
        print(t_crear_post_esperando_a_crear_post_para_publicar)

    html_textarea_post_created = driver.find_element(By.ID, "create_post_input")
    post = html_textarea_post_created.get_attribute("value")

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
        print(t_dismiss_alert_alerta_manejada)
    except:
        print(t_dismiss_alert_ninguna_alerta_encontrada)

# Recorremos el array con todos los links de grupos y publicamos en cada uno
def publicar_en_cada_grupo():
    for link in arr_links_grupos_obtenidos:
        dismiss_alert()
        try:
            driver.get(link)
            # Espera a que cargue el escribe algo box y localizamos el elemento para clicarlo posteriormente
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            WebDriverWait(driver, 10).until(EC.any_of(
                EC.presence_of_element_located((loc.GROUP_WRITE_STG_LINEBOX_ES)),
                EC.presence_of_element_located((loc.GROUP_WRITE_STG_LINEBOX_EN))
            ))
            escribe_algo_box = WebDriverWait(driver, 10).until(EC.any_of(
                EC.element_to_be_clickable((loc.GROUP_WRITE_STG_LINEBOX_ES)),
                EC.element_to_be_clickable((loc.GROUP_WRITE_STG_LINEBOX_EN))
            ))
            escribe_algo_box.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 1 de tipo {type(err).__name__} - Encontrar cuadro de dialogo para escribir --> {err}')
        
        dismiss_alert()
        try:
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.POST_WRITE_BOX))
            crea_una_publicacion_publica = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.POST_WRITE_BOX))
            print(contenido_publicacion)
            crea_una_publicacion_publica.click()
            crea_una_publicacion_publica.send_keys(contenido_publicacion)
            try:
                # Si sale un cuadro de texto sobre "Información adicional sobre este contenido" le damos a "Compartir de todas formas"
                WebDriverWait(driver, 3).until(EC.any_of(
                    EC.presence_of_element_located((loc.WARNING_LINK_POPUP_ES)),
                    EC.presence_of_element_located((loc.WARNING_LINK_POPUP_EN))
                ))
                popup_adicional_al_pegar_link = WebDriverWait(driver, 3).until(EC.any_of(
                    EC.element_to_be_clickable((loc.WARNING_LINK_POPUP_ES)),
                    EC.element_to_be_clickable((loc.WARNING_LINK_POPUP_EN))
                ))
                popup_adicional_al_pegar_link.click()
            except:
                print(t_publicar_en_cada_grupo_sin_problemas_al_agregar_link)
            # Tiempo de espera para que la miniatura del posible link de la publicación se cargue correctamente (tiempo de espera estimado, a ojimetro)
            time.sleep(2)
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 2 de tipo {type(err).__name__} - Escribir en el recuadro --> {err}')

        dismiss_alert()
        try:
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            WebDriverWait(driver, 10).until(EC.any_of(
            EC.presence_of_element_located((loc.POST_BTN_ES)),
            EC.presence_of_element_located((loc.POST_BTN_EN))
        ))
            btn_publicar = WebDriverWait(driver, 10).until(EC.any_of(
            EC.element_to_be_clickable((loc.POST_BTN_ES)),
            EC.element_to_be_clickable((loc.POST_BTN_EN))
        ))
            btn_publicar.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 3 de tipo {type(err).__name__} - Click en el boton Publicar --> {err}')
            
        # Esperar a que el boton de Publicar desaparezca
        btn_publicar = WebDriverWait(driver, 20).until_not(EC.any_of(
            EC.presence_of_element_located((loc.POST_BTN_ES)),
            EC.presence_of_element_located((loc.POST_BTN_EN))
        ))
        
        #Se vuelve a ejecutar el bucle for, hasta que no queden mas links en el arr --> arr_links_grupos_obtenidos

################################# ABRIR LINKS Y PUBLICAR #################################
##########################################################################################

def mensage_final_cerrar_bot():
    informe_porcenataje_completado()
    print(t_mensage_final_cerrar_bot_contenido_publicado_en_todos_grupos)

    print(t_mensage_final_cerrar_bot_cerrando_en_10s_y_agradecimiento)
    print(r"                       _            ")
    print(r"                      (_)           ")
    print(r"   __ _ _ __ __ _  ___ _  __ _ ___  ")
    print(r"  / _` | '__/ _` |/ __| |/ _` / __| ")
    print(r" | (_| | | | (_| | (__| | (_| \__ \ ")
    print(r"  \__, |_|  \__,_|\___|_|\__,_|___/ ")
    print(r"   __/ |                            ")
    print(r"  |___/   ")
    time.sleep(7)
    print(t_mensage_final_cerrar_bot_cerrando_en_3s)
    time.sleep(1)
    print(t_mensage_final_cerrar_bot_cerrando_en_2s)
    time.sleep(1)
    print(t_mensage_final_cerrar_bot_cerrando_en_1s)
    time.sleep(1)
    driver.close()


############################################################################
################################# FUNCIONES ################################
############################################################################
# CONFIG
open_url_after_driver_config()
verify_page_title()

# LANGUAGE
###################### Automatic language ######################
# To set the language automatically for every execution, you can add your data between quotes (single or double), like this:
# -->> language = ask_language('your_language_here') <<--
# Here is the available abbreviations:
    # for English put --> EN
    # for Spanish put --> ES
# below:
language = ask_language('')
language_set_function()
cookies()
# LOGIN
###################### Automatic login ######################
# To log in automatically, you can add your data between quotes (single or double) separated by a comma, like this:
# -->> user_email, user_password = ask_credentials('your_email_here', 'your_password_here') <<--
# below:
user_email, user_password = ask_credentials('', '')
############################################################################


facebook_login()
# SELECCIÓN GRUPOS 
ir_a_grupos()
arr_obj_grupos_obtenidos = obtener_obj_grupos()
js_function()
esperar_hasta_cliente_selecciona_grupos()
# CREAR POST
contenido_publicacion = crear_post()
# PUBLICAR
arr_links_grupos_obtenidos = finds_links_with_ids_ocultos_arr()
publicar_en_cada_grupo()
# AGRADECIMIENTOS Y CERRAR
mensage_final_cerrar_bot()
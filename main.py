import time
import requests
from bs4 import BeautifulSoup
import winsound
import threading

def check_availability(url, keyword, check_interval=60):
    """
    Monitorea una página web para detectar si un producto está disponible.
    
    Args:
        url (str): La URL de la página del producto.
        keyword (str): Texto que indica que el producto NO está disponible (ejemplo: 'SOLD OUT').
        check_interval (int): Intervalo de tiempo entre verificaciones (en segundos).
    """
    print(f"Monitoreando {url} cada {check_interval} segundos...")

    while True:
        try:
            # Hacer la solicitud HTTP
            response = requests.get(url)
            response.raise_for_status()  # Verifica que la solicitud fue exitosa

            # Analizar el contenido HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text().lower()  # Todo en minúsculas para buscar el keyword

            # Verificar si el producto sigue "SOLD OUT"
            if keyword.lower() not in page_text:
                print(f"¡El producto en {url} está DISPONIBLE!")
                
                # Reproducir un "beep" usando winsound
                winsound.Beep(500, 8000)  # Frecuencia 1000 Hz, duración 500 ms
                break
            else:
                print(f"El producto en {url} sigue SOLD OUT...")

        except Exception as e:
            print(f"Error durante la solicitud a {url}: {e}")

        time.sleep(check_interval)  # Esperar antes de volver a consultar

def monitor_multiple_sites(urls, keyword, check_interval=60):
    """
    Monitorea múltiples sitios web para detectar si un producto está disponible usando hilos.
    
    Args:
        urls (list): Lista de URLs de los productos.
        keyword (str): Texto que indica que el producto NO está disponible (ejemplo: 'SOLD OUT').
        check_interval (int): Intervalo de tiempo entre verificaciones (en segundos).
    """
    threads = []

    # Crear un hilo por cada URL
    for url in urls:
        thread = threading.Thread(target=check_availability, args=(url, keyword, check_interval))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

# Configura las URLs de los productos y la palabra clave
product_urls = [
    "https://fioko.shop/collections/sonny-angel/products/sonny-angel-kiss-kiss",  # Primera página que deseas monitorear
    "https://www.sonnyangel-france.com/collections/sonny-angel/products/serie-sonny-angel-kiss-kiss"   # Segunda página que deseas monitorear
]
sold_out_keyword = "Épuisé"  # Cambia según el texto que indique que no hay stock (Ejemplo: "SOLD OUT")
interval = 60  # Tiempo entre verificaciones en segundos (1 minuto)

# Inicia el monitoreo de ambos sitios web usando hilos
monitor_multiple_sites(product_urls, sold_out_keyword, interval)

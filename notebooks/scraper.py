import requests
import re
import csv
import os
from bs4 import BeautifulSoup

# Ruta de salida para el CSV
output_dir = r"C:\DataAnalysis\PortalInmobiliario\data\raw"
output_file = os.path.join(output_dir, "properties.csv")

# Eliminar el archivo CSV si ya existe
if os.path.exists(output_file):
    os.remove(output_file)
    print(f"Archivo existente '{output_file}' eliminado.")

# Función para obtener las URL de los HTML de todas las propiedades
def fetch_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        property_list = soup.find_all('div', class_='ui-search-result__wrapper')

        for property_item in property_list:
            link_tag = property_item.find('a', class_='ui-search-link')
            link = link_tag['href'] if link_tag else None
            if link:
                links.append(link)

        return links
    else:
        print(f"Error al acceder a {url}")
        return None

# Función para extraer información de una URL dada
def extract_info_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        lines_lower = response.text.lower()
        
        palabras_clave = ["baños", "m² totales", "dormitorios"]
        resultados = {}
        
        for palabra in palabras_clave:
            pattern = re.compile(r'(\d+)\s+' + re.escape(palabra))
            numeros_encontrados = pattern.findall(lines_lower)
            numeros_unicos = list(set(numeros_encontrados))
            resultados[palabra] = numeros_unicos[0] if numeros_unicos else None

        return resultados
    else:
        print(f"Error al acceder a {url}")
        return None

# URL principal de la búsqueda
main_url = "https://www.portalinmobiliario.com/arriendo/casa/concepcion-biobio"

# Obtener las URLs de todas las propiedades
property_urls = fetch_links(main_url)

# Contador de URLs que no pudieron ser leídas correctamente
errores_count = 0

# Escribir los resultados en un archivo CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["url", "baños", "m² totales", "dormitorios", "error"])  # Cabecera del CSV
    
    for property_url in property_urls:
        print(f"Extrayendo información de: {property_url}")
        info = extract_info_from_url(property_url)
        if info:
            writer.writerow([
                property_url,
                info.get("baños"),
                info.get("m² totales"),
                info.get("dormitorios"),
                "No"
            ])
        else:
            writer.writerow([
                property_url,
                None,  # Sin datos para baños
                None,  # Sin datos para m² totales
                None,  # Sin datos para dormitorios
                "Sí"  # Indica que hubo un error
            ])
            errores_count += 1

# Imprimir el número de URLs que no pudieron ser leídas
print(f"Proceso completado. No se pudieron leer {errores_count} URLs.")

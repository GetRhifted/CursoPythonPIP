import requests
from bs4 import BeautifulSoup

# Establecer la URL de búsqueda
url = "https://co.indeed.com/jobs?q=Desarrollador+python&l=&from=sug&vjk=ec5b0e9f0e6dd504"

# Parámetros de búsqueda
params = {
    "q": "Desarrollador Python",
    "l": "Colombia o Remoto",
    "sort": "date"
}

# Realizar la petición HTTP y obtener la respuesta
response = requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar los elementos de trabajo
results = soup.find(id='resultsCol')
job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

# Verificar si se encontraron trabajos
if len(job_elems) == 0:
    print("No se encontraron trabajos.")
else:
    # Crear y abrir el archivo para escribir los datos
    with open("jobs.txt", "w", encoding='utf-8') as file:
        # Iterar sobre cada elemento de trabajo y extraer los datos necesarios
        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('span', class_='company')
            location_elem = job_elem.find('div', class_='recJobLoc')
            summary_elem = job_elem.find('div', class_='summary')

            # Verificar que todos los elementos necesarios se hayan encontrado antes de escribirlos en el archivo
            if None in (title_elem, company_elem, location_elem, summary_elem):
                continue

            # Escribir los datos en el archivo
            file.write("Título: {}\n".format(title_elem.text.strip()))
            file.write("Empresa: {}\n".format(company_elem.text.strip()))
            file.write("Ubicación: {}\n".format(location_elem.text.strip()))
            file.write("Descripción: {}\n".format(summary_elem.text.strip()))
            file.write("\n")

    # Imprimir mensaje de éxito
    print("Programa ejecutado correctamente.")








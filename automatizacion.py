import requests
import csv
import time

while True:  # Bucle infinito para ejecutar la tarea repetidamente
    try:
        response = requests.get('http://localhost:3000/names')  # Hacer una solicitud GET a la API
        response.raise_for_status()  # Verificar si la solicitud fue exitosa (código de estado 200)
        try:
            data = response.json()  # Obtener los datos en formato JSON
        except requests.exceptions.JSONDecodeError:
            print("Error: No se pudo decodificar la respuesta JSON.")
            data = []
        
        if data:  # Verificar si data no está vacío
            with open('data.csv', mode='w', newline='') as file:  # Abrir un archivo CSV en modo escritura
                writer = csv.writer(file)  # Crear un escritor de CSV
                # Escribir los encabezados de las columnas
                writer.writerow(['id', 'nombre', 'correo'])
                # Iterar sobre los datos obtenidos y escribir cada fila en el archivo CSV
                for row in data:
                    writer.writerow([row['id'], row['nombre'], row['correo']])
            print("Datos guardados correctamente en data.csv")
        else:
            print("No se recibieron datos válidos de la API.")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")

    time.sleep(3600)  # Esperar una hora antes de la siguiente ejecución

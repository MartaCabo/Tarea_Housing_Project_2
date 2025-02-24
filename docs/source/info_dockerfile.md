
# 🐳 Uso del Dockerfile

Este proyecto incluye un `Dockerfile` para facilitar la ejecución del código en un entorno aislado.

Ejecuta el siguiente comando en la terminal desde la raíz del proyecto:

```bash
docker build -t housing_price .
```

Este comando construirá la imagen de Docker con el nombre `housing_price`.

Para ejecutar el contenedor, utiliza el siguiente comando:

```bash
docker run -it --rm -v  $(pwd):/app housing_price train.csv test.csv prediciones.csv
```
Donde `$(pwd)` es el directorio actual en tu máquina local.

Este comando ejecutará el script `main.py` dentro del contenedor de Docker y guardará las predicciones en un archivo `predicciones.csv`, utilizando los archivos `train.csv` y `test.csv` como entrada. 

Asegúrate de tener dichos archivos en tu máquina locales, ya que no vienen en el repositorio.
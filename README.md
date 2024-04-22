
# GopyFlow 

GopyFlow reune todo el potencial de la clase Translator de la API de traducción de texto de googletrans con las poderosas herramientas de pytesseract de reconocimiento de texto en imágenes.

## Metodo gopy:

El método Gopy permite extraer textos en inglés de una lista de imágenes, los traduce al español y los guarda como contenido unitario, tanto el texto detectado como su respectiva traducción, cuyo título acompañante hace referencia al nombre de la imágen gestionada.

## Documentación técnica

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |
| Paso 5 | Corra el programa. | py demo.py |

### Librerías del proyecto.
| librería  | Descripción              | Comando                           |
| :----     | :---                     | :---                              |
| pytesseract | Herramienta de reconocimiento de texto en imagenes. | Se debe descargar una librería y un ejectuable en el sistema operativo.|
||Descarga del ejecutable |https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe|
||Descarga de la librería| pip install pytesseract |
| Pillow  | La biblioteca de imágenes de Python agrega capacidades de procesamiento de imágenes a su intérprete de Python.  | pip install pillow |
| googletrans      | API gratuita de traducción de texto. | pip install googletrans==4.0.0rc1|


> Con la instalación de la librería pytesseract se instalarán las
siguientes librerías de manera automática:
<pre>
packaging==24.0
pillow==10.3.0
pytesseract==0.3.10
</pre>

> Con la instalación de la librería googletrans==4.0.0rc1 se instalarán las siguientes librerías de manera automática:
<pre>
certifi==2024.2.2
chardet==3.0.4
googletrans==4.0.0rc1
h11==0.9.0
h2==3.2.0
hpack==3.0.0
hstspreload==2024.4.1
httpcore==0.9.1
httpx==0.13.3
hyperframe==5.2.0
idna==2.10
rfc3986==1.5.0
sniffio==1.3.1
</pre>

---

### Realice sus pruebas, actualizaciones o modificaciones.
> Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

> Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Corra el programa. |  py demo.py |
| Paso 8 | Finalice su gestión.                          | deactivate                            |

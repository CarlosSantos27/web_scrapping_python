# Web Scraping con Selenium y Poetry

Este proyecto está diseñado para realizar web scraping en sitios web protegidos por CAPTCHA utilizando Selenium como herramienta de automatización y Poetry para gestionar las dependencias.

## Instalación

Asegúrate de tener [Python](https://www.python.org/) instalado en tu sistema. Luego, sigue estos pasos:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/CarlosSantos27/web_scrapping_python.git
    cd web_scrapping_python

2. Instala y configura [poetry](https://python-poetry.org/docs/#installation)

3. Instala las dependencias

    ```bash
    poetry install

Esto instalará las bibliotecas necesarias, incluyendo Selenium.

4. Ejecuta el comando
    ```bash
    poetry run ffdl install --add-path

Esto instalará los complementos faltantes de ffdl

5. El proyecto require un WebDriver de acuerdo al sistema operativo en este caso, el proyecto fue desarrollado y probado en Windows, si desea probar en otros sistemas operativos siga los siguientes pasos:
    1. Descarga el driver de acuerdo a su sistema operativo [driver web](https://github.com/mozilla/geckodriver/releases)
    2. Una vez descargado copiar en la carpeta files de acuerdo al navegador (chrome o Firefox-gecko)
    3. En el archivo config.ini cambiar las propiedades por:
    ```bash
    web_driver=< nombre del archivo >
    default_web_browser=chrome | firefox

6. Ejecutar el servidor usando el comando
    ```bash
    poetry run uvicorn:app

7. (Opcional). Si desea visualizar el proceso para validar el catpcha cambiar el valor de la propiedad **preview** por **True**






# OCR: Validar Cuenta y Moneda
# ![OCR: Validar Cuenta y Moneda](https://pbs.twimg.com/profile_images/1219745045731074048/rPOgxE1X_400x400.jpg)




----------

# Getting started

## Requisitos
Instalar docker:

    https://docs.docker.com/get-docker/
## Instalación del contenedor

Clonar  repositorio

    git clone https://github.com/csticorp/tesseract_valida_estado_cta.git


Compilación del contenedor

    docker build -t sjp_tesseract .

Ejecutar el contenedor

    docker run --name sjp_tesseract -d -p 8000:8000 sjp_tesseract:latest

## Ejecución

Llamar a la siguiente URL

# ![Postman](postman.png)

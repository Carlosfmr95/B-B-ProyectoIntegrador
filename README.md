# B&B-ProyectoIntegrador
Bits&Bytes
Integrantes: 
- Marin, Agustín
- Muñoz, Carlos
- Ortiz, Erik Joaquín
- Rolon, Octavio
  
# EJECUCIÓN EN DOCKER

1) Clone el repositorio remoto del siguinte enlace [https://github.com/Carlosfmr95/B-B-ProyectoIntegrador.git]
2) Abra la aplicación de Docker
3) En la carpeta del repositorio clonado, abra la terminal (CMD)
4) Ingrese el siguiente comando, creará la imagen necesaria para correr la aplicación
            
    docker build -t byb_app_clima:1.0 . 

5) Para iniciar la aplicación ejecute el siguiente comando

    docker run -it --rm --name docker_byb byb_app_clima:1.0 

# Proyecto_Diciembre Víctor Sánchez Nogueira 1ºDAM

## Clockify:
Estas son las horas que dediqué al proyecto y en que las gasté:

![clockify](./Clockify.png)
No esta completamente actualizada ni estan todos los dias de trabajo pero esto es todo a lo que le hice recuento.

<!-- arquitectura -->


## Instrucciones de instalacion

1. Situate donde quieras crear la app:

```bash
$ cd C:\Users\nombredeusuario\Escritorio
```

2. Crea un directorio donde almacenar la app

```bash
$ mkdir Directorio
```

3. Situate en el directorio

```bash
$ cd Directorio
```
4. Instala python, pip3 y git:

[Instala python en este enlace si no lo tienes descargado]https://www.python.org/downloads/

```bash
$ pip --version
```
Si lo tienes instalado saltate el siguiente paso si no:

```bash
$ python -m pip install
```

Ahora instala git y comprueba que lo tienes:

```bash
$ pip install git
$ git --version
```


5. clona el proyecto en el directorio

```bash
$ git clone https://github.com/VoctorSN/Proyecto_Diciembre.git
```

6. Instala las dependencias
```bash
$ pip install -r requirements.txt
```


## Instrucciones de uso

1. Desde el cmd
--Dirigete al direcotorio Proyecto_Diciembre
--Ejecuta la app con python3
--Puedes elegir no darle parametros para que el programa busque los xspf en el directorio de PROYECTO_DICIEMBRE o  ponerle la direccion del directorio padre de los ficheros xspf, ademas tendras que darle la direccion del vlc al programa com te dice la propia app al llamarla
--La app te deevolvera mensajes si sale cualquier error de los recogidos y tambien te devolvera cuantas de las canciones del xspf se van a reproducir y cuantas no

Dificultades y mejoras
-Conventional Commits
-clockify deade el principio
-Tox
-Branches


Menciones Honorificas
-gelpi -https://github.com/dfleta/kata_tdd_pytest -katatdd -base ideas para los markers
-XploitU -me ayudo con la logica y con librerias para el desarrollo de la app 
-makigas -https://www.youtube.com/@makigas -Conventional commits
-programing5393 -https://www.youtube.com/@programming5393 -requirements.txt
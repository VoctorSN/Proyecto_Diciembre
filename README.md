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
4. Instala `python`, `pip3` y `git`:

![Instala `python` en este enlace si no lo tienes descargado]https://www.python.org/downloads/

```bash
$ pip --version
```
Si lo tienes instalado saltate el siguiente paso si no:

```bash
$ python -m pip install
```

Ahora instala `git` y comprueba que lo tienes:

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

- Desde el cmd:

1. Dirigete al direcotorio `Proyecto_Diciembre`

```bash
$ cd C:\Users\nombredeusuario\Escritorio\nombredeldirectorio\PROYECTO_DICIEMBRE
```

2. Ejecuta la app con `python3`

```bash
$ python3 app.py
```

3. Puedes elegir no darle parametros para que el programa busque los `xspf` en el directorio de `PROYECTO_DICIEMBRE` o  ponerle la direccion del directorio padre de los ficheros `xspf`, ademas tendras que darle la direccion del `vlc` al programa com te dice la propia app al llamarla

```bash
$ C:\Users\victo\Escritorio\Clase\PR\Proyecto_Diciembre>py app.py
Introduce la ruta del VLC, si pulsas ENTER se entiende por que esta en program Files C:/users/nombredeusuario/Program Files (x86)
Introduce el directorio donde se encuentran los xspf, si pulsas ENTER se entiende por que esta en este directorio
```

4. La app te deevolvera mensajes si sale cualquier error de los recogidos y tambien te devolvera cuantas de las canciones del `xspf` se van a reproducir y cuantas no

```bash
No se encuentra el vlc.exe
```

- Desde tu `IDE` favorito:

1. Abre el directorio PROYECTO_DICIEMBRE desde tu `IDE`

2. Ejecuta el archivo `app.py`

3. Selecciona los parametros

## Dificultades y mejoras

Estas son las dificultades y las mejoras que podria haber implementado al proyecto
1. `Conventional Commits`:

- Me habria gustado conocer que son los conventional Commits y como se deven escribir estos commits antes de haber empezado con el proyecto

2. `Clockify`:

- Clockify es el programa de la imagen del principio, este programa sirve para hacer recuento de cuanto tiempo dedicas a hacer cualquier actividad, y aunque solo la use la ultima semada de desarrollo sirve para que nos demos cuenta de cuanto tiempo dedicamos a que partes del proyecto

3. `Tox`:

- Tox es un programa para entre otras cosas automatizar los casos test y validar tu programa en diferentes versiones, actualmente no controlo el programa pero si le dedicase un tiempo estoy seguro de que implementar sus funcionalidades al proyecto habria sido beneficioso para él

4. `Branches`:

- Las branches que utilicé en este programa no fueron las adecuadoas ya que me cuensta entender su proposito

## Menciones Honorificas
- Este apartado lo dedico a personas y desarrolladores que me ayudaron a la creacion del programa:
1. ![dfleta](https://github.com/dfleta/kata_tdd_pytest) -katatdd -base ideas para los markers
2. `XploitU` - me ayudó con la logica y con librerias para el desarrollo de la app 
3. ![makigas](https://www.youtube.com/@makigas) - Conventional commits
4. ![programing5393](https://www.youtube.com/@programming5393) - requirements.txt
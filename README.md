# EncryptoManiac

## Encriptador de contraseñas con python y sql Lite:

Encriptador simetrico de contraseñas, son guardadas en una base de sql-lite que permiten ser recuperadas en cualquier momento con un simple comando. La consola se puede correr tanto en linux como en windows, mediante un script creado por cada uno. Cuenta con un docker file que permite dockerizar la aplicacion como tambien scripts para crear un contenedor que funcione como cli.

## Comandos de la consola:

* modificar -> para cambiar la clave de una cuenta
* eliminar  -> para borrar una cuenta
* mostrar   -> para ver la contraseña de una cuenta
* listar    -> para ver todas las cuentas en la base
* agregar   -> para agregar una nueva cuenta y contraseña en la base
* vermas    -> para ver el lista de comandos en la consola
* exit      -> para salir del terminal
* login     -> te puedes registrar o logear dentro de la app
* Pd: para ver como usar un comando escribi -> ayuda nombreComando <- ej: ayuda modificar

## Features:

- [x] Guardar contraseñas encryptadas.
- [x] Listar las contraseñas listadas en la base
- [x] Eliminar contraseñas ingresadas
- [x] No poder ingresar una contrase duplicada.
- [x] Modificar contraseñas ya ingresadas
- [X] Al momento de ingresar una contraseña no se muestra que es lo que se esta escribiendo.
- [x] Cuando se muestra una contraseña se hace en un popUp que dura 4 segundos.
- [x] Modificar contraseÃ±as ya ingresadas
- [X] Al momento de ingresar una contraseÃ±a no se muestra que es lo que se esta escribiendo.
- [x] Cuando se muestra una contraseÃ±a se hace en un popUp que dura 4 segundos.
- [x] El popUp tiene un boton para copiar al porta papeles.
- [x] Agregar prompt
- [X] Cargar una base anteriormente creada con su archivo de claves
- [ ] Agregar sitio web local.
- [X] Agregar cli.

## El espiruto del proyecto:
Este proyecto no es brindar únicamente una consola simple para poder administrar contraseñas, sino el hecho de poder desarrollar el mismo con todas las buenas 
prácticas que conozco al día de la fecha y que, creo yo, van a aportar mucho más valor al producto final por más simple que sea. En otras palabras, en este proyecto busco 
desarrollar esas habilidades que en mi día a día en mi trabajo no puedo usar.
Espero que te sirva.
Saludos!

version 1.5.0


## Hello world con Flask

antes de arrancar Flask debemos declarar una variable de entorno.

```sh
# Windows
export FLASK_APP=main.py
#Linux
set FLASK_APP=main.py
# modo debug
export FLASK_DEBUG=1

# levantar el servidro, desde el path de main
flask run
```
## Template de Jinja

mostrar variables

```html
    {{ variable }}
```

if- else
```html
    {% if <condicion>%}
        <--! html -->
    {% else %}
        <--! html -->
    {% endif %}

```
ciclo for
```html
    {% for todo in todos %}
        <li>{{todo}}</li>
    {% endfor %}
```

## Herencia de templates

podemos heredar de template ya generados, por ejemplo

tenemos a base.html


Modo debug en Flask

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
y podemos hacer que nuestro template, extienda de la misma, por ejemplo.

```html

```

## flask bootstrap 
Una vez instalado se tiene que inicializar

## configuración Development, Sesion en Flask
declaramos una variable de entorno
```sh
set FLASK_ENV=development
```
como podemos utilizar una sesión en Flask, me sirve para almacenar datos encriptados.
```python
app.config['SECRET_KEY'] = 'SUPER SECRETO'
```
guardamos la ip en la session.

## implementación de flask-bootstrap y flask-wtf

se instala, importa, despues se crea una clase para pasarlo por contexto de manera mas simple, wtf.quick_form() para que renderize de manera simple el form.

## Uso del método POST en Flask-wtf
Nuestra ruta no aceptas post, por eso agregamos un parametro "app.route('/hello', methods=['GET','POST']")"
Ya con esto tendria que estar funcionando, pero no estamos almacenando los datos que se estan ingresando.

## Desplegar flashes (mensajes emergentes)
tuve problemas con la x, se tiene que importar la libreria javascript para que tenga animacion las cosas de bootstrap.

## Pruebas basicas con Flask-testing
instalamos flask-testing
primero tenemos que crear un comando de consola para que corran todos los test, que quisieramos probrar.
importamos la libreria, pero debemos configurar la variable de entorno

se usa unittest para crar un directorio donde se encuentren todos los test.
cada test tiene que ser unico, y se debe probar un elemento a la vez.

## App Factory

## Implementación firestore

cambiar de proyecto
```sh
gcloud config set <nombre-proyecto>
```

listar todos los proyectos que tengo
```sh
gcloud config list
```
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
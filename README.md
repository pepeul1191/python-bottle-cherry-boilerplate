## Bottle Access

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

---

Fuentes:

+ https://bottlepy.org/docs/dev/deployment.html
+ https://www.pylint.org/#install
+ https://bottlepy.org/docs/dev/
+ https://github.com/pepeul1191/python-accesos-v2
+ https://stackoverflow.com/questions/31080214/python-bottle-always-logs-to-console-no-logging-to-file

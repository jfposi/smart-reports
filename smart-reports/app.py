
#NO TOCAR-----------------------------------
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
#NO TOCAR-------------------------------------------

###############################################
# importar nuestras rutas de routes.py y las opciones de devoptions.py
from routes import *

#Comentar para producción!!
from devoptions import *
###############################################




# aqui importamos todos los restos de codigo que hacen que esto funcione funciones etc

# test  




#launch server cooo
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
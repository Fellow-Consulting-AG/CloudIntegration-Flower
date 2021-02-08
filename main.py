from celery import Celery

import app.app_initializer as app_initializer



app = app_initializer.create_app_load_configurations() 
client = app_initializer.init_celery(app)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

class Config(object): 
    pass               
class ProdConfig(Config):
    pass
class DevConfig(Config):#configuramos que nuestro servidor se 
    DEBUG = True        #active en modo DEBUG O modo Desarrollo
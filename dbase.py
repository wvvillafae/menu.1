from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://WenMass:0612wendy@senabasedata.ymceuxe.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["recetas"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db

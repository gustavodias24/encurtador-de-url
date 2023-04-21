from decouple import config
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://{}:{}@clusterurls.wwd3kag.mongodb.net/?retryWrites=true&w=majority".format(
        config("USER"),
        config("PASS")
    )
)

db = client["dataGeral"]
col = db["colUrls"]

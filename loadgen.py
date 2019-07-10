import json
#import kafka
import configparser

class LoadGen:
    def __init__(self):
        print("loadgen init")

    def get_val(self):
        print("getter")

    def set_val(self):
        print("setter")

    def readJson(self, file):
        print("Json file ")
        #str = "json_test.json" # json file
        with open(file,"r") as fp:
            fp_json = json.load(fp)

        return fp_json

    def jsonParsing(self):
        #specific parse for the json data and store in DB

        return

    def connectToDB(self, obj):
        my_cursor = kafka.connect()
        #prepare data and obj to write into
        my_cursor.write(obj)

    def readConfig(self, connection):
        # read properties
        my_prop = configparser.RawConfigParser()
        # read project specific configuration

        # connection to the server
        #IP, port name , protocol to be used,
        con = connection(ip, port)
        #

        return con


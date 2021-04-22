from flask import Flask
from flask_restful import Api,Resource,abort

app = Flask(__name__)
apiObject = Api(app)

place = {"A" : {"Name" : "A", "province" : "BKK", "Type":1}, "B" : {"Name" : "B", "province" : "BKK", "Type":2}}

#design
class Location(Resource):
     #get -> Get data from Server
    def get(self,name):
        #return Dict or JSON {"key" : "value"}
        return place[name]

    #post Client sent data
    def post(self):
        return {"Wat" : "BKK"}





#call
apiObject.add_resource(Location, "/path/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
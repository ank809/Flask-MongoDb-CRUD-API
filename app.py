from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test-api'
mongodb = PyMongo(app).db

@app.route('/get_or_post', methods=['GET', 'POST'])
def get_or_post():
    if request.method == 'GET':
        item=[]
        todo=mongodb.todo.find({})
        for todos in todo:
            items={
                'id': str(todos['_id']),
                'title':todos['title'],
                'desc':todos['desc']
            }
            item.append(items)
        return item
    else:
        item = {}
        item['title'] = request.json['title']
        item['desc'] = request.json['desc']
        mongodb.todo.insert_one(item)
        return 'todo add successfully'


@app.route("/update_or_delete/<string:id>", methods=['PUT', 'DELETE'])
def update_delete(id):
    if request.method=="PUT":
        mongoid= ObjectId(id)
        mongodb.todo.find_one_and_update({"_id":mongoid}, {"$set":{"title":"Ankita"}})
        return "todo successfully updated"
    else:
        mongoid = ObjectId(id)
        mongodb.todo.find_one_and_delete({"_id": mongoid})
        return "todo successfully deleted"
if __name__ == '__main__':
    app.run(debug=True)

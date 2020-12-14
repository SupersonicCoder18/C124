from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "title": "Buy Groceries",
        "description": "Milk, Cheese, Pizza Base, Vegetables, Fruits",
        "done": False
    },
    {
        "id": 2,
        "title": "Buy Laptops",
        "description": "AirBook, TufSeries3, DellInspiron, LenovoV3, SonyLivfree",
        "done": False
    }
]
@app.route("/")
def Hello_World():
    return "Hello World!!!!"
@app.route("/add-data", methods = ["post"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the Data"
        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task Added Successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })
if(__name__ == "__main__"):
    app.run(debug = True)
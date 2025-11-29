from flask import Flask, request, jsonify
import json

app = Flask(__name__)

FILE = "data.json"

# 读取数据
def load_data():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存数据
def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/publish", methods=["POST"])
def publish():
    data = load_data()
    data["homework"] = request.json.get("text")
    save_data(data)
    return {"msg": "作业发布成功"}

@app.route("/submit", methods=["POST"])
def submit():
    data = load_data()
    stu = request.json
    data["submissions"].append(stu)
    save_data(data)
    return {"msg": "提交成功"}

@app.route("/all")
def all_data():
    return load_data()

app.run(port=5000)

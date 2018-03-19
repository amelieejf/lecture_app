from eventbrite import Eventbrite
from flask import Flask , render_template, request, jsonify
from datetime import datetime
import requests

eventbrite = Eventbrite("5Q5HRS46AWMKIYGZGEAW")
user = eventbrite.get_user()
user["id"]
user["name"]

param = {
    "q" : "lecture",
    "location.address" : "London"
}
print param["location.address"]


first = results["events"][0]

#print(first['description']['text'])

#print(first.keys())

#print(first['name'])

app = Flask("My Flask App")

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route("/")
def default_path():
    return render_template ("index.html") #This


@app.route("/show_lectures", methods=["POST"])
def read_form():
	return render_template ("lectures.html", date=date, sign=sign, data=data) 
	#return "All OK"

if __name__ == '__main__':
	app.run(debug=True)



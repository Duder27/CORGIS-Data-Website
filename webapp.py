from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_car_options(cars):
	get_car_options = []
	for f in cars:
		if not(f['Identification']) in get_car_options:
			get_car_options.append(f['Identification'])
	#y = ''
	#for x in get_car_options:
		#y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	#return y

@app.route("/")
def render_main():
	with open('cars.json') as cars_data:
		cars = json.load(cars_data)
	return render_template('home.html', options = get_car_options(cars), car_options = get_car_options(cars))

app.route("/response")
def render_response():
	with open('cars.json') as cars_data:
		cars = json.load(cars_data)
	car = request.args['CarSelected']
	factT = ""
	factCM = ""
	factHM = ""
	factHP = ""
	for data in cars:
		if car == data["Car"]:
			data["Classification"]["Horsepower"]["City mpg"]["Highway mpg"]
			factT = data["Classification"]
			factCM = data["City mpg"]
			factHM = data["Highway mpg"]
			factHP = data["Horsepower"]
	return render_template('response.html', response = factT, response2 = factCM, response3 = factHM, response4 = factHP)


#if __name__=="__main__":
    #app.run(debug=True, port=54321)

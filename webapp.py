from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_car_options(cars):
	get_car_options = []
	for f in cars:
		if not(f['Identification']['ID']) in get_car_options:
			get_car_options.append(f['Identification']['ID'])
	y = ''
	for x in get_car_options:
		y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	return y

@app.route("/")
def render_main():
	with open('cars.json') as cars_data:
		cars = json.load(cars_data)
	return render_template('home.html', options = get_car_options(cars), car_options = get_car_options(cars))

app.route("/response", methods = ['GET'])
def render_response():
	with open('cars.json') as cars_data:
		cars = json.load(cars_data)
	car = request.args['CarSelected']
	factT = ""
	factCM = ""
	factHM = ""
	factHP = ""
	for data in cars:
		if car == data["Identification"]["ID"]:
			#data["Classification"]["Horsepower"]["City mpg"]["Highway mpg"]
			factT = data["Identification"]["Classification"]
			factCM = data["Fuel Information"]["City mpg"]
			factHM = data["Fuel Information"]["Highway mpg"]
			factHP = data["Engine Information"]["Horsepower"]
	return render_template('response.html', response = factT, response2 = factCM, response3 = factHM, response4 = factHP)


#if __name__=="__main__":
    #app.run(debug=True, port=54321)

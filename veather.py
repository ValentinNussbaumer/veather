import requests
from tkinter import *

# create window with the location input
def location():
    global locationt
    locationt = Tk()
    locationt.title("Veather")
    loc = Label(locationt, text="Location: ")
    global e1
    e1 = Entry(locationt)
    inp = e1
    st = Button(locationt, text=("Get Weather"), command=lambda: [weather()])
    loc.pack()
    inp.pack()
    st.pack()
    locationt.mainloop()

# connect to api
def weather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = e1.get()
    print("Location: " + CITY)
    API_KEY = "3d318d26675d02b9b41a957c7aa4c8de"
    URL = BASE_URL + "q=" + CITY + "&units=metric" + "&appid=" + API_KEY
    response = requests.get(URL)

    if response.status_code == 200:
        # decline variables
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']
        wind_report = data['wind']

        cityo = (f"{CITY:-^15}")
        tempo = (f"Temperature: {int(temperature)}°")
        huo = (f"Humidity: {humidity}%")
        skyo = (f"Sky: {weather_report[0]['description']}")
        pressureo = (f"Pressure: {pressure}hPa")
        windo = (f"Wind Speed: {wind_report['speed']}km/h")

        # print weather data
        print(tempo)
        print(huo)
        print(skyo)
        print(pressureo)
        print(windo)
        print()

    # create widget with the weather data
    widget = Tk()
    widget.title("Veather")
    lab1 = Label(widget, text=cityo)
    lab2 = Label(widget, text=tempo)
    lab4 = Label(widget, text=huo)
    lab5 = Label(widget, text=skyo)
    lab6 = Label(widget, text=pressureo)
    lab7 = Label(widget, text=windo)
    but1 = Button(widget, text="New Location", command=lambda: [widget.destroy(), location()])
    lab1.pack()
    lab2.pack()
    lab4.pack()
    lab5.pack()
    lab6.pack()
    lab7.pack()
    but1.pack()
    locationt.destroy()
    widget.mainloop()

# create welcome window
root = Tk()
root.title("Veather")
wlabel = Label(root, text=("Welocme to the Veather App"))
start = Button(root, text=("Choose Location"), command=lambda: [root.destroy(), location()])
wlabel.pack()
start.pack()
root.mainloop()

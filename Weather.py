import requests
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class Weatherdashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard")
        self.api_key = "93b47e9da3ba978ac819f8a88389c991"

        #create label for city name entry
        self.city_label = tk.Label(root, text="Enter City Name:")
        self.city_label.pack(pady=5)


        #Create Entry field for city name
        self.city_entry = tk.Entry(root)
        self.city_entry.pack(pady=10)


        #Create weather lookup button

        tk.Button(root, text="Get Weather News", command=self.get_weather).pack()

        #create label to display weather info
        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack(pady=20)

        self.history = self.load_history()  #store history

    def load_history(self):
        if os.path.exists('weather_history.json'):
            with open('weather_history.json', 'r') as f:
                return json.load(f)
            return[]

    def get_weather(self):
        city = self.city_entry.get()

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()  #convert response to json

            if response.status_code ==200:
                #extract weather data
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']

                #create weather info dictionary
                weather_info = {
                    'city': city,
                    'temp': temp,
                    'humidty': humidity,
                    'description': description,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                self.history.append(weather_info)
                self.save_history()


                #Format display text
                display_text = f"""
                City: {city}
                Temperature: {temp}°C
                Humidity: {humidity}%
                Conditions: {description.title()}
                """
                self.weather_label.config(text=display_text)

        except requests.exceptions.RequestException:
            self.weather_label.config(text="Error fetching weather data")

    def save_history(self):
        #save history to JSON file
        with open('weather_history.json', 'w') as f:
            json.dump(self.history, f, indent=4)

#create and run application
if __name__ == "__main__":
    root = tk.Tk()
    app = Weatherdashboard(root)
    root.mainloop()    

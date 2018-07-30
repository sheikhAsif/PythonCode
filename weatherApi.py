import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=e4de3b23d52fd7a162d7479a771d554d&q='
city = input("City Name :")

url = api_address + city

json_data = requests.get(url).json()

coordinates = json_data['coord']
main = json_data['weather'][0]['main']
desc = json_data['weather'][0]['description']
temp = json_data['main']['temp'] - 273.15

print("city : ",city)
print("temperature : {} degree celcius".format(temp))
print("main : ",main)
print("description : ",desc)

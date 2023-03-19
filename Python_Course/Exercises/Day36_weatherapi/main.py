import requests

weather_translation = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "Fog  depositing",
    48: "rime fog",
    51: "Drizzle: Light",
    53: "Drizzle: moderate",
    55: "Drizzle: dense intensity",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: dense intensity",
    61: "Rain: Slight",
    63: "Rain: moderate",
    65: "Rain: heavy intensity",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: intensity",
    71: "Snow fall: slight",
    73: "Snow fall: soderate",
    75: "Snow fall: heavy intensity",
    77:	"Snow fall: Snow grains",
    80: "Rain showers: slight",
    81: "Rain showers: moderate",
    82: "Rain showers: violent",
    85: "Snow showers: slight",
    86: "Snow showers: heavy",
    95: "Thunderstorm: slight",
    96: "Thunderstorm: moderate",
    99: "Thunderstorm with slight and heavy hail",
}
new_dic = {value:[] for key, value in weather_translation.items()}
parameters = {
    "latitude": -22.38,
    "longitude": -41.78,
    "hourly": "weathercode",

}
final_dic = {}



response = requests.get(url="https://api.open-meteo.com/v1/forecast", params=parameters)
data = response.json()
new_weather_list = [code for code in data['hourly']['weathercode'][6:18:]]

count = 6

for hour in new_weather_list:
    count += 1
    if hour > 3:
        print('Bring a Umbrella ')








































        '''new_dic[weather_translation[hour]].append(str(count)+":00")
        print(new_dic)
for key,value in new_dic.items():
    if value != []:
        final_dic[key] = value

print(final_dic)


print(f"Bring a umbrella its gonna be {final_dic}")'''
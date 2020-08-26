import json
from urllib.request import urlopen
x="n"
while(x!='y'and x!='Y'):
    city = input("City/State \t")
    print("")
    key = "<your api key>"
    url = "http://api.openweathermap.org/"
    url = url+"data/2.5/weather?appid="+key+f"&q={city}&units=metric"
    response = urlopen(url)
    decoded = response.read().decode('utf-8')
    data = json.loads(decoded)
    for key,value in data.items():
        print(key," ",value)

    t=data['main']
    print("\n Temperature:",t['temp']," C","\n Pressure",t['pressure'],"\n Humidity:",t['humidity'],)
    
    print(t['temp_min'],t['temp_max'])
    x=input("Do u want to exit y/n ?\t")

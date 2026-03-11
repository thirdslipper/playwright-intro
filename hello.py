from datetime import datetime
print("Hello! Here's the current time:")
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Have a great day!")

trails = [
"Griffith Observatory / Mount Hollywood Trail",
"Runyon Canyon Park",
"Eaton Canyon Falls Trail",
"Temescal Gateway Park Trail",
"Solstice Canyon Trail",
]

for trail in trails:
    print(trail)
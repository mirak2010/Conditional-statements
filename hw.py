print("Hello, to complete the weather analysis, please enter the details with no signs of measures!(Just the number please!)")
weather=int(input("Please enter the weather in celsius: "))
precipitation=int(input("Please enter the precipitation in percentage: "))
humidity=int(input("Please enter the humidity in percentage: "))
wind=int(input("Please enter the wind speed in km/h: "))
if weather>30:
    print("The season is summer,","The temperature is ",weather,"℃")
elif weather<20:
    print("The season is fall,","The temperature is ", weather,"℃")
elif weather>20<30:
    print("The season is spring,","The temperature is ", weather,"℃")
elif weather<20:
    print("The season is winter,","The temperature is ", weather,"℃")
if precipitation>0:
    print("It is probably raining,","The chance is ", precipitation,"%")
else:
    print("It is not raining today,","The chance is ",precipitation,"%")
if humidity>60:
    print("It is humid today,","The humidity is ",humidity,"%")
elif humidity==50<50>30:
    print("It is average humidity today,","The humidity is ",humidity,"%")
elif humidity<30:
    print("It is dry today,","The humidity is ", humidity,"%")
if wind>5:
    print("It is windy today,","The wind speed is ", wind,"km/h")
else:
    print("It is not that windy today,","The wind speed is ",wind,"km/h")


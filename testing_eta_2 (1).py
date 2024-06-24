import sys
import os
import requests
from waveshare import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont
import time

epd = epd7in5_V2.EPD()

epd.width = 800    #this is for landscape 
epd.height = 480
i=True
try:
    while i==True:
        epd.init()
        Make_image = Image.new('1', (epd.width, epd.height), 255)
        draw = ImageDraw.Draw(Make_image)
        font = ImageFont.truetype(os.path.join("avenir-next-medium.ttf",90))   #this is the font attached with the file
        base_url=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=Whereyoulive&destinations=destination1|destination2|destination3|&departure_time=now&key=API_KEY')
        #base_url is just a variable. It is asking for three destinations. Change this: origin="Where you live" and change this destinations="desination1|destination2|destination3". Also make sure to use your API key
        data=base_url.json() #creates a dictionary
        print("status = "+ str(data["status"]))
        if data["status"] == "OK":
            duration_to_destination1=data["rows"][0]["elements"][0]["duration_in_traffic"]["text"] #turns everything to variables
            duration_to_destination2=data["rows"][0]["elements"][1]["duration_in_traffic"]["text"]
            duration_to_destination3=data["rows"][0]["elements"][2]["duration_in_traffic"]["text"]
        draw.text((50,50),f"Destination1: {duration_to_destination1}",font=font,fill=0)
        draw.text((50,175),f"Destination2: {duration_to_destination2}",font=font,fill=0)
        draw.text((50,300),f"Destination3: {duration_to_destination3}",font=font,fill=0)
        i=True
        epd.display(epd.getbuffer(Make_image))
        epd.sleep()#prevent damage to screen
        time.sleep(500)# I have changed it to every 5 minutes to make it more accurate

except:
    print("status = "+ str(data["status"]))
    draw.text((50,300),f"Error",font=font,fill=0)
        

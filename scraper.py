import requests
from bs4 import BeautifulSoup
import smtplib
import time

def price_track():
  Link = 'https://www.amazon.de/-/en/Mizuno-Unisex-Momentum-Volleyball-Ignition/dp/B098QX72L5/ref=sr_1_4?crid=3I9AKQLTE9N79&keywords=mizuno+wave+momentum+2&qid=1680294589&sprefix=momentum+wave+2+%2Caps%2C109&sr=8-4'
  header  = {"User-Agent": "Search in google for my user agent and then copy past here" }

  page = request.get(Link, headers = header)

  split = BeatifulSoup(page.content, 'html.parser')

  price = split.find(class_="a-offscreen").get_text()

  extracted_price = float(price[1:3])

  if (extracted_price <90):
    sendmail() 
 

def sendmail():
 server = smtplib.SMTP("smtp.gmail.com", 587)
 server.ehlo()
 server.tls()
 server.ehlo()
 server.login("your@gmail.com" , 'your gmail password')
    subject = 'Price opportunity'
    body = "check the amazon link https://www.amazon.de/-/en/Mizuno-Unisex-Momentum-Volleyball-Ignition/dp/B098QX72L5/ref=sr_1_4?crid=3I9AKQLTE9N79&keywords=mizuno+wave+momentum+2&qid=1680294589&sprefix=momentum+wave+2+%2Caps%2C109&sr=8-4"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'your@gmail.com',
        'adressyouwanttosend@gmail.com',
        msg
    )
    print('The email went through')

    server.quit()
    
 while(True):
  price_track()
  time.sleep(24*60) // checks price once a day - you can change that too whatever amount you like
 

from django.shortcuts import render, redirect
from django.contrib import messages
import json
from urllib import request as reqst

# Create your views here.
def index(req):
    data = {"city": ''}
    if req.method=='POST':
        city = req.POST['city']
        try:
            res = reqst.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        except:
            messages.info(req, "City Not Found... Try again")
            return redirect("index")
        jdata = json.loads(res)
        data = {
            "city": city,
            "ct_code": jdata['sys']['country'],
            "coor": 'lon-'+str(jdata['coord']['lon'])+', lat-'+str(jdata['coord']['lat']),
            "temp": str(round(jdata['main']['temp']-273.15))+' Degree Celsius',
            "pres": str(jdata['main']['pressure']),
            "humid": str(jdata['main']['humidity'])
        }
    
    return render(req, 'index.html', data)
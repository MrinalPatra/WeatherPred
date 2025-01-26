from tkinter import *
import requests
import json
from PIL import Image,ImageTk

edit=Tk()
edit.geometry('370x400')

global x
x=Entry(edit,width=30)
x.grid(row=0,column=1,columnspan=2,padx=1)

my_label=Label(edit,text="Choose Location:")
my_label.grid(row=0,column=0)


    
def next_pg():
    
        from PIL import Image,ImageTk
      
        cdtn=[
            	{
            		"code" : 1000,
            		"day" : "Sunny",
            		"night" : "Clear",
            		"icon1" : 'img0',
                    "icon2" : 'img48'
            	},
            	{
            		"code" : 1003,
            		"day" : "Partly cloudy",
            		"night" : "Partly cloudy",
            		"icon1" : 'img1',
                    "icon2" : 'img49'
            	},
            	{
            		"code" : 1006,
            		"day" : "Cloudy",
            		"night" : "Cloudy",
            		"icon1" : 'img2',
                    "icon2" : 'img50'
            	},
            	{
            		"code" : 1009,
            		"day" : "Overcast",
            		"night" : "Overcast",
            		"icon1" : 'img3',
                    "icon2" : 'img51'
            	},
            	{
            		"code" : 1030,
            		"day" : "Mist",
            		"night" : "Mist",
            		"icon1" : 'img4',
                    "icon2" : 'img52'
            	},
            	{
            		"code" : 1063,
            		"day" : "Patchy rain possible",
            		"night" : "Patchy rain possible",
            		"icon1" : 'img5',
                    "icon2" : 'img53'

            	},
            	{
            		"code" : 1066,
            		"day" : "Patchy snow possible",
            		"night" : "Patchy snow possible",
            		"icon1" : 'img6',
                    "icon2" : 'img54'

            	},
            	{
            		"code" : 1069,
            		"day" : "Patchy sleet possible",
            		"night" : "Patchy sleet possible",
            		"icon1" : 'img7',
                    "icon2" : 'img55'

            	},
            	{
            		"code" : 1072,
            		"day" : "Patchy freezing drizzle possible",
            		"night" : "Patchy freezing drizzle possible",
            		"icon1" : 'img8',
                    "icon2" : 'img56'

            	},
            	{
            		"code" : 1087,
            		"day" : "Thundery outbreaks possible",
            		"night" : "Thundery outbreaks possible",
            		"icon1" : 'img9',
                    "icon2" : 'img57'

            	},
            	{
            		"code" : 1114,
            		"day" : "Blowing snow",
            		"night" : "Blowing snow",
            		"icon1" : 'img10',
                    "icon2" : 'img1=58'

            	},
            	{
            		"code" : 1117,
            		"day" : "Blizzard",
            		"night" : "Blizzard",
            		"icon1" : 'img11',
                    "icon2" : 'img59'

            	},
            	{
            		"code" : 1135,
            		"day" : "Fog",
            		"night" : "Fog",
            		"icon1" : 'img12',
                    "icon2" : 'img60'

            	},
            	{
            		"code" : 1147,
            		"day" : "Freezing fog",
            		"night" : "Freezing fog",
            		"icon1" : 'img13',
                    "icon2" : 'img61'

            	},
            	{
            		"code" : 1150,
            		"day" : "Patchy light drizzle",
            		"night" : "Patchy light drizzle",
            		"icon1" : 'img14',
                    "icon2" : 'img62'

            	},
            	{
            		"code" : 1153,
            		"day" : "Light drizzle",
            		"night" : "Light drizzle",
            		"icon1" : 'img15',
                    "icon2" : 'img63'

            	},
            	{
            		"code" : 1168,
            		"day" : "Freezing drizzle",
            		"night" : "Freezing drizzle",
            		"icon1" : 'img16',
                    "icon2" : 'img64'

            	},
            	{
            		"code" : 1171,
            		"day" : "Heavy freezing drizzle",
            		"night" : "Heavy freezing drizzle",
            		"icon1" : 'img17',
                    "icon2" : 'img65'

            	},
            	{
            		"code" : 1180,
            		"day" : "Patchy light rain",
            		"night" : "Patchy light rain",
            		"icon1" : 'img18',
                    "icon2" : 'img66'

            	},
            	{
            		"code" : 1183,
            		"day" : "Light rain",
            		"night" : "Light rain",
            		"icon1" : 'img19',
                    "icon2" : 'img67'

            	},
            	{
            		"code" : 1186,
            		"day" : "Moderate rain at times",
            		"night" : "Moderate rain at times",
            		"icon1" : 'img20',
                    "icon2" : 'img68'

            	},
            	{
            		"code" : 1189,
            		"day" : "Moderate rain",
            		"night" : "Moderate rain",
            		"icon1" : 'img21',
                    "icon2" : 'img69'

            	},
            	{
            		"code" : 1192,
            		"day" : "Heavy rain at times",
            		"night" : "Heavy rain at times",
            		"icon1" : 'img22',
                    "icon2" : 'img70'

            	},
            	{
            		"code" : 1195,
            		"day" : "Heavy rain",
            		"night" : "Heavy rain",
            		"icon1" : 'img23',
                    "icon2" : 'img71'

            	},
            	{
            		"code" : 1198,
            		"day" : "Light freezing rain",
            		"night" : "Light freezing rain",
            		"icon1" : 'img24',
                    "icon2" : 'img72'

            	},
            	{
            		"code" : 1201,
            		"day" : "Moderate or heavy freezing rain",
            		"night" : "Moderate or heavy freezing rain",
            		"icon1" : 'img25',
                    "icon2" : 'img73'

            	},
            	{
            		"code" : 1204,
            		"day" : "Light sleet",
            		"night" : "Light sleet",
            		"icon1" : 'img26',
                    "icon2" : 'img74'

            	},
            	{
            		"code" : 1207,
            		"day" : "Moderate or heavy sleet",
            		"night" : "Moderate or heavy sleet",
            		"icon1" : 'img27',
                    "icon2" : 'img75'

            	},
            	{
            		"code" : 1210,
            		"day" : "Patchy light snow",
            		"night" : "Patchy light snow",
            		"icon1" : 'img28',
                    "icon2" : 'img76'

            	},
            	{
            		"code" : 1213,
            		"day" : "Light snow",
            		"night" : "Light snow",
            		"icon1" : 'img29',
                    "icon2" : 'img77'

            	},
            	{
            		"code" : 1216,
            		"day" : "Patchy moderate snow",
            		"night" : "Patchy moderate snow",
            		"icon1" : 'img30',
                    "icon2" : 'img78'

            	},
            	{
            		"code" : 1219,
            		"day" : "Moderate snow",
            		"night" : "Moderate snow",
            		"icon1" : 'img31',
                    "icon2" : 'img79'

            	},
            	{
            		"code" : 1222,
            		"day" : "Patchy heavy snow",
            		"night" : "Patchy heavy snow",
            		"icon1" : 'img32',
                    "icon2" : 'img80'

            	},
            	{
            		"code" : 1225,
            		"day" : "Heavy snow",
            		"night" : "Heavy snow",
            		"icon1" : 'img33',
                    "icon2" : 'img81'

            	},
            	{
            		"code" : 1237,
            		"day" : "Ice pellets",
            		"night" : "Ice pellets",
            		"icon1" : 'img34',
                    "icon2" : 'img82'

            	},
            	{
            		"code" : 1240,
            		"day" : "Light rain shower",
            		"night" : "Light rain shower",
            		"icon1" : 'img35',
                    "icon2" : 'img83'

            	},
            	{
            		"code" : 1243,
            		"day" : "Moderate or heavy rain shower",
            		"night" : "Moderate or heavy rain shower",
            		"icon1" : 'img36',
                    "icon2" : 'img84'

            	},
            	{
            		"code" : 1246,
            		"day" : "Torrential rain shower",
            		"night" : "Torrential rain shower",
            		"icon1" : 'img37',
                    "icon2" : 'img85'

            	},
            	{
            		"code" : 1249,
            		"day" : "Light sleet showers",
            		"night" : "Light sleet showers",
            		"icon1" : 'img38',
                    "icon2" : 'img86'

            	},
            	{
            		"code" : 1252,
            		"day" : "Moderate or heavy sleet showers",
            		"night" : "Moderate or heavy sleet showers",
            		"icon1" : 'img39',
                    "icon2" : 'img87'

            	},
            	{
            		"code" : 1255,
            		"day" : "Light snow showers",
            		"night" : "Light snow showers",
            		"icon1" : 'img40',
                    "icon2" : 'img88'

            	},
            	{
            		"code" : 1258,
            		"day" : "Moderate or heavy snow showers",
            		"night" : "Moderate or heavy snow showers",
            		"icon1" : 'img41',
                    "icon2" : 'img89'

            	},
            	{
            		"code" : 1261,
            		"day" : "Light showers of ice pellets",
            		"night" : "Light showers of ice pellets",
            		"icon1" : 'img42',
                    "icon2" : 'img90'

            	},
            	{
            		"code" : 1264,
            		"day" : "Moderate or heavy showers of ice pellets",
            		"night" : "Moderate or heavy showers of ice pellets",
            		"icon1" : 'img43',
                    "icon2" : 'img91'

            	},
            	{
            		"code" : 1273,
            		"day" : "Patchy light rain with thunder",
            		"night" : "Patchy light rain with thunder",
            		"icon1" : 'img44',
                    "icon2" : 'img92'

            	},
            	{
            		"code" : 1276,
            		"day" : "Moderate or heavy rain with thunder",
            		"night" : "Moderate or heavy rain with thunder",
            		"icon1" : 'img45',
                    "icon2" : 'img93'

            	},
            	{
            		"code" : 1279,
            		"day" : "Patchy light snow with thunder",
            		"night" : "Patchy light snow with thunder",
            		"icon1" : 'img46',
                    "icon2" : 'img94'
                    
            	},
            	{
            		"code" : 1282,
            		"day" : "Moderate or heavy snow with thunder",
            		"night" : "Moderate or heavy snow with thunder",
            		"icon1" : 'img47',
                    "icon2" : 'img95'

            	}
            ]
        
        global my_image
        global my_label
        
        try:
                api_request=requests.get("http://api.weatherapi.com/v1/current.json?key=" "Give your own API key from weather api website "="+x.get())
                api=json.loads(api_request.content)
                b=str(api["current"]["condition"]["text"])
                if(api["current"]["is_day"]==1):
                   for i in range(0,48,1):
                           l=str(cdtn[i]["day"])
                           if(b == l):
                               y=str(cdtn[i]["icon1"])
                               my_image=ImageTk.PhotoImage(Image.open(y+".png"))
                               my_label=Label(edit,image=my_image)
                               my_label.grid(row=4,column=0,columnspan=3)
                               break    
                
                else:
                   for i in range(0,48,1): 
                       l=str(cdtn[i]["night"])
                       if(b == l):
                           y=str(cdtn[i]["icon2"])
                           my_image=ImageTk.PhotoImage(Image.open(y+".png"))
                           my_label=Label(edit,image=my_image)
                           my_label.grid(row=4,column=0,columnspan=3)
                           break
                   
                    
                    
        except Exception as e:
                api='Error...'
                
        label1=Label(edit,text='Location: '+ api["location"]["name"]+" , "+"State: "+api["location"]["region"]+
                        " , "+"Country: "+api["location"]["country"])  
        label2=Label(edit,text="Localtime: "+api["location"]["localtime"]+' , '+"UpdatedTime: "+api["current"]["last_updated"]) 
        label3=Label(edit,text="Temperature in Celcius: "+str(api["current"]["temp_c"])+" , "+"Temperature in Farenheit: "+str(api["current"]["temp_f"]))
        label4=Label(edit,text="Condition: "+api["current"]["condition"]["text"]+" , "+"Day=1/Night=0: "+str(api["current"]["is_day"]))
        label5=Label(edit,text="Windspeed: "+str(api["current"]["wind_kph"])+" , "+"Wind_direction: "+api["current"]["wind_dir"]
                         +" , "+"Pressure: "+str(api["current"]["pressure_mb"])+" , "+"\n"+"Precipitation :"+str(api["current"]["precip_mm"])
                         +" , "+"Humidity: "+str(api["current"]["humidity"]))
        label6=Label(edit,text=" Feelslike_in_C:"+str(api["current"]["feelslike_c"])+" , "+"Feelslike_in_F:"+str(api["current"]["feelslike_f"]))
        label7=Label(edit,text="UV: "+str(api["current"]["uv"]))        
        label1.grid(row=5,column=0,columnspan=3)
        label2.grid(row=6,column=0,columnspan=3)
        label3.grid(row=7,column=0,columnspan=3)
        label4.grid(row=8,column=0,columnspan=3)
        label5.grid(row=9,column=0,columnspan=3)
        label6.grid(row=10,column=0,columnspan=3)
        label7.grid(row=11,column=0,columnspan=3)
        


show_btn=Button(edit,text='Show',command=next_pg,bg='cyan')
show_btn.grid(row=2,column=0,columnspan=3,padx=10,pady=10,ipadx=133)

exit_btn=Button(edit,text='Exit',command=edit.destroy,bg='cyan')
exit_btn.grid(row=3,column=0,columnspan=3,padx=10,pady=10,ipadx=140)

edit.mainloop()

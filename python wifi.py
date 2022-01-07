from bottle import get, run
 
dico={'co2':[], 'humidity':[], 'temperature': [],'sound' : []}
 
 
@get('/sensor/co2/<co2value>')
def Co2(co2value):
   print(f'co2 : {co2value}')
   dico['co2'].append(co2value)
   print(dico)
   return
 
@get('/sensor/humidity/<hum>')
def Humidity(hum):
   print(f'humidity : {hum}')
   dico['humidity'].append(hum)
   print(dico)
   return
 
@get('/sensor/temperature/<temp>')
def Temperature(temp):
   print(f'temperature : {temp}')
   dico['temperature'].append(temp)
   print(dico)
   return
 
@get('/sensor/sound/<soundvalue>')
def Sound(soundvalue):
   print(f'sound : {soundvalue}')
   dico['sound'].append(soundvalue)
   print(dico)
   return
 
run( host="172.20.10.4", port = 8000)

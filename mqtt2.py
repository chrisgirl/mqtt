import paho.mqtt.client as mqtt
def on_connect(client, userdta, flags, rc):    
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("gc/trio")
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
client = mqtt.Client()
client.connect("192.168.1.144", 1883, 60)

while True:
    message= input('Your message: ')
    new_message = '\033[1m' + message + '\033[0m' 

  
    client.publish('gc/trio', new_message)

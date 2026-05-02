import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = "localhost"
PORT = 1883

#Topic que sirven para enviar o recibir información y pública la lectura
TOPIC_TEMP = "sensores/temperatura"
#Node-RED pública si debe activar o desactivar motor 
TOPIC_CMD = "sensores/ventilador"
#pública el estado del motor para mostrarlo en el dashboard del Node-RED
TOPIC_ESTADO = "sensores/ventilador/estado" 

estado_motor = 0  # 0 = apagado, 1 = encendido


# --- CALLBACK CUANDO LLEGA UN MENSAJE ---
def on_message(client, userdata, msg):
    global estado_motor

    comando = int(msg.payload.decode())

    if comando != estado_motor:
        estado_motor = comando

        if estado_motor == 1:
            print("Motor ENCENDIDO")
        else:
            print("Motor APAGADO")

 # Enviar estado actualizado a Node-RED para ebcebder Led en pantalla y #mostrar ventilador en movimiento
        client.publish(TOPIC_ESTADO, estado_motor)

# --- CALLBACK DE CONEXIÓN ---
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker")
    client.subscribe(TOPIC_CMD)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

print("Sistema iniciado...")

while True:
    temperatura = round(random.uniform(20.0, 30.0), 2)

    data = {
        "sensor": "sensor_temp_1",
        "temperatura": temperatura,
        "unidad": "C",
	#"estado motor": estado_motor
    }
    payload = json.dumps(data)
    client.publish(TOPIC_TEMP, payload)

    print(f"Temp enviada: {payload} | Estado motor: {estado_motor}")

    time.sleep(5)#cada 5 segundos envía una temperatura random entre 20 y 30

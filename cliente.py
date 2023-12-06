import socket

# Configurar el cliente
host = '127.0.0.1'  # Dirección IP del servidor
port = 12345  # Puerto en el que el servidor está escuchando

# Crear un socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client.connect((host, port))
print(f"Conexión establecida con el servidor en {host}:{port}")

# Enviar un mensaje al servidor
message = "Hola, servidor"
client.send(message.encode('utf-8'))
print(f"Mensaje enviado al servidor: {message}")

# Recibir la respuesta del servidor
response = client.recv(1024)
print(f"Respuesta del servidor: {response.decode('utf-8')}")

# Cerrar la conexión con el servidor
client.close()
print("Conexión cerrada")

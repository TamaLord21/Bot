import random
import time
from instagrapi import Client

cl = Client()
cl.login("Usuario", "Contraseña")

url = "https://www.instagram.com/p/DOEiK9vjfBd/?img_index=1"
media_id = cl.media_id(cl.media_pk_from_url(url))

comentarios = [
    "La sport100 es la del vacile",
    "Si no es esa moto no quiero nada",
    "Está linda, pa visitar al pétalo!🙂‍↕️"
]

for i in range(5):
    comentario = random.choice(comentarios)
    cl.media_comment(media_id, comentario)
    print(f"Comentario {i+1} publicado: {comentario}")
    time.sleep(random.randint(30, 60))

print("Bot finalizado.")
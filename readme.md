# Bot de comentarios en Instagram

Este proyecto nació como un experimento para aprender y saber si era posible automatizar acciones en Instagram usando Python.  
La idea es sencilla: dejar comentarios en una publicación cada cierto tiempo, pero que no parezca un robot spameando.  

---

## ¿Qué hace el bot?

1. Se conecta a Instagram con tu usuario y contraseña.  
2. Toma la URL de una publicación y la convierte en el identificador interno que Instagram usa (el famoso `media_id`).  
3. Tiene una lista de comentarios predefinidos.  
4. Elige uno al azar cada vez.  
5. Lo publica en la publicación objetivo.  
6. Espera entre **2 y 4 minutos** (también al azar) antes de volver a comentar.  
7. Repite el proceso tantas veces como le indiques.  

---

## ¿Cómo lo construí?

- Usé **Python 3** como lenguaje base.  
- La librería principal es [`instagrapi`](https://github.com/adw0rd/instagrapi), que facilita conectarse a Instagram.  
- También usé módulos estándar de Python:  
  - `time` para manejar las pausas.  
  - `random` para elegir tanto comentarios como tiempos de espera.  

El cerebro del bot es un bucle `for`, que controla cuántos comentarios se van a hacer. Dentro de ese bucle:
- Se selecciona un comentario con `random.choice()`.  
- Se envía con `cl.media_comment(media_id, comentario)`.  
- Se espera con `time.sleep(random.randint(120, 240))`.  

---

## Ejemplo rápido

```python
for i in range(5):
    comentario = random.choice(comentarios)
    cl.media_comment(media_id, comentario)
    print(f"Comentario {i+1} publicado: {comentario}")
    time.sleep(random.randint(120, 240))
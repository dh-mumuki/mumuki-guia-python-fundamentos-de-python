A medida que avancemos, vamos a empezar a recibir avisos de errores. No hay nada de que preocuparse!

Un error en Python significa que Python no comprendió alguna de las instrucciones que le dimos. Lo bueno es que nos da indicios de que es lo que no comprendió. Un buena práctica es detenerse, leer los errores y entenderlos para poder corregirlos y seguir adelante.

Un error común es olvidarse de poner las comillas para declarar un _string_.


``` python
print(Veran en la salida lo que sucede cuando uno se olvida las comillas)
```

**_Salida>> SyntaxError: EOL while scanning a string literal_**

``` python
print("Ahora Python comprende la instrucción e imprime esto mismo que estas leyendo.")
```
**_Salida>> Ahora Python comprende la instrucción e imprime esto mismo que estas leyendo._**

<br>

**Cuál es el problema en este código?**<br>

``` python
print("Alguna vez se preguntaron"¿Por qué Python se llama así?"")
print("Guido van Rossum, su creador, se inspiró en un comic que estaba leyendo:'Monty Python’s Flying Circus'. Cumplía con ser corto, único y misterioso"!)
```


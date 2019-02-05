Si Python divide dos números de tipo _int_, entonces devolverá el resultado en ese tipo de dato.
Si, en cambio, uno o ambos números son de tipo _float_, Python devolverá el resultado en formato _float_.<br>

Entonces, en cualquier operación donde haya un número tipo _float_, el resultado será devuelto en ese formato.

:bulb: **¿Por qué creen que con que uno de los dos valores sea de tipo _float_, el resultado será expresado en ese tipo y no en tipo _int_?** <br>
En cierta manera, el tipo de dato _float_ incluye a _int_, ya que `2.0` equivale a `2`. En la otra dirección, `2` no equivale a `2.1` o a cualquier otro 2 con decimales.
<br>


> :memo: **Escribí un código que resuelva las siguientes preguntas:**<br>
1. Si tengo 15 huevos, ¿cuántos maples de 6 unidades puedo completar? <br>
2. Una bolsa con 14 canicas pesa 234gr. Con una exactitud de dos decimales, ¿cuánto pesan 5 canicas? <br>

> Para redondear a dos decimales, investigá sobre la función round().
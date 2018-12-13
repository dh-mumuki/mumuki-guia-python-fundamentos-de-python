El verdadero poder de los Boolean es que pueden surgir al hacer comparaciones de distintos valores con algunos operadores matemáticos.

Por ejemplo sabemos que si le preguntamos a alguien "¿2 es mayor a 1?" la persona nos va a decir "Si, es verdadero, 2 es mayor a 1", lo mismo pasa en Python cuando escribimos lo siguiente:

```python
print(2 > 1) #Esto imprimirá por pantalla "true"
```

Esto quiere decir que "2 > 1" tiene un valor de **verdadero**. También podríamos haber escrito el mismo código de la siguiente manera: 

```python
valor_de_verdad = 2 > 1 #Como vimos 2 > 1 retorna un valor de verdad y se lo asignamos a una variable
print(valor_de_verdad) #Esto imprimirá por pantalla "true"
```

Y si le preguntamos a alguien "¿2 es menor a 1?" la persona nos va a decir "Eso es falso, 2 no es menor a 1", lo mismo pasa en Python cuando escribimos lo siguiente:

```python
print(2 < 1) # Esto imprimirá por pantalla "false"
```

> :memo: **Para continuar, defini dos variables: `un_numero_chico` y `un_numero_grande`, y asignales valores numéricos diferentes de acuerdo a sus nombres.  
Luego definí la variable `es_menor` y asignale el resultado de comparar si `un_numero_chico` es menor que `un_numero_grande`; y definí la variable `es_mayor`, con el resultado de comparar si `un_numero_chico` es mayor que `un_numero_grande`.
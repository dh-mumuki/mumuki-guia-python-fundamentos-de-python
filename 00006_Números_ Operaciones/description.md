Si hay algo en lo que las computadoras son muy buenas es haciendo cálculos. Vamos a aprovecharlo!


Aquí vemos un lista de los operadores de Python:

* `+`: Suma
* `-`: Resta
* `*`: Multiplicaión o Producto
* `/`: División
* `%`: Resto de la división o móodulo
* `**`: Potencia


Veamos algunas operaciones y sus salidas.

**SUMA**

``` python
#Suma
4 + 2

```
_**Salida>> 6**_



**RESTA**

``` python
#Resta
4 - 2
```
_**Salida>> 2**_



**PRODUCTO**

``` python
#Producto
4 * 2
```
_**Salida>> 8**_



**DIVISIÓN**

``` python
#División
4 / 2
4 / 3
```
_**Salida>> 2**_

_**Salida>> 1**_

> En este caso, pareciera haber un error porque 4 / 3 = 1.33. Lo que pasó es que usamos número enteros, _int_ (los recuerdan?) y entonces Python devuelve enteros. En el siguiente tema abordaremos estos casos.



**MÓDULO**

``` python
#Módulo
4 % 2
4 % 3
```
_**Salida>> 0**_

_**Salida>> 1**_



**POTENCIA**

``` python
#Potencia
4 ** 2
```
_**Salida>> 16**_


Lo operdaores son los que uno puede encontrar en un calculadora, a excepción de `%`. Basicamente, este operdor devuele el resto del cociente entre los dos números que estan a su lado. Por ejemplo en el primer caso `4 % 2`, la división resulta 2 y el resto 0, ya que 2 entra un número entero de veces en 4, completandolo.
En cambio, en el caso de `4 % 3`, la división y el resto resultan 1, dado que 3 entra una sola vez dentro de 4, pero resta una unidad para completar a 4.



> Imagino que se estan preguntando que significa `#` y por que no aparece en la salida. Paciencia ya vamos a llegar.

<br>

**Hagamos algunas operaciones. Escriban un código que imprima el resultado de los siguientes cálculos:**
1.  10 + 9
2.  8 - 7
3.  6 * 5
4.  4 / 3
5.  2 % 1
6.  10 ** 0
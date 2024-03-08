[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/A1I8Af3W)
# Trabajo Práctico 1

## Ejercicio 1

Para este ejercicio el objetivo es leer el código, anotar lo que piensen que los prints vayan a decir y luego correr el código para ver si les dio igual o no.

```python
i1 = 3
i2 = 5
i3 = i2 + i1
print("valor de i1:")
print(i1) # 3
print("valor de i2:")
print(i2) # 5
print("valor de i3:")
print(i3) # 8
print(i1 + i2 + i3) # 16

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3) # "Python is awesome"

x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z) # "valor de x: Naranja valor de y: Naranja valor de z: Naranja"

z1 = i3 / i2 
print(z1) # 1.6
z2 = i3 % i2 
print(z2) # 3
f1 = -.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero i3:") 
print(i3) # 9.5
print("variable f3:")
print(f3) # 9
f2 += i1
print("el valor de")
print(f2) # 13
print("más")
print(f1) # -.5
print("es:")
print(f2 + f1) # 12.5

```

## Ejercicio 2 - Math

Escribir un programa dentro de exercise_math.py que dado dos números enteros imprima en pantalla el resultado de las siguientes operaciones: la suma, la diferencia, el producto, el promedio, el cociente entero y el resto de la división entera y el valor real de la división. Para entregar correctamente se deberá imprimir dichos resultados en el orden que fueron pedidos en la consigna. Por ejemplo, primero la suma, despues la diferencia, y asi sucesivamente.

Ejemplo: Para a = 57 y b = 7 el output debera ser:

```python
64
50
399
32.0
8
1
8.142857142857142
```

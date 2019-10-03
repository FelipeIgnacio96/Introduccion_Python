def funcion_max_de_tres(x, y, z):
  if (x > y) and (x > z):
    return x
  elif (y > x) and (y > z):
    return y
  elif (z > y) and (z > x):
    return z

print (funcion_max_de_tres(5, 8, 6 ))
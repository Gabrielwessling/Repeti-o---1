begin = 1;
current = begin;
soma = 0;
final = 100;

while (current <= final):
  soma += current;
  current += 1;
  print (current)
else:
  print ("O resultado da soma de todos é:", soma)
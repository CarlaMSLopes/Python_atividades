numero1 = int(input("Digite um número: "));
numero2 = int(input("Digite outro número: "));
numero3 = int(input("Digite outro número: "));

maior = int(numero3);
menor = int(numero3);

if numero1 > maior or numero2 > maior:
    if numero1 > numero2:
        maior = numero1;
    else:
        maior = numero2;
if numero1 < menor or numero2 < menor:
    if numero1 < numero2:
        menor = numero1;
    else: 
        menor = numero2;

medio = (numero1 + numero2 + numero3) - (maior + menor);

print(menor);
print(medio);
print(maior);

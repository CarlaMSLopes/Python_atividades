numero1 = int(input("Digite um número: "));
numero2 = int(input("Digite outro número: "));
numero3 = int(input("Digite outro número: "));


numero_maior = numero1;

if numero2 > numero_maior:
    numero_maior = numero2;
if numero3 > numero_maior:
    numero_maior = numero3;

numero_menor = numero1;
if numero2 < numero_menor: 
    numero_menor = numero2;
if numero1 < numero_menor:
    numero_menor = numero3;

print("Maior: ", numero_maior);
print("Menor: ", numero_menor);
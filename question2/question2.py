numero_id = input("Digite seu id: ");
horas_trabalhadas = input("Digite suas horas trabalhadas: ");
valor_por_hora = input("Digite o valor por hora:");

salario_total = int(horas_trabalhadas) * float(valor_por_hora);

print("ID: ", numero_id);
print("Salário: R$ ", '{0:.2f}'.format(salario_total));

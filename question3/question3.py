nome_vendedor = input("Digite seu nome: ");
salario_fixo = input("Digite seu salário fixo: ");
venda_mensal = input("Digite sua venda mensal: ");

comissao = float(venda_mensal) * 0.15;
salario_final = float(salario_fixo) + float(comissao);

print("Total: R$ ", '{0:.2f}'.format(salario_final));
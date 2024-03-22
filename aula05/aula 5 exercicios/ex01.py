valor_horas = float(input('Digite o valor das hora trabalhada: '))
quantidade_horas= int(input('Digite a quantidade de horas trabalhadas no mes'))

salario_bruto= valor_horas * quantidade_horas

#calculo no imposto de renda
if salario_bruto <= 900:
    ir=0
    aliquota = 0
elif salario_bruto<= 1500:
    ir= salario_bruto * 0.05
    aliquota = 5
elif salario_bruto<= 2500:
    ir = salario_bruto * 0.1
    aliquota = 10
else:
    ir= salario_bruto * 0.2
    aliquota = 20

inss= salario_bruto *0.1
fgts= salario_bruto *0.11
imp_sind= salario_bruto*0.03

total_desc= ir+inss

sal_liq= salario_bruto -(ir+inss)

print('salario bruto: (' ,valor_horas,'*',quantidade_horas,") : R$ ", salario_bruto)
print('(-) IR (', aliquota, "%)   : R$", ir)
print('(-) INSS (10%)        : R$', inss)
print('FGTS (11%)            : R$', fgts)
print('total descontos       : R$', total_desc)
print('Salario liquido       : R$', sal_liq)
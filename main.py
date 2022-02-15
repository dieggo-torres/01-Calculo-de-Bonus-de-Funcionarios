# Valor total das vendas de cada funcionário
vendas_funcionario1 = 10000
vendas_funcionario2 = 7700
vendas_funcionario3 = 27000
vendas_funcionario4 = 15000


def calcular_bonus(vendas_funcionario):
    """Calcula o bônus que o funcionário receberá com base no valor total de suas vendas"""
    if vendas_funcionario >= 20000:
        bonus_funcionario = vendas_funcionario * 0.15
    elif vendas_funcionario >= 10000:
        bonus_funcionario = vendas_funcionario * 0.10
    else:
        bonus_funcionario = 0

    return bonus_funcionario


# Bônus de cada funcionário
bonus_funcionario1 = calcular_bonus(vendas_funcionario1)
bonus_funcionario2 = calcular_bonus(vendas_funcionario2)
bonus_funcionario3 = calcular_bonus(vendas_funcionario3)
bonus_funcionario4 = calcular_bonus(vendas_funcionario4)

# Exibição dos resultados
print(f"Bônus do Funcionário 1: R${bonus_funcionario1}")
print(f"Bônus do Funcionário 2: R${bonus_funcionario2}")
print(f"Bônus do Funcionário 3: R${bonus_funcionario3}")
print(f"Bônus do Funcionário 4: R${bonus_funcionario4}")

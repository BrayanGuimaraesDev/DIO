salario = 2000

def salario_bonus(bonus, lista):
    global salario
    salario += bonus

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_bonus)
print(lista)

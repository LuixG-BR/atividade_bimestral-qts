def calcular_total(quantidade, valor_unitario):
    return quantidade * valor_unitario

resultado = calcular_total(10,2)
print(resultado)

def validar_pedido(item, quantidade, valor_unitario):
    if item and quantidade > 0 and valor_unitario > 0:
        return "Pedido válido"
    else:
        return "Pedido inválido"

print(validar_pedido("",2,1))
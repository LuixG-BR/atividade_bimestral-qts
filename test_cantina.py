from main import calcular_total, validar_pedido

def test_calcular_total():
    assert calcular_total(2,3) == 6

def test_calcular_total_zero():
    assert calcular_total(0, 10) == 0


def test_validar_pedido():
    assert validar_pedido("teste",2,2) == "Pedido válido"

def test_validar_pedido_item_vazio():
    assert validar_pedido("", 2, 5) == "Pedido inválido"

def test_validar_pedido_quantidade_invalida():
    assert validar_pedido("teste", 0, 5) == "Pedido inválido"

def test_validar_pedido_error():
    assert validar_pedido("",2,2) == "Pedido válido"
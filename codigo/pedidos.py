#JUANQUISPE
def calcular_subtotal(precio, cantidad):
    return precio * cantidad          # RN-01

def calcular_envio(subtotal):
    if subtotal >= 300:               # RN-02
        return 0
    return 20                         # RN-03

def calcular_total(subtotal, envio):
    return subtotal + envio           # RN-04

def mostrar_pedido(precio, cantidad):
    subtotal = calcular_subtotal(precio, cantidad)
    envio = calcular_envio(subtotal)
    total = calcular_total(subtotal, envio)
    print("Precio: S/", precio, "| Cantidad:", cantidad)
    print("Subtotal: S/", subtotal)
    print("Envio: S/", envio)
    print("Total: S/", total)
    print("-" * 30)

mostrar_pedido(80, 3)
mostrar_pedido(100, 3)
mostrar_pedido(150, 3)

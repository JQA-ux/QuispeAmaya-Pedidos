<!-- JUANQUISPE -->
# Solicitudes de cambio

## INC-014
- **Descripción:** El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada.
- **Tipo de cambio:** Correctivo
- **Justificación:** El cálculo del subtotal es incorrecto y afecta el importe de todos los pedidos.
- **Requisito afectado:** RN-01
- **Archivos afectados:** codigo/pedidos.py
- **Riesgo:** Bajo (cambio de una sola línea, fácil de verificar)
- **Criterio de aceptación:** Para S/ 80 y 3 unidades, el subtotal es S/ 240.
- **Decisión de aprobación (simulada):** APROBADO

## CR-015
- **Descripción:** La gerencia comercial solicita calcular automáticamente el costo de envío y el total del pedido.
- **Tipo de cambio:** Evolutivo (nueva funcionalidad)
- **Justificación:** Permite conocer el importe final a cobrar al cliente.
- **Requisitos afectados:** RN-02, RN-03, RN-04
- **Archivos afectados:** codigo/pedidos.py, documentos/requisitos.md
- **Riesgo:** Medio (agrega lógica nueva y cambia la salida del programa)
- **Criterio de aceptación:** Los casos S/ 80x3, S/ 100x3 y S/ 150x3 dan envío y total correctos.
- **Decisión de aprobación (simulada):** APROBADO

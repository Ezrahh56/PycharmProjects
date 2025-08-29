print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio plátanos: '))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Cáculo con descuento (10%)

descuento = subtotal * 0.10
new_subtotal = subtotal - descuento

# Cálculo con impuestos (16%)
impuesto = new_subtotal * 0.16

# Cálculo total de la compra (con impuestos)
costo_total = new_subtotal + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento (10%): -${descuento:.2f}
Impuesto (16%): ${impuesto:.2f}
Costo Total de la compra: ${costo_total:.2f}''')
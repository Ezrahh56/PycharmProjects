print('Sistema Descuentos VIP ***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compras hoy?)'))
tiene_menmbresia = input('Tienes la membresía de la tienda (sí/no)?')

es_elegible_decuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                        and tiene_menmbresia.strip().lower() == 'sí')
print(f'Tienes acceso al descuento VIP? {es_elegible_decuento}')
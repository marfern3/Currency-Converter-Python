try:
    value = float(input('¿Qué cantidad de dinero quieres cambiar?'))
    original_money = input('¿Cuál es tu moneda?').strip().upper()
    change_money = input('¿Por qué moneda quieres cambiar?').strip().upper()

except ValueError:
    print("Error: Ingrese un número valido para la cantidad de dinero")
    exit()

print(f"Cantidad a cambiar: {value} {original_money} -> {change_money}")

tax = {
    'USD': 1.0,
    'EUR': 0.9515,
    'GBP': 0.7891,
    'JPY': 105.14,
    'ARS': 850.0
}

def money_converter(value, original_money, tax):
    if original_money not in tax or change_money not in tax:
        print('Moneda no encontrada')
        return None
    
    usd_value = value/tax[original_money]

    converted_value = usd_value * tax[change_money]

    return converted_value

converted_value = money_converter(value, original_money, tax)

if converted_value is not None:
    print(f'\nLa cantidad convertida es: {converted_value:.2f} {change_money}')
else:
    print("\nNo se pudo realizar la conversión debido a un error con las monedas ingresadas.")
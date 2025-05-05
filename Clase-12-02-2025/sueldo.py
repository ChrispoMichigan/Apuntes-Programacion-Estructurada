dias_trabajados = int(input("Ingrese la cantidad de días trabajados: "))
sueldo_diario = 248.96
horas_extras = float(input("Ingrese la cantidad de horas extras trabajadas: "))
pago_ahora_extra = sueldo_diario * 2
sueldo = dias_trabajados * sueldo_diario + horas_extras * pago_ahora_extra
print(f"El sueldo antes de impuestos: ${sueldo}")
print(f"Infonavit 15%: ${sueldo * 0.15:.2f}")
print(f"ISR 30%: ${sueldo * 0.3:.2f}")
print(f"El sueldo a pagar es: ${sueldo * 0.55:.2f}")

#MJUT
#Constantes(por convencion, se escriben en mayusculas)
SALARIO_BASE = 3500.00
BONO_PRODUCTIVIDAD = 500.00
IMPUESTO = 0.12

#MJUT
#Datos del empleado(variables)
nombre_empleado = "Mario Tumax"
es_empleado_fijo= True

#MJUT
#Calculo del salario bruto (salario base + bono)
salario_bruto = SALARIO_BASE + BONO_PRODUCTIVIDAD

#MJUT
#Calculo del descuento por impuestos
descuento = salario_bruto * IMPUESTO

#MJUT
#Calculo del salario neto
salario_neto = salario_bruto - descuento

#MJUT
#Mostrar la informacion
print("Nombre del Empleado: ", nombre_empleado)
print("¿Empleado fijo?: ", es_empleado_fijo)
print("Salario base: ", SALARIO_BASE)
print("Bono de productividad: ", BONO_PRODUCTIVIDAD)
print("Salario bruto: ",salario_bruto)
print("Descuento por impuesto: ",descuento)
print("Salario neto: ",salario_neto)

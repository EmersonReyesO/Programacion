empleados= {'1085273528': 50000000,
            '1085245785': 10000000,
            '1789785475': 7000000}

lista_empleados=('1789785475','1085273528',
'1085245785')

def validar_persona (empleados:dict,lista_empleados:tuple)->dict:
    
    for llave in empleados:
        if empleados[llave] >= 3000000 and llave in lista_empleados:
            empleados[llave] = empleados[llave]*0.20
        else:
            return 'revisar datos'
    
    return empleados

validar_persona(empleados,lista_empleados)
print(validar_persona(empleados,lista_empleados))
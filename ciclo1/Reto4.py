
def validar_funcionario(funcionario:dict)->tuple:
    funcionario1=funcionario.copy()
    lista_nombres=[]
    
    for llave in funcionario:
        if funcionario[llave]['areas'][0]['activo'] == 'no':
            del funcionario1[llave]
            
    for llave in funcionario1:
        primera_letra_n = funcionario1[llave]['nombres'][0].lower()
        primer_apellido = funcionario1[llave]['apellidos'].split(',')[0].lower()
        lista_nombres.append('{}.{}@gmail.com'.format(primera_letra_n,primer_apellido))
        
        tupla =(sorted(lista_nombres),funcionario1)
        return tupla
        
            
    funcionario1[llave]


funcionario = {
        10852758781: {
            "nombres": "Juana",
            "apellidos": "Gomez, Lopez",
            "annio_ingreso": 2000,
            "dependencia": "Rectoria",
            "areas": [
                {
                    "nombre": "Secretaria",
                    "codigo": 1,
                    "activo": "si"
                },
            ]
        },
    
    
        1010275871: {
            "nombres": "Pepito Carlos",
            "apellidos": "Mendieta, Castillo",
            "annio_ingreso": 2003,
            "dependencia": "Rectoria",
            "areas": [
                    {
                        "nombre": "Tesoreria",
                        "codigo": 2,
                        "activo": "si"
                    },
                ]
            },
        
            10102758715: {
            "nombres": "Miguel Angel",
            "apellidos": "Suarez, Quiroz",
            "annio_ingreso": 2005,
            "dependencia": "Rectoria",
            "areas": [
                    {
                        "nombre": "Tesoreria",
                        "codigo": 2,
                        "activo": "si"
                    },
                ]
            },
            
            10122758089: {
            "nombres": "Luisa Paula",
            "apellidos": "Fajardo, Fernandez",
            "annio_ingreso": 2005,
            "dependencia": "Vicerrectoria",
            "areas": [
                    {
                        "nombre": "Academica",
                        "codigo": 11,
                        "activo": "si"
                    },
                ]
            },
            
            
            101227580874: {
            "nombres": "Pablo Luis",
            "apellidos": "Jojoa, Ruiz",
            "annio_ingreso": 1999,
            "dependencia": "Vicerrectoria",
            "areas": [
                    {
                        "nombre": "Administrativa",
                        "codigo": 12,
                        "activo": "no"
                    },
                ]
            },

            1085273521: {
            "nombres": "Johana",
            "apellidos": "Gomez, Lopez",
            "annio_ingreso": 2000,
            "dependencia": "Rectoria",
            "areas": [
                    {
                        "nombre": "Secretaria",
                        "codigo": 1,
                        "activo": "no"
                    },
                ]   
            },
            
            
            1010275872: {
            "nombres": "Juan Carlos",
            "apellidos": "Mendieta, Castillo",
            "annio_ingreso": 2003,
            "dependencia": "Rectoria",
            "areas": [
                    {
                        "nombre": "Tesoreria",
                        "codigo": 2,
                        "activo": "no"
                    },
                ]
            },
            
            
            1010375891: {
            "nombres": "Miguel Angel",
            "apellidos": "Suarez, Quiroz",
            "annio_ingreso": 2005,
            "dependencia": "Rectoria",
            "areas": [
                    {
                        "nombre": "Tesoreria",
                        "codigo": 2,
                        "activo": "no"
                    },
                ]
            },
            
            
            1012025802: {
            "nombres": "Silvia Lorena",
            "apellidos": "Fajardo, Melo",
            "annio_ingreso": 2005,
            "dependencia": "Vicerrectoria",
            "areas": [
                    {
                        "nombre": "Academica",
                        "codigo": 11,
                        "activo": "no"
                    },
                ]
            },
            
            
            1085242433: {
            "nombres": "Gloria Sofia",
            "apellidos": "Jojoa, Ruiz",
            "annio_ingreso": 1999,
            "dependencia": "Vicerrectoria",
            "areas": [
                    {
                        "nombre": "Administrativa",
                        "codigo": 12,
                        "activo": "no"
                    },
                ]
            }
}

print(validar_funcionario(funcionario))
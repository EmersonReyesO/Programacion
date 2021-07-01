def validar_funcionario(funcionario:dict)->tuple:
    
    blacklist =[key for key in funcionario  if funcionario[key]['areas'][0]['activo']=='no']
    for x in blacklist:
        del funcionario[x]
        
    correos_ordenados = [funcionario[key]['nombres'][0].lower()+ '.'+ funcionario[key]['apellidos'].split(',')[0].lower()+'@gmail.com' for key in funcionario]
    
    return (sorted(correos_ordenados),funcionario)
    
    

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
        
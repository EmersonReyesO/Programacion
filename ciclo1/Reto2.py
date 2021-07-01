def calcularNivelExigencia (nombre, edad, medida): 
    
    MLPM = 220 - edad

    entradadatos={
        'nombre' : nombre.upper(),
        'edad' : edad,
        'medida' : medida,
    }
    
    if entradadatos['medida'] > 0 and entradadatos['medida'] <= MLPM*0.5:
        entradadatos['lpm'] = MLPM
        entradadatos['exigencia'] = 'En reposo'
        return entradadatos
    
    elif entradadatos['medida'] > MLPM*0.5  and entradadatos['medida'] <= MLPM*0.6:
        entradadatos['lpm'] = MLPM
        entradadatos['exigencia'] = 'Exigencia baja'
        return entradadatos
    
    elif entradadatos['medida'] > MLPM*0.6  and entradadatos['medida'] <= MLPM*0.8:
        entradadatos['lpm'] = MLPM
        entradadatos['exigencia'] = 'Exigencia media'
        return entradadatos
    
    elif entradadatos['medida'] > MLPM*0.8 and entradadatos['medida'] <= MLPM:
        entradadatos['lpm'] = MLPM
        entradadatos['exigencia'] = 'Exigencia maxima'
        return entradadatos
    
print(calcularNivelExigencia('carlos rengifo',35,100))


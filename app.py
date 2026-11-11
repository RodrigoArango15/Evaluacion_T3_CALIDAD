def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def evaluar_estudiante(promedio):
    if promedio >= 12:
        return "Aprobado"
    return "Desaprobado"

if __name__ == "__main__":
    print("SISTEMA DE GESTIÓN ACADÉMICA - INNOVATEC")
    prom = calcular_promedio(15, 12, 14)
    print(f"Promedio: {prom:.2f} - Estado: {evaluar_estudiante(prom)}")
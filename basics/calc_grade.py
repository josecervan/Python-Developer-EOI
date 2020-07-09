asistencia = input("Asistencia superior al 80% (s/n): ")
nota_asistencia = 5.5 if asistencia == 's' else 0

lista_notas = [float(input("Nota1: ")), float(input("Nota2: ")), float(input("Nota3: "))]

media = 0.4 * ((lista_notas[0] + lista_notas[1] + lista_notas[0]) / 3) if all(i >=5 for i in lista_notas) else 0

nota_participacion = 0.05 * (float(input('Participacion: ')))
suma_total = nota_asistencia + media + nota_participacion

print(suma_total)

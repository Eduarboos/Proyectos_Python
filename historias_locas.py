# Concatenar cadeas de caracteres.
# supongamos que queremos crear una cadena que diga:
# Aprendamos a programar con __________________.

# company = "Edward Technology"

#print("Aprende a programar con: " + company)
#print("Aprende a programar con {}".format(company))
#print(f"Aprende a programar con {company}")

########################################################
# Mad libs(Historias locas)
adj = input("Ingrese un Adjetivo: ")
verbo01 = input("Ingrese un Verbo: ")
verbo02 = input("Ingrese un Verbo: ")
sustantivo_plural = input ("Sustantivo(Plural): ")


madlib = f"Programar es tan {adj}! Siempre me emocina pro que me encata {verbo01} problemas. ¡Apre a {verbo02} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)

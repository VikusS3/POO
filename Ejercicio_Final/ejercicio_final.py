import openai

openai.api_key = "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"
system_rol = '''Eres un analizador de sentimientos.
                 Tu objetivo es analizar el sentimiento de un texto que yo te daré.
                 y me daras una respuesta con al menos un caracter y como maximo 4 caracteres.
                 SOLO RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, 0 es neutralidad y 1 es 
                 positividad maxima. Puedes ir entre esos rangos osea
                 0.3, -0.5, 0.9 etc tambien son validos . (Solo puedes responder con ints o floats)'''

mensajes = [{"role": "system", "content": system_rol}]


class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <=-0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <=-0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1  and polaridad <=0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <=0.4:
            return "\x1b[1;32m" + "Algo Positivo" + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <=0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9 and polaridad <=1:
            return "\x1b[1;32m" + "Positivo Maximo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Negativo Maximo" + "\x1b[0;37m"
        

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "Escribe un texto:  " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.Completion.create(
        model = "gpt-3.5-turbo",
        menssages = mensajes,
        max_tokens = 8,
    )
    
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento) 
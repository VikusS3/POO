import openai

openai.api_key = "API_KEY"
system_rol = '''Eres un analizador de sentimientos.
                 Tu objetivo es analizar el sentimiento de un texto que yo te daré.
                 y me daras una respuesta con al menos un caracter y como maximo 4 caracteres.
                 SOLO RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, 0 es neutralidad y 1 es 
                 positividad maxima. Puedes ir entre esos rangos osea
                 0.3, -0.5, 0.9 etc tambien son validos . (Solo puedes responder con ints o floats)'''

mensajes = [{"role": "system", "content": system_rol}]


class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)


class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] <= polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")


rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1, -0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.4), Sentimiento("Algo Positivo", "32")),
    ((0.4, 0.9), Sentimiento("Positivo", "32")),
    ((0.9, 1), Sentimiento("Positivo Maximo", "32"))
]


analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "Escribe un texto:  " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        menssages=mensajes,
        max_tokens=8,
    )

    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)

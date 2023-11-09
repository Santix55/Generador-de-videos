import re

class Censor:

    # Añade al diccionario del censor, las palabras de los archivos
    def __init__(self,banned_words_files):
        self.banned_words = set()
        for file_name in banned_words_files:
            with open(file_name, 'r', encoding="utf-8") as file:
                for word in file:
                    word = word.rstrip("\n")
                    self.banned_words.add(word)

    # Devuelve el string censurado (PUEDE SER OPTIMIZADO)
    def censura(self, texto):

        for palabra in self.banned_words:
            texto = re.sub(rf'\b{palabra}\b', palabra[0] + '*' * (len(palabra) - 1), texto, flags=re.IGNORECASE)

        return texto


# ES SOLO UNA PRUEBA, NO SOY RACISTA
if __name__ == "__main__":
    censor = Censor (["es.txt", "en.txt"])
    print(censor.banned_words)
    print(censor.censura("Buenos niggas, cabrones y muchas boobs"))
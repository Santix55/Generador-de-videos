from typing import List

class Comentario:
    def __init__(self, texto:str, nota:int, respuestas: List['Comentario'] = None):
        self.texto = texto
        self.respuestas = respuestas if respuestas is not None else []


# Recorre la lista aplicando la función a cada uno de los comentarios
# primero recorre lo aplica al comentario y posteriormente a sus respuestas
def recorrer (comentarios:List[Comentario], # Array de comentarios a recorrer
              funcion,                      # Función que quieres realizar
              max_profundidad:int = 2,      # Anidamiento de respuestas máximo
              profundidad:int = 0):         # Profudidad actual del arbol
    
    if not comentarios or profundidad > max_profundidad:
        return

    for comentario in comentarios:
        funcion(comentario)
        recorrer(comentario.respuestas, funcion, max_profundidad, profundidad+1)


# TEST DE EJEMPLO | SOLO SE EJECUTA SI EJECUTAS ESTE FICHERO COMO MAIN
if __name__ == "__main__":

    comentario0 = Comentario ("Hola soy la raíz", 0)
    comentario1 = Comentario ("Hola soy una respuesta", 1)
    comentario2 = Comentario ("Hola soy una respuesta a una respuesta", 2)
    comentario3 = Comentario ("De vuelta a la raíz", 3)
    comentarioN = Comentario ("Este comentario no debería de salir", -1)

    comentario0.respuestas.append(comentario1)
    comentario1.respuestas.append(comentario2)
    comentarioN.respuestas.append(comentarioN)

    comentarios = [comentario0, comentario3]

    def verTexto(comentario:Comentario):
        print(comentario.texto)

    recorrer(comentarios, verTexto)
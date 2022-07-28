def square(n):
    return n*n

def increment(n):
    return n+1

class Node:
    def __init__(self, parent, action, answer):
        self.parent = parent
        self.action = action
        self.answer = answer
    
    def path(self):
        if self.parent == None:
            return [(self.action, self.answer)]
        else:
            return self.parent.path() + [(self.action, self.answer)]

def findSequence(initial, goal):
    # inicio creando mi lista de nodos, con el nodo inicial.
    q = [Node(None, None, 1)]
    while q:
        # El primero nodo de la lista será el nodo padre,
        # así que lo apartamos.
        # Al parecer hará una busqueda de izquierda a derecha. 
        parent = q.pop(0)
        # Seteamos las dos acciones a realizar
        for (a,r) in [('increment', increment), ('square', square)]:
            # creamos el nuevo nodo, obviamente en base al padre
            # ya que usaremos el valor (parent.answer) que tiene el padre
            # y le aplicaremos ambas acciones.
            newNode = Node(parent, a, r(parent.answer))
            # Verificamos si este nuevo nodo ya es nuestro GOAL
            if newNode.answer == goal:
                # Notar que path alamacena toda la información
                # histórica de valores y acciones del nodo
                return newNode.path()
            else:
                q.append(newNode)

answer = findSequence(1,100)
print(f"answer: {answer}")


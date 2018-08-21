from pila import *
from arbol import *
from utilidades import readLinesFile, writeInFile

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)


def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

for exp in readLinesFile('expresiones.in'):
        listExp = exp.strip('\n').split(' ')
        print(listExp)
        writeInFile(listExp)
        pila = Pila()
        convertir(listExp, pila)
        print(evaluar(pila.desapilar()))
        writeInFile(evaluar(pila.desapilar()))





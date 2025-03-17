from principal import *
from configuracion import *
import random
import math
from extras import *

#esta funcion le saca el enter al archivo txt
def sacaUltimoCaracter (lista):
    nvaLista = [] #me fabrico una nueva lista para meter la lista de productos sin el enter(sin el ultimo caracter)

    for elem in lista: #recorro la lista por elemento
        nvaLista.append(elem[0:len(elem)-1]) # appendeo cada elemento a la lista vacia desde el primer caracter hasta el anteultimo(porque el ultimo es el enter)
    return nvaLista #retorno la lista con los elementos sin el ultimo caracter

#esta funcion, dada una cadena que tiene mas de una palabra separadas por una coma, lo que hace es ir concatenando a una lista vacia esas palabras que estan entre las comas y al final retorna una lista con esas palabras
def separarPorComas(cadena): #funcion creada por mi
    lista = []  #me fabrico una lista vacia para ir poniendo cada parte de la cadena separada por una coma
    nvaCad = ""  #me fabrico una cadena vacia para ir concatenando esas palabras que estan entre comas

    for char in cadena: #recorro la cadena por caracter
        if char == ",": #si el caracter es una coma
            lista.append(nvaCad)  #agrego a la lista vacia los caracteres que se fueron concatenando en la cadena vacia
            nvaCad = ""  #vuelvo a restablecer la cadena vacia para que vuelva a concatenar otra palabra que este entre comas
        else: # si no es una coma
            nvaCad = nvaCad + char  #concateno los caracteres que estan entre comas, // voy concatenando los caracteres

    lista.append(nvaCad) #concateno los ultimos caracteres que se guardaron en la cadena vacia en la lista vacia

    return lista #retorno la lista separadas por comas. Es decir, lo que hace es concatenar letras hasta llegar a una coma, todas esas letras hacen un "elemento" de la lista.

# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura(productos):
    nvaLista = [] #me fabrico una nvaLista para despues appendear a la lista ya dada por la funcion sacaUltimoCaracter(es porque esta como consigna, lista de lista)

    prod = "productos.txt" # asigno a la variable g, el nombre del archivo que quiero leer
    leer = open (prod,"r",encoding = "ISO_8859-1:1987") # le paso los parametros para leer el archivo txt
    leerPorLineas = leer.readlines() # asigno a la variable h, que lo lea por lineas

    sinEnter = sacaUltimoCaracter (leerPorLineas) # llamo a la funcion sacaUltimCaracter y lo asigno a la variable sinEnter

    for elem in sinEnter: #recorro la lista por elemento
        porComas = separarPorComas(elem) #llamo a la funcion separarPorComas y la asigno a la variable porComas
        nvaLista.append(porComas) #appendeo cada lista que retorna la funcion separarPorComas

    return nvaLista

#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    nvaLista = [] # creo una nueva variable a la cual le asigno una lista vacia

    productoAleatorio = random.choice(lista_productos) # en la variable productoAleatorio asigno un valor aleatorio extraido desde la lista_productos

    economico_premium = ["(economico)","(premium)"] # creo una variable economico_premium al cual le asigno una lista con dos cadenas adentro, "economico" y "premium"
    calidadAleatoria = random.choice(economico_premium) # en la variable calidadAleatoria asigno un valor aleatorio extraido desde la lista economico_premium

    cont = 0 # inicializo el contador en 0
    for elem in productoAleatorio: # recorro la lista generada aleatoriamente por elemento
        if cont == 0: # si el contador == 0 (esto es para appendear a la lista vacia el primer elemento, que seria el nombre del producto)
            nvaLista.append(elem) # appendeo
            cont = cont + 1 # incremento el contador en 1

    for pos in range(len(productoAleatorio)): # voy generando numeros desde 0 al len(productoAleatorio) en este caso seria 3, porque productoAleatorio es una lista con 3 elementos
        if calidadAleatoria == "(economico)": # si la calidadAleatoria coincide con la calidad economico
            nvaLista.append(calidadAleatoria) #lo appendeo a la lista que ya tenia el nombre del producto
            nvaLista.append(productoAleatorio[1]) # y ademas le appendeo el precio en la posicion 1(es donde esta el precio economico)
            return nvaLista # retorno lista["nombre Producto","economico/premium","precioEconomico/precioPremium"]
        else:
            nvaLista.append(calidadAleatoria) # si la calidadAleatoria no era economica, entonces es premium. La appendeo a la lista que ya tenia el nombre del producto
            nvaLista.append(productoAleatorio[2]) # y ademas le appendeo el precio en la posicion 2(es donde esta el precio premium)
            return nvaLista # retorno la lista. ["nombre Producto","economico/premium","precioEconomico/precioPremium"]

# esta funcion devuelve el valor absoluto de un numero
def valorAbsoluto (num):
    absoluto = num # creo una variable que se llama absoluto y le asigno el numero que recibe la funcion
    if absoluto < 0: # si absoluto es menor que 0
        absoluto = absoluto * (-1) # lo multiplico por -1 para que se haga positivo
    else:
        absoluto = absoluto # si no lo dejo como esta
    return absoluto # retorno la variable absoluto

# esta funcion retorna True si la resta entre el precio del primer producto y el precio del segundo producto es menor al margen. Si no retorna False
def similar (lista,margen):
    primerProducto = lista[0][2] # en la variable primerProducto me guardo el precio del primer producto
    segundoProducto = lista[1][2] #  en la variable segundoProducto me guardo el precio del segundo producto
    diferencia = int(primerProducto) - int(segundoProducto) # creo una variable diferencia y hago la resta entre ambos
    absoluto = valorAbsoluto(diferencia) # creo  una variable absoluto y llamo a la funcion valorAbsoluto para que me de el valor absoluto de la resta
    if absoluto < margen: # si el valor absoluto es menor a 1000
        return True # retorno True
    else:
        return False # sino False

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    parecido = similar(lista_productos,margen) # creo una variable parecido y le asigno el valor de la funcion similar(devuelve True o False

    while not parecido: # si parecido es False, lo niego para entre al while y entre en un ciclo infinito hasta que se vuelva True
        prod1 = buscar_producto(lista_productos) # a la variable prod1 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
        prod2 = buscar_producto(lista_productos) # a la variable prod2 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
        dosProd = prod1,prod2 # ala variable dosProd le asigno la variable prod1 y prod2, esto es para que se guarde en esa nueva variable dos listas
        parecido = similar(dosProd,margen) # actualizo la variable parecido

        if parecido == True: # si parecido es True
            prod1 = buscar_producto(lista_productos) # a la variable prod1 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
            prod2 = buscar_producto(lista_productos) # a la variable prod2 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
            dosProd = prod1,prod2 # ala variable dosProd le asigno la variable prod1 y prod2, esto es para que se guarde en esa nueva variable dos listas
            productoSimilar = random.choice(dosProd) # creo una variable productoSimilar y le asigno UNA lista de las dos que tenia (al azar)
            return productoSimilar # la retorno
    else:
        prod1 = buscar_producto(lista_productos) # a la variable prod1 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
        prod2 = buscar_producto(lista_productos) # a la variable prod2 le asigno un producto aleatorio (es lo que retorna la funcion buscar_producto)
        dosProd = prod1,prod2 # ala variable dosProd le asigno la variable prod1 y prod2, esto es para que se guarde en esa nueva variable dos listas
        productoSimilar = random.choice(dosProd) # creo una variable productoSimilar y le asigno UNA lista de las dos que tenia (al azar)
        return productoSimilar # la retorno


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont = 0 # inicializo un contador para ir contando la cantidad de productos similares
    while cont < 2: # mientras el contador sea menor a 3
        for producto in lista_productos : # recorro la lista por elemento
            diferencia = int(precio) - int(producto[2]) # hago una variable para guardar la resta del precio y el precio del producto
            absoluto = valorAbsoluto(diferencia) # le calculo el valor absoluto
            if absoluto <= margen : # si el valor absoluto es menor a 1000, es porque tiene precio similar
                cont = cont + 1 #sumo uno, es decir que encontre al menos un producto que tiene un valor similar
                 # cuando el contador llegue a 2(osea serian 3 productos) retorno True, porque ya encontre al menos 3 productos que son similares
    return cont >=2

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente el producto
def procesar(producto_principal, producto_candidato, margen):

    sonidoIncorrecto = pygame.mixer.Sound ("sonidos/precio_incorrecto1.mp3")
    sonidoCorrecto = pygame.mixer.Sound ("sonidos/precio_correcto.mp3")

    suma = 0 # declaro una variable suma para ir sumando cada precio correcto
    precioPrincipal = producto_principal[2] # precio del producto principal (lo que esta pintado de color)
    precioCandidato = producto_candidato[2] # precio del producto candidato( lo que ingresa el usuario)

    if producto_candidato[0] == producto_principal[0]: # si el usuario elije el mismo producto, es decir, la misma opcion que esta pintado de color
        sonidoIncorrecto.play()
        return 0 #retorno 0 puntos, NO vale
    else:
        if int(precioCandidato) == int(precioPrincipal) or (valorAbsoluto(int(precioCandidato) - int(precioPrincipal))) <= margen : #si el precio de ambos son iguales o la resta de ambos (en valor absoluto) es menor al margen
            sonidoCorrecto.play()
            suma = suma + int(precioCandidato) # a la variable suma, le sumo el precio del producto candidato (lo que ingreso el usuario)
        else:
            sonidoIncorrecto.play()
            return 0 # si no retorno 0, porque es incorrecto
    return suma

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)' para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    nvaLista = [] # creo una nueva variable a la cual le asigno una lista vacia
    nvaLista.append(producto) # appendeo el producto principal como primer elemento de la lista
    precioProductoPpal = producto[2] # creo una variable y le asigno el precio del producto principal

    while len(nvaLista) < 6: # mientras el len de la lista vacia es menor que 6 (0,1,2,3,4,5)
        productoAleatorio = buscar_producto(lista_productos) # creo una nueva variable productoAleatorio y le asigno lo que retorna la funcion buscar_producto. Esa funcion devuelve una lista aleatoria con 3 elementos.
                                                                # ["nombre Producto","economico/premium","precioEconomico/precioPremium"]

        if productoAleatorio not in nvaLista and esUnPrecioValido(precioProductoPpal,nvaLista,margen): # si el productoAleatorio NO esta en la nvaLista y ademas es unPrecioValido
            nvaLista.append(productoAleatorio) # entonces lo appendeo

    return nvaLista


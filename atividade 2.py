caracter = ""
def  parametroCaracter ():
    caracter = input ( "Insira os caracteres {[()]}:" )
    if  "{[()]}"  in  caracter:
        print ( "Parâmetro certo" )
        return  true
    else:
        print ( "ops, algo está errado!" )
        return  false
parametroCaracter ()
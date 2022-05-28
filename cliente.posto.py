prefCliente =int(input('Ola'
     '\nSelecione o tipo de combustivel que voce deseja!'
     '\nDigite o numero do combustivel.'
     '\n(1)Gasolina Aditivada'
     '\n(2)Gasolina Comum'
     '\n(3)Diesel'
     '\n(4)Etanol'
     '\n'))

dinheiroCliente =int(input ('Digite quanto de combustivel deseja colocar:'))

if prefCliente == 1 :
    combus1  =  dinheiroCliente/6.90
    print (f'Total de combustivel:{combus1:.2f}L')
elif prefCliente == 2 :
    combus2 = dinheiroCliente/7.27
    print(f'Total de combustivel:{combus2:.2f}L')
elif prefCliente == 3 :
    combus3 = dinheiroCliente/6.88
    print(f'Total de combustivel: {combus3:.2f}L')
elif prefCliente == 4 :
    combus4 = dinheiroCliente/4.99
    print(f'Total de combustivel:{combus4:.2f}L')


    
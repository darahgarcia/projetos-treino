valorCarro=int(input('Insira o valor do carro que deseja comprar: '))

formPagamento=int(input('Qual sera a forma de pagamento?\n'
                        '(1)A vista\n'
                        '(2)Parcelado\n'))

if formPagamento == 1:
    valorFinal=valorCarro-((20/100)*valorCarro)
    print(f'O valor final a ser pago e de:R${valorFinal:.2f}' )

if formPagamento == 2:
    qntParcela=int(input('Qual sera a quantidade de parcelas?\n'
                         '(1)6x\n'
                         '(2)12x\n'
                         '(3)18x\n'
                         '(4)24x\n'
                         '(5)30x\n'
                         '(6)36x\n'
                         '(7)42x\n'
                         '(8)48x\n'
                         '(9)54x\n'
                         '(10)60x\n'))
    
    if qntParcela == 1:
        valorFinal1=valorCarro+(valorCarro*(3/100))
        parcelas1=valorFinal1/6
        print(f'O valor da parcela sera de: R${parcelas1:.2f}\n'
              f'O valor total com juros e de: R${valorFinal1:.2f}')        
        
    if qntParcela == 2:
        valorFinal2=valorCarro+(valorCarro*(6/100))
        parcelas2=valorFinal2/12
        print(f'O valor da parcela sera de: R${parcelas2:.2f}\n'
              f'O valor total com juros e de: R${valorFinal2:.2f}')
        
    if qntParcela == 3:
        valorFinal3=valorCarro+(valorCarro*(9/100))
        parcelas3=valorFinal3/18
        print(f'O valor da parcela sera de: R${parcelas3:.2f}\n'
              f'O valor total com juros e de: R${valorFinal3:.2f}')
        
    if qntParcela == 4:
        valorFinal4=valorCarro+(valorCarro*(12/100))
        parcelas4=valorFinal4/24
        print(f'O valor da parcela sera de: R${parcelas4:.2f}\n'
              f'O valor total com juros e de: R${valorFinal4:.2f}')
        
    if qntParcela == 5:
        valorFinal5=valorCarro+(valorCarro*(15/100))
        parcelas5=valorFinal5/30
        print(f'O valor da parcela sera de: R${parcelas5:.2f}\n'
              f'O valor total com juros e de: R${valorFinal5:.2f}')
        
    if qntParcela == 6:
        valorFinal6=valorCarro+(valorCarro*(18/100))
        parcelas6=valorFinal6/36
        print(f'O valor da parcela sera de: R${parcelas6:.2f}\n'
              f'O valor total com juros e de: R${valorFinal6:.2f}')
        
    if qntParcela == 7:
        valorFinal7=valorCarro+(valorCarro*(21/100))
        parcelas7=valorFinal7/42
        print(f'O valor da parcela sera de: R${parcelas7:.2f}\n'
              f'O valor total com juros e de: R${valorFinal7:.2f}')
        
    if qntParcela == 8:
        valorFinal8=valorCarro+(valorCarro*(24/100))
        parcelas8=valorFinal8/48
        print(f'O valor da parcela sera de: R${parcelas8:.2f}\n'
              f'O valor total com juros e de: R${valorFinal8:.2f}')
        
    if qntParcela == 9:
        valorFinal9=valorCarro+(valorCarro*(27/100))
        parcelas9=valorFinal9/54
        print(f'O valor da parcela sera de: R${parcelas9:.2f}\n'
              f'O valor total com juros e de: R${valorFinal9:.2f}')
        
    if qntParcela == 10: 
        valorFinal10=valorCarro+(valorCarro*(30/100))
        parcelas10=valorFinal1/60
        print(f'O valor da parcela sera de: R${parcelas10:.2f}\n'
              f'O valor total com juros e de: R${valorFinal10:.2f}')                        
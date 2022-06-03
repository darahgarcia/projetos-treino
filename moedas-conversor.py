Moeda = int(input("Ola, escolha qual moeda voce deseja converter:"
                  "\n(1)Dolar para Real" 
                  "\n(2)Real para Dolar\n"))

Valortotal= float(input('Insira o valor que deseja converter:\n'))


conver1=Valortotal/4.80 #p/dolar
conver2=Valortotal*4.80 #p/real

cImposto=(Valortotal*6.38)/100

valorTotal2=Valortotal+cImposto

if Moeda == 1 : 
    print(f"O valor a ser recebido e de : R${conver2:.2f}")
    print(f"Imposto a ser pago: ${cImposto:.2f}\n")
    print(f"Total a pagar: ${valorTotal2:.2f}")

if Moeda == 2 : 
    print(f"O valor a ser recebido e de : ${conver1:.2f} \n")
    print(f"Imposto a ser pago: R${cImposto:.2f}\n")
    print(f"Total a pagar: R${valorTotal2:.2f}")

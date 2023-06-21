from ex110 import moeda # Ou from moeda import aumentar, dobro..

p = float(input('Digíte o preço: R$'))
moeda.resumo(p, 20, 10) # p = valor, 20 = taxa de aumento, 10 = taxa de redução (podem ser alteradas)
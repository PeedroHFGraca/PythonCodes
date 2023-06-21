from ex112.UtilidadesCV import moeda # Ou from moeda import aumentar, dobro..
from ex112.UtilidadesCV import dado

p = dado.leiaDinheiro('Digíte o preço: R$')
moeda.resumo(p, 20, 10) # p = valor, 20 = taxa de aumento, 10 = taxa de redução (podem ser alteradas)
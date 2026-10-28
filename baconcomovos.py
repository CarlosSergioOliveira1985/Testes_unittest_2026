"""
1 - receber um numero inteiro
2 - saber se o numero e multiplo de 3 ou 5
    Bacon com ovos 
3 - saber se o numero é multiplo somente de 3:
    bacon
4 - saber se o numerto é multiplo somente de 5:
    ovos
5 - saber se o numero não e multiplo de 3 e 5 :
    Passa fome 
"""

def bacon_com_ovos(n):
    assert isinstance(n,int), 'n deve ser int'

    if n % 3==0 and n % 5==0:
        return 'Bacon com ovos'

    if n % 3==0:
        return 'Bacon'

    if n % 5==0:
        return 'Ovos'
    
    return 'Passa fome'
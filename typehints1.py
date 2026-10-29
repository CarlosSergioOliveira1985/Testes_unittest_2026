from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable


numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = "Carlos Oliveora"

lista: List[int] = [1,2,3]
lista_str_int: List[Union[int, str]] = [1,2,3,'Carlos']
tupla: Tuple[int, int, int, str] = (1,2,3, 'Carlos')


MeuDict = Dict [str, Union[str, int, List[int]]] # Alias
pessoa:Dict [str, Union[str, int]] = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30}
pessoa2:Dict [str, Any] = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30}
pessoa3:MeuDict = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30, 'l':[1,2]}

UserId = NewType('UserId', int)
user_id = UserId(356255789453)

def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao

def fala_oi():
    print("oi")

def retorna_funcao2(funcao: Callable[[int,int], int]) -> Callable:
    return funcao


def soma(x:int,y:int) -> int:
    return (x+y)

retorna_funcao(fala_oi)()
print(retorna_funcao2(soma)(2,3))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self):
        print(f'{self.nome} {self.sobrenome} está falando...')

def iterar(sequencia:Sequence[int]):
    return [x * 2 for x in sequencia]

def iterar2(sequencia:Iterable[int]):
    return [x * 2 for x in sequencia]

print(iterar([1,2,3,4,5,6]))
print(iterar2([1,2,3,4,5,6]))


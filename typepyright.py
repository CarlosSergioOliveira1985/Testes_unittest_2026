from typing import Final, List, Set, Union, Tuple, Dict, Any



nome: str = "carlos"
x: int = 22
y: float = 3.3
c: complex = 3+ 4j
is_valid: bool = True
data: bytes = b"Whatever"


lista: List[int] = [1,2,3]
lista_str_int: List[Union[int, str]] = [1,2,3,'Carlos']
tupla: Tuple[int, int, int, str] = (1,2,3, 'Carlos')
set: Set[int] = {1,2,3,4, 4} # nao aceita repitidos e é mutavel
set_imutavel: frozenset[int] = frozenset([1,2,3,4,4]) #nao aceita repitidos e é imutavel


MeuDict = Dict [str, Union[str, int, List[int]]] # Alias
pessoa:Dict [str, Union[str, int]] = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30}
pessoa2:Dict [str, Any] = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30}
pessoa3:MeuDict = {'nome': 'Carlos' ,  'sobrenome':'Oliveira' , 'idade': 30, 'l':[1,2]}

numeros: range = range(10)

none: None = None # Representa falta de valor 
qualquer_coisa: object = 123 # tipo mas alplo de tiagem

CONSTANTE: Final[dict[str, int]] = {"numero": 123, "outro_numero": 452}



print(set)
print(set_imutavel)

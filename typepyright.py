
from collections.abc import Callable

from typing import Final, List, Set, Union, Tuple, Dict, Any

from utils import sep_print, cyan_print



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



def remove_duplicates(items: list[str]) -> list[str]:
    to_dict = dict.fromkeys(items)
    return list(to_dict)

list_with_duplicates = ['Carlos', 'a', 'b', 'a', 'Carlos']
unique_items = remove_duplicates(list_with_duplicates)

sep_print()

cyan_print(f'{unique_items = }')


def is_image_file(filename: str) -> bool:
    extensions = ('.jpg','.jpeg','.png','.gif','.bmp',)
    name_lowercase = filename.lower()
    return name_lowercase.endswith(extensions)

sep_print()

filename = "arquivo.exe"
cyan_print(f'{is_image_file(filename) = } | {filename = }')
filename2 = "imagem.jpeg"
cyan_print(f'{is_image_file(filename2) = } | {filename2 = }')

def with_callback(x: float, y: float, callback: Callable [..., None]) -> float:
    result = x + y
    callback(f'{result = }')
    return x + y 

sep_print()

with_callback(2, 5, cyan_print)

sep_print()


def with_args(*args: str):
    cyan_print(*args)

with_args("with_args", "a", "b", "c")


sep_print()

def with_kwargs(*args:int, **kwargs:str):
    cyan_print("Args:", *args)
    cyan_print("Kwargs:", kwargs)

with_kwargs(1,2,3, nome="carlos")

sep_print()
#
#
# autores: Michel

# data: 28/06/2023
#
# importando as classes
from ex01 import calcIdade
from ex02 import calcIdade2

# criando objeto da classe calcIdade e passando a idade em anos 
# terrestres como parâmetro para o construtor da classe calcIdade
israel = calcIdade(10)
print(f"em marte Israel têm a idade de {israel.marte()} anos")

# crianco objeto da classe calcIdade2 e passando a idade em anos
# terrestres como parâmetro para o construtor da classe calcIdade2
joao = calcIdade2(16)
joao.idadeSysSolar()
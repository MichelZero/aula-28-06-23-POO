#
#
# autores: Michel

# data: 28/06/2023
#

# Implemente uma classe que seja uma calculadora para estima qual seria a 
# idade de uma pessoa em outros planetas.
# a classe deve ter um método que receba a idade da pessoa em anos terrestres
#
# para saber a idade em outros planetas, basta multiplicar a idade em anos terrestres
# por um fator de conversão.

# 1 ano mercuriano = 0.2408467 anos terrestres (365.26 / 87.97)
# 1 ano marciano = 1.8808158 anos terrestres (365.26 / 686.98)
# ex: idade em marte = idade em anos terrestres * 1.8808158

class calcIdade:
    def __init__(self, idade):
        self.idade = idade

    def mercurio(self):
        return self.idade * 0.2408467

    def venus(self):
        return self.idade * 0.61519726

    def marte(self):
        return self.idade * 1.8808158

    def jupiter(self):
        return self.idade * 11.862615

    def saturno(self):
        return self.idade * 29.447498

    def urano(self):
        return self.idade * 84.016846

    def netuno(self):
        return self.idade * 164.79132

    def plutao(self):
        return self.idade * 248.00

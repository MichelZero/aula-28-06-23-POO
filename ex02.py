#
#
# autores: Michel

# data: 28/06/2023
#

# Implemente uma classe que seja uma calculadora para estima qual seria a 
# idade de uma pessoa em outros planetas.
# a classe deve ter um método que receba a idade da pessoa em anos terrestres

class calcIdade2:
    def __init__(self, idade):
      self.idade = idade

    def idadeSysSolar(self):
      print("Idade em Mercúrio: ", self.idade * 0.2408467)
      print("Idade em Vênus: ", self.idade * 0.61519726)
      print("Idade em Marte: ", self.idade * 1.8808158)
      print("Idade em Júpiter: ", self.idade * 11.862615)
      print("Idade em Saturno: ", self.idade * 29.447498)
      print("Idade em Urano: ", self.idade * 84.016846)
      print("Idade em Netuno: ", self.idade * 164.79132)
      print("Idade em Plutão: ", self.idade * 248.00)
      
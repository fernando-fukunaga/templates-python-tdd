from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_data_nascimento_recebe_13_09_2000_idade_retorna_22(self):
        entrada = '13/09/2000' #dado que
        esperado = 23

        funcionario_teste = Funcionario('teste', entrada, 1111) #quando
        resultado = funcionario_teste.idade()

        assert resultado == esperado #então, verifica

    def test_quando_nome_recebe_lucas_carvalho_sobrenome_retorna_carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho' #Given

        funcionario_lucas = Funcionario(entrada, '01/01/2000', 2000)
        resultado = funcionario_lucas.sobrenome() #When

        assert resultado == esperado #Then

    def test_quando_decrescimo_salario_recebe_igual_ou_maior_a_100000_deve_retornar_90000(self):
        entrada = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        func_paulo = Funcionario(entrada_nome, '10/10/1998', entrada)
        func_paulo.decrescimo_salario()
        resultado = func_paulo.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcula_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        func_teste = Funcionario('teste','01/01/2000',entrada)
        resultado = func_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000000_deve_retornar_uma_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000000

            func_teste = Funcionario('teste','01/01/2000',entrada)
            resultado = func_teste.calcular_bonus()

            assert resultado
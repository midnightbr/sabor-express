from models.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    # Construtor da classe
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    # Método de retorno quando chamado apenas o objeto igual ao Flutter
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Listando os restaurantes cadastrados:')
        print(f'  {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status')
        print('-------------------------------------------------------------------------------------')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return f'✅' if self._ativo else '❌'
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avliacoes(self):
        if not self._avaliacoes:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media

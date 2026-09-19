from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_japones = Restaurante('Japa', 'Japonesa')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_japones.exibir_cardapio

if __name__ == '__main__':
    main()
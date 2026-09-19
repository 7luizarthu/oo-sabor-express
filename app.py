from modelos.restaurante import Restaurante



restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('Gui', 10)
restaurante_japones.receber_avaliacao('Lais', 8)
restaurante_japones.receber_avaliacao('Arthur', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
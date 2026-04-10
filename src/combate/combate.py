
def iniciar_combate (jugador, enemigo):
    print("\n¡Comienza el combate!\n")
    input("\nPresiona Enter para continuar...")

    while enemigo.esta_vivo() and jugador.esta_vivo():

        print("\n" + "=" * 40)
        jugador.atacar(enemigo)
        input("\nPresiona Enter para continuar...")
        if not enemigo.esta_vivo():
            break

        print("\n" + "=" * 40)
        enemigo.atacar(jugador)
        input("\nPresiona Enter para continuar...")
        if not jugador.esta_vivo():
            break

    if jugador.esta_vivo():
        print("\n" + "=" * 35)
        print(f"\n¡{jugador.nombre} ({jugador.raza}) ganó el combate!")
        print("\n" + "=" * 35)

    else:
        print("\n" + "=" * 35)
        print(f"\n¡{enemigo.nombre} ({enemigo.raza}) ganó el combate!")
        print("\n" + "=" * 35)
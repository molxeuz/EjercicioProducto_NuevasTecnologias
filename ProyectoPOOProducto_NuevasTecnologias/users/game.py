# game.py
import os
from users.user import User
from database.queries import Queries

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Game(User):
    def perform_action(self, db):
        while True:
            limpiar_consola()
            print("\n-> Realizar acciones para juegos <-\n")
            print("1. Agregar juego")
            print("2. Ver todos los juegos registrados")
            print("3. Eliminar juego de la base de datos")
            print("4. Salir")
            opcion = input("\n <- Elija una opción: ")
            if opcion == "1":
                DesarrolladoraJuego = input("\nDesarrolladora: ")
                NombreJuego = input("Nombre: ")
                ConsolaJuego = input("Consola: ")
                db.insert_game(DesarrolladoraJuego, NombreJuego, ConsolaJuego)
            elif opcion == "2":
                Queries.get_game_with_developer(db)
            elif opcion == "3":
                limpiar_consola()
                nombre_juego = input("\n <- Nombre del juego a eliminar: ")
                db.delete_game(nombre_juego)
            elif opcion == "4":
                limpiar_consola()
                break
            else:
                limpiar_consola()
                print("\n -> Opción no válida. Intente de nuevo.")
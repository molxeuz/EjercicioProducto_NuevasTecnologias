# gamer.py
import os
from users.user import User
from database.queries import Queries

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Admin(User):
    def perform_action(self, db):
        while True:
            limpiar_consola()
            print("\n-> Realizar acciones para jugadores <-\n")
            print("1. Agregar jugador")
            print("2. Ver todos los juegadores registrados")
            print("3. Eliminar juegador de la base de datos")
            print("4. Salir")
            opcion = input("\n <- Elija una opción: ")
            if opcion == "1":
                idJugador = input("\nId jugador: ")
                NombreJugador = input("Nombre jugador: ")
                Especialidad = input("Especialidad: ")
                ConsolaFavorita = input("Consola favorita: ")
                db.insert_gamer(idJugador, NombreJugador, Especialidad, ConsolaFavorita)
            elif opcion == "2":
                Queries.get_sorted_gamers(db)
            elif opcion == "3":
                limpiar_consola()
                nombre_jugador = input("\n <- Nombre del juego a eliminar: ")
                db.delete_gamer(nombre_jugador)
            elif opcion == "4":
                limpiar_consola()
                break
            else:
                limpiar_consola()
                print("\n -> Opción no válida. Intente de nuevo.")
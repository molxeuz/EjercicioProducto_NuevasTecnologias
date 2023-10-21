#queries.py
import sqlite3, os

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Queries:
    @staticmethod
    def get_sorted_gamers(db):
        try:
            limpiar_consola()
            print("\n-> Ver jugadores registrados <-\n")
            db.cursor.execute("SELECT * FROM jugadores ORDER BY NombreJugador")
            result = db.cursor.fetchall()
            for row in result:
                print(row)
            input("\n enter para continuar ")
        except sqlite3.Error as e:
            print(f"Error al obtener jugadores: {e}")
    @staticmethod
    def get_game_with_developer(db):
        try:
            limpiar_consola()
            print("\n-> Ver juegos registrados <-\n")
            db.cursor.execute("SELECT * FROM juegos ORDER BY NombreJuego")
            result = db.cursor.fetchall()
            for row in result:
                print(row)
            input("\n enter para continuar ")
        except sqlite3.Error as e:
            print(f"Error al obtener nombre del juego: {e}")

            
#connection.py
import sqlite3, os

limpiar_consola = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class DataBase:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def connect(self):
        self.connection = sqlite3.connect('playzone.db')
        self.cursor = self.connection.cursor()
        limpiar_consola()
        print("\n -> Conexión a la base de datos exitosa <-")
        self.create_tables()
    def close(self):
        if self.connection:
            self.connection.close()
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jugadores (
                idJugador INTEGER PRIMARY KEY,
                NombreJugador TEXT NOT NULL,
                Especialidad TEXT NOT NULL,
                ConsolaFavorita TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS juegos (
                DesarrolladoraJuego TEXT NOT NULL,
                NombreJuego TEXT NOT NULL,
                ConsolaJuego INTEGER NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    def authenticate(self, username, password):
        try:
            self.cursor.execute("SELECT user_type FROM usuarios WHERE username = ? AND password = ?", (username, password))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"\n <- Error al autenticar al usuario: {e}")
            return None

    def user_exists(self, username):
        try:
            self.cursor.execute("SELECT username FROM usuarios WHERE username = ?", (username,))
            result = self.cursor.fetchone()
            return result is not None
        except sqlite3.Error as e:
            print(f"\n <- Error al verificar si el usuario existe: {e}")
            return False
    def insert_gamer(self, idJugador, NombreJugador, Especialidad, ConsolaFavorita):
        try:
            self.cursor.execute("INSERT INTO jugadores (idJugador, NombreJugador, Especialidad, ConsolaFavorita) VALUES (?, ?, ?, ?)", (idJugador, NombreJugador, Especialidad, ConsolaFavorita))
            self.connection.commit()
            print(f"\n -> Jugador {NombreJugador} agregado a la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar el jugador: {e}")
            
    def insert_usuario(self, username, password, user_type):
        try:
            self.cursor.execute("INSERT INTO usuarios (username, password, user_type) VALUES (?, ?, ?)", (username, password, user_type))
            self.connection.commit()
            print(f"\n -> Usuario {username} registrado en la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar usuario: {e}")
    def insert_game(self, DesarrolladoraJuego, NombreJuego, ConsolaJuego):
        try:
            self.cursor.execute("INSERT INTO juegos (DesarrolladoraJuego, NombreJuego, ConsolaJuego) VALUES (?, ?, ?)", (DesarrolladoraJuego, NombreJuego, ConsolaJuego))
            self.connection.commit()
            print(f"\n -> Juego {NombreJuego} agregado a la base de datos <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al insertar el juego: {e}")
    def delete_game(self, NombreJuego):
        try:
            self.cursor.execute("DELETE FROM juegos WHERE NombreJuego = ?", (NombreJuego,))
            self.connection.commit()
            print(f"\n -> Juego {NombreJuego} eliminado de la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al eliminar el juego: {e}")
    def delete_gamer(self, NombreJugador):
        try:
            self.cursor.execute("DELETE FROM jugadores WHERE NombreJugador = ?", (NombreJugador,))
            self.connection.commit()
            print(f"\n -> Jugador {NombreJugador} eliminado de la base de datos. <-")
        except sqlite3.Error as e:
            print(f"\n <- Error al eliminar el jugador: {e}")
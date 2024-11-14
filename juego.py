from pymongo import MongoClient


client = MongoClient("localhost",27017)
db = client["local"]


def insertar_datos_iniciales():
    
    jugadores = db["jugadores"]
    jugadores.insert_many([
        {
            "_id": "jugador_001",
            "nombre": "Karla Martínez",
            "nickname": "ShadowQueen",
            "ranking": "Platino",
            "equipo": "NightRaiders",
            "estadisticas": {
                "partidas_jugadas": 10,
                "partidas_ganadas": 7,
                "eliminaciones_promedio": 12.5
            }
        },
        {
            "_id": "jugador_002",
            "nombre": "Juan Pérez",
            "nickname": "StormRider",
            "ranking": "Diamante",
            "equipo": "NightRaiders",
            "estadisticas": {
                "partidas_jugadas": 15,
                "partidas_ganadas": 10,
                "eliminaciones_promedio": 14.2
            }
        }
    ])

    
    equipos = db["equipos"]
    equipos.insert_one({
        "_id": "equipo_001",
        "nombre": "NightRaiders",
        "jugadores": ["jugador_001", "jugador_002"],
        "entrenador": "Luis Pérez"
    })

    
    arbitros = db["arbitros"]
    arbitros.insert_one({
        "_id": "arbitro_001",
        "nombre": "Andrea López",
        "experiencia": 5,
        "especialidad": "Valorant"
    })

    
    encuentros = db["encuentros"]
    encuentros.insert_one({
        "_id": "encuentro_001",
        "equipo_1": "NightRaiders",
        "equipo_2": "SkyBreakers",
        "fecha": "2024-11-12",
        "mapas": ["Ascent", "Bind"],
        "resultado": {
            "ganador": "NightRaiders",
            "detalles": {
                "mapa_1": "NightRaiders",
                "mapa_2": "NightRaiders"
            }
        },
        "arbitro": "arbitro_001"
    })

    
    resultados = db["resultados"]
    resultados.insert_one({
        "_id": "posicion_001",
        "equipo": "NightRaiders",
        "puntos": 3,
        "partidas_jugadas": 1,
        "partidas_ganadas": 1,
        "diferencia_rondas": 5
    })


def generar_informes():
    
    print("\nTabla de Posiciones:")
    for resultado in db["resultados"].find().sort("puntos", -1):
        print(f"Equipo: {resultado['equipo']}, Puntos: {resultado['puntos']}")

    
    print("\nResultados de Encuentros:")
    for encuentro in db["encuentros"].find():
        print(f"Encuentro {encuentro['_id']} - {encuentro['equipo_1']} vs {encuentro['equipo_2']}")
        print(f"Ganador: {encuentro['resultado']['ganador']}")

    
    print("\nEstadísticas Individuales:")
    for jugador in db["jugadores"].find():
        print(f"Jugador: {jugador['nickname']}, Partidas Ganadas: {jugador['estadisticas']['partidas_ganadas']}, "
              f"Promedio de Eliminaciones: {jugador['estadisticas']['eliminaciones_promedio']}")

if __name__ == "__main__":
    print("Iniciando el proyecto de gestión del torneo...")
    insertar_datos_iniciales()  
    generar_informes()  

class Punto:
    def __init__(self):
        self.tipo
        self.coordenada = {
            "x": 0,
            "y": 0
        }

    def retornarPunto(self):
        return {"tipo": self.tipo,
                "coordenada":{
                    "x": int(self.coordenada["x"]),
                    "y": int(self.coordenada["y"])
                }}
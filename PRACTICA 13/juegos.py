info_tienda = ("Game Start!", "2007")
inventario = {
    "zelda" : {"Precio": 2000, "Stock": 15},
    "PvZ" : {"Precio":200, "Stock": 40},
    "Resident Evil" : {"Precio":1000, "Stock": 24}
    }

print (f"El precio de mi segundo juego es: {inventario ["PvZ"]["Precio"]}")
inventario ["zelda"]["Stock"]=14
print (inventario) 
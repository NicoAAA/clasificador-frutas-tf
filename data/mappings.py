# data/mappings.py

# El "cerebro" de la API. Mapea la etiqueta en INGLÉS de AWS a TU categoría en ESPAÑOL.
MAPA_CLASIFICACION = {
    # Verduras (muy fuertes en la Sabana)
    "potato": "Verduras",
    "onion": "Verduras",
    "scallion": "Verduras",        # Cebolla larga
    "green onion": "Verduras",    # Cebolla larga
    "carrot": "Verduras",
    "lettuce": "Verduras",
    "cabbage": "Verduras",
    "broccoli": "Verduras",
    "cauliflower": "Verduras",
    "spinach": "Verduras",
    "swiss chard": "Verduras",
    "leafy green vegetable": "Verduras",
    "corn": "Verduras",
    "corn on the cob": "Verduras",
    "vegetable": "Verduras",

    # Frutas (fresa es clave en Cundinamarca)
    "apple": "Frutas",
    "strawberry": "Frutas",
    "blackberry": "Frutas",
    "cape gooseberry": "Frutas",  # Uchuva
    "tamarillo": "Frutas",        # Tomate de árbol
    "fruit": "Frutas",

    # Granos y Legumbres
    "pea": "Granos y Legumbres",          # Arveja
    "fava bean": "Granos y Legumbres",    # Haba
    "broad bean": "Granos y Legumbres",   # Haba
    "bean": "Granos y Legumbres",

    # Lácteos y Derivados (la Sabana es una cuenca lechera)
    "milk": "Lácteos y Derivados",
    "cheese": "Lácteos y Derivados",
    "yogurt": "Lácteos y Derivados",

    # Carnes Frescas
    "beef": "Carnes Frescas",
    "meat": "Carnes Frescas",
    
    # Huevos y Derivados
    "egg": "Huevos y Derivados",
    
    # Panadería y Repostería
    "bread": "Panadería y Repostería",
    "pastry": "Panadería y Repostería",

    # Miel y Derivados Apícolas
    "honey": "Miel y Derivados Apícolas",
    "honeycomb": "Miel y Derivados Apícolas",

    # Plantas y Flores (Cundinamarca es potencia exportadora)
    "flower": "Plantas y Flores",
    "rose": "Plantas y Flores",
    "carnation": "Plantas y Flores",
    "plant": "Plantas y Flores"
}

# Diccionario de traducción para los nombres de productos.
DICCIONARIO_TRADUCCION_ES = {
    # Verduras
    "Potato": "Papa", "Onion": "Cebolla Cabezona", "Scallion": "Cebolla Larga",
    "Green Onion": "Cebolla Larga", "Carrot": "Zanahoria", "Lettuce": "Lechuga",
    "Cabbage": "Repollo", "Broccoli": "Brócoli", "Cauliflower": "Coliflor",
    "Spinach": "Espinaca", "Swiss Chard": "Acelga", "Leafy Green Vegetable": "Vegetal de Hoja Verde",
    "Corn": "Maíz", "Corn on the Cob": "Mazorca",
    
    # Frutas
    "Strawberry": "Fresa", "Blackberry": "Mora", "Cape Gooseberry": "Uchuva",
    "Tamarillo": "Tomate de Árbol", "Apple": "Manzana", 
    
    # Granos y Legumbres
    "Pea": "Arveja", "Fava Bean": "Haba", "Broad Bean": "Haba",
    
    # Lácteos
    "Milk": "Leche", "Cheese": "Queso", "Yogurt": "Yogur",

    # Carnes
    "Beef": "Carne de Res", "Meat": "Carne",
    
    # Otros
    "Egg": "Huevo", "Bread": "Pan", "Pastry": "Producto de Pastelería",
    "Honey": "Miel", "Honeycomb": "Panal de Miel",

    # Flores
    "Flower": "Flor", "Rose": "Rosa", "Carnation": "Clavel", "Plant": "Planta"
}
# Etiquetas genéricas que queremos ignorar en la clasificación principal.
ETIQUETAS_GENERICAS_A_IGNORAR = {
    "Food", "Produce", "Plant", "Vegetable", "Fruit", "Dish", "Meal"
}
# data/mappings.py

# ==============================================================================
# DICCIONARIO 1: MAPA DE CATEGORÍAS
# Mapea la etiqueta en INGLÉS (minúscula) de AWS a TU categoría en ESPAÑOL.
# ==============================================================================
MAPA_CLASIFICACION = {
    # --- Verduras ---
    "potato": "Verduras",
    "onion": "Verduras",
    "scallion": "Verduras",
    "green onion": "Verduras",
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
    "tomato": "Verduras",
    "cucumber": "Verduras",
    "bell pepper": "Verduras",
    "pepper": "Verduras",
    "garlic": "Verduras",
    "zucchini": "Verduras",
    "eggplant": "Verduras",
    "mushroom": "Verduras",
    "avocado": "Verduras", # Frecuentemente clasificado como verdura en cocina

    # --- Frutas ---
    "strawberry": "Frutas",
    "blackberry": "Frutas",
    "cape gooseberry": "Frutas",
    "tamarillo": "Frutas",
    "fruit": "Frutas",
    "apple": "Frutas",
    "banana": "Frutas",
    "orange": "Frutas",
    "lemon": "Frutas",
    "lime": "Frutas",
    "grape": "Frutas",
    "pineapple": "Frutas",
    "mango": "Frutas",
    "watermelon": "Frutas",
    "melon": "Frutas",
    "peach": "Frutas",
    "pear": "Frutas",

    # --- Granos y Legumbres ---
    "pea": "Granos y Legumbres",
    "fava bean": "Granos y Legumbres",
    "broad bean": "Granos y Legumbres",
    "bean": "Granos y Legumbres",
    "rice": "Granos y Legumbres",
    "lentil": "Granos y Legumbres",

    # --- Lácteos y Derivados ---
    "milk": "Lácteos y Derivados",
    "cheese": "Lácteos y Derivados",
    "yogurt": "Lácteos y Derivados",
    "butter": "Lácteos y Derivados",
    "cream": "Lácteos y Derivados",

    # --- Carnes Frescas ---
    "beef": "Carnes Frescas",
    "meat": "Carnes Frescas",
    "pork": "Carnes Frescas",
    "chicken": "Carnes Frescas",
    "sausage": "Carnes Frescas",
    "bacon": "Carnes Frescas",
    "ham": "Carnes Frescas",
    "steak": "Carnes Frescas",
    "lamb": "Carnes Frescas",
    
    # --- Pescados y Mariscos (Nueva Categoría) ---
    "fish": "Pescados y Mariscos",
    "salmon": "Pescados y Mariscos",
    "tuna": "Pescados y Mariscos",
    "shrimp": "Pescados y Mariscos",
    "seafood": "Pescados y Mariscos",
    
    # --- Huevos y Derivados ---
    "egg": "Huevos y Derivados",
    
    # --- Panadería y Repostería ---
    "bread": "Panadería y Repostería",
    "pastry": "Panadería y Repostería",
    "cake": "Panadería y Repostería",
    "cookie": "Panadería y Repostería",
    "donut": "Panadería y Repostería",
    "croissant": "Panadería y Repostería",
    
    # --- Miel y Derivados Apícolas ---
    "honey": "Miel y Derivados Apícolas",
    "honeycomb": "Miel y Derivados Apícolas",

    # --- Plantas y Flores ---
    "flower": "Plantas y Flores",
    "rose": "Plantas y Flores",
    "carnation": "Plantas y Flores",
    "plant": "Plantas y Flores"
}


# ==============================================================================
# DICCIONARIO 2: TRADUCTOR DE NOMBRES
# Mapea la etiqueta en INGLÉS (Mayúscula Inicial) a TU nombre de producto en ESPAÑOL.
# ==============================================================================
DICCIONARIO_TRADUCCION_ES = {
    # --- Verduras ---
    "Potato": "Papa", "Onion": "Cebolla Cabezona", "Scallion": "Cebolla Larga",
    "Green Onion": "Cebolla Larga", "Carrot": "Zanahoria", "Lettuce": "Lechuga",
    "Cabbage": "Repollo", "Broccoli": "Brócoli", "Cauliflower": "Coliflor",
    "Spinach": "Espinaca", "Swiss Chard": "Acelga", "Leafy Green Vegetable": "Vegetal de Hoja Verde",
    "Corn": "Maíz", "Corn on the Cob": "Mazorca", "Vegetable": "Verdura",
    "Tomato": "Tomate", "Cucumber": "Pepino", "Bell Pepper": "Pimentón",
    "Pepper": "Pimiento", "Garlic": "Ajo", "Zucchini": "Calabacín",
    "Eggplant": "Berenjena", "Mushroom": "Champiñón", "Avocado": "Aguacate",

    # --- Frutas ---
    "Strawberry": "Fresa", "Blackberry": "Mora", "Cape Gooseberry": "Uchuva",
    "Tamarillo": "Tomate de Árbol", "Fruit": "Fruta", "Apple": "Manzana",
    "Banana": "Banano", "Orange": "Naranja", "Lemon": "Limón",
    "Lime": "Lima", "Grape": "Uvas", "Pineapple": "Piña", "Mango": "Mango",
    "Watermelon": "Sandía", "Melon": "Melón", "Peach": "Durazno", "Pear": "Pera",
    
    # --- Granos y Legumbres ---
    "Pea": "Arveja", "Fava Bean": "Haba", "Broad Bean": "Haba", "Bean": "Fríjol",
    "Rice": "Arroz", "Lentil": "Lenteja",
    
    # --- Lácteos y Derivados ---
    "Milk": "Leche", "Cheese": "Queso", "Yogurt": "Yogur",
    "Butter": "Mantequilla", "Cream": "Crema de Leche",

    # --- Carnes Frescas ---
    "Beef": "Carne de Res", "Meat": "Carne", "Pork": "Carne de Cerdo",
    "Chicken": "Pollo", "Sausage": "Salchicha", "Bacon": "Tocineta",
    "Ham": "Jamón", "Steak": "Bistec", "Lamb": "Cordero",
    
    # --- Pescados y Mariscos ---
    "Fish": "Pescado", "Salmon": "Salmón", "Tuna": "Atún",
    "Shrimp": "Camarones", "Seafood": "Mariscos",
    
    # --- Otros ---
    "Egg": "Huevo", "Bread": "Pan", "Pastry": "Producto de Pastelería",
    "Cake": "Torta", "Cookie": "Galleta", "Donut": "Dona", "Croissant": "Croissant",
    "Honey": "Miel", "Honeycomb": "Panal de Miel",

    # --- Flores ---
    "Flower": "Flor", "Rose": "Rosa", "Carnation": "Clavel", "Plant": "Planta"
}


# ==============================================================================
# DICCIONARIO 3: MAPA DE UNIDADES DE MEDIDA
# Mapea la etiqueta en INGLÉS (minúscula) a la unidad de medida sugerida.
# ==============================================================================
MAPA_UNIDADES = {
    # --- Verduras y Frutas ---
    "potato": "kg", "onion": "kg", "scallion": "kg", "green onion": "kg",
    "carrot": "kg", "lettuce": "unidad", "cabbage": "unidad", "broccoli": "unidad",
    "cauliflower": "unidad", "spinach": "kg", "swiss chard": "kg",
    "corn": "unidad", "corn on the cob": "unidad", "strawberry": "kg",
    "blackberry": "kg", "cape gooseberry": "kg", "tamarillo": "kg",
    "vegetable": "kg", "fruit": "kg", "tomato": "kg", "cucumber": "unidad",
    "bell pepper": "unidad", "pepper": "unidad", "garlic": "unidad",
    "zucchini": "unidad", "eggplant": "unidad", "mushroom": "kg", "avocado": "kg",
    "apple": "kg", "banana": "kg", "orange": "kg", "lemon": "kg",
    "lime": "kg", "grape": "kg", "pineapple": "unidad", "mango": "kg",
    "watermelon": "unidad", "melon": "unidad", "peach": "kg", "pear": "kg",

    # --- Granos y Legumbres ---
    "pea": "kg", "fava bean": "kg", "broad bean": "kg", "bean": "kg",
    "rice": "kg", "lentil": "kg",

    # --- Lácteos (por litro o unidad) ---
    "milk": "l", "cheese": "kg", "yogurt": "unidad", "butter": "unidad", "cream": "unidad",

    # --- Carnes, Pescados y Mariscos (por peso) ---
    "beef": "kg", "meat": "kg", "pork": "kg", "chicken": "kg", "sausage": "kg",
    "bacon": "kg", "ham": "kg", "steak": "kg", "lamb": "kg", "fish": "kg",
    "salmon": "kg", "tuna": "kg", "shrimp": "kg", "seafood": "kg",
    
    # --- Otros (por unidad) ---
    "egg": "unidad", "bread": "unidad", "pastry": "unidad", "cake": "unidad",
    "cookie": "unidad", "donut": "unidad", "croissant": "unidad",
    "honey": "unidad", "honeycomb": "unidad",

    # --- Plantas y Flores (por unidad) ---
    "flower": "unidad", "rose": "unidad", "carnation": "unidad", "plant": "unidad"
}
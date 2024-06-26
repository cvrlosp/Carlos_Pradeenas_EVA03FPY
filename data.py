from pathlib import Path

home = Path(__file__).parent.parent
ruta_j = Path(home/'base.json')
ruta_c = Path(home/'mandarina.csv')
menup = ['Ver pinturas', 
         'Buscar pinturas', 
         'Agregar pinturas', 
         'Eliminar pinturas',
         'Exportar pinturas', 
         'Salir']
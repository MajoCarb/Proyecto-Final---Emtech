usuario_registrado = ('admin', 'lifestore123')
intentos=3
login_exitoso = False
#print(usuario_registrado[0])

def open_lifestore(user):
    from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

    print("Hola, bienvenido ",user,'\n')

    #lista inicializada en ceros para guardar la sumatoria de las ventas de cada producto 
    total_ventas = [0]*len(lifestore_products)
    #print(mayores_ventas)
    ventasXproducto = {}
    

    print(f"Hay {len(lifestore_products)} productos")
    print(f"Hay {len(lifestore_sales)} ventas")
    print(f"Hay {len(lifestore_searches)} busquedas\n")

    

    """
   ----------- 5 PRODUCTOS CON MAYORES VENTAS ----------------

    """

    id_productos_list = list(range(1,len(lifestore_products)+1)) #lista con los ID de todos los productos

    for i in range(len(lifestore_sales)):
        total_ventas[lifestore_sales[i][1]-1]+=1 #sumatoria de las ventas de cada producto y se ordenarán de acuerdo al ID

    #en este diccionario se guardarán el id_producto como clave y su numero de ventas como valor
    ventasXproducto = dict(zip(id_productos_list, total_ventas))

    ventasXproducto_asc = sorted(ventasXproducto.items(),key=lambda x: x[1]) #devuelve una lista con ventasXproduto de menor a mayor
    ventasXproducto_ord = sorted(ventasXproducto.items(),key=lambda x: x[1], reverse=True) #devuelve una lista con ventasXproduto de mayor a menor
    mayores_ventas = ventasXproducto_ord[:5] #5 productos con mayores ventas

    
    print("         *Los 5 productos con mayores ventas son: *\n")
    for producto in mayores_ventas:
        print('Con ',producto[1],' ventas: ',lifestore_products[producto[0]-1][1],'\n')

    """
   ----------- 10 PRODUCTOS CON MAYORES BÚSQUEDAS ----------------
    El proceso es igual al anterior, pero trabajando con lifestore_searches e imprimiendo 10 elementos
    """

    total_busquedas = [0]*len(lifestore_products)
    for i in range(len(lifestore_searches)):
        total_busquedas[lifestore_searches[i][1]-1]+=1
    
    productoXbusqueda = dict(zip(id_productos_list, total_busquedas))
    #print(productoXbusqueda)
    productoXbusqueda_asc = sorted(productoXbusqueda.items(),key=lambda x: x[1])
    mayores_busquedas = sorted(productoXbusqueda.items(),key=lambda x: x[1], reverse=True)

    mayores_busquedas = mayores_busquedas[:10]

    print("\n         *Los 10 productos con mayores búsquedas son: *\n")
    for producto in mayores_busquedas:
        print("Con",producto[1],' busquedas: ',lifestore_products[producto[0]-1][1],'\n')

    """
   ----------- 5 PRODUCTOS CON MENORES VENTAS POR CATEGORÍA ----------------
    """

    print("\n         *Los 5 productos con menores ventas por categoría son: *\n")

    categories_list=[producto[3] for producto in lifestore_products]

    #ya existía esta lista, pero se manejará como diccionario
    ventasXproducto_asc = dict(ventasXproducto_asc)

    productoXcategoria = (dict(zip(id_productos_list,categories_list))) # {id_producto: 'categoria', }

    categoriasXventas = {**ventasXproducto_asc , **productoXcategoria}
    #de esta manera combino los dos diccionarios anteriores , donde: {id_producto: 'categoria', } pero ordenados por la cantidad de ventas de cada producto de forma ascendente

    productsXcatXventa = {} #{'categoria': [lista de productos en esa categoria ordenados por sus ventas de menor a mayor]}
 
    for elemento in categoriasXventas.items():
        cat = elemento[1]
        if cat not in productsXcatXventa.keys():
            productsXcatXventa[cat] = []
        productsXcatXventa[cat].append(elemento[0])
    
    for categoria, value in productsXcatXventa.items():
        print(categoria, "con menores ventas: ")
        print("\n")
        i = 0
        for element in value:
            if i > 4:
                continue
            else:            
                print('Con ',ventasXproducto[element], ' ventas: ',lifestore_products[element-1][1])
                i+=1
        print("\n")

        """
   ----------- 10 PRODUCTOS CON MENORES BÚSQUEDAS POR CATEGORÍA ----------------
   El proceso es igual al anterior, pero trabajando con lifestore_searches e imprimiendo 10 elementos
    """
    print("\n         *Los 10 productos con menores búsquedas por categoría son: *\n")

    productoXbusqueda_asc = dict(productoXbusqueda_asc)
    categoriasXbusquedas = {**productoXbusqueda_asc , **productoXcategoria}

    productsXcatXbusqueda = {}
     
    for elemento in categoriasXbusquedas.items():
        cat = elemento[1]
        if cat not in productsXcatXbusqueda.keys():
            productsXcatXbusqueda[cat] = []
        productsXcatXbusqueda[cat].append(elemento[0])
    
    for categoria, value in productsXcatXbusqueda.items():
        print(categoria, "con menores busquedas: ")
        print("\n")
        i = 0
        for element in value:
            if i > 10:
                continue
            else:            
                print('Con ',productoXbusqueda[element], ' búsquedas: ',lifestore_products[element-1][1])
                #print(element,i)
                i+=1
        print("\n")

    """
   -----------  PRODUCTOS POR RESEÑA EN EL SERVICIO ----------------
   Este código sirve para obtener dos listados: uno con las mejores opiniones y otro con las peores

    """
    sold_products={}
    productoXresena={}

    #se hace uso del diccionario ya existente de ventasXproducto
    for producto in ventasXproducto.items():
        if producto[1]!=0:
            sold_products[producto[0]]=producto[1]

    #obtener la calificación promedio de cada producto
    for producto in sold_products.items():
        ventas = producto[1]
        id = producto[0]
        review = 0

        for i in range(len(lifestore_sales)):
            if id == lifestore_sales[i][1]:
                review+= lifestore_sales[i][2]

        promedio = round(review/ventas,2)
        productoXresena[id]=promedio


    productoXresena_ord = sorted(productoXresena.items(),key=lambda x: x[1], reverse=True)
    best_products = dict(productoXresena_ord[:18]) #tomar solo los de calificacion = 5, que son los primero 18

    #-------------Determinar los 5 mejores de acuerdo a sus ventas, todos tienen 5 estrellas
    temp_best= list(best_products.keys())
    sold_products_ord = sorted(sold_products.items(),key=lambda x: x[1], reverse=True)
    sold_products_ord = dict(sold_products_ord)
    id_mas_ventas= [key[0] for key in sold_products_ord.items()]

    mejoresXventas =[id for id in id_mas_ventas if id in temp_best]

    mejoresXventas = mejoresXventas[:5]

    top_best5 = productoXresena_ord[:5]

    print("\n         *Los 5 productos con mejores reseñas son: *\n")
    i = 1
    for producto in mejoresXventas:
        # print(producto)
        print(f"Puesto {i}-> ID: {producto}, que es el {lifestore_products[producto-1][1]} con {sold_products[producto]} ventas y una calificación de {best_products[producto]}")
        i+=1

    top_worse5 = sorted(productoXresena_ord[len(productoXresena_ord)-5:],key=lambda x: x[1])
    #print(top_worse5)

    productoXresena_ord = dict(productoXresena_ord)
    print("\n")
    print("\n         *Los 5 productos con peores reseñas son: *\n")
    
    i = 1
    for producto in top_worse5:
        # print(producto[0])
        print(f"Puesto {i}-> ID: {producto[0]}, que es el {lifestore_products[producto[0]-1][1]} con {sold_products[producto[0]]} ventas y una calificación de {productoXresena_ord[producto[0]]}")
        i+=1
    
    """
    ----------- TOATAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES.
    TOTAL ANUAL Y MESES CON MÁS VENTAS AL AÑO ----------------
    """
    print("\n         *Análisis de ingresos y ventas por mes: *\n")

    #id de cada venta y la fecha en que ocurrió siempre y cuando no sea una devolucion
    from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

    ventaXfecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]

    meses = {"01": ["Enero"], '02':['Febrero'], '03':['Marzo'],'04':['Abril'],'05':['Mayo'],'06':['Junio'],'07':['Julio'],'08':['Agosto'],'09':['Septiembre'], '10':['Octubre'], '11':['Noviembre'],'12': ['Diciembre']}

    ventasXmes={}

    for venta in ventaXfecha:
        id = venta[0]
        _, mes, _   = venta[1].split('/')
        if mes not in ventasXmes.keys():
            ventasXmes[mes]=[]
        ventasXmes[mes].append(id)

    ingresosXmes={}
    for mes in ventasXmes.keys():
        lista_mes = ventasXmes[mes]
        gananciaXmes = 0
        for venta in lista_mes:
            #print(venta)
            id_producto = lifestore_sales[venta-1][1]
            precio=lifestore_products[id_producto-1][2]
            #print(f"{precio} de {id_producto}")
            gananciaXmes += precio
        if mes in meses.keys():
            meses[mes].append(gananciaXmes)
            meses[mes].append(len(lista_mes))
            #print(meses[mes])
            
    meses.pop('09')
    meses.pop('10')
    meses.pop('11')
    meses.pop('12')

    ventasXmes_list = sorted([ [meses[mes][1],mes ] for mes in meses.keys() ], reverse=True)

    total_anual=0
    for venta in ventasXmes_list:
        print(f"En {meses[(venta[1])][0]} se obtuvieron ${meses[(venta[1])][1]} en ingresos con {meses[(venta[1])][2]} artículos vendidos")
        total_anual+= int(meses[(venta[1])][1])

    print(f'Total anual de ingresos: ${total_anual}')

"""
LOGIN: Aquí se determina si se accede o no al análisis

"""



while not login_exitoso != False and intentos>0:
    user = input('Ingresa tu usuario: \n')
    password = input('Ingresa tu contraseña: ')
    if user  == usuario_registrado[0] and password == usuario_registrado[1]:
        open_lifestore(user)
        login_exitoso = True
        
    else:
        intentos-=1
        
        if intentos == 0:
            print("ACCESO DENEGADO")
        else:
            print(f"\nDatos incorrectos. {intentos} intentos restantes")
    

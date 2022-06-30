from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientesSerializer, ArticulosSerializer, VendedoresSerializer, FacturacionSerializer
from .models import Clientes, Articulos, Vendedores, Facturacion

# Listar todos los clientes
@api_view(['GET', 'POST'])
def ClienteList(request):
    # List
    if request.method == 'GET':
        # Queryset
        clientes = Clientes.objects.all()
        # Serializer
        serializer = ClientesSerializer(clientes,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar un solo cliente
@api_view(['GET','PUT', 'DELETE'])
def ClienteRetrieve(request, pk = None):
    # Queryset
    cliente = Clientes.objects.filter(id = pk).first()
    
    # Validacion
    if cliente:
        
        # Retrieve
        if request.method == 'GET':
            # Serializer
            serializer = ClientesSerializer(cliente)
            return Response(serializer.data)

        # Update
        elif request.method == 'PUT':
            # Serializer   
            serializer = ClientesSerializer(cliente, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        # Delete
        elif request.method == 'DELETE':
            cliente.delete()
            return Response({'message':'Cliente eliminado correctamente'}, )

    return Response({'message':'No se ha encontrado un cliente'})

# Listar todos los articulos
@api_view(['GET', 'POST'])
def ArticulosList(request):
    # List
    if request.method == 'GET':
        # Queryset
        articulo = Articulos.objects.all()
        # Serializer
        serializer = ArticulosSerializer(articulo,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        serializer = ArticulosSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar un solo articulo
@api_view(['GET','PUT', 'DELETE'])
def ArticulosRetrieve(request, pk = None):
    
    # Queryset
    articulo = Articulos.objects.filter(id = pk).first()
    
    # Validacion
    if articulo:
        
        # Retrieve
        if request.method == 'GET':
            # Serializer
            serializer = ArticulosSerializer(articulo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            # Serializer   
            serializer = ArticulosSerializer(articulo, data=request.data,)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            articulo.delete()
            return Response({'message':'Articulo eliminado correctamente'}, status=status.HTTP_200_OK )

    return Response({'message':'No se ha encontrado un articulo'}, status=status.HTTP_400_BAD_REQUEST)

# Listar todos los vendedores
@api_view(['GET', 'POST'])
def VendedoresList(request):
    # List
    if request.method == 'GET':
        # Queryset
        vendedore = Vendedores.objects.all()
        # Serializer
        serializer = VendedoresSerializer(vendedore,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        serializer = VendedoresSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar un solo vendedor
@api_view(['GET','PUT', 'DELETE'])
def VendedoresRetrieve(request, pk = None):
    # Queryset
    vendedore = Vendedores.objects.filter(id = pk).first()
    
    # Validacion
    if vendedore:
        
        # Retrieve
        if request.method == 'GET':
            # Serializer
            serializer = VendedoresSerializer(vendedore)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            # Serializer   
            serializer = VendedoresSerializer(vendedore, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            vendedore.delete()
            return Response({'message':'Cliente eliminado correctamente'}, status=status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un cliente'}, status=status.HTTP_400_BAD_REQUEST)

# Listar todas las facturaciones
@api_view(['GET', 'POST'])
def FacturacionList(request):
    # List
    if request.method == 'GET':
        # Queryset
        facturacion = Facturacion.objects.all()
        # Serializer
        serializer = FacturacionSerializer(facturacion,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        serializer = FacturacionSerializer(data=request.data)
        
        # Validacion
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar una sola facturacion
@api_view(['GET','PUT', 'DELETE'])
def FacturacionRetrieve(request, pk = None):
    # Queryset
    facturacion = Facturacion.objects.filter(id = pk).first()
    
    # Validacion
    if facturacion:
        
        # Retrieve
        if request.method == 'GET':
            # Serializer
            serializer = FacturacionSerializer(facturacion)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            # Serializer   
            serializer = FacturacionSerializer(facturacion, data=request.data)
            
            # Validacion
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            facturacion.delete()
            return Response({'message':'Cliente eliminado correctamente'}, status=status.HTTP_200_OK )

    return Response({'message':'No se ha encontrado un cliente'}, status=status.HTTP_400_BAD_REQUEST)
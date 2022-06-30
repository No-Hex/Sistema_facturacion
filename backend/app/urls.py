from django.urls import path
from .views import ClienteList, ClienteRetrieve, ArticulosList, ArticulosRetrieve, FacturacionList, FacturacionRetrieve,  VendedoresList, VendedoresRetrieve, FacturacionList, FacturacionRetrieve
urlpatterns = [
    # Clientes Endpoints
    path('clientes', ClienteList),
    path('clientes/<int:pk>/', ClienteRetrieve),
    # Articulos Endpoints
    path('articulos', ArticulosList),
    path('articulos/<int:pk>/', ArticulosRetrieve),
    # Vendedores Endpoints
    path('vendedores', VendedoresList),
    path('vendedores/<int:pk>/', VendedoresRetrieve),
    # Facturacion Endpoints
    path('facturacion', FacturacionList),
    path('facturacion/<int:pk>/', FacturacionRetrieve)
]
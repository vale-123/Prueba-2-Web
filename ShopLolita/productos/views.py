from django.contrib import messages
from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    print("Estamos en la vista")
    context={}
    return render(request,'productos/index.html',context)

def listar(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar.html',context)






@permission_required('productos.add_producto')
def administrar(request):
    print("Estamos en la vista listar")

    context={}
    return render(request,'productos/administrar.html',context)

def Ropa(request):
    print("Estamos en la vista Ropa")
    data = {
        'productos': Producto.objects.filter(tipo='Ropa')
    }
    return render(request, 'productos/Ropa.html', data)

def Vestidos(request):
    print("Estamos en la vista Vestidos")
    data = {
        'productos': Producto.objects.filter(tipo='Vestidos')
    }
    return render(request,'productos/Vestidos.html',data)

def listar_productos(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar_productos.html',context)


def Calzado(request):
    print("Estamos en la vista Calzado")
    data = {
        'productos' :Producto.objects.filter(tipo='Calzado')
    }
    return render(request,'productos/Calzado.html' , data)

def Accesorios(request):
    print("Estamos en la vista Accesorios")
    data = {
        'productos' :Producto.objects.filter(tipo='Accesorios')
    }
    return render(request,'productos/Calzado.html' , data)

def mostrar_productos(request):
    print("Estamos en la vista mostrar productos")
    lista = Producto.objects.all()
    context={'listado':lista}
    return render(request,'productos/listar_productos.html',context)

def boton_buscar(request):
    print("Estamos en la vista boton buscar")
    context={}
    return render(request,'productos/boton_buscar.html',context)

def buscar_por_id(request):
    print("hola  estoy en buscar_por_id...")
    if request.method == 'POST':
       mi_nu = request.POST['numero']

       if mi_nu != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(numero=mi_nu)
               if producto is not None:
                   print("Producto=", producto)
                   context={'producto':producto}
                   return render(request, 'productos/mostrar_datos.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def agregar(request):
    print("Estamos en la vista agregar")
    context = {}
    return render(request, 'productos/formulario_agregar.html', context)

def eliminar(request):
    print("Estamos en la vista eliminar")
    context={}
    return render(request,'productos/boton_eliminar.html',context)

def eliminar_por_id(request):
    print("Hola estoy en eliminar_por_rut")
    if request.method == 'POST':
       mi_numero = request.POST['numero']

       if mi_numero != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(numero = mi_numero)
               if producto is not None:
                   print("Producto=", producto)
                   producto.delete()
                   context={}
                   return render(request, 'productos/mensaje_producto_eliminado.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def editar(request):
    print("Ok estamos en la vista editar")
    context={}
    return render(request,'productos/boton_editar.html',context)

def buscar_para_editar(request):

    print("hola  estoy en buscar_para_editar...")
    if request.method == 'POST':
        mi_numero = request.POST['numero']

        if mi_numero != "":
            try:
                producto = Producto()
                producto = Producto.objects.get(numero=mi_numero)
                if producto is not None:
                    print("Producto=", producto)
                    context = {'producto': producto}
                    return render(request, 'productos/formulario_editar.html', context)
                else:
                    return render(request, 'productos/error/error_202.html', {})
            except producto.DoesNotExist:
                return render(request, 'productos/error/error_202.html', {})
        else:
            return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})


def actualizar_producto(request):
        print("hola  estoy en actualizar_alumno...")
        if request.method == 'POST':
            mi_id = request.POST['id_producto']
            mi_numero = request.POST['numero']
            mi_precio = request.POST['precio']
            mi_nombre = request.POST['nombre']
            mi_foto = request.FILES.get('foto')
            mi_stock = request.POST['stock']
            mi_tipo = request.POST.get('tipo')



            if mi_numero != "":
                try:
                    producto = Producto()
                    producto.id_producto = mi_id
                    producto.numero = mi_numero
                    producto.precio = mi_precio
                    producto.nombre = mi_nombre
                    producto.foto = mi_foto
                    producto.stock = mi_stock
                    producto.tipo = mi_tipo

                    producto.save()

                    return render(request, 'productos/mensaje_datos_grabados.html', {})

                except producto.DoesNotExist:
                    return render(request, 'productos/error/error_204.html', {})
            else:
                return render(request, 'productos/error/error_201.html', {})
        else:
            return render(request, 'productos/error/error_203.html', {})

def agregar_producto(request):
    print("hola  estoy en actualizar_alumno...")
    if request.method == 'POST':
        mi_numero = request.POST['numero']
        mi_nombre = request.POST['nombre']
        mi_precio = request.POST['precio']
        mi_stock = request.POST['stock']
        mi_foto = request.FILES.get('foto')
        mi_tipo = request.POST.get('tipo')

        if mi_numero != "" and mi_nombre != "" and mi_precio != "" and mi_stock != "" and mi_tipo != "":
            if int(mi_stock) >= 1 and int(mi_precio) >= 1:

                try:
                    producto = Producto()
                    producto.numero = mi_numero
                    producto.nombre = mi_nombre
                    producto.precio = mi_precio
                    producto.foto = mi_foto
                    producto.stock = mi_stock
                    producto.activo = 1
                    producto.tipo = mi_tipo

                    producto.save()

                    return render(request, 'productos/mensaje_datos_grabados.html', {})

                except producto.DoesNotExist:
                    return render(request, 'productos/error/error_204.html', {})
            else:
                return render(request, 'productos/error/error_205.html', {})
        else:
            return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})


def inicio(request):
    print("ok, estamos en la vista menu alumnos")
    productos = Producto.objects.all()
    context={'Producto':productos}
    return render(request,'productos/inicio.html',context)



from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, login as login_aut, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .proceso_contexto import *
from .Carrito import *
# Create your views here.
def index(request):
    cate=Categoria.objects.all()
    obra=Obra.objects.filter(publicar=True).order_by("-idObra")[:3]
    
    data={'categorias':cate,'obras':obra}
    return render(request,"index.html", data)

def login(request):
    return render(request,"login.html")


@permission_required('auth.add_user',login_url='/login/')
def Registro(request):
    return render(request,"Registro.html")

def galeria(request):
    obras= Obra.objects.filter(publicar=True)
    cantidad= Obra.objects.all().count()
    data={'obras':obras}
    data['cantidad']=cantidad
    return render(request,"galeria.html", data)

def quienes(request):
    return render(request,"quienes_somos.html")

def formulario(request):
    return render(request,"formulario.html")

@login_required(login_url='/login/')
@permission_required(['webGrupoCero.add_obra','webGrupoCero.change_obra','webGrupoCero.delete_obra','webGrupoCero.view_obra'],login_url='/login/')
def admin_obra(request):
    cate = Categoria.objects.all()
    usuario= request.user.username
    usu=User.objects.get(username=usuario)
    obras= Obra.objects.filter(usuario=usu)
    data = {'categorias': cate, 'obras':obras}
    if request.POST:
        nom = request.POST.get("txtNombre")
        cre = request.POST.get("txtCreacion")
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        precio = request.POST.get("txtPrecio")
        cat = request.POST.get("cboCategoria")
        obj_cat = Categoria.objects.get(nombre=cat)
        nom_usu = request.user.username
        usu = User.objects.get(username=nom_usu)
        obr = Obra(
            nombre=nom,
            creacion=cre,
            descripcion=desc,
            foto=img,
            categoria=obj_cat,
            publicar=False,
            comentario='--', 
            usuario=usu,
            precio=precio
        )
        obr.save()
        data['mensaje'] = "Grabo"
    return render(request, "admin_obras.html", data)


def ficha_obra(request,id):
    obr = Obra.objects.get(idObra=id)
    galeria = Galeria.objects.filter(obra=obr)
    
    data={"item":obr,'galeria':galeria}
    return render(request,"ficha_obra.html",data)

def buscar_nombre(request):
    cate=Categoria.objects.all()
    data={'categorias':cate}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        obras = Obra.objects.filter(nombre__contains=nombre)
        data={'obras':obras}
        return render(request,"galeria.html",data)
    return render(request,"index.html",data)

def buscar_descripcion(request):
    cate=Categoria.objects.all()
    data={'categorias':cate}
    if request.POST:
        desc = request.POST.get("txtNombre")
        obras = Obra.objects.filter(descripcion__contains=desc)
        data={'obras':obras}
        return render(request,"galeria.html",data)
    return render(request,"index.html",data)

def buscar_categoria(request,id):
    cate=Categoria.objects.get(nombre=id)
    obras = Obra.objects.filter(categoria=cate)
    data={'obras':obras}
    return render(request,"galeria.html",data)

def registro_colaborador(request):
    data={'mensaje':''}
    if request.POST:
        nom = request.POST.get("txtNombre")
        ape = request.POST.get("txtApellido")
        p = request.POST.get("txtPass1")
        usu = request.POST.get("txtUser")
        email = request.POST.get("txtEmail")
        usuario=User()
        usuario.first_name=nom
        usuario.last_name=ape
        usuario.username=usu
        usuario.email= email
        usuario.set_password(p)
        grupo = Group.objects.get(name='colaborador')
        try:
            usuario.save() 
            usu.groups.add(grupo)
            data['mensaje']='Grabo usuario'
        except:
            data['mensaje']='error al grabar' 
    return render(request,"Registro.html",data)

def login_vista(request):
    data = {'mensaje': '', 'email': ''}
    if request.POST:
        nom = request.POST.get("txtUser")
        p = request.POST.get("txtPass1")
        email = request.POST.get("txtEmail")
        usu = authenticate(request, username=nom, email=email, password=p)
        if usu is not None and usu.is_active:
            login_aut(request, usu)
            
            cate = Categoria.objects.all()
            obra = Obra.objects.filter(publicar=True).order_by("-idObra")[:3]
            
            data = {'categorias': cate, 'obras': obra}
            
            return render(request, "index.html", data)
        else:
            data['mensaje'] = 'usuario/contraseña inválida'
            data['email'] = email
    return render(request, "login.html", data)


def cerrar(request):
    logout(request)
    cate=Categoria.objects.all()
    obra=Obra.objects.filter(publicar=True).order_by("-idObra")[:3]
    data={'categorias':cate,'obras':obra}
    return render(request,"index.html", data)

def eliminar(request,id):
    cate = Categoria.objects.all()
    usuario= request.user.username
    usu=User.objects.get(username=usuario)
    obras= Obra.objects.filter(usuario=usu)
    data = {'categorias': cate, 'obras':obras,'mensaje':''}
    obra = Obra.objects.get(idObra=id)
    try: 
        obra.delete()
        data["mensaje"]='Elimino'
    except:
        data["mensaje"]='No elimino'
    return render(request, "admin_obras.html", data)

def modificar(request,id):
    obra= Obra.objects.get(idObra=id)
    cate = Categoria.objects.all()
    data={'obra':obra, 'categorias': cate}
    return render(request,"modificar.html",data)

login_required(login_url='/login/')
def modificar_obra(request):
    if request.POST:
        nom = request.POST.get("txtNombre")
        cre = request.POST.get("txtCreacion")
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        cat = request.POST.get("cboCategoria")
        id = request.POST.get("txtId")
        obj_cat = Categoria.objects.get(nombre=cat)
        nom_usu = request.user.username
        usu = User.objects.get(username=nom_usu)
        obr = Obra.objects.get(idObra=id)
        obr.nombre=nom
        obr.creacion=cre
        obr.descripcion=desc
        obr.comentario='Revisar'
        obr.categoria=obj_cat
        obr.usuario=usu
        if img is not None:
            obr.foto=img 
        obr.save()
    return redirect('/admin_obra/')

login_required(login_url='/login/')
def subir_galeria(request):
    if request.POST:
        idObra = request.POST.get("txtId")
        obra = Obra.objects.get(idObra=idObra)
        foto = request.FILES.get("txtImg")
        gale = Galeria(
            foto=foto,
            obra=obra
        )
        gale.save()
    return redirect('/admin_obra/')


# controladores carrito #


def agregar_articulo(request,articulo_id):
    carrito = Carrito(request)
    obra = Obra.objects.get(idObra=articulo_id)
    carrito.agregar(obra)
    datos = request.session["carrito"]
    print(datos)
    return redirect('/carrito/')

def carrito(request):
    return render(request, 'carrito.html')

def quitar(request,articulo_id):
    carrito = Carrito(request)
    obra = Obra.objects.get(idObra=articulo_id)
    carrito.resta(obra)
    return redirect('/carrito/')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('/carrito/')

def comprar(request):
    if request.method == 'POST':
        carrito = Carrito(request)
        usuario = request.user
        total = 0
        for producto in carrito.carrito.values():
            total += producto['acumulado']
        compra = Compra.objects.create(usuario=usuario, total=total)
        for producto in carrito.carrito.values():
            obra = Obra.objects.get(idObra=producto['producto_id'])
            compra.obras.add(obra)
        carrito.vaciar()
        return redirect('historial_compra')  

    return render(request, 'carrito.html')


def historial_compra(request):
    usuario = request.user
    historial_compras = Compra.objects.filter(usuario=usuario)

    return render(request, 'historial_compra.html', {'historial': historial_compras})

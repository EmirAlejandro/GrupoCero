from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, login as login_aut, authenticate
# Create your views here.
def index(request):
    cate=Categoria.objects.all()
    obra=Obra.objects.filter(publicar=True).order_by("-idObra")[:3]
    
    data={'categorias':cate,'obras':obra}
    return render(request,"index.html", data)

def login(request):
    return render(request,"login.html")

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


def admin_obra(request):
    cate = Categoria.objects.all()
    data = {'categorias': cate}
    if request.POST:
        nom = request.POST.get("txtNombre")
        cre = request.POST.get("txtCreacion")
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
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
            comentario='--', 
            usuario=usu
        )
        obr.save()
        data['mensaje'] = "Grabo"
    return render(request, "admin_obras.html", data)

def ficha_obra(request,id):
    obr = Obra.objects.get(idObra=id)
    data={"item":obr}
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
        
        try:
            usuario.save() 
            data["mensaje"]='Grabo usuario'
        except:
            data["mensaje"]='error al grabar' 
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
            data["mensaje"] = 'usuario/contraseña inválida'
            data['email'] = email
    return render(request, "login.html", data)


def cerrar(request):
    logout(request)
    cate=Categoria.objects.all()
    obra=Obra.objects.filter(publicar=True).order_by("-idObra")[:3]
    data={'categorias':cate,'obras':obra}
    return render(request,"index.html", data)
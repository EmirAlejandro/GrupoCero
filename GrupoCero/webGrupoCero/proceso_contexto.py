def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total+= int(value["acumulado"])
    return {"total_carrito":total}


def cantidad(request):
    cantidad = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                cantidad+= int(value["cantidad"])
    return {"cantidad":cantidad}
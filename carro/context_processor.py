
def importe_total_carro(request):
    total=0.00

    if request.user.is_authenticated:
        carro = request.session.get("carro")
        if carro:
            for key, value in carro.items():
                total = total+(float(value["precio"]))

    return {"importe_total_carro":"{:.2f}".format(total)}
from django.shortcuts import redirect, render

from .models import lista_clientes


def home(request):
    return render(request, "cadastro/index.html")


def clientes(request):
    # if request.method == "POST":
    novo_cliente = lista_clientes()
    novo_cliente.nome = request.POST.get("nome")
    novo_cliente.idade = request.POST.get("idade")
    novo_cliente.foto = request.FILES.get("foto")
    novo_cliente.save()

    clientes = {"clientes": lista_clientes.objects.all()}

    return render(request, "cadastro/clientes.html", clientes)


# else:
#  return render(request, "cadastro/clientes.html")

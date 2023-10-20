from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistroForm


def pagina_inicial(request):
    return render(request, "home.html")


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "register.html", {"form": form})


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def fazer_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("Login bem-sucedido! Redirecionando para a página inicial.")
                return redirect("home")
            else:
                print("Login falhou. Credenciais inválidas.")
        else:
            print("Formulário de login inválido.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UsuarioRegistroForm  # ✅ Importa el formulario correcto

# -------------------------------
# Vista de inicio de sesión
# -------------------------------
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')  # Redirige al menú principal
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html', {'form': form})

# -------------------------------
# Vista para registro de usuario
# -------------------------------
def registro_view(request):  # ✅ Nombre más claro
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UsuarioRegistroForm()
    return render(request, 'registro.html', {'form': form})

# -------------------------------
# Vista del menú principal
# -------------------------------
@login_required
def menu_principal(request):
    return render(request, 'menu.html')

# -------------------------------
# Vista para crear una factura
# -------------------------------
@login_required
def crear_factura(request):
    if request.method == 'POST':
        # Aquí podrías guardar la factura en la base de datos
        return redirect('menu')  # Redirige al menú después de crearla
    return render(request, 'crear_factura.html')

# -------------------------------
# Vista para ver facturas existentes
# -------------------------------
@login_required
def ver_facturas(request):
    return render(request, 'ver_facturas.html')

# -------------------------------
# Vista para gestión de clientes
# -------------------------------
@login_required
def clientes(request):
    return render(request, 'clientes.html')

# -------------------------------
# Vista para configuración
# -------------------------------
@login_required
def configuracion(request):
    return render(request, 'configuracion.html')





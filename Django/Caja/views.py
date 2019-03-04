from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . import models
from . import forms

# Inicio

def index(request):
  return render(request, 'index.html', {})

# Acerca de

def acerca_de(request):
  return render(request, 'acerca_de.html', {})

# Usuarios

def usuario_cerrar_sesion(request):
  logout(request)
  return index(request)

# Empleados

def empleados(request):
  return render(request, 'empleados/index.html', {'empleados': models.Empleado.objects.all(), 'messages': messages.get_messages(request)})


def empleado_create(request):
  form = forms.EmpleadoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return empleados(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  if not models.Horario.objects.filter(hor_acti=True).count() > 0:
    messages.error(request, ('No hay horarios disponibles.'))
    return empleados(request)

  if not User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id')).count() > 0:
    messages.error(request, ('No hay usuarios disponibles.'))
    return empleados(request)

  return render(request, 'empleados/create.html', {'form': form, 'horarios': models.Horario.objects.filter(hor_acti=True), 'usuarios': User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id'))})


def empleado_update(request, empleado_id):
  empleado = models.Empleado.objects.get(pk=empleado_id)
  form = forms.EmpleadoForm(None)

  if request.method == 'POST':
    form = forms.EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return empleados(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  print(User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id')) | User.objects.filter(pk=models.Empleado.objects.get(pk=empleado_id).usu_id.id))

  return render(request, 'empleados/update.html', {'form': form, 'empleado': empleado, 'horarios': models.Horario.objects.filter(hor_acti=True).exclude(pk=empleado.hor_id.hor_id) | models.Horario.objects.filter(pk=empleado.hor_id.hor_id), 'usuarios': User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id')) | User.objects.filter(pk=models.Empleado.objects.get(pk=empleado_id).usu_id.id)})


def empleado_delete(request, empleado_id):
  models.Empleado.objects.get(pk=empleado_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return empleados(request)

# Clientes

def clientes(request):
  return render(request, 'clientes/index.html', {'clientes': models.Cliente.objects.all(), 'messages': messages.get_messages(request)})


def cliente_create(request):
  form = forms.ClienteForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return clientes(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  if models.TipoCliente.objects.filter(tcli_acti=True).count() == 0:
    messages.error(request, ('No hay tipos de cliente disponibles.'))
    return clientes(request)

  return render(request, 'clientes/create.html', {'tipos_cliente': models.TipoCliente.objects.filter(tcli_acti=True), 'carreras': models.Carrera.objects.filter(carr_acti=True)})


def cliente_update(request, cliente_id):
  cliente = models.Cliente.objects.get(pk=cliente_id)
  form = forms.ClienteForm(None)

  if request.method == 'POST':
    form = forms.ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return clientes(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'clientes/update.html', {'cliente': cliente, 'tipos_cliente': models.TipoCliente.objects.filter(tcli_acti=True).exclude(pk=cliente.tcli_id.tcli_id) | models.TipoCliente.objects.filter(pk=cliente.tcli_id.tcli_id), 'carreras': models.Carrera.objects.filter(carr_acti=True) if cliente.carr_id == None else models.Carrera.objects.filter(carr_acti=True).exclude(pk=cliente.carr_id.carr_id) | models.Carrera.objects.filter(pk=cliente.carr_id.carr_id)})


def cliente_delete(request, cliente_id):
  models.Cliente.objects.get(pk=cliente_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return clientes(request)

# Movimientos

def movimientos(request):
  return render(request, 'movimientos/index.html', {'movimientos': models.Movimiento.objects.all(), 'messages': messages.get_messages(request)})

def movimiento_create(request):
  form = forms.MovimientoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return movimientos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  if request.user.is_authenticated and request.user.is_staff:
    if models.Empleado.objects.filter(usu_id=request.user.id).count() == 0:
      messages.error(request, ('Su usuario no está configurado como empleado. Contacto a su administrador.'))
      return movimientos(request)

  if models.Cliente.objects.filter(cli_acti=True).count() == 0:
    messages.error(request, ('No hay clientes disponibles.'))
    return movimientos(request)

  if models.Producto.objects.filter(prod_acti=True).count() == 0:
    messages.error(request, ('No hay productos disponibles.'))
    return movimientos(request)

  if models.TipoDocumento.objects.filter(tdoc_acti=True).count() == 0:
    messages.error(request, ('No hay tipos de documento disponibles.'))
    return movimientos(request)

  if models.FormaPago.objects.filter(fpago_acti=True).count() == 0:
    messages.error(request, ('No hay formas de pago disponibles.'))
    return movimientos(request)

  if models.ModoPago.objects.filter(mpago_acti=True).count() == 0:
    messages.error(request, ('No hay modalidades de pago disponibles.'))
    return movimientos(request)

  return render(request, 'movimientos/create.html', {'form': form, })


def movimiento_update(request, movimiento_id):
  movimiento = models.Movimiento.objects.get(pk=movimiento_id)
  form = forms.MovimientoForm(request.POST or None, instance=movimiento)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return movimientos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'movimientos/update.html', {'form': form})


def movimiento_delete(request, movimiento_id):
  models.Movimiento.objects.get(pk=movimiento_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return movimientos(request)

# Tipos de Cliente

def tipos_cliente(request):
  return render(request, 'tipos_cliente/index.html', {'tipos_cliente': models.TipoCliente.objects.all(), 'messages': messages.get_messages(request)})


def tipo_cliente_create(request):
  if request.method == 'POST':
    form = forms.TipoClienteForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_cliente(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_cliente/create.html', {})


def tipo_cliente_update(request, tipo_cliente_id):
  tipo_cliente = models.TipoCliente.objects.get(pk=tipo_cliente_id)

  if request.method == 'POST':
    form = forms.TipoClienteForm(request.POST or None, instance=tipo_cliente)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_cliente(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_cliente/update.html', {'tipo_cliente': tipo_cliente})


def tipo_cliente_delete(request, tipo_cliente_id):
  models.TipoCliente.objects.get(pk=tipo_cliente_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return tipos_cliente(request)

# Carreras

def carreras(request):
  return render(request, 'carreras/index.html', {'carreras': models.Carrera.objects.all(), 'messages': messages.get_messages(request)})


def carrera_create(request):

  if request.method == 'POST':
    form = forms.CarreraForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return carreras(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'carreras/create.html', {})


def carrera_update(request, carrera_id):
  carrera = models.Carrera.objects.get(pk=carrera_id)

  if request.method == 'POST':
    form = forms.CarreraForm(request.POST or None, instance=carrera)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return carreras(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'carreras/update.html', {'carrera': carrera})


def carrera_delete(request, carrera_id):
  models.Carrera.objects.get(pk=carrera_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return carreras(request)

# Productos

def productos(request):
  return render(request, 'productos/index.html', {'productos': models.Producto.objects.all(), 'messages': messages.get_messages(request)})


def producto_create(request):

  if request.method == 'POST':
    form = forms.ProductoForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return productos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'productos/create.html', {})


def producto_update(request, producto_id):
  producto = models.Producto.objects.get(pk=producto_id)
  form = forms.ProductoForm(request.POST or None, instance=producto)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return productos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'productos/update.html', {'producto': producto})


def producto_delete(request, producto_id):
  models.Producto.objects.get(pk=producto_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return productos(request)

# Horarios

def horarios(request):
  return render(request, 'horarios/index.html', {'horarios': models.Horario.objects.all(), 'messages': messages.get_messages(request)})


def horario_create(request):
  form = forms.HorarioForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return horarios(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/create.html', {'form': form})


def horario_update(request, horario_id):
  horario = models.Horario.objects.get(pk=horario_id)
  form = forms.HorarioForm(request.POST or None, instance=horario)

  if request.method == 'POST':

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return horarios(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/update.html', {'form': form, 'horario': horario})


def horario_delete(request, horario_id):
  models.Horario.objects.get(pk=horario_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return horarios(request)

# Formas de Pago

def formas_pago(request):
  return render(request, 'formas_pago/index.html', {'formas_pago': models.FormaPago.objects.all(), 'messages': messages.get_messages(request)})


def forma_pago_create(request):
  form = forms.FormaPagoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return formas_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'formas_pago/create.html', {})


def forma_pago_update(request, forma_pago_id):
  forma_pago = models.FormaPago.objects.get(pk=forma_pago_id)
  form = forms.FormaPagoForm(request.POST or None, instance=forma_pago)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return formas_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'formas_pago/update.html', {'forma_pago': forma_pago})


def forma_pago_delete(request, forma_pago_id):
  models.FormaPago.objects.get(pk=forma_pago_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return formas_pago(request)

# Modalidades de Pago

def modos_pago(request):
  return render(request, 'modos_pago/index.html', {'modos_pago': models.ModoPago.objects.all(), 'messages': messages.get_messages(request)})


def modo_pago_create(request):
  form = forms.ModoPagoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return modos_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'modos_pago/create.html', {})


def modo_pago_update(request, modo_pago_id):
  modo_pago = models.ModoPago.objects.get(pk=modo_pago_id)
  form = forms.ModoPagoForm(request.POST or None, instance=modo_pago)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return modos_pago(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'modos_pago/update.html', {'modo_pago': modo_pago})


def modo_pago_delete(request, modo_pago_id):
  models.ModoPago.objects.get(pk=modo_pago_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return modos_pago(request)

# Tipos de Documento

def tipos_documento(request):
  return render(request, 'tipos_documento/index.html', {'tipos_documento': models.TipoDocumento.objects.all(), 'messages': messages.get_messages(request)})


def tipo_documento_create(request):
  form = forms.TipoDocumentoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_documento(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_documento/create.html', {})


def tipo_documento_update(request, tipo_documento_id):
  tipo_documento = models.TipoDocumento.objects.get(pk=tipo_documento_id)
  form = forms.TipoDocumentoForm(request.POST or None, instance=tipo_documento)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return tipos_documento(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_documento/update.html', {'tipo_documento': tipo_documento})


def tipo_documento_delete(request, tipo_documento_id):
  models.TipoDocumento.objects.get(pk=tipo_documento_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return tipos_documento(request)


from django.shortcuts import render
from django.contrib import messages
from . import models
from . import forms

# Create your views here.

def index(request):
  return render(request, 'index.html', {})


def acerca_de(request):
  return render(request, 'acerca_de.html', {})

# Empleados

def empleados(request):
  return render(request, 'empleados/index.html', {'empleados': models.Empleado.objects.all(), 'messages': messages.get_messages(request)})

def empleado_create(request):
  if request.method == 'POST':
    form = forms.EmpleadoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  if models.Horario.objects.count() == 0:
    messages.error(request, ('No se han definido horarios.'))
    return empleados(request)

  return render(request, 'empleados/create.html', {'horarios': models.Horario.objects.all()})


def empleado_update(request, empleado_id):
  empleado = models.Empleado.objects.get(pk=empleado_id)

  if request.method == 'POST':
    form = forms.EmpleadoForm(request.POST or None, instance=empleado)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return empleados(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'empleados/update.html', {'empleado': empleado, 'horarios': models.Horario.objects.all()})


def empleado_delete(request, empleado_id):
  models.Empleado.objects.get(pk=empleado_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return empleados(request)

# Clientes

def clientes(request):
  return render(request, 'clientes/index.html', {'clientes': models.Cliente.objects.all(), 'messages': messages.get_messages(request)})


def cliente_create(request):
  if request.method == 'POST':
    form = forms.ClienteForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  if models.TipoCliente.objects.count() == 0:
    messages.error(request, ('No se han definido tipos de cliente.'))
    return empleados(request)

  if models.Carrera.objects.count() == 0:
    messages.error(request, ('No se han definido carreras.'))
    return empleados(request)

  return render(request, 'clientes/create.html', {'tipos_cliente': models.TipoCliente.objects.all(), 'carreras': models.Carrera.objects.all()})


def cliente_update(request, cliente_id):
  cliente = models.Cliente.objects.get(pk=cliente_id)

  if request.method == 'POST':
    form = forms.ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return clientes(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'clientes/update.html', {'cliente': cliente, 'tipos_cliente': models.TipoCliente.objects.all(), 'carreras': models.Carrera.objects.all()})


def cliente_delete(request, cliente_id):
  models.Cliente.objects.get(pk=cliente_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return clientes(request)

# Movimientos

def movimientos(request):
  return render(request, 'movimientos/index.html', {'movimientos': models.Movimiento.objects.all(), 'messages': messages.get_messages(request)})

def movimiento_create(request):
  if request.method == 'POST':
    form = forms.MovimientoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  if models.Horario.objects.count() == 0:
    messages.error(request, ('No se han definido horarios.'))
    return movimientos(request)

  return render(request, 'movimientos/create.html', {})


def movimiento_update(request, movimiento_id):
  movimiento = models.Movimiento.objects.get(pk=movimiento_id)

  if request.method == 'POST':
    form = forms.MovimientoForm(request.POST or None, instance=movimiento)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return movimientos(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'movimientos/update.html', {})


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
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'productos/create.html', {})


def producto_update(request, producto_id):
  producto = models.Producto.objects.get(pk=producto_id)

  if request.method == 'POST':
    form = forms.ProductoForm(request.POST or None, instance=producto)

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
  if request.method == 'POST':
    form = forms.HorarioForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/create.html', {})


def horario_update(request, horario_id):
  horario = models.Horario.objects.get(pk=horario_id)

  if request.method == 'POST':
    form = forms.HorarioForm(request.POST or None, instance=horario)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return horarios(request)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'horarios/update.html', {'horario': horario})


def horario_delete(request, horario_id):
  models.Horario.objects.get(pk=horario_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return horarios(request)

# Formas de Pago

def formas_pago(request):
  return render(request, 'formas_pago/index.html', {'formas_pago': models.FormaPago.objects.all(), 'messages': messages.get_messages(request)})


def forma_pago_create(request):
  if request.method == 'POST':
    form = forms.FormaPagoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'formas_pago/create.html', {})


def forma_pago_update(request, forma_pago_id):
  forma_pago = models.FormaPago.objects.get(pk=forma_pago_id)

  if request.method == 'POST':
    form = forms.FormaPagoForm(request.POST or None, instance=forma_pago)

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
  if request.method == 'POST':
    form = forms.ModoPagoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'modos_pago/create.html', {})


def modo_pago_update(request, modo_pago_id):
  modo_pago = models.ModoPago.objects.get(pk=modo_pago_id)

  if request.method == 'POST':
    form = forms.ModoPagoForm(request.POST or None, instance=modo_pago)

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
  if request.method == 'POST':
    form = forms.TipoDocumentoForm(request.POST or None)

    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'tipos_documento/create.html', {})


def tipo_documento_update(request, tipo_documento_id):
  tipo_documento = models.TipoDocumento.objects.get(pk=tipo_documento_id)

  if request.method == 'POST':
    form = forms.TipoDocumentoForm(request.POST or None, instance=tipo_documento)

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


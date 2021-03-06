from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . import models
from . import forms
import csv
from django.http import HttpResponse

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

# clientes

def empleados(request):
  empleados = models.Empleado.objects.all()
  filtered = None

  if request.GET.get('query') is not None:
    if len(request.GET.get('query')) > 0:
      if request.method == 'GET':
        if request.GET.get('field') == 'emp_id':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(emp_id=request.GET.get('query'))
            messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(emp_id__iregex=r'(' + request.GET.get('query') + r')+')
            messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'emp_nomb':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(emp_nomb=request.GET.get('query'))
            messages.success(request, 'Nombres igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(emp_nomb__iregex=r'(' + request.GET.get('query') + r')+')
            messages.success(request, 'Nombres que contengan ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'emp_ape1':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(emp_ape1=request.GET.get('query'))
            messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(emp_ape1__iregex=r'(' + request.GET.get('query') + r')+')
            messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'emp_ape2':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(emp_ape2=request.GET.get('query'))
            messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(emp_ape2__iregex=r'(' + request.GET.get('query') + r')+')
            messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'emp_cedu':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(emp_cedu=request.GET.get('query'))
            messages.success(request, 'Cédula de Identidad igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(emp_cedu__iregex=r'(' + request.GET.get('query') + r')+')
            messages.success(request, 'Cédula de Identidad que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'usu_nomb':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username=request.GET.get('query')))
            messages.success(request, 'Nombre de Usuario igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Nombre de Usuario que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'usu_tipo':
          if request.GET.get('query').upper().strip() == 'ADMINISTRADOR':
            empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(is_superuser=True).filter(is_staff=True))
            messages.success(request, 'Tipo de Usuario Administrador.')
          elif request.GET.get('query').upper().strip() == 'EMPLEADO':
            empleados = models.Empleado.objects.filter(usu_id__in=User.objects.exclude(is_superuser=True).filter(is_staff=True))
            messages.success(request, 'Tipo de Usuario Empleado.')
          else:
            messages.error(request, 'Por favor, introduzca un tipo de usuario válido (Administrador, Empleado).')
          filtered = True

        if request.GET.get('field') == 'emp_entra':
          empleados = models.Empleado.objects.filter(emp_entra__range=(request.GET.get('query'),request.GET.get('query2')))
          messages.success(request, 'Fecha de Entrada entre ' + request.GET.get('query') + ' y ' + request.GET.get('query2') + '.')
          filtered = True

        if request.GET.get('field') == 'hor_nomb':
          if request.GET.get('match') == 'on':
            empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb=request.GET.get('query')))
            messages.success(request, 'Nombre de Horario igual a ' + request.GET.get('query') + '.')
          else:
            empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Nombre de Horario que contenga ' + request.GET.get('query') + '.')
          filtered = True

        if request.GET.get('field') == 'emp_acti':
          if request.GET.get('query').upper().strip() == 'ACTIVO':
            empleados = models.Empleado.objects.filter(emp_acti=True)
            messages.success(request, 'Activo.')
          elif request.GET.get('query').upper().strip() == 'INACTIVO':
            empleados = models.Empleado.objects.filter(emp_acti=False)
            messages.success(request, 'Inactivo.')
          else:
            messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
          filtered = True

  return render(request, 'empleados/index.html', {'empleados': empleados, 'filtered': filtered, 'messages': messages.get_messages(request)})


def empleados_print(request):
  empleados = models.Empleado.objects.all()
  filtered = None

  if request.method == 'GET':
    if len(request.GET.get('query')) > 0:
      if request.GET.get('field') == 'emp_id':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_id=request.GET.get('query'))
          messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_id__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_nomb=request.GET.get('query'))
          messages.success(request, 'Nombres igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_nomb__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Nombres que contengan ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_ape1':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_ape1=request.GET.get('query'))
          messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_ape1__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_ape2':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_ape2=request.GET.get('query'))
          messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_ape2__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_cedu':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_cedu=request.GET.get('query'))
          messages.success(request, 'Cédula de Identidad igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_cedu__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Cédula de Identidad que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'usu_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username=request.GET.get('query')))
          messages.success(request, 'Nombre de Usuario igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Nombre de Usuario que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'usu_tipo':
        if request.GET.get('query').upper().strip() == 'ADMINISTRADOR':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(is_superuser=True).filter(is_staff=True))
          messages.success(request, 'Tipo de Usuario Administrador.')
        elif request.GET.get('query').upper().strip() == 'EMPLEADO':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.exclude(is_superuser=True).filter(is_staff=True))
          messages.success(request, 'Tipo de Usuario Empleado.')
        else:
          messages.error(request, 'Por favor, introduzca un tipo de usuario válido (Administrador, Empleado).')
        filtered = True

      if request.GET.get('field') == 'emp_entra':
        empleados = models.Empleado.objects.filter(emp_entra__range=(request.GET.get('query'),request.GET.get('query2')))
        messages.success(request, 'Fecha de Entrada entre ' + request.GET.get('query') + ' y ' + request.GET.get('query2') + '.')
        filtered = True

      if request.GET.get('field') == 'hor_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb=request.GET.get('query')))
          messages.success(request, 'Nombre de Horario igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Nombre de Horario que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_acti':
        if request.GET.get('query').upper().strip() == 'ACTIVO':
          empleados = models.Empleado.objects.filter(emp_acti=True)
          messages.success(request, 'Activo.')
        elif request.GET.get('query').upper().strip() == 'INACTIVO':
          empleados = models.Empleado.objects.filter(emp_acti=False)
          messages.success(request, 'Inactivo.')
        else:
          messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
          return redirect(empleados)
        filtered = True

  return render(request, 'empleados/print.html', {'empleados': empleados, 'filtered': filtered, 'messages': messages.get_messages(request)})


def empleados_excel(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

  writer = csv.writer(response)
  writer.writerow(['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Cedula', 'Usuario', 'Fecha de Entrada', 'Fecha de Salida', 'Horario', 'Activo'])

  empleados = models.Empleado.objects.all()

  if request.method == 'GET':
    if len(request.GET.get('query')) > 0:
      if request.GET.get('field') == 'emp_id':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_id=request.GET.get('query'))
          messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_id__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_nomb=request.GET.get('query'))
          messages.success(request, 'Nombres igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_nomb__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Nombres que contengan ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_ape1':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_ape1=request.GET.get('query'))
          messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_ape1__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_ape2':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_ape2=request.GET.get('query'))
          messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_ape2__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_cedu':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(emp_cedu=request.GET.get('query'))
          messages.success(request, 'Cédula de Identidad igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(emp_cedu__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Cédula de Identidad que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'usu_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username=request.GET.get('query')))
          messages.success(request, 'Nombre de Usuario igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(username__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Nombre de Usuario que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'usu_tipo':
        if request.GET.get('query').upper().strip() == 'ADMINISTRADOR':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.filter(is_superuser=True).filter(is_staff=True))
          messages.success(request, 'Tipo de Usuario Administrador.')
        elif request.GET.get('query').upper().strip() == 'EMPLEADO':
          empleados = models.Empleado.objects.filter(usu_id__in=User.objects.exclude(is_superuser=True).filter(is_staff=True))
          messages.success(request, 'Tipo de Usuario Empleado.')
        else:
          messages.error(request, 'Por favor, introduzca un tipo de usuario válido (Administrador, Empleado).')
        filtered = True

      if request.GET.get('field') == 'emp_entra':
        empleados = models.Empleado.objects.filter(emp_entra__range=(request.GET.get('query'),request.GET.get('query2')))
        messages.success(request, 'Fecha de Entrada entre ' + request.GET.get('query') + ' y ' + request.GET.get('query2') + '.')
        filtered = True

      if request.GET.get('field') == 'hor_nomb':
        if request.GET.get('match') == 'on':
          empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb=request.GET.get('query')))
          messages.success(request, 'Nombre de Horario igual a ' + request.GET.get('query') + '.')
        else:
          empleados = models.Empleado.objects.filter(hor_id__in=models.Horario.objects.filter(hor_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Nombre de Horario que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'emp_acti':
        if request.GET.get('query').upper().strip() == 'ACTIVO':
          empleados = models.Empleado.objects.filter(emp_acti=True)
        elif request.GET.get('query').upper().strip() == 'INACTIVO':
          empleados = models.Empleado.objects.filter(emp_acti=False)
        filtered = True

    empleados = empleados.values_list('emp_id', 'emp_nomb', 'emp_ape1', 'emp_ape2', 'emp_cedu', 'usu_id', 'emp_entra', 'emp_sale', 'hor_id', 'emp_acti')

    for empleado in empleados:
        writer.writerow(empleado)

    return response


def empleado_print(request, empleado_id):
  return render(request, 'empleados/print-1.html', {'empleado': models.Empleado.objects.get(pk=empleado_id)})


def empleado_create(request):
  form = forms.EmpleadoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return redirect(empleados)
    else:
      messages.error(request, ('Información incorrecta.'))

  if not models.Horario.objects.filter(hor_acti=True).count() > 0:
    messages.error(request, ('No hay horarios disponibles.'))
    return redirect(empleados)

  if not User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id')).count() > 0:
    messages.error(request, ('No hay usuarios disponibles.'))
    return redirect(empleados)

  return render(request, 'empleados/create.html', {'form': form, 'horarios': models.Horario.objects.filter(hor_acti=True), 'usuarios': User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id'))})


def empleado_update(request, empleado_id):
  empleado = models.Empleado.objects.get(pk=empleado_id)
  form = forms.EmpleadoForm(None)

  if request.method == 'POST':
    form = forms.EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return redirect(empleados)
    else:
      messages.error(request, ('Información incorrecta.'))

  return render(request, 'empleados/update.html', {'form': form, 'empleado': empleado, 'horarios': models.Horario.objects.filter(hor_acti=True).exclude(pk=empleado.hor_id.hor_id) | models.Horario.objects.filter(pk=empleado.hor_id.hor_id), 'usuarios': User.objects.filter(is_active=True).exclude(pk__in=models.Empleado.objects.values('usu_id')) | User.objects.filter(pk=models.Empleado.objects.get(pk=empleado_id).usu_id.id)})


def empleado_delete(request, empleado_id):
  models.Empleado.objects.get(pk=empleado_id).delete()
  messages.success(request, ('Operación realizada con éxito.'))
  return empleados(request)

# Clientes

def clientes(request):
  clientes = models.Cliente.objects.all()
  filtered = None

  if request.method == 'GET':
    if request.GET.get('field') == 'cli_id':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(cli_id=request.GET.get('query'))
        messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(cli_id__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'cli_nomb':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(cli_nomb=request.GET.get('query'))
        messages.success(request, 'Nombre igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(cli_nomb__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'Nombre que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'cli_ape1':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(cli_ape1=request.GET.get('query'))
        messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(cli_ape1__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'cli_ape2':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(cli_ape2=request.GET.get('query'))
        messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(cli_ape2__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'tcli_nomb':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb=request.GET.get('query')))
        messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
        messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'carr_nomb':
      if request.GET.get('match') == 'on':
        clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb=request.GET.get('query')))
        messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
      else:
        clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
        messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'cli_acti':
      if request.GET.get('query').upper().strip() == 'ACTIVO':
        clientes = models.Cliente.objects.filter(cli_acti=True)
        messages.success(request, 'Activo.')
      elif request.GET.get('query').upper().strip() == 'INACTIVO':
        clientes = models.Cliente.objects.filter(cli_acti=False)
        messages.success(request, 'Inactivo.')
      else:
        messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
      filtered = True

  return render(request, 'clientes/index.html', {'clientes': clientes, 'filtered': filtered, 'messages': messages.get_messages(request)})


def clientes_print(request):
  clientes = models.Cliente.objects.all()
  filtered = None

  if request.method == 'GET':
    if len(request.GET.get('query')) > 0:
      if request.GET.get('field') == 'cli_id':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_id=request.GET.get('query'))
          messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_id__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'cli_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_nomb=request.GET.get('query'))
          messages.success(request, 'Nombre igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_nomb__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Nombre que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'cli_ape1':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_ape1=request.GET.get('query'))
          messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_ape1__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'cli_ape2':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_ape2=request.GET.get('query'))
          messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_ape2__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'tcli_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb=request.GET.get('query')))
          messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'carr_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb=request.GET.get('query')))
          messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')
        filtered = True

      if request.GET.get('field') == 'cli_acti':
        if request.GET.get('query').upper().strip() == 'ACTIVO':
          clientes = models.Cliente.objects.filter(cli_acti=True)
          messages.success(request, 'Activo.')
        elif request.GET.get('query').upper().strip() == 'INACTIVO':
          clientes = models.Cliente.objects.filter(cli_acti=False)
          messages.success(request, 'Inactivo.')
        else:
          messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
          return redirect(clientes)
        filtered = True
  return render(request, 'clientes/print.html', {'clientes': clientes, 'filtered': filtered, 'messages': messages.get_messages(request)})


def clientes_excel(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

  writer = csv.writer(response)
  writer.writerow(['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Tipo', 'Carrera', 'Activo'])

  clientes = models.Cliente.objects.all()

  if request.method == 'GET':
    if len(request.GET.get('query')) > 0:
      if request.GET.get('field') == 'cli_id':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_id=request.GET.get('query'))
          messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_id__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'cli_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_nomb=request.GET.get('query'))
          messages.success(request, 'Nombre igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_nomb__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Nombre que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'cli_ape1':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_ape1=request.GET.get('query'))
          messages.success(request, 'Apellido Paterno igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_ape1__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Paterno que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'cli_ape2':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(cli_ape2=request.GET.get('query'))
          messages.success(request, 'Apellido Materno igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(cli_ape2__iregex=r'(' + request.GET.get('query') + r')+')
          messages.success(request, 'Apellido Materno que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'tcli_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb=request.GET.get('query')))
          messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(tcli_id__in=models.TipoCliente.objects.filter(tcli_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'carr_nomb':
        if request.GET.get('match') == 'on':
          clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb=request.GET.get('query')))
          messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
        else:
          clientes = models.Cliente.objects.filter(carr_id__in=models.Carrera.objects.filter(carr_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
          messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')

      if request.GET.get('field') == 'cli_acti':
        if request.GET.get('query').upper().strip() == 'ACTIVO':
          clientes = models.Cliente.objects.filter(cli_acti=True)
          messages.success(request, 'Activo.')
        elif request.GET.get('query').upper().strip() == 'INACTIVO':
          clientes = models.Cliente.objects.filter(cli_acti=False)
          messages.success(request, 'Inactivo.')
        else:
          messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
          return redirect(clientes)

    clientes = clientes.values_list('cli_id', 'cli_nomb', 'cli_ape1', 'cli_ape2', 'tcli_id', 'carr_id', 'cli_acti')

    for cliente in clientes:
        writer.writerow(cliente)

  return response


def cliente_print(request, cliente_id):
  return render(request, 'clientes/print-1.html', {'cliente': models.Cliente.objects.get(pk=cliente_id)})


def cliente_create(request):
  form = forms.ClienteForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return redirect(clientes)
    else:
      messages.error(request, ('Información incorrecta.'))

  if models.TipoCliente.objects.filter(tcli_acti=True).count() == 0:
    messages.error(request, ('No hay tipos de cliente disponibles.'))
    return redirect(clientes)

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
  movimientos = models.Movimiento.objects.all()
  filtered = None

  if request.method == 'GET':
    if request.GET.get('field') == 'mov_id':
      if request.GET.get('match') == 'on':
        movimientos = models.Movimiento.objects.filter(mov_id=request.GET.get('query'))
        messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
      else:
        movimientos = models.Movimiento.objects.filter(mov_id__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'ID que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'mov_fecha':
      if request.GET.get('match') == 'on':
        movimientos = models.Movimiento.objects.filter(mov_fecha=request.GET.get('query'))
        messages.success(request, 'Fecha igual a ' + request.GET.get('query') + '.')
      else:
        movimientos = models.Movimiento.objects.filter(mov_fecha__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'Fecha que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'doc_id':
      if request.GET.get('match') == 'on': 
        movimientos = models.Movimiento.objects.filter(doc_id__in=models.Documento.objects.filter(doc_id=request.GET.get('query')))
        messages.success(request, 'Documento igual a ' + request.GET.get('query') + '.')
      else:
        movimientos = models.Movimiento.objects.filter(doc_id__in=models.FormaPago.objects.filter(doc_id__iregex=r'(' + request.GET.get('query') + r')+'))
        messages.success(request, 'Documento que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'fpago_id':
      if request.GET.get('match') == 'on': 
        movimientos = models.Movimiento.objects.filter(fpago_id__in=models.FormaPago.objects.filter(fpago_id=request.GET.get('query')))
        messages.success(request, 'Forma de Pago igual a ' + request.GET.get('query') + '.')
      else:
        movimientos = models.Movimiento.objects.filter(fpago_id__in=models.FormaPago.objects.filter(fpago_id__iregex=r'(' + request.GET.get('query') + r')+'))
        messages.success(request, 'Forma de Pago que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'mov_monto':
      if request.GET.get('match') == 'on':
        movimientos = models.Movimiento.objects.filter(mov_monto=request.GET.get('query'))
        messages.success(request, 'Tipo de Cliente igual a ' + request.GET.get('query') + '.')
      else:
        movimientos = models.Movimiento.objects.filter(mov_monto__iregex=r'(' + request.GET.get('query') + r')+')
        messages.success(request, 'Tipo de Cliente que contenga ' + request.GET.get('query') + '.')
      filtered = True

    if request.GET.get('field') == 'mov_acti':
      if request.GET.get('query').upper().strip() == 'ACTIVO':
        movimientos = models.Movimiento.objects.filter(mov_acti=True)
        messages.success(request, 'Activo.')
      elif request.GET.get('query').upper().strip() == 'INACTIVO':
        movimientos = models.Movimiento.objects.filter(mov_acti=False)
        messages.success(request, 'Inactivo.')
      else:
        messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
      filtered = True

  return render(request, 'movimientos/index.html', {'movimientos': movimientos, 'filtered': filtered, 'messages': messages.get_messages(request)})

def movimiento_create(request, documento_id):
  documento = models.Documento.objects.filter(pk=documento_id)
  form = forms.MovimientoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return redirect(documentos)
    else:
      messages.error(request, ('Información incorrecta.'))

  if request.user.is_authenticated and request.user.is_staff:
    if models.Empleado.objects.filter(usu_id=request.user.id).count() == 0:
      messages.error(request, ('Su usuario no está configurado como empleado. Contacte a su administrador.'))
      return redirect(documentos)

  if models.FormaPago.objects.filter(fpago_acti=True).count() == 0:
    messages.error(request, ('No hay formas de pago disponibles.'))
    return redirect(documentos)

  return render(request, 'movimientos/create.html', {'form': form, 'empleado': models.Empleado.objects.get(usu_id=request.user.id) if models.Empleado.objects.filter(usu_id=request.user.id).count() > 0 else None, 'formas_pago': models.FormaPago.objects.filter(fpago_acti=True), 'documento': documento[0]})


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
  movimiento = models.Movimiento.objects.filter(pk=movimiento_id)
  if request.method == 'POST':
    movimiento.update(mov_acti=0)
    messages.success(request, ('Operación realizada con éxito.'))
    return redirect(movimientos)

  return render(request, 'movimientos/delete.html', {'movimiento': movimiento[0]})


def movimientos_excel(request):
  return redirect(movimientos)


def movimientos_print(request):
  return render(movimientos, {'movimiento': models.Movimiento.objects.all().get(pk=movimiento_id)})


def movimiento_print(request, movimiento_id):
  return render(request, 'movimientos/print-1.html', {'movimiento': models.Movimiento.objects.all().get(pk=movimiento_id)})


def documentos(request):
  documentos = models.Documento.objects.all()
  filtered = None

  if request.method == 'GET':
    if request.GET.get('query') is not None:
      if len(request.GET.get('query')) > 0:
        if request.GET.get('field') == 'doc_id':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(doc_id=request.GET.get('query'))
            messages.success(request, 'ID igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(doc_id__iregex=r'(' + request.GET.get('query') + r')+')

        if request.GET.get('field') == 'emp_nomb':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(emp_nomb_id__in=models.Empleado.objects.filter(emp_nomb_nomb=request.GET.get('query')))
            messages.success(request, 'Empleado igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(emp_nomb_id__in=models.Empleado.objects.filter(emp_nomb_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Empleado que contenga ' + request.GET.get('query') + '.')

        if request.GET.get('field') == 'cli_nomb':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(cli_nomb_id__in=models.Cliente.objects.filter(cli_nomb_nomb=request.GET.get('query')))
            messages.success(request, 'Cliente igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(cli_nomb_id__in=models.Cliente.objects.filter(cli_nomb_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Cliente que contenga ' + request.GET.get('query') + '.')

        if request.GET.get('field') == 'prod_nomb':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(prod_id__in=models.Producto.objects.filter(prod_nomb=request.GET.get('query')))
            messages.success(request, 'Producto igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(prod_id__in=models.Producto.objects.filter(prod_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Producto que contenga ' + request.GET.get('query') + '.')

        if request.GET.get('field') == 'tdoc_nomb':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(tdoc_id__in=models.TipoDocumento.objects.filter(tdoc_nomb=request.GET.get('query')))
            messages.success(request, 'Tipo de Documento igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(tdoc_id__in=models.TipoDocumento.objects.filter(tdoc_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Tipo de Documento que contenga ' + request.GET.get('query') + '.')

        if request.GET.get('field') == 'mpago_nomb':
          if request.GET.get('match') == 'on':
            documentos = models.Documento.objects.filter(mpago_id__in=models.ModoPago.objects.filter(mpago_nomb=request.GET.get('query')))
            messages.success(request, 'Modo de Pago igual a ' + request.GET.get('query') + '.')
          else:
            documentos = models.Documento.objects.filter(mpago_id__in=models.ModoPago.objects.filter(mpago_nomb__iregex=r'(' + request.GET.get('query') + r')+'))
            messages.success(request, 'Modo de Pago que contenga ' + request.GET.get('query') + '.')

        if request.GET.get('field') == 'doc_acti':
          if request.GET.get('query').upper().strip() == 'ACTIVO':
            documentos = models.Documento.objects.filter(doc_acti=True)
            messages.success(request, 'Activo.')
          elif request.GET.get('query').upper().strip() == 'INACTIVO':
            documentos = models.Documento.objects.filter(doc_acti=False)
            messages.success(request, 'Inactivo.')
          else:
            messages.error(request, 'Por favor, introduzca un estado válido (Activo, Inactivo).')
            return redirect(documentos)

  return render(request, 'documentos/index.html', {'documentos': documentos, 'filtered': filtered, 'messages': messages.get_messages(request)})


def documento_create(request):
  form = forms.DocumentoForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, ('Operación realizada con éxito.'))
      return redirect(documentos)
    else:
      messages.error(request, ('Información incorrecta.'))

# Validación

  if request.user.is_authenticated and request.user.is_staff:
    if models.Empleado.objects.filter(usu_id=request.user.id).count() == 0:
      messages.error(request, ('Su usuario no está configurado como empleado. Contacte a su administrador.'))
      return redirect(documentos)

  if models.Cliente.objects.filter(cli_acti=True).count() == 0:
    messages.error(request, ('No hay clientes disponibles.'))
    return redirect(documentos)

  if models.Producto.objects.filter(prod_acti=True).count() == 0:
    messages.error(request, ('No hay productos disponibles.'))
    return redirect(documentos)

  if models.TipoDocumento.objects.filter(tdoc_acti=True).count() == 0:
    messages.error(request, ('No hay tipos de documento disponibles.'))
    return redirect(documentos)

  if models.ModoPago.objects.filter(mpago_acti=True).count() == 0:
    messages.error(request, ('No hay modalidades de pago disponibles.'))
    return redirect(documentos)

  return render(request, 'documentos/create.html', {'form': form, 'empleado': models.Empleado.objects.get(usu_id=request.user.id) if models.Empleado.objects.filter(usu_id=request.user.id).count() > 0 else None, 'clientes': models.Cliente.objects.filter(cli_acti=True), 'productos': models.Producto.objects.filter(prod_acti=True), 'tipos_documento': models.TipoDocumento.objects.filter(tdoc_acti=True), 'modos_pago': models.ModoPago.objects.filter(mpago_acti=True)})


def documentos_print(request):
  return redirect(documentos)


def documentos_excel(request):
  return redirect(documentos)


def documento_print(request):
  return redirect(documentos)

def documento_delete(request, documento_id):
  documento = models.Documento.objects.filter(pk=documento_id)
  if request.method == 'POST':
    documento.update(doc_acti=0)
    messages.success(request, ('Operación realizada con éxito.'))
    return redirect(documentos)

  return render(request, 'documentos/delete.html', {'documento': documento[0]})

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


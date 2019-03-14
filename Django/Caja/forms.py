import re
import datetime
from django import forms
from . import models


class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = models.Empleado
    fields = ['emp_nomb', 'emp_ape1', 'emp_ape2', 'emp_cedu', 'usu_id', 'emp_entra', 'emp_sale', 'hor_id', 'emp_acti']

  def clean(self):
    cleaned_data = super(EmpleadoForm, self).clean()

    emp_cedu = cleaned_data.get('emp_cedu')
    emp_entra = cleaned_data.get('emp_entra')
    emp_sale = cleaned_data.get('emp_sale')
    emp_acti = cleaned_data.get('emp_acti')

    if emp_cedu:
      if len(emp_cedu) == 11:
        if (int(emp_cedu[0:3]) < 122 and int(emp_cedu[0:3]) > 0 or int(emp_cedu[0:3]) == 402):
          suma = 0
          verificador = 0
          mutliplicador = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

          for i in range(10):

            digito = int(emp_cedu[i]) * mutliplicador[i]

            if (digito > 9):
              digito = digito // 10 + digito % 10

            suma = suma + digito

          verificador = (10 - (suma % 10)) % 10

          if not verificador == int(emp_cedu[10]):
            raise forms.ValidationError('Cédula de identidad introducida no es válida')
        else:
          raise forms.ValidationError('Cédula de identidad introducida no es válida')

    if emp_entra:
      if emp_entra > datetime.date.today():
        raise forms.ValidationError("Fecha de entrada no puede ser mayor que la fecha actual.")

    if emp_sale:
      if emp_sale > datetime.date.today():
        raise forms.ValidationError("Fecha de salida no puede ser mayor que la fecha actual.")

      if emp_acti:
        raise forms.ValidationError("Empleado con fecha de salida no puede estar activo.")

      if emp_entra:
        if emp_entra > emp_sale:
          raise forms.ValidationError("Fecha de entrada no puede ser mayor que fecha de salida.")

    else:
      if not emp_acti:
        raise forms.ValidationError("Empleado no puede estar inactivo sin fecha de salida.")

    return cleaned_data


class ClienteForm(forms.ModelForm):
  class Meta:
    model = models.Cliente
    fields = ['cli_nomb', 'cli_ape1', 'cli_ape2', 'tcli_id', 'carr_id', 'cli_acti']


class MovimientoForm(forms.ModelForm):
  class Meta:
    model = models.Movimiento
    fields = ['mov_id', 'doc_id', 'fpago_id', 'mov_monto', 'mov_acti']


class TipoClienteForm(forms.ModelForm):
  class Meta:
    model = models.TipoCliente
    fields = ['tcli_nomb', 'tcli_acti']


class CarreraForm(forms.ModelForm):
  class Meta:
    model = models.Carrera
    fields = ['carr_codi', 'carr_nomb', 'carr_acti']


class HorarioForm(forms.ModelForm):
  class Meta:
    model = models.Horario
    fields = ['hor_nomb', 'hor_entra', 'hor_sale', 'hor_acti']

  def clean(self):
    cleaned_data = super(HorarioForm, self).clean()

    hor_entra = cleaned_data.get('hor_entra')
    hor_sale = cleaned_data.get('hor_sale')

    if hor_entra and hor_sale:
      if hor_entra >= hor_sale:
        raise forms.ValidationError("Hora de entrada no puede ser mayor ni igual que la hora de salida.")

    return cleaned_data


class ProductoForm(forms.ModelForm):
  class Meta:
    model = models.Producto
    fields = ['prod_nomb', 'prod_prec', 'prod_acti']


class FormaPagoForm(forms.ModelForm):
  class Meta:
    model = models.FormaPago
    fields = ['fpago_nomb', 'fpago_acti']


class ModoPagoForm(forms.ModelForm):
  class Meta:
    model = models.ModoPago
    fields = ['mpago_nomb', 'mpago_cuot', 'mpago_inte', 'mpago_acti']


class TipoDocumentoForm(forms.ModelForm):
  class Meta:
    model = models.TipoDocumento
    fields = ['tdoc_nomb', 'tdoc_acti']


import re
from django import forms
from . import models


class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = models.Empleado
    fields = ['emp_nomb', 'emp_ape1', 'emp_ape2', 'emp_cedu', 'usu_id', 'emp_entra', 'emp_sale', 'hor_id', 'emp_acti']


class ClienteForm(forms.ModelForm):
  class Meta:
    model = models.Cliente
    fields = ['cli_nomb', 'cli_ape1', 'cli_ape2', 'tcli_id', 'carr_id', 'cli_acti']


class MovimientoForm(forms.ModelForm):
  class Meta:
    model = models.Movimiento
    fields = ['emp_id', 'cli_id', 'prod_id', 'tdoc_id', 'fpago_id', 'mpago_id', 'mov_monto', 'mov_acti']


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

  def clean_hor_nomb(self):
    nombre_horario=self.cleaned_data['hor_nomb']
    if not re.match('^[a-zA-Z0-9_]+$', nombre_horario):
      raise forms.ValidationError("Nombre sólo puede contener carácteres alfanuméricos.")
    return nombre_horario

  def clean_hor_sale(self):
    if self.cleaned_data['hor_entra'] >= self.cleaned_data['hor_sale']:
      raise forms.ValidationError("Hora de entrada no puede ser mayor o igual que la hora de salida.")
    return self.cleaned_data['hor_sale']


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


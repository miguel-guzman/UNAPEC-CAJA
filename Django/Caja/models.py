from django.db import models
from django.contrib.auth.models import User

class TipoCliente(models.Model):
    tcli_id = models.AutoField(primary_key=True)
    tcli_nomb = models.CharField(max_length=30)
    tcli_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipo_cliente'


class Carrera(models.Model):
    carr_id = models.AutoField(primary_key=True)
    carr_codi = models.CharField(max_length=3)
    carr_nomb = models.CharField(max_length=30)
    carr_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'carrera'


class Producto(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_nomb = models.CharField(max_length=30)
    prod_prec = models.DecimalField(max_digits=12, decimal_places=2)
    prod_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'producto'


class Horario(models.Model):
    hor_id = models.AutoField(primary_key=True)
    hor_nomb = models.CharField(max_length=30)
    hor_entra = models.TimeField()
    hor_sale = models.TimeField()
    hor_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'horario'


class FormaPago(models.Model):
    fpago_id = models.AutoField(primary_key=True)
    fpago_nomb = models.CharField(max_length=30)
    fpago_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'forma_pago'


class ModoPago(models.Model):
    mpago_id = models.AutoField(primary_key=True)
    mpago_nomb = models.CharField(max_length=30)
    # Cuotas
    mpago_cuot = models.IntegerField()
    # Interés
    mpago_inte = models.DecimalField(max_digits=5, decimal_places=2)
    mpago_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'modo_pago'


class TipoDocumento(models.Model):
    tdoc_id = models.AutoField(primary_key=True)
    tdoc_nomb = models.CharField(max_length=30)
    tdoc_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipo_documento'


class Empleado(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_nomb = models.CharField(max_length=60)
    emp_ape1 = models.CharField(max_length=30)
    emp_ape2 = models.CharField(max_length=30, blank=True, null=True)
    # Cédula de Identidad
    emp_cedu = models.CharField(max_length=11, blank=True, null=True)
    usu_id = models.OneToOneField(User, on_delete=models.DO_NOTHING, db_column='usu_id')
    emp_entra = models.DateField()
    emp_sale = models.DateField(blank=True, null=True)
    hor_id = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, db_column='hor_id')
    emp_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'empleado'


class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nomb = models.CharField(max_length=60)
    cli_ape1 = models.CharField(max_length=30)
    cli_ape2 = models.CharField(max_length=30, blank=True, null=True)
    tcli_id = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING, db_column='tcli_id')
    carr_id = models.ForeignKey(Carrera, on_delete=models.DO_NOTHING, db_column='carr_id')
    cli_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'cliente'


class Movimiento(models.Model):
    mov_id = models.AutoField(primary_key=True)
    mov_fecha = models.DateTimeField(auto_now_add=True)
    emp_id = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='emp_id')
    cli_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='cli_id')
    prod_id = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, db_column='prod_id')
    tdoc_id = models.ForeignKey(TipoDocumento, on_delete=models.DO_NOTHING, db_column='tdoc_id')
    fpago_id = models.ForeignKey(FormaPago, on_delete=models.DO_NOTHING, db_column='fpago_id')
    mpago_id = models.ForeignKey(ModoPago, on_delete=models.DO_NOTHING, db_column='mpago_id')
    mov_monto = models.DecimalField(max_digits=12, decimal_places=2)
    mov_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'movimiento'


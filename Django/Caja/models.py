from django.db import models


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
    emp_cedu = models.CharField(max_length=11, blank=True, null=True)
    emp_entra = models.DateField()
    emp_sale = models.DateField(blank=True, null=True)
    hor_id = models.ForeignKey('Horario', models.DO_NOTHING)
    emp_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'empleado'


class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nomb = models.CharField(max_length=30)
    tcli_id = models.ForeignKey('TipoCliente', models.DO_NOTHING)
    carr_id = models.ForeignKey(Carrera, models.DO_NOTHING)
    cli_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'cliente'


class Movimiento(models.Model):
    mov_id = models.AutoField(primary_key=True)
    mov_fecha = models.DateTimeField()
    emp_id = models.ForeignKey(Empleado, models.DO_NOTHING)
    cli_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    prod_id = models.ForeignKey(Producto, models.DO_NOTHING)
    tdoc_id = models.ForeignKey(TipoDocumento, models.DO_NOTHING)
    fpago_id = models.ForeignKey(FormaPago, models.DO_NOTHING)
    mov_monto = models.DecimalField(max_digits=12, decimal_places=2)
    mov_acti = models.BooleanField(default=True)

    class Meta:
        db_table = 'movimiento'


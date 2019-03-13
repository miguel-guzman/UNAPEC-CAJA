"""UNAPEC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de', views.acerca_de, name="acerca_de"),
    path('empleados', views.empleados, name="empleados"),
    path('empleado/create', views.empleado_create, name="empleado_create"),
    path('empleado/update/<empleado_id>', views.empleado_update, name="empleado_update"),
    path('empleado/delete/<empleado_id>', views.empleado_delete, name="empleado_delete"),
    path('clientes', views.clientes, name="clientes"),
    path('cliente/create', views.cliente_create, name="cliente_create"),
    path('cliente/update/<cliente_id>', views.cliente_update, name="cliente_update"),
    path('cliente/delete/<cliente_id>', views.cliente_delete, name="cliente_delete"),
    path('movimientos', views.movimientos, name="movimientos"),
    path('movimiento/create', views.movimiento_create, name="movimiento_create"),
    path('movimiento/update/<movimiento_id>', views.movimiento_update, name="movimiento_update"),
    path('movimiento/delete/<movimiento_id>', views.movimiento_delete, name="movimiento_delete"),
    path('tipos-cliente', views.tipos_cliente, name="tipos_cliente"),
    path('tipo-cliente/create', views.tipo_cliente_create, name="tipo_cliente_create"),
    path('tipo-cliente/update/<tipo_cliente_id>', views.tipo_cliente_update, name="tipo_cliente_update"),
    path('tipo-cliente/delete/<tipo_cliente_id>', views.tipo_cliente_delete, name="tipo_cliente_delete"),
    path('carreras', views.carreras, name="carreras"),
    path('carrera/create', views.carrera_create, name="carrera_create"),
    path('carrera/update/<carrera_id>', views.carrera_update, name="carrera_update"),
    path('carrera/delete/<carrera_id>', views.carrera_delete, name="carrera_delete"),
    path('productos', views.productos, name="productos"),
    path('producto/create', views.producto_create, name="producto_create"),
    path('producto/update/<producto_id>', views.producto_update, name="producto_update"),
    path('producto/delete/<producto_id>', views.producto_delete, name="producto_delete"),
    path('horarios', views.horarios, name="horarios"),
    path('horario/create', views.horario_create, name="horario_create"),
    path('horario/update/<horario_id>', views.horario_update, name="horario_update"),
    path('horario/delete/<horario_id>', views.horario_delete, name="horario_delete"),
    path('formas-pago', views.formas_pago, name="formas_pago"),
    path('forma-pago/create', views.forma_pago_create, name="forma_pago_create"),
    path('forma-pago/update/<forma_pago_id>', views.forma_pago_update, name="forma_pago_update"),
    path('forma-pago/delete/<forma_pago_id>', views.forma_pago_delete, name="forma_pago_delete"),
    path('modos-pago', views.modos_pago, name="modos_pago"),
    path('modo-pago/create', views.modo_pago_create, name="modo_pago_create"),
    path('modo-pago/update/<modo_pago_id>', views.modo_pago_update, name="modo_pago_update"),
    path('modo-pago/delete/<modo_pago_id>', views.modo_pago_delete, name="modo_pago_delete"),
    path('tipos-documento', views.tipos_documento, name="tipos_documento"),
    path('tipo-documento/create', views.tipo_documento_create, name="tipo_documento_create"),
    path('tipo-documento/update/<tipo_documento_id>', views.tipo_documento_update, name="tipo_documento_update"),
    path('tipo-documento/delete/<tipo_documento_id>', views.tipo_documento_delete, name="tipo_documento_delete"),
    path('usuarios/cerrar-sesion', views.usuario_cerrar_sesion, name="usuario_cerrar_sesion"),
    path(r'^export/csv/$', views.export_emp_csv, name='export_emp_csv'),
]

from django.contrib import admin
from proveedores.models import Proveedor, Factura, Pago, LineaFactura
from proveedores.forms import ProveedorForm, FacturaForm
from proveedores.forms import PagoForm, LineaForm


class AdminProveedor(admin.ModelAdmin):
    form = ProveedorForm

    list_display = ['nombre', 'razon_social', 'cuil', 'email',
                    'telefono', 'saldo']
    # readonly_fields = ['fecha_alta']
    search_fields = ['dni', 'razon_social', 'nombre']
    #  list_filter = ['apellido', 'saldo']
    titulo = 'Datos del proveedor'
    fieldsets = [(titulo, {'fields': [('dni', 'cuil'), 'nombre',
                                      'razon_social',
                                      'domicilio',
                                      ('telefono', 'email'),
                                      'saldo',
                                      ]
                           }
                  ),
                 ]


class AdminFactura(admin.ModelAdmin):
    form = FacturaForm
    list_display = ['id', 'proveedor', 'tipo', 'fecha_alta', 'detalle']
    search_fields = ['proveedor']
    list_filter = ['tipo', 'fecha_alta']
    titulo = 'Detalle de la Factura'
    fieldsets = [(titulo, {'fields': ['proveedor', 'tipo', 'fecha_vencimiento',
                                      'detalle'
                                      ]

                           }
                  ),
                 ]


class AdminPago(admin.ModelAdmin):
    form = PagoForm
    list_display = ['id', 'factura', 'fecha_alta', 'detalle', 'medio', 'monto']
    search_fields = ['medio']
    list_filter = ['medio', 'fecha_alta']
    titulo = 'Detalle del pago'
    fieldsets = [(titulo, {'fields': ['factura', 'medio', 'detalle', 'monto']
                           }
                  ),
                 ]


class AdminLinea(admin.ModelAdmin):
    form = LineaForm
    list_display = ['factura', 'id', 'detalle', 'monto']
    titulo = 'Detalle de la linea'
    fieldsets = [(titulo, {'fields': ['factura', 'detalle', 'monto']
                           }
                  ),
                 ]


admin.site.register(Proveedor, AdminProveedor)
admin.site.register(Factura, AdminFactura)
admin.site.register(LineaFactura, AdminLinea)
admin.site.register(Pago, AdminPago)

from django.contrib import admin
from clientes.forms import ClienteForm, FacturaForm
from clientes.forms import CobroForm, LineaForm
from clientes.models import Cliente, Factura, Cobro, LineaFactura


class AdminCliente(admin.ModelAdmin):
    form = ClienteForm

    list_display = ['dni', 'apellido', 'nombre', 'razon_social', 'email',
                    'telefono', 'saldo']
    # readonly_fields = ['fecha_alta']
    search_fields = ['dni', 'razon_social', 'apellido', 'nombre']
    list_filter = ['apellido', 'saldo']
    titulo = 'Datos personales'
    fieldsets = [(titulo, {'fields': [('dni', 'cuil'), ('apellido', 'nombre'),
                                      'razon_social',
                                      'fecha_nacimiento', 'domicilio',
                                      ('telefono', 'email'),
                                      'saldo',
                                      ]
                           }
                  ),
                 ]


class AdminFactura(admin.ModelAdmin):
    form = FacturaForm
    list_display = ['id', 'cliente', 'tipo', 'fecha_alta', 'detalle']
    search_fields = ['cliente']
    list_filter = ['tipo', 'fecha_alta']
    titulo = 'Detalle de la Factura'
    fieldsets = [(titulo, {'fields': ['cliente', 'tipo', 'fecha_vencimiento',
                                      'detalle'
                                      ]

                           }
                  ),
                 ]


class AdminCobro(admin.ModelAdmin):
    form = CobroForm
    list_display = ['id', 'factura', 'fecha_alta', 'detalle', 'medio', 'monto']
    search_fields = ['medio']
    list_filter = ['medio', 'fecha_alta']
    titulo = 'Detalle del cobro'
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


admin.site.register(Cliente, AdminCliente)
admin.site.register(Factura, AdminFactura)
admin.site.register(Cobro, AdminCobro)
admin.site.register(LineaFactura, AdminLinea)

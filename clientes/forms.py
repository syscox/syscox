from django import forms
from clientes.models import Cliente, Factura, Cobro, LineaFactura


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['apellido', 'nombre', 'razon_social', 'dni', 'cuil',
                  'fecha_nacimiento',
                  'telefono', 'domicilio', 'email', 'saldo'
                  ]


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'tipo', 'fecha_vencimiento', 'detalle']


class CobroForm(forms.ModelForm):
    class Meta:
        model = Cobro
        fields = ['factura', 'detalle', 'medio', 'monto']


class LineaForm(forms.ModelForm):
    class Meta:
        model = LineaFactura
        fields = ['factura', 'detalle', 'monto']

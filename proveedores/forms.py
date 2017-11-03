from django import forms
from proveedores.models import Proveedor, Factura, Pago, LineaFactura


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'razon_social', 'dni', 'cuil',
                  'telefono', 'domicilio', 'email', 'saldo'
                  ]


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['proveedor', 'tipo', 'fecha_vencimiento', 'detalle']


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['factura', 'detalle', 'medio', 'monto']


class LineaForm(forms.ModelForm):
    class Meta:
        model = LineaFactura
        fields = ['factura', 'detalle', 'monto']

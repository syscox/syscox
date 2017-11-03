from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    cuil = models.CharField(max_length=13, unique=True)
    fecha_alta = models.DateTimeField(
        auto_now_add=True, auto_now=False, editable=False)
    email = models.EmailField(default='ejemplo@gmail.com')
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    saldo = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Proveedores'
        verbose_name = 'Proveedor'


class Factura(models.Model):
    FA = 'A'  # esto va en la BD
    FB = 'B'
    FC = 'C'

    tipoFactura = (
        (FA, 'Factura A'),  # string se muestra en el admin
        (FB, 'Factura B'),
        (FC, 'Factura C')
    )

    fecha_alta = models.DateTimeField(
        auto_now_add=True, auto_now=False, editable=False)
    fecha_vencimiento = models.DateField()
    # hay otra fecha mas en la caputra
    proveedor = models.ForeignKey(Proveedor)
    tipo = models.CharField(max_length=1, choices=tipoFactura, default=FB)
    detalle = models.TextField(max_length=50)

    def __str__(self):
        return 'Factura ' + str(self.id)

    class Meta:
        ordering = ["fecha_alta"]
        verbose_name = 'Factura'


class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura)  # donde mierda va esta foranea e.e
    detalle = models.TextField(max_length=50)
    monto = models.FloatField(default=0)

    def __str__(self):
        nrofac = self.factura
        return "linea " + str(self.id) + ' - ' + str(nrofac)


class Pago(models.Model):
    EF = 'EF'
    TC = 'TC'
    CEC = 'CRC'
    CED = 'CRD'
    CDT = 'CET'
    TF = 'TF'

    tipoMedios = (
        (CDT, 'Cheque de tercero'),
        (CEC, 'Cheque emitido comun'),
        (CED, 'Cheque emitido diferido'),
        (EF, 'Efectivo'),
        (TC, 'Tarjeta de Credito'),
        (TF, 'Transferencia'),
    )

    factura = models.ForeignKey(Factura)
    monto = models.FloatField(default=0)
    fecha_alta = models.DateTimeField(
        auto_now_add=True, auto_now=False, editable=False)
    detalle = models.TextField(max_length=50)
    medio = models.CharField(max_length=3, choices=tipoMedios, default=EF)

    def __str__(self):
        return "Pago" + " " + str(self.id)

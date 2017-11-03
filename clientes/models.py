from django.db import models


class Cliente(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    cuil = models.CharField(max_length=13, unique=True)
    fecha_nacimiento = models.DateField(
        null=False, blank=False, help_text="DD/MM/AAAA")
    fecha_alta = models.DateTimeField(
        auto_now_add=True, auto_now=False, editable=False)
    email = models.EmailField(default='ejemplo@gmail.com')
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    saldo = models.FloatField(default=0)

    def __str__(self):
        return self.apellido + " " + self.nombre

    class Meta:
        ordering = ["apellido"]
        verbose_name = 'Cliente'


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
    cliente = models.ForeignKey(Cliente)
    tipo = models.CharField(max_length=1, choices=tipoFactura, default=FB)
    detalle = models.TextField(max_length=50)

    def __str__(self):
        return 'Factura ' + str(self.id)

    #  def fecha(self):
    #    return self.fecha_alta.date()

    class Meta:
        ordering = ["-fecha_alta"]
        verbose_name = 'Factura'


class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura)  # donde mierda va esta foranea
    detalle = models.TextField(max_length=50)
    monto = models.FloatField(default=0)

    def __str__(self):
        nrofac = self.factura
        return "linea " + str(self.id) + ' - ' + str(nrofac)


class Cobro(models.Model):
    EF = 'EF'
    TC = 'TC'
    CRC = 'CRC'
    CRD = 'CRD'
    TF = 'TF'

    tipoMedios = (
        (CRC, 'Cheque recibido comun'),
        (CRD, 'Cheque recibido diferido'),
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
        return "Cobro" + " " + str(self.id)

    class Meta:
        ordering = ["-fecha_alta"]
        verbose_name = 'Cobro'

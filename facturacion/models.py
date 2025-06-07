from django.db import models

class Cliente(models.Model):
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula'),
        ('NIT', 'NIT'),
        ('CE', 'Cédula Extranjería'),
    ]

    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO)
    numero_documento = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.numero_documento})"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje (ej: 19%)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    numero_factura = models.CharField(max_length=50, unique=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.cliente.nombre}"

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class UsuarioRegistro(models.Model):
    tipo_usuario = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100, blank=True)
    tipo_documento = models.CharField(max_length=20)
    numero_documento_1 = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    regimen = models.CharField(max_length=100, blank=True)
    responsabilidad = models.CharField(max_length=100, blank=True)
    obligaciones_dian = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre_completo

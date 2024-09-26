# biblioteca\apps\maestros\models\models_base.py
from django.db import models
from apps.maestros.models.base_gen_models import ModeloBaseGenerico


# -- Datos estándares aplicables a los modelos.
ESTATUS_GEN = [
    (True, 'Activo'),
    (False, 'Inactivo'),
]

# Modelo TipoBiblioteca - Tipos de Biblioteca
class TipoBiblioteca(ModeloBaseGenerico):
    id_tipo_biblioteca = models.AutoField(primary_key=True)
    estatus_tipo_biblioteca = models.BooleanField("Estatus", default=True,
                                                choices=ESTATUS_GEN)
    nombre_tipo_biblioteca = models.CharField("Nombre Biblioteca", max_length=50,
                                      null=True, blank=True)
    
    def __str__(self):
        return self.nombre_tipo_biblioteca

    class Meta:
        db_table = 'tipo_biblioteca'
        verbose_name = ('Tipo de Biblioteca')
        verbose_name_plural = ('Tipos de Biblioteca')
        ordering = ['nombre_tipo_biblioteca']


# Modelo Categoria - Categoría
class Categoria(ModeloBaseGenerico):
    id_categoria = models.AutoField(primary_key=True)
    estatus_categoria = models.BooleanField("Estatus", default=True,
                                                choices=ESTATUS_GEN)
    id_tipo_biblioteca = models.ForeignKey(TipoBiblioteca,
                                         on_delete=models.PROTECT,
                                         null=True, blank=True)
    nombre_categoria = models.CharField("Categoría", max_length=50,
                                      null=True, blank=True)
    
    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'categoria'
        verbose_name = ('Categoría')
        verbose_name_plural = ('Categoría')
        ordering = ['nombre_categoria']


# Modelo SubCategoria - Sub Categoría
class SubCategoria(ModeloBaseGenerico):
    id_subcategoria_producto = models.AutoField(primary_key=True)
    estatus_subcategoria = models.BooleanField("Estatus", default=True,
                                                    choices=ESTATUS_GEN)
    id_tipo_biblioteca = models.ForeignKey(TipoBiblioteca,
                                         on_delete=models.PROTECT,
                                         null=True, blank=True)
    id_categoria = models.ForeignKey(Categoria,
                                         on_delete=models.PROTECT,
                                         null=True, blank=True)
    nombre_subcategoria = models.CharField("Sub Categoría", max_length=20,
                                          null=True, blank=True)

    def __str__(self):
        return self.nombre_subcategoria

    class Meta:
        db_table = 'sub_categoria'
        verbose_name = ('Sub Categoría')
        verbose_name_plural = ('Sub Categorías')
        ordering = ['nombre_subcategoria']
        

# Modelo TipoDocumento - Tipo de Documento
class TipoDocumento(ModeloBaseGenerico):
    id_tipo_documento = models.AutoField(primary_key=True)
    estatus_tipo_documento = models.BooleanField("Estatus", default=True,
                                        choices=ESTATUS_GEN)
    nombre_tipo_documento = models.CharField("Tipo de Documento", max_length=40, null=True,
                                    blank=True)

    def __str__(self):
        return self.nombre_tipo_documento

    class Meta:
        db_table = 'tipo_documento'
        verbose_name = ('Tipo de Documento')
        verbose_name_plural = ('Tipos de Documento')
        ordering = ['nombre_tipo_documento']

        
# Modelo TipoEditor - Tipos de Editor
class TipoEditor(ModeloBaseGenerico):
    id_tipo_editor = models.AutoField(primary_key=True)
    estatus_tipo_editor = models.BooleanField("Estatus", default=True,
                                        choices=ESTATUS_GEN)
    nombre_tipo_editor = models.CharField("Tipo de Editor", max_length=40, null=True,
                                    blank=True)
    observacion_tipo_editor = models.CharField("Observaciones", max_length=80, null=True,
                                    blank=True)

    def __str__(self):
        return self.nombre_tipo_editor

    class Meta:
        db_table = 'editor'
        verbose_name = ('Tipo de Editor')
        verbose_name_plural = ('Tipos de Editor')
        ordering = ['nombre_tipo_editor']


# Modelo Pais - Pais
class Pais(ModeloBaseGenerico):
    CONTINENTES = (
        ("América", "América"),
        ("Europa", "Europa"),
        ("Asia", "Asia"),
        ("África", "África"),
        ("Oceanía", "Oceanía"),
        ("Antártida", "Antártida"),
        ("", "Seleccione una opción"))

    id_pais = models.AutoField(primary_key=True)
    estatus_pais = models.BooleanField("Estatus", default=True,
                                       choices=ESTATUS_GEN)
    nombre_pais = models.CharField("País", max_length=100, null=True,
                                   blank=True)
    nombre_pais_ingles = models.CharField("Country", max_length=100, null=True,
                                          blank=True)
    nombre_pais_frances = models.CharField("Pays", max_length=100, null=True,
                                           blank=True)
    continente = models.CharField("Continente", max_length=15,
                                  choices=CONTINENTES, default="América")
    codigo_telefonico = models.CharField("Código Telefónico", max_length=5,
                                         null=True, blank=True)
    codigo_iso2 = models.CharField("Código ISO2", max_length=2, null=True,
                                   blank=True)
    codigo_iso3 = models.CharField("Código ISO3", max_length=3, null=True,
                                   blank=True)

    def __str__(self):
        return f"{self.nombre_pais} - {self.codigo_telefonico}"

    class Meta:
        db_table = 'pais'
        verbose_name = ('País')
        verbose_name_plural = ('Paises')
        ordering = ['nombre_pais']
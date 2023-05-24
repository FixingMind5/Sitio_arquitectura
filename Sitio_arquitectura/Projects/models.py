from django.db import models

from Biographies.models import Biography

TYPE_OF_URBAN_PLACES_CHOICES = [
    ("COL", "Colonias"), 
    ("PLAZAS Y PARQUES", "Plazas y Parques"),
    ("VIA", "Vialidades")
] 
BUILDING_CHOICES = [
    ("NA", "None"), 
    ("PLANT", "Architectural plant"),
    ("FACADES", "facades"), 
    ("OR", "ornaments")
]


class Location(models.Model):
    
    latitude = models.DecimalField(max_digits=10, decimal_places=10)
    altitude = models.DecimalField(max_digits=10, decimal_places=10)
    longitude = models.DecimalField(max_digits=10, decimal_places=10)


class Project(models.Model):
    """Tabla Projecto
    Almacena los datos esenciales de los tipos de proyecto, ya sea por edificio o por espacio urbano.

    name: El nombre del proyecto
    year_of_construction: año de construcción
    address: dirección en cadena de texto
    historical_context: descripción del contexto temporal en el que existió
    urban_space_transformation: manera en la que el espacio urbano se ha transformado al paso del tiempo
    """

    name = models.CharField(max_length=350)
    year_of_construction = models.DateField()
    adress = models.TextField()
    historical_context = models.TextField()
    urban_space_transformation = models.TextField()
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
    )
    project_designer = models.ManyToManyField(
        Biography
    )


class Building(Project):
    """Tabla Edifico
    
    Hereda de Projecto por lo que tiene sus propiedades más las propiedades particulares.
    """
    gender = models.TextField(help_text="Género al que pertenece la corriente artistica del edificio")
    typology = models.TextField()
    current_use = models.TextField()
    concept = models.TextField()
    stylistic_current = models.TextField()

    surrounding_buildings = models.ManyToManyField(
        'Projects.UrbanSpace',
        # vebose_name="surrounding buildings"
    )


class UrbanSpace(Project):
    role = models.TextField()
    urban_policy = models.TextField(
        help_text= (
            "Plan urbanistico o política urbana del cual surgió "
            "(sie es parte de un plan de Gobierno, de expansión urbana u otros)"
        )
    )
    type_of_place = models.CharField(max_length=200, choices=TYPE_OF_URBAN_PLACES_CHOICES)
    special_features = models.TextField()
    orientation = models.TextField()
    dimensions = models.FloatField(
        help_text=("longitud o área según sea el caso")
    )
    section = models.TextField()
    urban_image_element = models.TextField()
    surrounding_buildings = models.ManyToManyField(
        Building,
        # vebose_name="surrounding buildings"
    )
    design_princples = models.TextField()
    relevance = models.TextField()


class Image(models.Model):
    content_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    url = models.URLField()
    alt = models.CharField(max_length=300)
    kind_of_element = models.CharField(max_length=200, choices=BUILDING_CHOICES)
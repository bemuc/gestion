import django_filters 
from django_filters import DateFilter, CharFilter

from .models import *

class ClientFilter(django_filters.FilterSet):
    # nom = CharFilter(field_name="nom",lookup_expr='icontains')
    # type = CharFilter(field_name="type",lookup_expr='icontains')
    # start_date = DateFilter(field_name="dateAtri",lookup_expr='gte')
    # end_date = DateFilter(field_name="date_created",lookup_expr='lte')
    # note = CharFilter(field_name="note",lookup_expr='icontains')

    class Meta:
        model = Client
        fields =  ['type','nom','nif','dateAtri']
        # exclude = ['status']

class ffNumeroFilter(django_filters.FilterSet):
    # nom = CharFilter(field_name="nom",lookup_expr='icontains')
    # type = CharFilter(field_name="type",lookup_expr='icontains')
    # start_date = DateFilter(field_name="dateAtri",lookup_expr='gte')
    class Meta:
        model = FF_Numero
        fields = ['client', 'dateAtri']

class numCourtFilter(django_filters.FilterSet):
    # Client = CharFilter(field_name="client",lookup_expr='icontains')
    # Type = CharFilter(field_name="type",lookup_expr='icontains')
    # Numero = CharFilter(field_name="numero",lookup_expr='icontains')
    # Date = DateFilter(field_name="dateAtri",lookup_expr='gte')
    class Meta:
        model = NumeroCourt
        fields = ['client', 'type','numero','dateAtri']

class certAgrFilter(django_filters.FilterSet):
    class Meta:
        model = CertAgr
        fields = ['client','dateAttri']

class certConfFilter(django_filters.FilterSet):
    class Meta:
        model = CertConf
        fields = ['client','dateAttri']

class HomoloEquiFilter(django_filters.FilterSet):
    class Meta:
        model = HomologationEqui
        fields = ['client','dateAttri']

class equipementFilter(django_filters.FilterSet):
    class Meta:
        model = Equipement
        # fields = ['constructeur','designation','marque','type','modele','pays_origine']
        fields = '__all__'

class constructeurFilter(django_filters.FilterSet):
    class Meta:
        model = Constructeur
        fields = ['nom']

class fhFilter(django_filters.FilterSet):
    class Meta:
        model = FaisceauxHertzien
        fields = ['client','dateAtri']

class fhAnnFilter(django_filters.FilterSet):
    class Meta:
        model = Repere
        fields = ['client']

class ffNumeroFilter(django_filters.FilterSet):
    class Meta:
        model = FF_Numero
        fields = ['client','dateAtri']

class certAgrAfFilter(django_filters.FilterSet):
    class Meta:
        model = CertAgr
        fields = ['client','dateAttri']

class certConfAfFilter(django_filters.FilterSet):
    class Meta:
        model = CertConf
        fields = ['client','dateAttri']

class certHomoAfFilter(django_filters.FilterSet):
    class Meta:
        model = HomologationEqui
        fields = ['client','dateAttri']

class fhAfFilter(django_filters.FilterSet):
    class Meta:
        model = FaisceauxHertzien
        fields = ['client','dateAtri']

class fhAnnAfFilter(django_filters.FilterSet):
    class Meta:
        model = Repere
        fields = ['client','dateAtri']
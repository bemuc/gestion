import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ClientFilter(django_filters.FilterSet):
    # nom = CharFilter(field_name="nom",lookup_expr='icontains')
    # type = CharFilter(field_name="type",lookup_expr='icontains')
    # start_date = DateFilter(field_name="date_created",lookup_expr='gte')
    # end_date = DateFilter(field_name="date_created",lookup_expr='lte')
    # note = CharFilter(field_name="note",lookup_expr='icontains')

    class Meta:
        model = Client
        fields =  ['type','nom','nif']
        # exclude = ['status']
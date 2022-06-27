from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Client)
admin.site.register(CertAgr)

admin.site.register(Constructeur)
admin.site.register(Equipement)
admin.site.register(HomologationEqui)
admin.site.register(NumeroCourt)
admin.site.register(PQ)
admin.site.register(AB)
# admin.site.register(Megas)
# admin.site.register(Minutes)
# admin.site.register(ChiffreAffaire)
# @admin.register(ChiffreAffaire)
class TauxAdmin(admin.ModelAdmin):
    list_display = ['client','ca','dateAtri']
    ordering = ['client','dateAtri']


@admin.register(Client)
class TauxAdmin(admin.ModelAdmin):
    list_display = ['id','nom','type','status']
    # ordering = ['client','dateAtri']
# admin.site.register(CertConf)
@admin.register(CertConf)
class TauxAdmin(admin.ModelAdmin):
    list_display = ['client','pourfact','facturer','etat']


@admin.register(TarifFFNumero)
class TauxAdmin(admin.ModelAdmin):
    list_display = ['type','etat']

    
# admin.site.register(FrequenceRadio)
admin.site.register(FaisceauxHertzien)
admin.site.register(FF_Numero)
admin.site.register(Taux)
admin.site.register(Facture_FFNumero)


admin.site.register(Facture_CertAgr)
admin.site.register(TarifAgre)
admin.site.register(TarifConf)
admin.site.register(FactureConf)
admin.site.register(TarifHom)
admin.site.register(FactureHom)
# admin.site.register(TarifFH)
@admin.register(TarifFH)
class TauxAdmin(admin.ModelAdmin):
    list_display = ['nature','p_canal','p_mhz','etat','dateAtri']
    ordering = ['-nature']
admin.site.register(Facture_FH)
admin.site.register(ListeFHAnnuelle)
admin.site.register(Repere)
admin.site.register(PersonneContact)
# admin.site.register(Direction)







# admin.site.register(TarifFFNumero)









# admin.site.register(Service)
# admin.site.register(Exploite)
# admin.site.register(PersonneContact)

# admin.site.register(Category)
# @admin.register(Taux)
# class TauxAdmin(admin.ModelAdmin):
#     list_display = ['taux','date']


from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms

from .models import *

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['status','dateAtri']
        widgets = {
            'type': forms.Select(attrs={'class':'form-control', }),
            'nom' : forms.TextInput(attrs={'class':'form-control',}),
            'adresse' : forms.TextInput(attrs={'class':'form-control',}),
            'téléphone' : forms.TextInput(attrs={'class':'form-control',}),
            'fax' : forms.TextInput(attrs={'class':'form-control', }),
            'email' : forms.EmailInput(attrs={'class':'form-control', }),
            'siteweb' : forms.TextInput(attrs={'class':'form-control', }),
            'boite_postale' : forms.TextInput(attrs={'class':'form-control', }),
            'nif' : forms.TextInput(attrs={'class':'form-control', }),
            }

class PersonneContactForm(ModelForm):
    class Meta:
        model = PersonneContact
        fields = '__all__'
        exclude = ['etat','dateAtri']
        widgets = {
            'client': forms.Select(attrs={'class':'form-control', }),
            'nom' : forms.TextInput(attrs={'class':'form-control',}),
            'telephone' : forms.TextInput(attrs={'class':'form-control',}),
            'email' : forms.EmailInput(attrs={'class':'form-control', }),
            'poste' : forms.TextInput(attrs={'class':'form-control', }),
            }

class CertAgreForm(ModelForm):
    def __init__(self, *args, **kwargs):
       super(CertAgreForm, self).__init__(*args, **kwargs)
       self.fields['nature'].widget.attrs['readonly'] = True
    class Meta:
        model = CertAgr
        fields = '__all__'
        exclude = ['etat','porfact','facturer']
        widgets = {
            'client': forms.Select(attrs={'class':'form-control',}),
            # 'contact': forms.Select(attrs={'class':'form-control',}),
            # 'category' : forms.Select(attrs={'class':'form-control',}),
            'type' : forms.Select(attrs={'class':'form-control',}),
            'nature' : forms.TextInput(attrs={'class':'form-control',}),
            'dateAttri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class TarifAgreForm(ModelForm):
     class Meta:
        model = TarifAgre
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'type' : forms.Select(attrs={'class':'form-control'}),
            'tarifs': forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
        }


class CertConfForm(ModelForm):
    def __init__(self, *args, **kwargs):
       super(CertConfForm, self).__init__(*args, **kwargs)
       self.fields['nature'].widget.attrs['readonly'] = True
    class Meta:
        model = CertConf
        fields = '__all__'
        exclude = ['etat','pourfact','facturer']
        widgets = {
            'client': forms.Select(attrs={'class':'form-control',}),
            'type' : forms.Select(attrs={'class':'form-control',}),
            'nature' : forms.TextInput(attrs={'class':'form-control',}),
            'dateAttri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class TarifConfForm(ModelForm):
     class Meta:
        model = CertConf
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'type' : forms.Select(attrs={'class':'form-control'}),
            'tarif': forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
        }

class FactureConfForm(ModelForm):
    class Meta:
        model = FactureConf
        fields = '__all__'
        exclude = ['etat','pourfact','facturer','date']
        widgets = {
            'certificat': forms.Select(attrs={'class':'form-control',}),
            'tarif' : forms.Select(attrs={'class':'form-control',}),
            'taux' : forms.Select(attrs={'class':'form-control',}),
            'total' : forms.TextInput(attrs={'class':'form-control',}),
            'total_bif' : forms.TextInput(attrs={'class':'form-control',}),
            # 'total_bif' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }



class ConstructeurForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #    super(CertConfForm, self).__init__(*args, **kwargs)
    #    self.fields['nature'].widget.attrs['readonly'] = True
    class Meta:
        model = Constructeur
        fields = '__all__'
        exclude = ['etat','date_creation']
        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control',}),
            'adresse' : forms.TextInput(attrs={'class':'form-control',}),
            'téléphone' : forms.TextInput(attrs={'class':'form-control',}),
            'fax' : forms.TextInput(attrs={'class':'form-control', }),
            'email' : forms.EmailInput(attrs={'class':'form-control', }),
            # 'dateAttri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            # 'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class EquipementForm(ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'
        exclude = ['etat','date_creation']
        widgets = {
            'constructeur' :  forms.Select(attrs={'class':'form-control',}),
            'designation' : forms.TextInput(attrs={'class':'form-control',}),
            'marque' : forms.TextInput(attrs={'class':'form-control',}),
            'type' : forms.TextInput(attrs={'class':'form-control',}),
            'modele' : forms.TextInput(attrs={'class':'form-control', }),
            'pays_origine' : forms.TextInput(attrs={'class':'form-control', }),
            # 'email' : forms.EmailInput(attrs={'class':'form-control', }),
            # 'dateAttri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            # 'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }



class HomologationForm(ModelForm):
    class Meta:
        model = HomologationEqui
        fields = '__all__'
        exclude = ['etat','nature','pourfact','facturer']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'equipement' :  forms.Select(attrs={'class':'form-control',}),
            'categorie' :  forms.Select(attrs={'class':'form-control',}),
            # 'designation' : forms.TextInput(attrs={'class':'form-control',}),
            # 'marque' : forms.TextInput(attrs={'class':'form-control',}),
            # 'type' : forms.TextInput(attrs={'class':'form-control',}),
            # 'modele' : forms.TextInput(attrs={'class':'form-control', }),
            # 'pays_origine' : forms.TextInput(attrs={'class':'form-control', }),
            # 'email' : forms.EmailInput(attrs={'class':'form-control', }),
            'dateAttri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'dateExp' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class TarifHomologation(ModelForm):
     class Meta:
        model = TarifHom
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'type' :  forms.Select(attrs={'class':'form-control'}),
            'tarif': forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
        }



class NumeroCourtForm(ModelForm):
    class Meta:
        model = NumeroCourt
        fields = '__all__'
        exclude = ['ffnumero','etat','dateAtri']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'type' :  forms.Select(attrs={'class':'form-control',}),
            'numero' :  forms.TextInput(attrs={'class':'form-control',}),
            'periode' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0,'max':365}),
            # 'etat' :  forms.TextInput(attrs={'class':'form-control',}),
            # 'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class PQForm(ModelForm):
    class Meta:
        model = PQ
        fields = '__all__'
        exclude = ['etat','dateAtri','ffnumero',]
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'pq' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            # 'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class ABForm(ModelForm):
    class Meta:
        model = AB
        fields = '__all__'
        exclude = ['etat','dateAtri']
        widgets = {
            'pq' :  forms.Select(attrs={'class':'form-control',}),
            'ab' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class MegasForm(ModelForm):
    class Meta:
        model = Megas
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'megas' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class MinutesForm(ModelForm):
    class Meta:
        model = Minutes
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'minutes' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class CAForm(ModelForm):
    class Meta:
        model = ChiffreAffaire
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'ca' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class FrForm(ModelForm):
    class Meta:
        model = FrequenceRadio
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'bande' :  forms.TextInput(attrs={'class':'form-control',}),
            'bande_attribuee' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class FhForm(ModelForm):
    class Meta:
        model = FaisceauxHertzien
        fields = '__all__'
        exclude = ['etat','facturer','efacturer','dateAtri']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control',}),
            'bande' :  forms.TextInput(attrs={'class':'form-control',}),
            'bande_passante' :  forms.TextInput(attrs={'class':'form-control',}),
            'nombre_canaux' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class TFhForm(ModelForm):
    class Meta:
        model = TarifFH
        fields = '__all__'
        exclude = ['etat','dateAtri']
        widgets = {
            'nature' :  forms.Select(attrs={'class':'form-control',}),
            'p_canal' :  forms.TextInput(attrs={'class':'form-control',}),
            'p_mhz' :  forms.TextInput(attrs={'class':'form-control',}),
            # 'nombre_canaux' :  forms.TextInput(attrs={'class':'form-control',}),
            # 'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

class FactureFH_Form(ModelForm):
    class Meta:
        model = Facture_FH
        fields = '__all__'
        exclude = ['dateAtri']
        widgets = {
            'faisceaux' :  forms.Select(attrs={'class':'form-control',}),
            'tarif' :  forms.Select(attrs={'class':'form-control',}),
            'taux' :  forms.Select(attrs={'class':'form-control',}),
            'total_bif' :  forms.TextInput(attrs={'class':'form-control',}),
            'total' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            
        }

class FFacture_FH_A_Form(ModelForm):
    class Meta:
        model = Facture_FH_A
        fields = '__all__'
        exclude = ['dateAtri']
        widgets = {
            'repere' :  forms.Select(attrs={'class':'form-control',}),
            'taux' :  forms.Select(attrs={'class':'form-control',}),
            'total_bif' :  forms.TextInput(attrs={'class':'form-control',}),
            'total' :  forms.TextInput(attrs={'class':'form-control',}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            
        }








class FF_NumeroForm(ModelForm):
    class Meta:
        model = FF_Numero
        fields = '__all__'
        exclude = ['etat','facturer','efacturer','dateAtri']
        widgets = {
            'client' :  forms.Select(attrs={'class':'form-control'}),
            'q_pq' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_ordinaire' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_ussd' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_mnemonique' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_mnc' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_nspc' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_ispc' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'q_cpti' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'periode' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0,'max':365}),
            'RN_etudeDossier' :  forms.CheckboxInput(attrs={'class':'form-control',}),
            'RN_fraisGestion' :  forms.CheckboxInput(attrs={'class':'form-control',}),
            'RN_redevanceAnn' :  forms.CheckboxInput(attrs={'class':'form-control',}),
            'FS_etudeDossier' :  forms.CheckboxInput(attrs={'class':'form-control',}),
            'FS_agreEquipe' :  forms.CheckboxInput(attrs={'class':'form-control',}),
            'FS_autoARCT' :  forms.CheckboxInput(attrs={'class':'form-control'}),
            'nature' :  forms.Select(attrs={'class':'form-control'}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
            'observation' : forms.TextInput(attrs={'class':'form-control'}),
        }


class TarifFFNumeroForm(ModelForm):
    class Meta:
        model = TarifFFNumero
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'type' :  forms.Select(attrs={'class':'form-control'}),
            'etudeDossier' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'fraisGestion' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'redevanceAnn' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class TarifFSVANumeroForm(ModelForm):
    class Meta:
        model = TarifFSVANumero
        fields = '__all__'
        exclude = ['etat']
        widgets = {
            'etudeDossier' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'agrementEquip' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'redevanceAnn' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'autorisationARCT' :  forms.TextInput(attrs={'class':'form-control','type':'number','min':0}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class Facture_FFNumeroForm(ModelForm):
    class Meta:
        model = Facture_FFNumero
        fields = '__all__'
        widgets = {
            'ffnumero' :  forms.Select(attrs={'class':'form-control'}),
            'taux' :  forms.Select(attrs={'class':'form-control'}),
            'total' :  forms.TextInput(attrs={'class':'form-control'}),
            'total_bif' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_pq' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_ordinaire' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_ussd' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_mnemonique' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_mnc' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_nspc' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_ispc' :  forms.TextInput(attrs={'class':'form-control'}),
            'q_cpti' :  forms.TextInput(attrs={'class':'form-control'}),
            'fsva' :  forms.TextInput(attrs={'class':'form-control'}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class TauxForm(ModelForm):
    class Meta:
        model = Taux
        fields = '__all__'
        exclude = ['etat','dateAtri','updated']
        widgets = {
            'taux' :  forms.TextInput(attrs={'class':'form-control'}),
            'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }

# class TarifAgreForm(ModelForm):
#     class Meta:
#         model = TarifAgre
#         fields = '__all__'
#         exclude = ['etat','date']
#         widgets = {
#             'tarifs' :  forms.TextInput(attrs={'class':'form-control'}),
#             'dateAtri' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
#         }

class Facture_CertAgrForm(ModelForm):
    class Meta:
        model = Facture_CertAgr
        fields = '__all__'
        exclude = ['date']
        widgets = {
            'certificat' :  forms.Select(attrs={'class':'form-control'}),
            'tarif' :  forms.Select(attrs={'class':'form-control'}),
            'taux' :  forms.Select(attrs={'class':'form-control'}),
            'total' :  forms.TextInput(attrs={'class':'form-control'}),
            'total_bif' :  forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }



class FactureHomForm(ModelForm):
    class Meta:
        model = FactureHom
        fields = '__all__'
        exclude = ['date']
        widgets = {
            'certificat' :  forms.Select(attrs={'class':'form-control'}),
            'tarif' :  forms.Select(attrs={'class':'form-control'}),
            'taux' :  forms.Select(attrs={'class':'form-control'}),
            'total' :  forms.TextInput(attrs={'class':'form-control'}),
            'total_bif' :  forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date' }),
        }


class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'
        exclude = ['dateAtri','etat']
        widgets = {
            'type' :  forms.Select(attrs={'class':'form-control'}),
            'nom' :  forms.TextInput(attrs={'class':'form-control'}),
        }


class constructeurForm(ModelForm):
    class Meta:
        model = Constructeur
        fields = '__all__'
        exclude = ['date_creation','etat']
        widgets = {
            'nom' :  forms.TextInput(attrs={'class':'form-control'}),
            'adresse' :  forms.TextInput(attrs={'class':'form-control'}),
            'téléphone' :  forms.TextInput(attrs={'class':'form-control'}),
            'fax' :  forms.TextInput(attrs={'class':'form-control'}),
            'email' :  forms.TextInput(attrs={'class':'form-control'}),
        }

class EquipementForm(ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'
        exclude = ['date_creation','etat']
        widgets = {
            'constructeur' :  forms.Select(attrs={'class':'form-control'}),
            'designation' :  forms.TextInput(attrs={'class':'form-control'}),
            'marque' :  forms.TextInput(attrs={'class':'form-control'}),
            'type' :  forms.TextInput(attrs={'class':'form-control'}),
            'modele' :  forms.TextInput(attrs={'class':'form-control'}),
            'pays_origine' :  forms.TextInput(attrs={'class':'form-control'}),
        }





    

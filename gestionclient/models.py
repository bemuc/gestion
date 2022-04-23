import email
from http import client
from random import choice
from xml.dom import NoModificationAllowedErr
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    TYPE = (
        ('Autre','Autre'),
        ('FAI','FAI'),
        ('FSVA','FSVA'),
        ('Public','Public'),
        ('Operateur telephonique','Operateur telephonique'),
    )
    type = models.CharField(max_length=200,  null=True, choices=TYPE)
    nom = models.CharField(max_length=200,  null=False)
    adresse = models.CharField(max_length=200,  null=True)
    téléphone = models.CharField(max_length=200,  null=True)
    fax = models.CharField(max_length=200,  null=True)
    email = models.CharField(max_length=200,  null=True)
    siteweb = models.CharField(max_length=200,  null=True)
    boite_postale = models.CharField(max_length=200,  null=True)
    nif = models.CharField(max_length=200,  null=False)
    status = models.CharField(max_length=200, default= "actif",  null=False)


    def __str__(self):
        return self.nom

    # class Meta:
    #     ordering = ['type']

# class PersonneContact(models.Model):
#     client = models.OneToOneField(Client,on_delete=models.PROTECT)
#     nom = models.CharField(max_length=200,  null=False)
#     telephone = models.CharField(max_length=200,  null=False)
#     email = models.CharField(max_length=200,  null=False)
#     poste = models.CharField(max_length=200,  null=False)
#     status = models.CharField(max_length=200, default= "actif",  null=False)

#     def __str__(self):
#         return (self.nom+'/'+self.client.nom)




# class Service(models.Model):
#     TYPE = (
#         ('Aucun','Aucun'),
#         ('VHF-UHF','VHF-UHF'),
#         ('HF','HF'),
#         ('International','International'),
#         ('National','National'),
#         ('Province','Province'),
#         ('Local','Local'),
#         ('Numero long','Numero long'),
#         ('Numero court','Numero court'),
#         ("Codes attribues par l'ARCT","Codes attribues par l'ARCT"),
#         ('Terminaux simples et de faible puissance','Terminaux simples et de faible puissance'),
#         ('Terminaux simples et de faible puissance/Terminaux de communication','Terminaux simples et de faible puissance/Terminaux de communication'),
#         ('Terminaux radioelectriques des reseaux','Terminaux radioelectriques des reseaux'),
#     )
#     CATEGORY = (
#         ('Reseaux radioelectrique fixe et mobiles a usage prive(non commercial)','Reseaux radioelectrique fixe et mobiles a usage prive(non commercial)'),
#         ('Reseaux ou services ouvert au public(commercial)','Reseaux ou services ouvert au public(commercial)'),
#         ('Communication par satellite','Communication par satellite'),
#         ('Station de radiodiffusion sonore et televisuelle','Station de radiodiffusion sonore et televisuelle'),
#         ('Exploitation des ressources en numerotage','Exploitation des ressources en numerotage'),
#         ("Certificat d'homologation des terminaux","Certificat d'homologation des terminaux"),
#         ("Certificat de conformite des reseaux","Certificat de conformite des reseaux"),
#         ("Certificat d'agrement","Certificat d'agrement"),
#     )
#     nom = models.CharField(max_length=200,  null=False)
#     type = models.CharField(max_length=200, default='Aucun', null=True,choices=TYPE)
#     categorie = models.CharField(max_length=200,  null=True,choices=CATEGORY)

#     def __str__(self):
#         return (self.nom +'/'+ self.categorie)


# class Exploite(models.Model):
#     client = models.ForeignKey(Client,on_delete=models.PROTECT)
#     service = models.ForeignKey(Service,null=False,on_delete=models.PROTECT)
#     date_created = models.DateTimeField(auto_now_add= True, null= True)

# class Category(models.Model):
#     STATUS = (
#         ('ACTIF','ACTIF'),
#         ('NON ACTIF','NON ACTIF'),
#     )
#     nom = models.CharField(max_length=200, null=True)
#     prix = models.FloatField(max_length=200, null=True)
#     status = models.CharField(max_length=200, null=True,choices=STATUS)

#     def __str__(self):
#         return (self.nom)


class CertAgr(models.Model):
    TYPE = (
        ('VENDEUR','VENDEUR'),
        ('INSTALLATEUR','INSTALLATEUR'),
        ('DISTRIBUTEUR','DISTRIBUTEUR'),
    )
    NATURE = (
        ('Nouveau certificat','Nouveau certificat'),
        ('Renouvellement certificat','Renouvellement certificat'),
    )
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    type = models.CharField(max_length=200, null=True,choices=TYPE)
    nature = models.CharField(max_length=200, null=True,choices=NATURE)
    dateAttri = models.DateField(auto_now= False, null= True)
    dateExp = models.DateField(auto_now=False, null=True)
    porfact = models.CharField(max_length=200, null=True, default='non')
    facturer = models.CharField(max_length=200, null=True, default='non')
    etat = models.CharField(max_length=200, null=True, default='actif')

    
    def __str__(self):
        return (self.client.nom +'/'+ self.type + '/'+ self.nature)

    class Meta:
        ordering = ['-dateAttri']

class Taux(models.Model):
    taux = models.FloatField(max_length=200, null=True)
    dateAtri = models.DateField(auto_now_add=True,null=True)
    updated = models.DateField(auto_now=True,null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')

class TarifAgre(models.Model):
    TYPE = (
        ('VENDEUR','VENDEUR'),
        ('INSTALLATEUR','INSTALLATEUR'),
        ('DISTRIBUTEUR','DISTRIBUTEUR'),
       )
    type = models.CharField(max_length=200,  null=True, choices=TYPE)
    tarifs = models.IntegerField(null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    date = models.DateField(auto_now_add= True, null= True)

    def __str__(self):
        return (self.type)


class Facture_CertAgr(models.Model):
    certificat = models.ForeignKey(CertAgr,on_delete=models.PROTECT)
    tarif =  models.ForeignKey(TarifAgre,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,on_delete=models.PROTECT)
    total = models.IntegerField(null=True)
    total_bif = models.IntegerField(null=True)
    date = models.DateField(auto_now= True, null= True)


class CertConf(models.Model):
    TYPE = (
        ('RESEAU LOCAL','RESEAU LOCAL'),
        ('RESEAU NATIONAL','RESEAU NATIONAL'),
    )
    NATURE = (
        ('Nouveau certificat','Nouveau certificat'),
        ('Renouvellement certificat','Renouvellement certificat'),
    )
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    type = models.CharField(max_length=200, null=True,choices=TYPE)
    nature = models.CharField(max_length=200, null=True,choices=NATURE)
    dateAttri = models.DateField(auto_now= False, null= True)
    dateExp = models.DateField(auto_now=False, null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    pourfact = models.CharField(max_length=200, null=True, default='non')
    facturer = models.CharField(max_length=200, null=True, default='non')

    
    def __str__(self):
        return (self.client.nom +'/'+ self.type + '/'+ self.nature)

    class Meta:
        ordering = ['-dateAttri']

class TarifConf(models.Model):
    TYPE = (
        ('RESEAU LOCAL','RESEAU LOCAL'),
        ('RESEAU NATIONAL','RESEAU NATIONAL'),
    )
    type = models.CharField(max_length=200,  null=True, choices=TYPE)
    tarif = models.IntegerField(null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    date = models.DateField(auto_now_add= True, null= True)

    def __str__(self):
        return (self.type)

class FactureConf(models.Model):
    certificat = models.ForeignKey(CertConf,on_delete=models.PROTECT)
    tarif =  models.ForeignKey(TarifConf,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,on_delete=models.PROTECT)
    total = models.IntegerField(null=True)
    total_bif = models.IntegerField(null=True)
    date = models.DateField(auto_now= True, null= True)

class Constructeur(models.Model):
    nom = models.CharField(max_length=200,  null=False)
    adresse = models.CharField(max_length=200,  null=True)
    téléphone = models.CharField(max_length=200,  null=True)
    fax = models.CharField(max_length=200,  null=True)
    email = models.CharField(max_length=200,  null=True)
    date_creation = models.DateField(auto_now= True, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.nom)
    
    class Meta:
        ordering = ['-date_creation']

class Equipement(models.Model):
    constructeur = models.ForeignKey(Constructeur,on_delete=models.PROTECT)
    designation = models.CharField(max_length=200,  null=False)
    marque = models.CharField(max_length=200,  null=False)
    type = models.CharField(max_length=200,  null=False)
    modele = models.CharField(max_length=200,  null=False)
    pays_origine = models.CharField(max_length=200,  null=False)
    etat = models.CharField(max_length=200, null=True, default='actif')
    date_creation = models.DateField(auto_now= True, null= True)

    def __str__(self):
        return (self.designation +'/'+   self.constructeur.nom )

    class Meta:
        ordering = ['-date_creation']

class HomologationEqui(models.Model):
    NATURE = (
        ('Nouveau certificat','Nouveau certificat'),
        ('Renouvellement certificat','Renouvellement certificat'),
    )
    CATEGORIE = (
        ('Terminal Simple et de Faible Puissance','Terminal Simple et de Faible Puissance'),
        ("Terminal Simple et de Faible Puissance/Terminal de communication d'Entreprise","Terminal Simple et de Faible Puissance/Terminal de communication d'Entreprise"),
        ('Terminal Radioelectrique de Reseau','Terminal Radioelectrique de Reseau'),
    )
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    equipement = models.ForeignKey(Equipement,on_delete=models.PROTECT)
    categorie =  models.CharField(max_length=200, null=True,choices=CATEGORIE)
    dateAttri = models.DateField(auto_now= False, null= True)
    dateExp = models.DateField(auto_now=False, null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    nature = models.CharField(max_length=200, null=True,choices=NATURE)
    pourfact = models.CharField(max_length=200, null=True, default='non')
    facturer = models.CharField(max_length=200, null=True, default='non')

    def __str__(self):
        return (self.client.nom +'/'+ self.equipement.designation)


    class Meta:
        ordering = ['-dateAttri']

class TarifHom(models.Model):
    TYPE = (
        ('Terminal Simple et de Faible Puissance','Terminal Simple et de Faible Puissance'),
        ("Terminal Simple et de Faible Puissance/Terminal de communication d'Entreprise","Terminal Simple et de Faible Puissance/Terminal de communication d'Entreprise"),
        ('Terminal Radioelectrique de Reseau','Terminal Radioelectrique de Reseau'),
    )
    type = models.CharField(max_length=200,  null=True, choices=TYPE)
    tarif = models.IntegerField(null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    date = models.DateField(auto_now_add= True, null= True)

    def __str__(self):
        return (self.type)

class FactureHom(models.Model):
    certificat = models.ForeignKey(HomologationEqui,on_delete=models.PROTECT)
    tarif =  models.ForeignKey(TarifHom,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,on_delete=models.PROTECT)
    total = models.IntegerField(null=True)
    total_bif = models.IntegerField(null=True)
    date = models.DateField(auto_now= True, null= True)






class Megas(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    megas = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.client.nom)

    class Meta:
        ordering = ['-dateAtri']

class Minutes(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    minutes = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.client.nom +' | '+ self.dateAtri)

    class Meta:
        ordering = ['-dateAtri']


class ChiffreAffaire(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    ca = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.client.nom)
    
    class Meta:
        ordering = ['client__nom','dateAtri']

class FrequenceRadio(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    bande = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    bande_attribuee = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    facturer = models.CharField(max_length=200, null=True, default='non')
    efacturer = models.CharField(max_length=200, null=True, default='non')
    etat = models.CharField(max_length=200, null=True, default='actif')

    

class FaisceauxHertzien(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    bande = models.FloatField(max_length=200, null=True)
    bande_passante = models.FloatField(max_length=200, null=True)
    nombre_canaux = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now_add= True, null= True)
    facturer = models.CharField(max_length=200, null=True, default='non')
    efacturer = models.CharField(max_length=200, null=True, default='non')
    etat = models.CharField(max_length=200, null=True, default='actif')
  
class TarifFH(models.Model):
    NATURE = (
        (23,'>23 Ghz'),
        (13,'>13 Ghz'),
        (3,'>3 Ghz'),
        (0,'<3 Ghz'),
    )
    nature = models.IntegerField(null=True, choices=NATURE)
    # repere =  models.IntegerField(null=True)
    p_canal = models.FloatField(max_length=200, null=True)
    p_mhz = models.FloatField(max_length=200, null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    dateAtri = models.DateField(auto_now_add= True, null= True)

class Facture_FH(models.Model):
    faisceaux = models.ForeignKey(FaisceauxHertzien,on_delete=models.PROTECT)
    tarif = models.ForeignKey(TarifFH,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,null=True,on_delete=models.PROTECT)
    total_bif = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now_add= True, null= True)

class Repere(models.Model):
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    date_repere =models.DateField(auto_now= False, null= True)
    dateAtri = models.DateField(auto_now_add= True, null= True)
    facturer = models.CharField(max_length=200, null=True, default='non')
    efacturer = models.CharField(max_length=200, null=True, default='non')

class ListeFHAnnuelle(models.Model):
    repere = models.ForeignKey(Repere,on_delete=models.PROTECT)
    faisceaux = models.ForeignKey(FaisceauxHertzien,null=True,on_delete=models.PROTECT)

class Facture_FH_A(models.Model):
    repere = models.ForeignKey(Repere,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,null=True,on_delete=models.PROTECT)
    total_bif = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now_add= True, null= True)







class FF_Numero(models.Model):
    NATURE = (
        ('Client Nouveau','Client Nouveau'),
        ('Client Existant','Client Existant'),
    )
    client  = models.ForeignKey(Client,on_delete=models.PROTECT)
    q_pq = models.IntegerField(null=True,default= 0)
    q_ordinaire = models.IntegerField(null=True,default= 0)
    q_ussd = models.IntegerField(null=True,default= 0)
    q_mnemonique = models.IntegerField(null=True,default= 0)
    q_mnc = models.IntegerField(null=True,default= 0)
    q_nspc = models.IntegerField(null=True,default= 0)
    q_ispc = models.IntegerField(null=True,default= 0)
    q_cpti = models.IntegerField(null=True,default= 0)
    RN_etudeDossier = models.BooleanField(default= False)
    RN_fraisGestion = models.BooleanField(default= False)
    RN_redevanceAnn = models.BooleanField(default= False)
    FS_etudeDossier = models.BooleanField(default= False)
    FS_agreEquipe = models.BooleanField(default= False)
    FS_autoARCT = models.BooleanField(default= False)
    nature = models.CharField(max_length=200,  null=True, choices=NATURE)
    periode = models.IntegerField(null=True,default= 0)
    facturer = models.CharField(max_length=200, null=True, default='non')
    efacturer = models.CharField(max_length=200, null=True, default='non')
    etat = models.CharField(max_length=200, null=True, default='actif')
    dateAtri = models.DateField(auto_now= True, null= True)
    observation = models.TextField(max_length= 300,null=True,default='-')

class NumeroCourt(models.Model):
    TYPE = (
        ('Code Ordinaire','Code Ordinaire'),
        ('USSD','USSD'),
        ('Code Mnemonique','Code Mnemonique'),
        ('ISPC','ISPC'),
        ('NSPC','NSPC'),
        ('MNC','MNC'),
        ('Code de preselection pour les transporteurs internationaux','Code de preselection pour les transporteurs internationaux'),
    )
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    ffnumero = models.ForeignKey(FF_Numero,null=True,on_delete=models.PROTECT)
    type = models.CharField(max_length=200, null=True,choices=TYPE)
    numero = models.CharField(max_length=200,  null=True)
    periode = models.IntegerField(null=True,default= 0)
    dateAtri = models.DateField(auto_now= True, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.client.nom)

    class Meta:
        ordering = ['-dateAtri']

class PQ(models.Model):
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    ffnumero = models.ForeignKey(FF_Numero,null=True,on_delete=models.PROTECT)
    pq =  models.CharField(max_length=200, null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.client.nom )

    class Meta:
        ordering = ['-dateAtri']
  
class AB(models.Model):
    pq = models.ForeignKey(PQ,on_delete=models.PROTECT)
    ab = models.CharField(max_length=200, null=True)
    dateAtri = models.DateField(auto_now= False, null= True)
    etat = models.CharField(max_length=200, null=True, default='actif')

    def __str__(self):
        return (self.pq.client.nom +' | '+ self.pq.pq+' | '+self.ab)

    class Meta:
        ordering = ['-dateAtri']



    # def __str__(self):
    #     return (self.taux )

class TarifFSVANumero(models.Model):
    etudeDossier = models.FloatField(max_length=200, null=True)
    agrementEquip = models.FloatField(max_length=200, null=True)
    redevanceAnn = models.FloatField(max_length=200, null=True)
    autorisationARCT = models.FloatField(max_length=200, null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    dateAtri = models.DateField(auto_now= True, null= True)



class TarifFFNumero(models.Model):
    TYPE = (
        ('PQ','PQ'),
        ('Code Ordinaire','Code Ordinaire'),
        ('USSD','USSD'),
        ('Code Mnemonique','Code Mnemonique'),
        ('ISPC','ISPC'),
        ('NSPC','NSPC'),
        ('MNC','MNC'),
        ('Code de preselection pour les transporteurs internationaux','Code de preselection pour les transporteurs internationaux'),
    )
    type = models.CharField(max_length=200,  null=True, choices=TYPE)
    etudeDossier = models.FloatField(max_length=200, null=True)
    fraisGestion = models.FloatField(max_length=200, null=True)
    redevanceAnn = models.FloatField(max_length=200, null=True)
    etat = models.CharField(max_length=200, null=True, default='actif')
    dateAtri = models.DateField(auto_now_add= True, null= True)


class Facture_FFNumero(models.Model):
    ffnumero = models.ForeignKey(FF_Numero,null=True,on_delete=models.PROTECT)
    taux = models.ForeignKey(Taux,null=True,on_delete=models.PROTECT)
    total = models.IntegerField(null=True)
    total_bif = models.IntegerField(null=True)
    dateAtri = models.DateField(auto_now= True, null= True)
    q_pq = models.IntegerField(null=True)
    q_ordinaire = models.IntegerField(null=True)
    q_ussd = models.IntegerField(null=True)
    q_mnemonique = models.IntegerField(null=True)
    q_mnc = models.IntegerField(null=True)
    q_nspc = models.IntegerField(null=True)
    q_ispc = models.IntegerField(null=True)
    q_cpti = models.IntegerField(null=True)
    fsva = models.IntegerField(null=True)














# class factureCertAgr(models.Model):
#     certificat = models.ForeignKey(CertAgr,null=True,on_delete=models.PROTECT)
#     category = models.ForeignKey(Category,on_delete=models.PROTECT)
#     taux = models.ForeignKey(Taux,on_delete=models.PROTECT)
#     date = models.DateField(auto_now= True, null= True)

#     def __str__(self):
#         return (self.certificat.client.nom +'/'+ self.certificat.category.nom + '/'+ self.date)


    


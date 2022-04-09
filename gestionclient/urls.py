from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    path('', views.loginPage,name='login_page'),
    path('logout/', views.logout_page,name='logout'),


    path('ajoutClient/', views.ajoutClient,name='ajoutClient_page'),
    path('listeClient/', views.listeClient,name='listeClient_page'),
    path('detailsClient/<str:pk>', views.detailsClient,name='detailsClient_page'),
    path('modifierClient/<str:pk>', views.modifierClient,name='modifierClient_page'),
    path('deactiverClient/<str:pk>', views.deactiverClient,name='deactiverClient_page'),

    
    # path('ajoutPersonneContact/', views.ajoutPersonneContact,name='ajoutPersonneContact_page'),
    # path('listePContact/', views.listePContact,name='listePContact_page'), 
    

# certificat agrement
    # path('listeCertAgr/<str:pk>', views.listeCertAgr,name='listeCertAgr_page'),
    path('listeCertAgr/', views.CertListAgr,name='CertListAgr_page'),
    path('detailCertAgr/<str:pk>', views.detailCertAgr,name='detailCertAgr_page'),
    path('renouvCertAgr/<str:pk>', views.renouCertAgre,name='renouCertAgr_page'),
    path('ajoutCertAgr/', views.ajoutCert,name='ajoutCertAgr_page'),
    path('updateCertAgr/<str:pk>', views.updateCertAgre,name='updateCertAgr_page'),
    path('deactiverCertAgr/<str:pk>', views.deactiveCertAgr,name='deactiverCertAgr_page'),
    path('pourfactCertAgr/<str:pk>', views.pourFactCertAgr,name='pourfactCertAgr_page'),
    # path('printcert/<str:pk>', views.thepdf,name='printcert_page'),
    path('Cert_Agr_facturer/', views.Certfacturer,name='ListCetAfact'),
    path('facturer_cert_agre/<str:pk>', views.factCert,name = 'factCert'),

# certificat conformite

    path('liste_certificat_conformite/', views.ListCertConf,name='ListCertConf'),
    path('detail_Certificat_conformite/<str:pk>', views.DetailConf,name='DetailConf'),
    path('ajoutCertConf/', views.ajoutCertConf,name='ajoutCertConf'),
    path('updateCertConf/<str:pk>', views.updateCertConf,name='updateCertConf'),
    path('renouvCertConf/<str:pk>', views.renouvCertConf,name='renouvCertConf'),
    path('pourfactCertConf/<str:pk>', views.pourfactCertConf,name='pourfactCertConf'), 
    path('Cert_Conf_facturer/', views.CertConfAfact,name='ListCertConfAfact'),
    path('facturer_cert_conf/<str:pk>', views.factCertConf,name = 'factCertConf'),

#Homologations
    
    #constructeur 

    path('liste_constructeur/', views.ListConstructeur,name='ListConstructeur'),
    path('ajouter_Constructeur/', views.ajoutConstructeur,name='ajoutConstructeur'),
    path('update_constructeur/<str:pk>', views.updateConstr,name='updateConstr'),

    #equipement

    path('liste_equipement/', views.ListEqui,name='ListEqui'),
    path('ajouter_equipement/', views.ajoutEquipement,name='ajoutEquipement'),
    path('update_equipement/<str:pk>', views.updateEquip,name='updateEquip'),

    #certificat homologation

    path('liste_Homologation/', views.ListeHomo,name='ListeHomo'),
    path('ajouter_Homologation/', views.ajoutHomologation,name='ajoutHomologation'),
    path('detail_Homologation/<str:pk>', views.detailHomologation,name='detailHomologation'),
    path('update_Homologation/<str:pk>', views.updateHomologation,name='updateHomologation'),
    path('modifier_Homologation/<str:pk>', views.modifierHomo,name='modifierHomo'),

    path('pourfactCertHom/<str:pk>', views.pourfactCertHom,name='pourfactCertHom'), 
    path('Cert_Hom_facturer/', views.CertHomAfact,name='ListCertHomAfact'),
    path('facturer_cert_hom/<str:pk>', views.factCertHom,name = 'factCertHom'),


#numerotation
    #numero Court
    path('liste_numCourt/', views.ListeNumCourt,name='ListeNumCourt'),
    path('ajouter_numCourt/', views.ajoutnumCourt,name='ajoutnumCourt'),
    path('update_numcourt/<str:pk>', views.updateNumcourt,name='updateNumcourt'),

    #numero long
    path('liste_pq/', views.ListePQ,name='ListePQ'),
    path('ajouter_pq/', views.ajoutPQ,name='ajoutPQ'),
    path('ajouter_ab/<str:pk>', views.ajoutAB,name='ajoutAB'),
    path('details_pq/<str:pk>', views.detailsPQ,name='detailsPQ'),
    path('update_ab/<str:pk>', views.updateAB,name='updateAB'),
    path('update_pq/<str:pk>', views.updatePQ,name='updatePQ'),


#megas
    path('liste_megas/', views.ListeMegas,name='ListeMegas'),
    path('ajouter_megas/', views.ajoutMegas,name='ajoutMegas'),
    path('update_megas/<str:pk>', views.updateMegas,name='updateMegas'),

#minutes
    path('liste_minutes/', views.ListeMinutes,name='ListeMinutes'),
    path('ajouter_minutes/', views.ajoutMinutes,name='ajoutMinutes'),
    path('update_minutes/<str:pk>', views.updateMinutes,name='updateMinutes'),

#chiffre d'affaire
    path('liste_ca/', views.ListeCA,name='ListeCA'),
    path('ajouter_ca/', views.ajoutCA,name='ajoutCA'),
    path('update_ca/<str:pk>', views.updateCA,name='updateCA'),

#frequence radio
    path('liste_fr/', views.ListeFR,name='ListeFR'),
    path('ajouter_fr/', views.ajoutFR,name='ajoutFR'),
    path('update_fr/<str:pk>', views.updateFR,name='updateFR'),

#faisceaux hertzien
    path('liste_fh/', views.ListeFH,name='ListeFH'),
    path('ajouter_fh/', views.ajoutFH,name='ajoutFH'),
    path('update_fh/<str:pk>', views.updateFH,name='updateFH'),

#fiche facturation
    path('liste_client_facturation_numero/', views.ListeCli,name='ListeCli'),
    path('liste_fiche_facturation_numero/', views.ListeFFNumero,name='ListeFFNumero'),
    path('ajouter_fiche_facturation_numero/<str:pk>', views.ajoutFFNumero,name='ajoutFFNumero'),
    path('ajouter_fiche_facturation_numero_annuelle/<str:pk>', views.ajoutFFANumero,name='ajoutFFANumero'),
    path('details_fiche_facturation_numero/<str:pk>', views.detailsFFNumero,name='detailsFFNumero'),
    path('update_fiche_facturation_numero/<str:pk>', views.updateFFNumero,name='updateFFNumero'),
    path('facturer_fiche_facturation_numero/<str:pk>', views.facturerFFNumero,name='facturerFFNumero'),
    path('supprimer_fiche_facturation_numero/<str:pk>', views.supprimerFFNumero,name='supprimerFFNumero'),
    # path('ajouter_numeros/<str:pk>', views.ajoutNumeros,name='ajoutNumeros'),

#taux
    path('liste_taux/', views.ListeTaux,name='ListeTaux'),
    path('ajouter_taux/', views.ajouterTaux,name='ajouterTaux'),
    path('update_taux/<str:pk>', views.updateTaux,name='updateTaux'),

#tarif numeros
    path('liste_tarifNumero/', views.ListeTarifNum,name='ListeTarifNum'),
    path('liste_tarifFSVANumero/', views.ListeTarifFSVANum,name='ListeTarifFSVANum'),
    path('ajouter_tarifNumero/', views.ajoutertarifNumero,name='ajoutertarifNumero'),
    path('detail_tarifNumero/<str:pk>', views.detailtarifNumero,name='detailtarifNumero'),
    path('detail_tarifFSVANumero/<str:pk>', views.detailtarifFSVANumero,name='detailtarifFSVANumero'),
    path('deactiver_tarifNumero/<str:pk>', views.deactiverTarifNumero,name='deactiverTarifNumero'),
    path('deactiver_tarifFSVANumero/<str:pk>', views.deactiverTarifFSVANumero,name='deactiverTarifFSVANumero'),
    path('activer_tarifNumero/<str:pk>', views.activerTarifNum,name='activerTarifNum'),
    path('ajouter_tarifFSVANumero/', views.ajoutertarifFSVANumero,name='ajoutertarifFSVANumero'),

#tarifs homologations
    path('liste_tarifs_homologations/', views.ListeTarifsHomo,name='ListeTarifsHomo'),
    path('ajouter_tarif_homologations/', views.ajoutertarifHomo,name='ajoutertarifHomo'),
    path('detail_tarif_homologations/<str:pk>', views.detailtarifHomo,name='detailtarifHomo'),
    path('deactiver_tarif_homologations/<str:pk>', views.deactiverTarifHomo,name='deactiverTarifHomo'),

#tarif Agrements
    path('liste_tarifs_agrement/', views.ListeTarifsAgr,name='ListeTarifsAgr'),
    path('ajouter_tarif_agrement/', views.ajoutertarifAgr,name='ajoutertarifAgr'),
    path('detail_tarif_agrement/<str:pk>', views.detailtarifAgr,name='detailtarifAgr'),
    path('deactiver_tarif_agrement/<str:pk>', views.deactiverTarifAgr,name='deactiverTarifAgr'),

#tarif conformite
    path('liste_tarifs_conformite/', views.ListeTarifsConf,name='ListeTarifsConf'),
    path('ajouter_tarif_conformite/', views.ajoutertarifConf,name='ajoutertarifConf'),

#facturer
    path('liste_ff/', views.Listeff,name='Listeff'),
    path('liste_facture_fiche/', views.Listefactfiche,name='Listefactfiche'),
    path('details_ff_numero/<str:pk>', views.detailsFFNum,name='detailsFFNum'),
    path('facturer_num/<str:pk>', views.facturerNum,name='facturerNum'),


    
]
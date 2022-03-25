from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from datetime import date,timedelta
from datetime import datetime
# from.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .filters import *
from django.forms import inlineformset_factory

####

from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
###

from .forms import *


# @unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(request, username=user_name, password=pass_word)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password incorect')
            return render(request,'gestionclient/login.html')

    # context ={}
    return render(request,'gestionclient/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def is_group1(user):
  return user.groups.filter(name='finance').exists()

def afacturer(request):
    return {
        'afacturer':FF_Numero.objects.filter( efacturer = 'non').count(),
    }

@login_required(login_url='login_page')
def home(request):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    context={
        'name':poste,
        
    }
    return render(request,'gestionclient/base.html',context)


@login_required(login_url='login_page')
def ajoutClient(request):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            thenif = form.cleaned_data.get('nif')
            clients = Client.objects.all()
            for client in clients:
                if thenif == client.nif:
                    messages.error(request, f'Le client est deja enregister!')
                    return redirect('ajoutClient_page')
                else:
                    form.save()
                    # username = form.cleaned_data.get('name')
                    messages.success(request, f'Le client est bien enregister!')
                    return redirect('ajoutClient_page')
    else:
        form = ClientForm()
    
    context = {
        'form':form,
        'titre': "Ajouter",
        'name':poste,
    }
    return render(request,'gestionclient/Clientts/ajoutClient.html',context)

@login_required(login_url='login_page')
def modifierClient(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect ('listeClient_page')
    
    context = {
        'form':form,
        'titre':"Modifier",
        'name':poste,
        }

    return render(request,'gestionclient/Clientts/ajoutClient.html',context)


@login_required(login_url='login_page')
def deactiverClient(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.status = "deactiver"
        client.save()
        return redirect ('listeClient_page')
    context ={'item':client,'name':poste,}
    return render(request,'gestionclient/deactiver.html',context)

@login_required(login_url='login_page')
def listeClient(request):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    clients = Client.objects.all()
    myfilter = ClientFilter(request.GET, queryset=clients)
    clients = myfilter.qs
    context = {
        # 'clients': Client.objects.filter(status ="actif"),
        'clients':clients, 
        'myfilter':myfilter,
        'name':poste,
        }
    return render(request,'gestionclient/Clientts/listeClient.html',context)

@login_required(login_url='login_page')
def detailsClient(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'


    context = {
        'client': Client.objects.get(id = pk),
        'certificats': CertAgr.objects.filter(client__id = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/Clientts/detailsClient.html',context)

# def ajoutPersonneContact(request):
#     if request.user.groups.filter(name='finance'):
#         poste = 'finance'
#     else:
#         poste = 'nothing'

    
#     if request.method == 'POST':
#         form = PersonneContactForm(request.POST)
#         if form.is_valid():
#             thenif = form.cleaned_data.get('nom')
#             theclient = form.cleaned_data.get('client')
#             contacts = PersonneContact.objects.all()
#             for contact in contacts:
#                 if thenif == contact.nom and theclient == contact.cleint:
#                     messages.error(request, f'La personne de contact est deja enregister!')
#                     return redirect('ajoutPersonneContact_page')
#                 else:
#                     form.save()
#                     # username = form.cleaned_data.get('name')
#                     messages.success(request, f'La personne de contact est bien enregister!')
#                     return redirect('ajoutPersonneContact_page')
#     else:
#         form = PersonneContactForm()
#     context = {
#         'name':poste,
#         'form':form,
#     }
#     return render(request,'gestionclient/ajoutPContact.html',context)

# def listePContact(request):
#     if request.user.groups.filter(name='finance'):
#         poste = 'finance'
#     else:
#         poste = 'nothing'

    
#     context = {
#         'contacts': PersonneContact.objects.all(),
#         'name':poste,
#         }
#     return render(request,'gestionclient/listePContact.html',context)

@login_required(login_url='login_page')
def listeCertAgr(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    context = {
        'certificats': CertAgr.objects.filter(client__id = pk).filter(etat = 'actif'),
        'client':Client.objects.get(id=pk),
        'today':date.today(),
        'name':poste,
    }

    return render(request,'gestionclient/certificatAgrement/certiAgrement.html',context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['technicien'])
def ajoutCert(request):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    clients = Client.objects.all()
    # contact = PersonneContact.objects.get(client__id = clients.pk)
    today = date.today()
    form = CertAgreForm(initial={'client':clients,'nature':'Nouveau certificat','dateAttri':today})
    if request.method == 'POST':
        form = CertAgreForm(request.POST)
        if form.is_valid():
            thetype = form.cleaned_data.get('type')
            theclient = form.cleaned_data.get('client')
            thenature = form.cleaned_data.get('nature')
            thestart = form.cleaned_data.get('dateAttri')
            theEnd = form.cleaned_data.get('dateExp')
            thetat = form.cleaned_data.get('etat')
            certis = CertAgr.objects.all().filter(etat = 'actif')
            count = 0
            if(thenature == 'Nouveau certificat' ):
                for certi in certis:
                    if ( thetype == certi.type and theclient == certi.client):
                        count += 1

                if count > 0:
                    messages.warning(request, f'Certificat existant deja! il faut renouveller')
                
                else:
                    if(thestart < today or theEnd < thestart or theEnd.year - thestart.year < 5):
                        messages.warning(request, f"Erreur verifier les dates")
                    else:
                        form.dateExp = datetime.date(thestart.year+5,thestart.month,thestart.day-5)
                        form.save()
                        messages.success(request, f'Certificat bien ajouter')
                        return redirect('CertListAgr_page')
        else:
            messages.error(request, f' ERREUR Certificat invalid non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        'client': clients,
        'name':poste,
        }

    return render(request,'gestionclient/certificatAgrement/ajoutCertAgr.html',context)


@login_required(login_url='login_page')
@allowed_users(allowed_roles=['technicien'])
def renouCertAgre(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    certiAgrs = CertAgr.objects.get(id=pk)
    today = date.today()
    form = CertAgreForm(instance = certiAgrs,initial={'nature':'Renouvellement certificat','etat':'actif','dateAttri':today} )
    if request.method == 'POST':
        form = CertAgreForm(request.POST,instance = certiAgrs)
        if form.is_valid():
            form.save()
            certiAgrs.etat = 'deactif'
            certiAgrs.save()
            messages.success(request, f'Certificat bien renouveller' )
            return redirect('detailCertAgr_page',pk = pk )
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Renouvellemet',
        'client': Client.objects.get(id=certiAgrs.client.id),
        'name':poste,
        }
    
    return render(request,'gestionclient/certificatAgrement/ajoutCertAgr.html',context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['technicien'])
def updateCertAgre(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    certiAgrs = CertAgr.objects.get(id=pk)
    form = CertAgreForm(instance = certiAgrs)
    if request.method == 'POST':
        form = CertAgreForm(request.POST,instance = certiAgrs)
        if form.is_valid():
            form.save()
            messages.success(request, f'Certificat bien mis a jour' )
            return redirect('detailCertAgr_page',pk = pk )
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Modifier',
        'client': Client.objects.get(id=certiAgrs.client.id),
        'name':poste,
        }

    return render(request,'gestionclient/certificatAgrement/ajoutCertAgr.html',context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['technicien'])
def deactiveCertAgr(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    certiAgrs = CertAgr.objects.get(id=pk)
    if request.method == 'POST':
        certiAgrs.etat = 'nonActif'
        certiAgrs.save()
        messages.success(request, f'Certificat bien supprimer' )
        return redirect ('listeCertAgr_page',pk = certiAgrs.client.id)


    context ={
        'certificat':certiAgrs,
        'name':poste,
        }
    return render(request,'gestionclient/certificatAgrement/deactiverCertAgr.html',context)

# !!!!!!!!!!!!!
@allowed_users(allowed_roles=['technicien'])
def pourFactCertAgr(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    certiAgrs = CertAgr.objects.get(id=pk)
    if certiAgrs.pourfacturation == 'non' and date.today() < certiAgrs.dateExp:
        certiAgrs.pourfacturation = 'oui'
        certiAgrs.save()
        return redirect ('listeCertAgr_page',pk = certiAgrs.client.id)
    else:
        messages.warning(request, f'le Certificat est expirer il ne peut etre envoyer a la facturation' )
    context ={
        'certificat':certiAgrs,
        'name':poste,
        }
    return render(request,'gestionclient/ficheCertAgr.html',context)

@login_required(login_url='login_page')
def detailCertAgr(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    context = {
        # 'client': Client.objects.get(id = pk),
        'certificat': CertAgr.objects.get(id = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/certificatAgrement/ficheCertAgr.html',context)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def render_pdf_view(request,pk):
#     template_path = 'gestionclient/CertAgrpdf.html'
#     context = {
#         'certificat': CertAgr.objects.get(id = pk),
#         'today': date.today(),
#         }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     #if display 
#     # response['Content-Disposition'] = 'filename="certificatAgrement.pdf"'
#     response['Content-Disposition'] = 'filename= certificat agrement'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

#!!!!!!!!!!!!!!!!!!!!!!!!!!!
def thepdf(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    context = {
        'certificat': CertAgr.objects.get(id = pk),
        'today': date.today(),
        'name':poste,
        }
    return render(request,'gestionclient/CertAgrpdf.html',context)

# def facturer(request,pk):
#     if request.user.groups.filter(name='finance'):
#         poste = 'finance'
#     else:
#         poste = 'nothing'
#     today = date.today()
#     certificat = CertAgr.objects.get(id = pk)
#     category = Category.objects.get(id = certificat.category)
#     if Taux.objects.filter(date = today ):
#        ki = 20
        
#     else:
#         messages.success(request, f"Ajouter le taux d'echange du jout" )
       

#     context = {
#         'certificat': certificat,
#         'category': category,
#         'today': today ,
#         'name':poste,
#         }
#     return render(request,'gestionclient/facturationCertAgr.html',context)

@login_required(login_url='login_page')
def CertListAgr(request):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    
    context = {
        # 'certificats': CertAgr.objects.all().filter(etat = 'actif'),
        'certificats': CertAgr.objects.all(),
        # 'client':Client.objects.get(id=pk),
        'today':date.today(),
        'name':poste,
    }

    return render(request,'gestionclient/certificatAgrement/certListagr.html',context)


# certificat conformite

@login_required(login_url='login_page')
def ListCertConf(request):
    context = {
        'certificats': CertConf.objects.all().filter(etat='actif'),
        'today':date.today(),
    }

    return render(request,'gestionclient/certificatConf/ListCertConf.html',context)

@login_required(login_url='login_page')
def DetailConf(request,pk):
    context = {
        'certificat': CertConf.objects.get(id = pk),
        'today': date.today(),
    }
    return render(request,'gestionclient/certificatConf/DetailConf.html',context)

@login_required(login_url='login_page')
def ajoutCertConf(request):
    clients = Client.objects.all()
    today = date.today()
    form = CertConfForm(initial={'client':clients,'nature':'Nouveau certificat','dateAttri':today})
    if request.method == 'POST':
        form = CertConfForm(request.POST)
        if form.is_valid():
            thetype = form.cleaned_data.get('type')
            theclient = form.cleaned_data.get('client')
            thenature = form.cleaned_data.get('nature')
            thestart = form.cleaned_data.get('dateAttri')
            theEnd = form.cleaned_data.get('dateExp')
            certis = CertConf.objects.all().filter(etat = 'actif')
            count = 0
            if(thenature == 'Nouveau certificat' ):
                for certi in certis:
                    if ( thetype == certi.type and theclient == certi.client):
                        count += 1

                if count > 0:
                    messages.warning(request, f'Certificat existe deja! ')
            
                else:
                    if(thestart < today or theEnd < thestart or (theEnd.year - thestart.year) < 5):
                        messages.warning(request, f"Erreur verifier les dates")
                    else:
                        form.dateExp = datetime.date(thestart.year+5,thestart.month,thestart.day-5)
                        form.save()
                        messages.success(request, f'Certificat bien ajouter')
                        return redirect('ListCertConf')
        else:
            messages.error(request, f' ERREUR Certificat invalid non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        'client': clients,
        }

    return render(request,'gestionclient/certificatConf/ajoutCertConf.html',context)

@login_required(login_url='login_page')
def updateCertConf(request,pk):
    certiConf = CertConf.objects.get(id=pk)
    form = CertConfForm(instance = certiConf)
    if request.method == 'POST':
        form = CertConfForm(request.POST,instance = certiConf)
        if form.is_valid():
            form.save()
            messages.success(request, f'Certificat bien mis a jour' )
            return redirect('DetailConf',pk = pk )
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Modifier',
        'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/certificatConf/ajoutCertConf.html',context)

@login_required(login_url='login_page')
def renouvCertConf(request,pk):
    certiAgrs = CertConf.objects.get(id=pk)
    today = date.today()
    form = CertConfForm(initial={'client':certiAgrs.client,'type':certiAgrs.type,'nature':'Renouvellement certificat','etat':'actif','dateAttri':today} )
    if request.method == 'POST':
        form = CertConfForm(request.POST)
        if form.is_valid():
            form.save()
            certiAgrs.etat = 'deactif'
            certiAgrs.save()
            messages.success(request, f'Certificat bien renouveller' )
            return redirect('DetailConf',pk = pk )
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Renouvellemet',
        'client': Client.objects.get(id=certiAgrs.client.id),
        }
    
    return render(request,'gestionclient/certificatConf/ajoutCertConf.html',context)


## constructeur

@login_required(login_url='login_page')
def ListConstructeur(request):
    context = {
        'constructeurs': Constructeur.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/constructeur/ListeConstructeur.html',context)

@login_required(login_url='login_page')
def ajoutConstructeur(request):
    # clients = Client.objects.all()
    today = date.today()
    form = ConstructeurForm(initial={'dateAttri':today})
    if request.method == 'POST':
        form = ConstructeurForm(request.POST)
        if form.is_valid():
            thenom = form.cleaned_data.get('nom')
            construs = Constructeur.objects.all()
            count = 0
            for constru in construs:
                if ( thenom == constru.nom):
                    count += 1

            if count > 0:
                messages.warning(request, f'Constructeur existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'Constructeur bien ajouter')
                return redirect('ListConstructeur')
                
        else:
            messages.error(request, f' ERREUR Certificat invalid non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/constructeur/ajoutConstructeur.html',context)

@login_required(login_url='login_page')
def updateConstr(request,pk):
    constructeur = Constructeur.objects.get(id=pk)
    form = ConstructeurForm(instance = constructeur)
    if request.method == 'POST':
        form = ConstructeurForm(request.POST,instance = constructeur)
        if form.is_valid():
            form.save()
            messages.success(request, f'Certificat bien mis a jour' )
            return redirect('ListConstructeur')
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Modifier',
        # 'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/constructeur/ajoutConstructeur.html',context)


# equipement

@login_required(login_url='login_page')
def ListEqui(request):
    context = {
        'equipements': Equipement.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/equipement/ListeEquip.html',context)

@login_required(login_url='login_page')
def ajoutEquipement(request):
    # clients = Client.objects.all()
    today = date.today()
    form = EquipementForm(initial={'dateAttri':today})
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            thenom = form.cleaned_data.get('designation')
            equipes = Equipement.objects.all()
            count = 0
            for equipe in equipes:
                if ( thenom == equipe.designation):
                    count += 1

            if count > 0:
                messages.warning(request, f'Equipement existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'Equipement bien ajouter')
                return redirect('ListEqui')
                
        else:
            messages.error(request, f' ERREUR Certificat invalid non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/equipement/ajoutEquipement.html',context)

@login_required(login_url='login_page')
def updateEquip(request,pk):
    equipement = Equipement.objects.get(id=pk)
    form = EquipementForm(instance = equipement)
    if request.method == 'POST':
        form = EquipementForm(request.POST,instance = equipement)
        if form.is_valid():
            thenom = form.cleaned_data.get('designation')
            equipes = Equipement.objects.all()
            count = 0
            for equipe in equipes:
                if ( thenom == equipe.designation):
                    count += 1

            if count > 0:
                messages.warning(request, f'Equipement existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'Equipement bien ajouter')
                return redirect('ListEqui')
                
        else:
            messages.error(request, f' ERREUR Certificat invalid non ajouter!')

    context = {
        'form':form,
        'titre':'Modifier',
        # 'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/equipement/ajoutEquipement.html',context)

# certificat homologation

@login_required(login_url='login_page')
def ListeHomo(request):
    context = {
        'homologations': HomologationEqui.objects.all().filter(etat = 'actif'),
        'today':date.today(),
    }

    return render(request,'gestionclient/certificatHomo/ListeHomolo.html',context)

@login_required(login_url='login_page')
def ajoutHomologation(request):
    # clients = Client.objects.all()
    today = date.today()
    form = HomologationForm(initial={'dateAttri':today,'nature':'Nouveau certificat'})
    if request.method == 'POST':
        form = HomologationForm(request.POST)
        if form.is_valid():
            thenclient = form.cleaned_data.get('client')
            thenequipe = form.cleaned_data.get('equipement')
            thencate = form.cleaned_data.get('categorie')
            thestart = form.cleaned_data.get('dateAttri')
            theEnd = form.cleaned_data.get('dateExp')
            homolos = HomologationEqui.objects.all()
            count = 0
            
            for homolo in homolos:
                if ( thenclient == homolo.client and thenequipe == homolo.equipement and thencate == homolo.categorie):
                    count += 1

            if count > 0:
                messages.warning(request, f'Homologation existe deja! ')
        
            else:
                if(thestart < today or theEnd < thestart or (theEnd.year - thestart.year) < 5):
                        messages.warning(request, f"Erreur verifier les dates")
                else:
                    form.save()
                    messages.success(request, f'Homologation bien ajouter')
                    return redirect('ListeHomo')
                
        else:
            messages.error(request, f' ERREUR Homologation invalid non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/certificatHomo/ajoutHomolo.html',context)

@login_required(login_url='login_page')
def detailHomologation(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'

    context = {
        # 'client': Client.objects.get(id = pk),
        'homologation': HomologationEqui.objects.get(id = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/certificatHomo/DetailHomo.html',context)

@login_required(login_url='login_page')
def modifierHomo(request,pk):
    homologation = HomologationEqui.objects.get(id=pk)
    today = date.today()
    form = HomologationForm(instance = homologation)
    if request.method == 'POST':
        form = HomologationForm(request.POST,instance = homologation)
        if form.is_valid():
            form.save()
            messages.success(request, f'Homologation bien modifier' )
            return redirect('ListeHomo')
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Modifier',
        'homologation':homologation,
        # 'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/certificatHomo/ajoutHomolo.html',context)

@login_required(login_url='login_page')
def updateHomologation(request,pk):
    homologation = HomologationEqui.objects.get(id=pk)
    today = date.today()
    form = HomologationForm(initial={'dateAttri':today,'client':homologation.client,'equipement':homologation.equipement,'categorie':homologation.categorie,'nature':'Renouvellement certificat','etat':'actif'})
    if request.method == 'POST':
        form = HomologationForm(request.POST)
        if form.is_valid():
            form.save()
            homologation.etat = 'deactif'
            homologation.save()
            messages.success(request, f'Homologation bien mis a jour' )
            return redirect('ListeHomo')
        else:
            messages.warning(request, f"Erreur form invalid")

    context = {
        'form':form,
        'titre':'Renouveller',
        'homologation':homologation,
        # 'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/certificatHomo/updateHomo.html',context)

# num court 

@login_required(login_url='login_page')
def ListeNumCourt(request):
    context = {
        'numcourts': NumeroCourt.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/numeroCourt/ListeNumCourt.html',context)

@login_required(login_url='login_page')
def ajoutnumCourt(request):
    today = date.today()
    form = NumeroCourtForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = NumeroCourtForm(request.POST)
        if form.is_valid():
            thennum = form.cleaned_data.get('numero')
            # thenequipe = form.cleaned_data.get('equipement')
            # thencate = form.cleaned_data.get('categorie')
            # thestart = form.cleaned_data.get('dateAttri')
            # theEnd = form.cleaned_data.get('dateExp')
            numeros = NumeroCourt.objects.all().filter(etat = 'actif')
            count = 0
            
            for numero in numeros:
                if ( thennum == numero.numero):
                    count += 1

            if count > 0:
                messages.warning(request, f'Numero existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'Numero bien ajouter')
                return redirect('ListeNumCourt')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Numero non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/numeroCourt/ajoutNumCourt.html',context)

@login_required(login_url='login_page')
def updateNumcourt(request,pk):
    numero = NumeroCourt.objects.get(id=pk)
    form = NumeroCourtForm(instance = numero)
    if request.method == 'POST':
        form = NumeroCourtForm(request.POST,instance = numero)
        if form.is_valid():
            thennum = form.cleaned_data.get('numero')
            numeros = NumeroCourt.objects.all().filter(etat = 'actif')
            count = 0
            if numero.numero == thennum:
                form.save()
                messages.success(request, f'Numero bien mis a jour')
                return redirect('ListeNumCourt')
            else:
                for numero in numeros:
                    if ( thennum == numero.numero):
                        count += 1

                if count > 0:
                    messages.warning(request, f'Numero existe deja! ')
            
                else:
                    form.save()
                    messages.success(request, f'Numero bien mis a jour')
                    return redirect('ListeNumCourt')

        else:
            messages.error(request, f' ERREUR formulaire invalide. Numero non ajouter!')

    context = {
        'form':form,
        'titre':'Modifier',
        # 'client': Client.objects.get(id=certiConf.client.id),
        }

    return render(request,'gestionclient/numeroCourt/ajoutNumCourt.html',context)

#numero long 

@login_required(login_url='login_page')
def ListePQ(request):
    context = {
        'pqs': PQ.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/numeroLong/PQ/ListePQ.html',context)

@login_required(login_url='login_page')
def ajoutPQ(request):
    today = date.today()
    form = PQForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = PQForm(request.POST)
        if form.is_valid():
            thepq = form.cleaned_data.get('pq')
            pqs = PQ.objects.all().filter(etat = 'actif')
            count = 0
            
            for pq in pqs:
                if ( thepq == pq.pq):
                    count += 1

            if count > 0:
                messages.warning(request, f'PQ existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'PQ bien ajouter')
                return redirect('ListePQ')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. PQ non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/numeroLong/PQ/ajoutPQ.html',context)

@login_required(login_url='login_page')
def ajoutAB(request,pk):
    today = date.today()
    pq = PQ.objects.get(id = pk)
    form = ABForm(initial={'pq':pq,'dateAtri':today})
    if request.method == 'POST':
        form = ABForm(request.POST)
        if form.is_valid():
            theab = form.cleaned_data.get('ab')
            abs = AB.objects.filter(pq = pk).filter(etat = 'actif')
            count = 0
            
            for ab in abs:
                if ( theab == ab.ab):
                    count += 1

            if count > 0:
                messages.warning(request, f'AB existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'AB bien ajouter')
                return redirect('detailsPQ',pk = pk)
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. AB non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        'pq':pq,
        }

    return render(request,'gestionclient/numeroLong/PQ/ajoutAB.html',context)

@login_required(login_url='login_page')
def detailsPQ(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'


    context = {
        'pq': PQ.objects.get(id = pk),
        'abs': AB.objects.filter(pq = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/numeroLong/PQ/detailPQ.html',context)

@login_required(login_url='login_page')
def updateAB(request,pk):
    ab = AB.objects.get(id=pk)
    pq = PQ.objects.get(id = pk)
    form = ABForm(instance = ab)
    if request.method == 'POST':
        form = ABForm(request.POST,instance = ab)
        if form.is_valid():
            theab = form.cleaned_data.get('ab')
            abs = AB.objects.filter(pq = pk).filter(etat = 'actif')
            count = 0
            
            for ab in abs:
                if ( theab == ab.ab):
                    count += 1

            if count > 0:
                messages.warning(request, f'AB existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'AB bien ajouter')
                return redirect('detailsPQ',pk = pk)
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. AB non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        'pq':pq,
        }

    return render(request,'gestionclient/numeroLong/PQ/ajoutAB.html',context)

@login_required(login_url='login_page')
def updatePQ(request,pk):
    # ab = AB.objects.get(id=pk)
    pq = PQ.objects.get(id = pk)
    form = PQForm(instance = pq)
    if request.method == 'POST':
        form = PQForm(request.POST,instance = pq)
        if form.is_valid():
            thepq = form.cleaned_data.get('pq')
            pqs = PQ.objects.all().filter(etat = 'actif')
            count = 0
            
            for pq in pqs:
                if ( thepq == pq.pq):
                    count += 1

            if count > 0:
                messages.warning(request, f'PQ existe deja! ')
        
            else:
                form.save()
                messages.success(request, f'PQ bien ajouter')
                return redirect('ListePQ')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. PQ non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/numeroLong/PQ/ajoutPQ.html',context)

# megas

@login_required(login_url='login_page')
def ListeMegas(request):
    context = {
        'megas': Megas.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/megas/ListeMegas.html',context)

@login_required(login_url='login_page')
def ajoutMegas(request):
    today = date.today()
    form = MegasForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = MegasForm(request.POST)
        if form.is_valid():
            # thedate = form.cleaned_data.get('date')
            # megas = Megas.objects.all().filter(etat = 'actif')
            # count = 0
            
            # for mega in megas:
            #     if ( thedate.month == mega.dateAtri):
            #         count += 1

            # if count > 0:
            #     messages.warning(request, f'PQ existe deja! ')
        
            # else:
                form.save()
                messages.success(request, f'Megas bien ajouter')
                return redirect('ListeMegas')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Megas non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/megas/ajoutMegas.html',context)

@login_required(login_url='login_page')
def updateMegas(request,pk):
    mega = Megas.objects.get(id = pk)
    form = MegasForm(instance = mega)
    if request.method == 'POST':
        form = MegasForm(request.POST,instance = mega)
        if form.is_valid():
           
            form.save()
            messages.success(request, f'Megas bien mis ajouter')
            return redirect('ListeMegas')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Megas non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/megas/ajoutMegas.html',context)

#minutes
@login_required(login_url='login_page')
def ListeMinutes(request):
    context = {
        'minutes': Minutes.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/minutes/ListeMinutes.html',context)

@login_required(login_url='login_page')
def ajoutMinutes(request):
    today = date.today()
    form = MinutesForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = MinutesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'MInutes bien ajouter')
            return redirect('ListeMinutes')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Minutes non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/minutes/ajoutMinutes.html',context)

@login_required(login_url='login_page')
def updateMinutes(request,pk):
    minutes = Minutes.objects.get(id = pk)
    form = MinutesForm(instance = minutes)
    if request.method == 'POST':
        form = MinutesForm(request.POST,instance = minutes)
        if form.is_valid():
           
            form.save()
            messages.success(request, f'Minutes bien mis ajouter')
            return redirect('ListeMinutes')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Minutes non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/minutes/ajoutMinutes.html',context)

#chiffre d'affaire
@login_required(login_url='login_page')
def ListeCA(request):
    context = {
        'cas': ChiffreAffaire.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/chiffre_Affaires/ListeCA.html',context)

@login_required(login_url='login_page')
def ajoutCA(request):
    today = date.today()
    form = CAForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = CAForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"chiffre d'affaire bien ajouter")
            return redirect('ListeCA')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. CA non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/chiffre_Affaires/ajoutCA.html',context)

@login_required(login_url='login_page')
def updateCA(request,pk):
    ca = ChiffreAffaire.objects.get(id = pk)
    form = CAForm(instance = ca)
    if request.method == 'POST':
        form = CAForm(request.POST,instance = ca)
        if form.is_valid():
            form.save()
            messages.success(request, f'ca bien mis ajouter')
            return redirect('ListeCA')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. ca non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/chiffre_Affaires/ajoutCA.html',context)

# frequence radio
@login_required(login_url='login_page')
def ListeFR(request):
    context = {
        'frs': FrequenceRadio.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/frequences_radio/ListeFR.html',context)

@login_required(login_url='login_page')
def ajoutFR(request):
    today = date.today()
    form = FrForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = FrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Frequence Radio bien ajouter")
            return redirect('ListeFR')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. FrequenceRadio non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/frequences_radio/ajoutFR.html',context)

@login_required(login_url='login_page')
def updateFR(request,pk):
    fr = FrequenceRadio.objects.get(id = pk)
    form = FrForm(instance = fr)
    if request.method == 'POST':
        form = FrForm(request.POST,instance = fr)
        if form.is_valid():
            form.save()
            messages.success(request, f'Frequence Radio bien mis ajouter')
            return redirect('ListeFR')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Frequence Radio non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/frequences_radio/ajoutFR.html',context)

#faisceaux hertzien
@login_required(login_url='login_page')
def ListeFH(request):
    context = {
        'fhs': FaisceauxHertzien.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/faisceaux_hertzien/ListeFH.html',context)

@login_required(login_url='login_page')
def ajoutFH(request):
    today = date.today()
    form = FhForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = FhForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Faisceaux Hertzien bien ajouter")
            return redirect('ListeFH')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Faisceaux Hertzien non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/faisceaux_hertzien/ajoutFH.html',context)

@login_required(login_url='login_page')
def updateFH(request,pk):
    fh = FaisceauxHertzien.objects.get(id = pk)
    form = FhForm(instance = fh)
    if request.method == 'POST':
        form = FhForm(request.POST,instance = fh)
        if form.is_valid():
            form.save()
            messages.success(request, f'Faisceaux Hertzien bien mis ajouter')
            return redirect('ListeFH')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Faisceaux Hertzien non ajouter!')

    context = {
        'form':form,
        'titre':"Modifier",
        }

    return render(request,'gestionclient/faisceaux_hertzien/ajoutFH.html',context)


#taux

@login_required(login_url='login_page')
def ListeTaux(request):
    context = {
        'tauxs': Taux.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/taux/ListeTaux.html',context)

@login_required(login_url='login_page')
def ajouterTaux(request):
    today = date.today()
    tauxs = Taux.objects.all()
    count = 0
    for taux in tauxs:
        if taux.dateAtri == today:
            count = count + 1
    if count > 0:
        messages.error(request, f'Taux du jour deja existant')
        return redirect('ListeTaux')
    else:
        form = TauxForm(initial={'dateAtri':today})
        if request.method == 'POST':
            form = TauxForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"Taux bien ajouter")
                return redirect('ListeTaux')
                    
            else:
                messages.error(request, f' ERREUR formulaire invalide. Taux non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        'date':today,
        }

    return render(request,'gestionclient/taux/ajoutTaux.html',context)



@login_required(login_url='login_page')
def updateTaux(request,pk):
    today = date.today()
    taux = Taux.objects.get(id = pk)
    factures = Facture_FFNumero.objects.filter(taux = taux).count()
    count = 0
    if factures > 0:
        messages.error(request, f'Le taux est deja utilise pour une facturation. elle ne peut etre modifier')
        return redirect('ListeTaux')
    else:
        form = TauxForm(instance = taux,initial={'dateAtri':today})
        if request.method == 'POST':
            form = TauxForm(request.POST,instance = taux)
            if form.is_valid():
                form.save()
                messages.success(request, f"Taux bien ajouter")
                return redirect('ListeTaux')
                    
            else:
                messages.error(request, f' ERREUR formulaire invalide. Taux non ajouter!')

    context = {
        'form':form,
        'titre':"Modifer",
        'date':today,
        }

    return render(request,'gestionclient/taux/ajoutTaux.html',context)


#tarif numero
@login_required(login_url='login_page')
def ListeTarifNum(request):
    context = {
        'tarifs': TarifFFNumero.objects.all(),
        'today':date.today(),
    }

    return render(request,'gestionclient/Tarif_Numero/ListeTarif.html',context)

@login_required(login_url='login_page')
def ListeTarifFSVANum(request):
    context = {
        'tarifFSVAs': TarifFSVANumero.objects.filter(etat = 'actif'),
        'today':date.today(),
    }

    return render(request,'gestionclient/Tarif_Numero/ListeTarifFSVA.html',context)

@login_required(login_url='login_page')
def ajoutertarifNumero(request):
    today = date.today()
    form = TarifFFNumeroForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = TarifFFNumeroForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            tarifs = TarifFFNumero.objects.filter(type = type).filter(etat = 'actif').count()
            if tarifs > 0:
                messages.error(request, f'Tarif existe deja !')
            else:
                form.save()
                messages.success(request, f"Tarif bien ajouter")
                return redirect('ListeTarifNum')  
        else:
            messages.error(request, f' ERREUR formulaire invalide. Tarif non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/Tarif_Numero/ajoutTarifNumero.html',context)


@login_required(login_url='login_page')
def ajoutertarifFSVANumero(request):
    today = date.today()
    form = TarifFSVANumeroForm(initial={'dateAtri':today})
    if request.method == 'POST':
        form = TarifFSVANumeroForm(request.POST)
        if form.is_valid():
            tarifs = TarifFSVANumero.objects.filter(etat = 'actif').count()
            if tarifs > 0:
                messages.error(request, f'Tarif existe deja !')
            else:
                form.save()
                messages.success(request, f"Tarif bien ajouter")
                return redirect('ListeTarifFSVANum')  
        else:
            messages.error(request, f' ERREUR formulaire invalide. Tarif non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        }

    return render(request,'gestionclient/Tarif_Numero/ajoutTarifFSVA.html',context)


# factures
@login_required(login_url='login_page')
def Listeff(request):
    context = {
        'ffs': FF_Numero.objects.filter(efacturer = 'non'),
        'today':date.today(),
    }

    return render(request,'gestionclient/factures_numero/listeAfacturer.html',context)

@login_required(login_url='login_page')
def detailsFFNum(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'


    context = {
        'FF_Numero': FF_Numero.objects.get(id = pk),
        # 'client': FF_Numero.objects.get(id = pk),
        # 'abs': AB.objects.filter(pq = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/factures_numero/detailffNum.html',context)

@login_required(login_url='login_page')
def facturerNum(request,pk):
    ff = FF_Numero.objects.get(id = pk)
    total = 0
    taux = Taux.objects.get(etat = 'actif')
    q_pq = TarifFFNumero.objects.filter( type = 'PQ').filter(etat = 'actif').first()
    q_ordinaire = TarifFFNumero.objects.filter( type = 'Code Ordinaire').filter(etat = 'actif').first()
    q_ussd = TarifFFNumero.objects.filter( type = 'USSD').filter(etat = 'actif').first()
    q_mnemonique = TarifFFNumero.objects.filter( type = 'Code Mnemonique').filter(etat = 'actif').first()
    q_mnc = TarifFFNumero.objects.filter( type = 'MNC').filter(etat = 'actif').first()
    q_nspc = TarifFFNumero.objects.filter( type = 'NSPC').filter(etat = 'actif').first()
    q_ispc = TarifFFNumero.objects.filter( type = 'ISPC').filter(etat = 'actif').first()
    q_cpti = TarifFFNumero.objects.filter( type = 'Code de preselection pour les transporteurs internationaux').filter(etat = 'actif').first()
    fsva = TarifFSVANumero.objects.filter(etat = 'actif').first()
    
    if ff.q_pq > 0:
        total = total + (q_pq * ff.q_pq)

    if ff.FS_etudeDossier == True:
        total = total + fsva.etudeDossier
    if ff.FS_agreEquipe == True:
        total = total + fsva.agrementEquip
    if ff.FS_autoARCT == True:
        total = total + fsva.autorisationARCT
        
    if ff.q_ordinaire > 0:
        
        if ff.RN_etudeDossier == True:
            total = total + q_ordinaire.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_ordinaire.fraisGestion
        if ff.RN_redevanceAnn == True:
            total = total + (q_ordinaire.redevanceAnn * ff.q_ordinaire)
            if ff.periode >  0:
                total = total *(ff.periode/365)

    if ff.q_ussd > 0:
        total = total + (q_ussd.redevanceAnn * ff.q_ussd)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_ussd.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_ussd.fraisGestion
    if ff.q_mnemonique > 0:
        total = total + (q_mnemonique.redevanceAnn * ff.q_mnemonique)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_mnemonique.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_mnemonique.fraisGestion
    if ff.q_mnc > 0:
        total = total + (q_mnc.redevanceAnn * ff.q_mnc)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_mnc.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_mnc.fraisGestion
    if ff.q_nspc > 0:
        total = total + (q_nspc.redevanceAnn * ff.q_nspc)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_nspc.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_nspc.fraisGestion
    if ff.q_ispc > 0:
        total = total + (q_ispc.redevanceAnn * ff.q_ispc)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_ispc.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_ispc.fraisGestion
    if ff.q_cpti > 0:
        total = total + (q_cpti.redevanceAnn * ff.q_cpti)
        if ff.periode >  0:
            total = total *(ff.periode/365)

        if ff.RN_etudeDossier == True:
            total = total + q_cpti.etudeDossier
        if ff.RN_fraisGestion == True:
            total = total + q_cpti.fraisGestion
   
    context = {
            'total': total,
            'totals': total*taux.taux,
            'taux':taux.taux,
        }
    return render(request,'gestionclient/factures_numero/factureNum.html',context)










# fiche facturation
@login_required(login_url='login_page')
def ListeCli(request):
    context = {
        'clients': Client.objects.all().filter(type = 'FSVA' and 'Operateur telephonique').filter(status = 'actif'),
        'today':date.today(),
    }

    return render(request,'gestionclient/FF_numero/ListeCliN.html',context)

@login_required(login_url='login_page')
def ListeFFNumero(request):
    context = {
        'FF_numeros': FF_Numero.objects.all().filter(etat = 'actif').order_by('-id'),
        'today':date.today(),
    }

    return render(request,'gestionclient/FF_numero/ListeFFNumero.html',context)

@login_required(login_url='login_page')
def ajoutFFNumero(request,pk):
    client = Client.objects.get(id = pk)
    today = date.today()
    form = FF_NumeroForm(initial={'dateAtri':today,'client':client})
    if request.method == 'POST':
        form = FF_NumeroForm(request.POST) 
        if form.is_valid(): 
            q_pq = form.cleaned_data.get('q_pq')
            q_ordinaire = form.cleaned_data.get('q_ordinaire')
            q_ussd = form.cleaned_data.get('q_ussd')
            q_mnemonique = form.cleaned_data.get('q_mnemonique')
            q_mnc = form.cleaned_data.get('q_mnc')
            q_nspc = form.cleaned_data.get('q_nspc')
            q_ispc = form.cleaned_data.get('q_ispc')
            q_cpti = form.cleaned_data.get('q_cpti')
            if q_pq and q_ordinaire and q_ussd and q_mnemonique and q_mnc and q_nspc and q_ispc and q_cpti == 0:
                messages.error(request, f' ERREUR formulaire incomplet! ajouter au moins un numero')
            else:
                if q_pq >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_pq):
                        numlong = PQ(client = client,ffnumero = ff,dateAtri= ff.dateAtri)
                        numlong.save()
                if q_ordinaire >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_ordinaire):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code Ordinaire',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_ussd >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_ussd):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'USSD',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_mnemonique >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_mnemonique):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code Mnemonique',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_mnc >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_mnc):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'MNC',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_nspc >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_nspc):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'NSPC',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_ispc >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_ispc):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'ISPC',dateAtri= ff.dateAtri)
                        numcourt.save()
                if q_cpti >0:
                    ff = FF_Numero.objects.all().last()
                    for q in range(q_cpti):
                        numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code de preselection pour les transporteurs internationaux',dateAtri= ff.dateAtri)
                        numcourt.save()
                form.save()
            messages.success(request, f"Fiche facturation bien ajouter")
            return redirect('ListeCli')
                
        else:
            messages.error(request, f' ERREUR formulaire invalide. Fiche facturation non ajouter!')

    context = {
        'form':form,
        'titre':"Ajouter",
        'client' : client,
        }

    return render(request,'gestionclient/FF_numero/ajoutFFNumero.html',context)

@login_required(login_url='login_page')
def detailsFFNumero(request,pk):
    if request.user.groups.filter(name='finance'):
        poste = 'finance'
    else:
        poste = 'nothing'


    context = {
        'FF_Numero': FF_Numero.objects.get(id = pk),
        # 'client': FF_Numero.objects.get(id = pk),
        # 'abs': AB.objects.filter(pq = pk),
        'today': date.today(),
        'name':poste,
    }
    return render(request,'gestionclient/FF_numero/detailsFFNumero.html',context)

@login_required(login_url='login_page')
def updateFFNumero(request,pk):
    ffnumero = FF_Numero.objects.get(id = pk)
    date = ffnumero.dateAtri
    client = Client.objects.get(id = ffnumero.client.id)
    form = FF_NumeroForm(instance = ffnumero,initial = {'nature':ffnumero.nature,'dateAtri':date})
    if request.method == 'POST':
        form = FF_NumeroForm(request.POST,instance = ffnumero)
        if form.is_valid(): 
            q_pq = form.cleaned_data.get('q_pq')
            q_ordinaire = form.cleaned_data.get('q_ordinaire')
            q_ussd = form.cleaned_data.get('q_ussd')
            q_mnemonique = form.cleaned_data.get('q_mnemonique')
            q_mnc = form.cleaned_data.get('q_mnc')
            q_nspc = form.cleaned_data.get('q_nspc')
            q_ispc = form.cleaned_data.get('q_ispc')
            q_cpti = form.cleaned_data.get('q_cpti')
            if q_pq and q_ordinaire and q_ussd and q_mnemonique and q_mnc and q_nspc and q_ispc and q_cpti == 0:
                messages.error(request, f' ERREUR formulaire incomplet!')
            else:
                if q_pq >=0:
                    ff = FF_Numero.objects.all().last()
                    lesnum = PQ.objects.all().filter(ffnumero = ff).count()
                    if q_pq > lesnum:
                        for q in range(q_pq - lesnum):
                            numlong = PQ(client = client,ffnumero = ff,dateAtri= ff.dateAtri)
                            numlong.save()
                    elif q_pq < lesnum:
                        for q in range(lesnum - q_pq):
                            numlong = PQ.objects.filter(ffnumero = ff).last()
                            numlong.delete()
                    if q_ordinaire >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code Ordinaire').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code Ordinaire',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code Ordinaire').last()
                                numcourt.delete()
                    if q_ussd >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'USSD').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'USSD',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'USSD').last()
                                numcourt.delete()
                    if q_mnemonique >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code Mnemonique').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code Mnemonique',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code Mnemonique').last()
                                numcourt.delete()
                    if q_mnc >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'MNC').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'MNC',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'MNC').last()
                                numcourt.delete()
                    if q_nspc >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'NSPC').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'NSPC',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'NSPC').last()
                                numcourt.delete()
                    if q_ispc >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'ISPC').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'ISPC',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'ISPC').last()
                                numcourt.delete()
                    if q_cpti >=0:
                        ff = FF_Numero.objects.all().last()
                        lecont = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code de preselection pour les transporteurs internationaux').count()
                        if q_ordinaire > lecont:
                            for q in range(q_ordinaire - lecont):
                                numcourt = NumeroCourt(client = client,ffnumero = ff,type = 'Code de preselection pour les transporteurs internationaux',dateAtri= ff.dateAtri)
                                numcourt.save()
                        elif q_ordinaire < lecont :
                            for q in range(lecont - q_ordinaire):
                                numcourt = NumeroCourt.objects.filter(ffnumero = ff).filter(type = 'Code de preselection pour les transporteurs internationaux').last()
                                numcourt.delete()
                    form.save()
                    messages.success(request, f"Fiche facturation bien modifier")
                    return redirect('ListeFFNumero')
        else:
            messages.error(request, f' ERREUR formulaire invalide. Fiche facturation non modifer!')

    context = {
        'form':form,
        'titre':"Modifier",
        'client' : client,
        'ff':ffnumero,
        }

    return render(request,'gestionclient/FF_numero/ajoutFFNumero.html',context)

@login_required(login_url='login_page')
def facturerFFNumero(request,pk):
    ffnumero = FF_Numero.objects.get(id = pk)
    ffnumero.facturer = 'oui'
    ffnumero.save()
    return redirect('ListeFFNumero')

@login_required(login_url='login_page')
def supprimerFFNumero(request,pk):
    ffnumero = FF_Numero.objects.get(id = pk)
    ffnumero.delete()
    return redirect('ListeFFNumero')

# @login_required(login_url='login_page')
# def FactureFFNumero(request,pk):






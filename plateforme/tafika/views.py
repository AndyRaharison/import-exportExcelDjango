from django.shortcuts import render , HttpResponseRedirect, get_object_or_404 , redirect
from .resources import BeneficiaireResource
from django.contrib import messages
from tablib import Dataset
from .forms import BeneficiaireRegistration
from .models import Beneficiaire, BeneficiaireModifie 
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views import View


# Create your views here.
#affichage des donnees
def afficher(request):
    return render(request, 'tafika/liste.html')

def afficher_modifications(request):
    beneficiaires_modifies = BeneficiaireModifie.objects.all()
    return render(request, 'tafika/donneModif.html', {'beneficiaires_modifies': beneficiaires_modifies})
    

def importation(request):
    if request.method == 'POST':
        beneficiaire_resource = BeneficiaireResource()
        dataset = Dataset()
        new_benenef = request.FILES['fichier']
        imported_data = dataset.load(new_benenef.read(), format= 'xlsx')
        for data in imported_data:
                value = Beneficiaire(
                     data[0],
                     data[1],
                     data[2],
                     data[3],
                     data[4],
                     data[5],
                     data[6],
                     data[7],
                     data[8],
                     data[9],
                     data[10],
                     data[11],
                     data[12],
                 )
        value.save()

    benef = Beneficiaire.objects.all() 
    messages = "donnees importer"
    
    return render(request,'tafika/liste.html',{'benefici':benef} )

#suppression des donnees

def suppression(request , id):
    if request.method =='POST':
            sup = Beneficiaire.objects.get(pk= id)
            sup.delete()
    return HttpResponseRedirect('/')

#Modification des donnees

def modifier_beneficiaire(request, beneficiaire_id):
    beneficiaire = get_object_or_404(Beneficiaire, id=beneficiaire_id)

    if request.method == 'POST':
        form = BeneficiaireRegistration(request.POST, instance=beneficiaire)
        if form.is_valid():
            form.save()
            # Après la modification, vous pouvez rediriger vers une page spécifique ou afficher un message de succès
            return redirect('tafika/moidification.html')
    else:
        form = BeneficiaireRegistration(instance=beneficiaire)

    return render(request, 'tafika/modification.html', {'form': form})

#detection des modifications 

class DetecterEtEnregistrerModificationsView(View):
    def get(self, request, *args, **kwargs):
        beneficiaires = Beneficiaire.objects.all()

        for beneficiaire in beneficiaires:
            beneficiaire_modifie, created = BeneficiaireModifie.objects.get_or_create(beneficiaire=beneficiaire)

            # Comparer les attributs de Beneficiaire et BeneficiaireModifie pour détecter les modifications
            if (
                beneficiaire.nom != beneficiaire_modifie.beneficiaire.nom or
                beneficiaire.prenom != beneficiaire_modifie.beneficiaire.prenom or
                beneficiaire.matricule != beneficiaire_modifie.beneficiaire.matricule or
                beneficiaire.numero_piece != beneficiaire_modifie.beneficiaire.numero_piece or
                beneficiaire.type_piece != beneficiaire_modifie.beneficiaire.type_piece or
                beneficiaire.date_livrance != beneficiaire_modifie.beneficiaire.date_livrance or
                beneficiaire.telephone != beneficiaire_modifie.beneficiaire.telephone or
                beneficiaire.email != beneficiaire_modifie.beneficiaire.email or
                beneficiaire.date_naissance != beneficiaire_modifie.beneficiaire.date_naissance or
                beneficiaire.code_postal != beneficiaire_modifie.beneficiaire.code_postal or
                beneficiaire.sexe != beneficiaire_modifie.beneficiaire.sexe or
                beneficiaire.addresse != beneficiaire_modifie.beneficiaire.addresse
            ):
                # Si les attributs sont différents, enregistrer dans BeneficiaireModifie
                beneficiaire_modifie.date_modification = datetime.now()
                beneficiaire_modifie.save()

        return render(request, 'tafika/donneModif.html', {})
 
# def modification(request, id):
#     pi = beneficiaire.objects.get(pk=id)

#     if request.method == 'POST':
#         fm = BeneficiaireRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return render(request, 'tafika/modification.html', {'form': fm, 'message': 'Les modifications ont été enregistrées'})
#             #return redirect('nom_de_la_vue_de_confirmation')  # Rediriger vers la vue de confirmation après la modification
#     else:
#         fm = BeneficiaireRegistration(instance=pi)

#     return render(request, 'tafika/modification.html', {'form': fm})
# def modification(request, id):
#     pi = beneficiaire.objects.get(pk=id)

#     if request.method == 'POST':
#         fm = BeneficiaireRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#         #BeneficiaireModifie.objects.create(beneficiaire=pi)  # Créer un objet BeneficiaireModifie
#     else:
#         fm = BeneficiaireRegistration(instance=pi)

#     return render(request, 'tafika/modification.html', {'form': fm})

# def liste_modifications(request):
#     modifications = BeneficiaireModifie.objects.order_by('-date_modification')
#     return render(request, 'tafika/donneModif.html', {'modifications': modifications})

#migration des donnees beneficiaire modifier 


# def modificationBenef(request, id):
#     pi = beneficiaire.objects.get(pk=id)

#     if request.method == 'POST':
#         fm = BeneficiaireRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             BeneficiaireModifie.objects.create(Beneficiaire=pi)  # Créer un objet BeneficiaireModifie
            
#     else:
#         fm = BeneficiaireRegistration(instance=pi)

#     return render(request, 'tafika/modification.html', {'form': fm})

# def modifierBeneficiaire(request, id):
    
#     benef = get_object_or_404(beneficiaire, pk=id)

#     if request.method == 'POST':
#         form = BeneficiaireRegistration(request.POST, instance=benef)
#         if form.is_valid():
#             form.save()

#             # Transférer les données modifiées vers BeneficiaireModifie
#             BeneficiaireModifie.objects.create(
#                 beneficiaire=beneficiaire,
#                 nom_modifie=form.cleaned_data['nom'],
#                 prenom_modifie=form.cleaned_data['prenom'],
#                 matricule_modif=form.cleaned_data['matricule'],
#                 numero_piece_modif=form.cleaned_data['numero_piece'],
#                 type_piece_modif=form.cleaned_data['type_piece'],
#                 date_livrance_modif=form.cleaned_data['date_livrance'],
#                 telephone_modif=form.cleaned_data['telephone'],
#                 email_modif=form.cleaned_data['email'],
#                 date_naissance_modif=form.cleaned_data['date_naissance'],
#                 code_postal_modif=form.cleaned_data['code_postal'],
#                 sexe_modif=form.cleaned_data['sexe'],
#                 adresse_modif=form.cleaned_data['adresse']
#             )
#     else:
#         form = BeneficiaireRegistration(instance=beneficiaire)

#     return render(request, 'tafika/donneModif.html', {'form': form})





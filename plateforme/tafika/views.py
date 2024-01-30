from django.shortcuts import render , HttpResponseRedirect, get_object_or_404 , redirect
from .resources import BeneficiaireResource
from django.contrib import messages
from tablib import Dataset
from .forms import BeneficiaireRegistration
from .models import Beneficiaire, BeneficiaireModifie 


# Create your views here.
#affichage des donnees
def afficher(request):
    return render(request, 'tafika/liste.html')

def afficher_modifications(request):
    beneficiaires_modifies = BeneficiaireModifie.objects.all()
    return render(request, 'tafika/afficher_modifications.html', {'beneficiaires_modifies': beneficiaires_modifies})

    

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
            return redirect('tafika/donneModif.html')
    else:
        form = BeneficiaireRegistration(instance=beneficiaire)

    return render(request, 'tafika/modification.html', {'form': form})






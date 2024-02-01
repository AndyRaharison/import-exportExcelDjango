from django.shortcuts import render , HttpResponseRedirect, get_object_or_404 , redirect
from .resources import BeneficiaireResource
from tablib import Dataset
from .forms import BeneficiaireRegistration
from .models import Beneficiaire, BeneficiaireModifie 
from django.core.paginator import Paginator


# Create your views here.
#affichage des donnees
def afficher(request):
    return render(request, 'tafika/liste.html')

def afficher_modifications(request):
    beneficiaires_modifies = BeneficiaireModifie.objects.all()
    
    # Nombre d'éléments à afficher par page
    elements_par_page = 3
    paginator = Paginator(beneficiaires_modifies, elements_par_page)
    # Récupérez le numéro de la page à afficher
    page = request.GET.get('page', 1)
    # Obtenez les éléments de la page spécifiée
    beneficiaires_modifies_page = paginator.get_page(page)
    
    return render(request, 'tafika/donneModif.html', {'beneficiaires_modifies': beneficiaires_modifies_page})

    

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
     # Nombre d'éléments à afficher par page
    elements_par_page = 3
    paginator = Paginator(benef, elements_par_page)
    # Récupérez le numéro de la page à afficher
    page = request.GET.get('page', 1)
    # Obtenez les éléments de la page spécifiée
    beneficiaires_pages = paginator.get_page(page)
    
    return render(request,'tafika/liste.html',{'benefici':beneficiaires_pages} )

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
            return redirect('afficher_modifications')
    else:
        form = BeneficiaireRegistration(instance=beneficiaire)

    return render(request, 'tafika/modification.html', {'form': form})






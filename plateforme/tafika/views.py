from django.shortcuts import render , HttpResponseRedirect
from .resources import BeneficiaireResource
from django.contrib import messages
from tablib import Dataset
from .forms import BeneficiaireRegistration
from .models import beneficiaire


# Create your views here.
#affichage des donnees
def afficher(request):
    return render(request, 'tafika/liste.html')
    

def importation(request):
    if request.method == 'POST':
        beneficiaire_resource = BeneficiaireResource()
        dataset = Dataset()
        new_benenef = request.FILES['fichier']
        imported_data = dataset.load(new_benenef.read(), format= 'xlsx')
        for data in imported_data:
                value = beneficiaire(
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

    benef = beneficiaire.objects.all() 
    messages = "donnees importer"
    
    return render(request,'tafika/liste.html',{'benefici':benef} )

#suppression des donnees

def suppression(request , id):
    if request.method =='POST':
            sup = beneficiaire.objects.get(pk= id)
            sup.delete()
    return HttpResponseRedirect('/')

#Modification des donnees
 
# def modification(request, id):
#     if request.method == 'POST':
#             pi = beneficiaire.objects.get(pk=id)
#             fm = BeneficiaireRegistration(request.POST, instance=pi)
#             if fm.is_valid():
#                 fm.save()
#     else:
#         pi = beneficiaire.objects.get(pk = id)
#         fm = BeneficiaireRegistration(instance=id)
#     return render(request,'tafika/modification.html',{'form':fm})
def modification(request, id):
    pi = beneficiaire.objects.get(pk=id)

    if request.method == 'POST':
        fm = BeneficiaireRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            #return redirect('nom_de_la_vue_de_confirmation')  # Rediriger vers la vue de confirmation après la modification
    else:
        fm = BeneficiaireRegistration(instance=pi)

    return render(request, 'tafika/modification.html', {'form': fm})



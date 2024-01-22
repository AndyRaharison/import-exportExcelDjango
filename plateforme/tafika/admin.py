from django.contrib import admin
from .models import beneficiaire
from import_export.admin import ImportExportModelAdmin
from .models import beneficiaire

# Register your models here.
@admin.register(beneficiaire)

class beneficiaireAdmin (ImportExportModelAdmin):
    list_display = ('id', 'nom', 'prenom','matricule','numero_piece','type_piece','date_livrance','email','date_naissance','code_postal','sexe','adresse')

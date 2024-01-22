from import_export import resources
from .models import beneficiaire

class BeneficiaireResource(resources.ModelResource):
    class Meta:
        model = beneficiaire
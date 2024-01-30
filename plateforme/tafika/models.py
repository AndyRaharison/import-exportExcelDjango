from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Beneficiaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    numero_piece = models.CharField(max_length=255)
    type_piece = models.CharField(max_length=255)
    date_livrance = models.DateField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_naissance = models.DateField()
    code_postal = models.CharField(max_length=10)
    sexe = models.CharField(max_length=10)
    adresse = models.CharField(max_length=255)

class BeneficiaireModifie(models.Model):
    beneficiaire = models.OneToOneField(Beneficiaire, on_delete=models.CASCADE)
    date_modification = models.DateTimeField(auto_now_add=True)

# Signal pour détecter les modifications et enregistrer dans BeneficiaireModifie

# post_save.connect(detecter_et_enregistrer_modifications, sender=Beneficiaire)
@receiver(post_save, sender=Beneficiaire)
def detecter_et_enregistrer_modifications(sender, instance, **kwargs):
    beneficiaire_modifie, created = BeneficiaireModifie.objects.get_or_create(beneficiaire=instance)

    # Comparer les attributs de Beneficiaire et BeneficiaireModifie pour détecter les modifications
    if (
        instance.nom != beneficiaire_modifie.beneficiaire.nom or
        instance.prenom != beneficiaire_modifie.beneficiaire.prenom or
        instance.matricule != beneficiaire_modifie.beneficiaire.matricule or
        instance.numero_piece != beneficiaire_modifie.beneficiaire.numero_piece or
        instance.type_piece != beneficiaire_modifie.beneficiaire.type_piece or
        instance.date_livrance != beneficiaire_modifie.beneficiaire.date_livrance or
        instance.telephone != beneficiaire_modifie.beneficiaire.telephone or
        instance.email != beneficiaire_modifie.beneficiaire.email or
        instance.date_naissance != beneficiaire_modifie.beneficiaire.date_naissance or
        instance.code_postal != beneficiaire_modifie.beneficiaire.code_postal or
        instance.sexe != beneficiaire_modifie.beneficiaire.sexe or
        instance.adresse != beneficiaire_modifie.beneficiaire.adresse
    ):
        # Si les attributs sont différents, enregistrer dans BeneficiaireModifie
        beneficiaire_modifie.date_modification = datetime.now()
        beneficiaire_modifie.save()
 


# from django.db import models




# # Creation des models
# class beneficiaire(models.Model):
#     nom = models.CharField(max_length=255, default='')
#     prenom =models.CharField(max_length=255, default='')
#     matricule = models.CharField(max_length=255, default='')
#     numero_piece = models.CharField(max_length=25, default='')
#     type_piece = models.CharField(max_length=25, default='')
#     date_livrance = models.DateTimeField( default='')
#     telephone = models.CharField(max_length=25, default='')
#     email = models.EmailField( default='')
#     date_naissance = models.CharField(max_length=25, default='')
#     code_postal = models.CharField(max_length=10, default='')
#     sexe = models.CharField(max_length=10, default='')
#     adresse = models.CharField(max_length=25, default='')
#     modifie = models.BooleanField(default=False)
    
# class BeneficiaireModifie(models.Model):
#     beneficiaire = models.ForeignKey(beneficiaire, on_delete=models.CASCADE)
#     nom_modifie = models.CharField(max_length=255, default='')
#     prenom_modif =models.CharField(max_length=255, default='')
#     matricule_modif = models.CharField(max_length=255, default='')
#     numero_piece_modif = models.CharField(max_length=25, default='')
#     type_piece_modif = models.CharField(max_length=25, default='')
#     date_livrance_modif = models.DateTimeField( default='')
#     telephone_modif = models.CharField(max_length=25, default='')
#     email_modif = models.EmailField( default='')
#     date_naissance_modif = models.CharField(max_length=25, default='')
#     code_postal_modif = models.CharField(max_length=10, default='')
#     sexe_modif = models.CharField(max_length=10, default='')
#     adresse_modif = models.CharField(max_length=25, default='')
#     date_modification = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.nom_modifie}{self.prenom_modifie}{self.matricule_modif}{self.numero_piece_modif}{self.type_piece_modif}{self.date_livrance_modif}{self.telephone_modif}{self.email_modif}{self.date_naissance_modif}{self.code_postal_modif}{self.sexe_modif}{self.adresse_modif}{self.date_modification}"
    
    
    
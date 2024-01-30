from django.db import models


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
    
    
    
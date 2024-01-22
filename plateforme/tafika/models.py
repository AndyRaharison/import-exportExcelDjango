from django.db import models

# Create your models here.
class beneficiaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom =models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    numero_piece = models.CharField(max_length=25)
    type_piece = models.CharField(max_length=25)
    date_livrance = models.DateTimeField()
    telephone = models.CharField(max_length=25)
    email = models.EmailField()
    date_naissance = models.CharField(max_length=25)
    code_postal = models.CharField(max_length=10)
    sexe = models.CharField(max_length=10)
    adresse = models.CharField(max_length=25)
    
    
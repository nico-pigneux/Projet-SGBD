from django.db import models
from django.conf import global_settings
from django.utils import translation
from compositefk.fields import CompositeForeignKey
from django.db.models.deletion import CASCADE, DO_NOTHING

# Create your models here.

class Utilisateur(models.Model):
    util_nom = models.CharField(db_column='Util_nom', primary_key=True, max_length=20) ## on retire la primary key ?##
    # Field name made lowercase. The composite primary key (Util_nom, Util_prenom) found, that is not supported.\
    # The first column is selected.
    util_prenom = models.CharField(db_column='Util_prenom', max_length=20)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=30)  # Field name made lowercase.
    profil = models.TextField(db_column='Profil')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'utilisateur'
        constraints = [
            models.UniqueConstraint(fields=['util_nom', 'util_prenom'], name='util_nom_prenom')
        ]

class CategorieDeSoumission(models.Model):
    nom = models.CharField(db_column='Nom', primary_key=True, max_length=10)  # Field name made lowercase.
    soumi_intitule = models.OneToOneField('Soumission', models.DO_NOTHING, db_column='Soumi_intitule', blank=True, null=True)  # Field name made lowercase.
    wk_intitule = models.OneToOneField('Workshop', models.DO_NOTHING, db_column='WK_intitule', blank=True, null=True)  # Field name made lowercase.
    nombre_de_pages_max = models.IntegerField(db_column='Nombre_de_pages_max')  # Field name made lowercase.
    mep_police = models.CharField(db_column='Mep_Police', max_length=10)  # Field name made lowercase.
    mep_taille_de_caracteres = models.IntegerField(db_column='Mep_Taille_de_caracteres')  # Field name made lowercase.
    mep_type_de_logiciel = models.CharField(db_column='Mep_Type_de_logiciel', max_length=10)  # Field name made lowercase.
    date_limite_de_soumission = models.DateField(db_column='Date_limite_de_soumission')  # Field name made lowercase.
    date_de_notification = models.CharField(db_column='Date_de_notification', max_length=1)  # Field name made lowercase.
    date_limite_de_correction = models.DateField(db_column='Date_limite_de_correction')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'categorie_de_soumission'


class Conference(models.Model):
    conf_intitule = models.CharField(db_column='Conf_intitule', primary_key=True, max_length=100)  # Field name made lowercase.
    date_de_debut = models.DateField(db_column='Date_de_debut')  # Field name made lowercase.
    date_de_fin = models.DateField(db_column='Date_de_fin')  # Field name made lowercase.
    loc_ville = models.CharField(db_column='Loc_Ville', max_length=15)  # Field name made lowercase.
    loc_pays = models.CharField(db_column='Loc_Pays', max_length=15)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=10)  # Field name made lowercase.
    text_introductif = models.TextField(db_column='Text_introductif')  # Field name made lowercase.
    editeur_actes = models.CharField(db_column='Editeur_actes', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'conference'



class Etat(models.Model):
    etat = models.CharField(db_column='Etat', primary_key=True, max_length=10)  # Field name made lowercase.
    soumi_intitule = models.OneToOneField('Soumission', models.DO_NOTHING, db_column='Soumi_intitule')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'etat'


class Evaluation(models.Model):
    soumi_intitule = models.OneToOneField('Soumission', models.DO_NOTHING, db_column='Soumi_intitule', primary_key=True)
    # Field name made lowercase. The composite primary key (Soumi_intitule, PC_nom, PC_prenom) found, that is not supported.\
    # The first column is selected.
    pc_nom = models.ForeignKey('ProgramCommitee', models.DO_NOTHING, db_column='PC_nom')  # Field name made lowercase.
    pc_prenom = models.ForeignKey('ProgramCommitee', models.DO_NOTHING, db_column='PC_prenom', to_field='pc_prenom', related_name='evaluation_pc_prenom_set')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'evaluation'
        constraints = [
            models.UniqueConstraint(fields=['soumi_intitule', 'pc_nom', 'pc_prenom'], name='soumi_nom_prenom')
        ]

class Inscription(models.Model):
    conf_intitule = models.OneToOneField(Conference, models.DO_NOTHING, db_column='Conf_intitule', primary_key=True)
    # Field name made lowercase. The composite primary key (Conf_intitule, Util_nom, Util_prenom) found, that is not supported.\
    # The first column is selected.
    util_nom = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='Util_nom')  # Field name made lowercase.
    util_prenom = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='Util_prenom', to_field='util_prenom', related_name='inscription_util_prenom_set')  # Field name made lowercase.
    #util_nom_prenom = CompositeForeignKey(Utilisateur, on_delete = DO_NOTHING, to_fields = ['util_nom', 'util_prenom'])  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'inscription'
        # unique_together = (('conf_intitule', 'util_nom', 'util_prenom'), ('conf_intitule', 'util_nom', 'util_prenom'),)
        constraints = [
            models.UniqueConstraint(fields=['conf_intitule', 'util_nom', 'util_prenom'], name='conf_nom_prenom')
        ]

class Organisateur(models.Model):
    orga_nom = models.CharField(db_column='Orga_nom', primary_key=True, max_length=20)  # Field name made lowercase.
    conf_intitule = models.OneToOneField(Conference, models.DO_NOTHING, db_column='Conf_intitule')  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=50)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'organisateur'


class Organise(models.Model):
    conf_intitule = models.OneToOneField(Conference, models.DO_NOTHING, db_column='Conf_intitule', primary_key=True)
    # Field name made lowercase. The composite primary key (Conf_intitule, PC_nom, PC_prenom) found, that is not supported. \
    # The first column is selected.
    pc_nom = models.ForeignKey('ProgramCommitee', models.DO_NOTHING, db_column='PC_nom')  # Field name made lowercase.
    pc_prenom = models.ForeignKey('ProgramCommitee', models.DO_NOTHING, db_column='PC_prenom', to_field='pc_prenom', related_name='organise_pc_prenom_set')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'organise'
        #unique_together = (('conf_intitule', 'pc_nom', 'pc_prenom'), ('conf_intitule', 'pc_nom', 'pc_prenom'),)
        constraints = [
            models.UniqueConstraint(fields=['conf_intitule', 'pc_nom', 'pc_prenom'], name='conf_pc_nom_prenom')
        ]

class ProgramCommitee(models.Model):
    pc_nom = models.CharField(db_column='PC_nom', max_length=20) 
    # Field name made lowercase. The composite primary key (PC_nom, PC_prenom) found, that is not supported. The first column is selected.
    pc_prenom = models.CharField(db_column='PC_prenom', primary_key=True, max_length=30)  # Field name made lowercase.
    adresse_professionnelle = models.CharField(db_column='Adresse_Professionnelle', max_length=50)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'program_commitee'
        # unique_together = (('pc_nom', 'pc_prenom'), ('pc_nom', 'pc_prenom'),)
        constraints = [
            models.UniqueConstraint(fields=['pc_nom', 'pc_prenom'], name='pc_nom_prenom')
        ]

class Responsabilite(models.Model):
    responsabilite = models.CharField(db_column='Responsabilite', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'responsabilite'


class Responsable(models.Model):
    resp_nom = models.CharField(db_column='Resp_nom', primary_key=True, max_length=20)
    # Field name made lowercase. The composite primary key (Resp_nom, Resp_prenom) found, that is not supported.\
    # The first column is selected.
    resp_prenom = models.CharField(db_column='Resp_prenom', max_length=30)  # Field name made lowercase.
    adresse_professionnelle = models.CharField(db_column='Adresse_Professionnelle', max_length=50)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=30)  # Field name made lowercase.
    responsabilite = models.ForeignKey(Responsabilite, models.DO_NOTHING, db_column='Responsabilite')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'responsable'
        #unique_together = (('resp_nom', 'resp_prenom'), ('resp_nom', 'resp_prenom'),)
        constraints = [
            models.UniqueConstraint(fields=['resp_nom', 'resp_prenom'], name='resp_nom_prenom')
        ]

class ResponsableDe(models.Model):
    conf_intitule = models.OneToOneField(Conference, models.DO_NOTHING, db_column='Conf_intitule', primary_key=True) 
    # Field name made lowercase. The composite primary key (Conf_intitule, Resp_nom, Resp_prenom) found, that is not supported.\
    # The first column is selected.
    resp_nom = models.ForeignKey(Responsable, models.DO_NOTHING, db_column='Resp_nom')  # Field name made lowercase.
    resp_prenom = models.ForeignKey(Responsable, models.DO_NOTHING, db_column='Resp_prenom', to_field='resp_prenom', related_name='responsablede_resp_prenom_set')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'responsable_de'
        # unique_together = (('conf_intitule', 'resp_nom', 'resp_prenom'), ('conf_intitule', 'resp_nom', 'resp_prenom'),)
        constraints = [
            models.UniqueConstraint(fields=['conf_intitule', 'resp_nom', 'resp_prenom'], name='conf_resp_nom_prenom')
        ]

class Session(models.Model):
    sess_intitule = models.CharField(db_column='Sess_intitule', primary_key=True, max_length=100)  # Field name made lowercase.
    themes = models.CharField(db_column='Themes', max_length=100)  # Field name made lowercase.
    de_intitule = models.ForeignKey(Conference, models.DO_NOTHING, db_column='De_Intitule')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'session'


class Soumission(models.Model):
    soumi_intitule = models.CharField(db_column='Soumi_intitule', primary_key=True, max_length=100)  # Field name made lowercase.
    date_de_soumission = models.DateField(db_column='Date_de_soumission')  # Field name made lowercase.
    session_intitule = models.ForeignKey(Session, models.DO_NOTHING, db_column='session_intitule')
    util_nom = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='Util_nom')  # Field name made lowercase.
    util_prenom = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='Util_prenom', to_field='util_prenom', related_name='soumission_util_prenom_set')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'soumission'


class Workshop(models.Model):
    wk_intitule = models.CharField(db_column='WK_intitule', primary_key=True, max_length=100)  # Field name made lowercase.
    date_de_debut = models.DateField(db_column='Date_de_debut')  # Field name made lowercase.
    date_de_fin = models.DateField(db_column='Date_de_fin')  # Field name made lowercase.
    loc_ville = models.CharField(db_column='Loc_Ville', max_length=15)  # Field name made lowercase.
    loc_pays = models.CharField(db_column='Loc_Pays', max_length=15)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=10)  # Field name made lowercase.
    text_introductif = models.TextField(db_column='Text_introductif')  # Field name made lowercase.
    editeur_actes = models.CharField(db_column='Editeur_actes', max_length=30)  # Field name made lowercase.
    conference_reliee_pour_workshop = models.CharField(db_column='Conference_reliee_pour_workshop', max_length=10)  # Field name made lowercase.
    conf_intitule = models.ForeignKey(Conference, models.DO_NOTHING, db_column='Conf_intitule')  # Field name made lowercase.
    soumi_intitule = models.ForeignKey(Soumission, models.DO_NOTHING, db_column='Soumi_intitule')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'workshop'

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

#     def __str__(self) :
#         return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self) :
#         return self.choice_text


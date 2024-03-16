from django.db import models

# Create your models here.
class InfoModel(models.Model):
  class Gender(models.TextChoices): 
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHERS = "OTHERS", "Others"
        
  class Country(models.TextChoices): 
    UG = "UG", "Uganda"
    KE = "KE", "Kenya"
    TZ = "TZ", "Tanzania"
    US = "US", "United states"
    CANADA = "CANADA", "Canada"
        
  first_name = models.CharField(max_length=25, default="", verbose_name="Surname")
  last_name = models.CharField(max_length=25, default="", verbose_name="Given name")
  bio = models.TextField(blank=True, verbose_name="Biodata")
  is_active = models.BooleanField(default="")
  gender = models.CharField(max_length=25, default=Gender.MALE, choices=Gender.choices)
  country = models.CharField(max_length=25, default=Country.UG, choices=Country.choices)
class Teacher(InfoModel): 
  class Subject(models.TextChoices): 
    MTC = "MTC", "Math"
    ENG = "ENG", "English"
    CHEM = "CHEM", "Chemistry"
    BIO = "BIO", "Biology"
    PHY = "PHY", "Physics"
    
  email = models.EmailField(max_length=50, default="")
  subject = models.CharField(max_length=25, default=Subject.MTC, choices=Subject.choices)
  
      
  def __str__(self): 
    return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
  title = models.CharField(max_length=40)
  
  def __str__(self): 
    return self.title
    
class Student(InfoModel):
  course = models.ForeignKey(Course, related_name="students", on_delete=models.CASCADE)
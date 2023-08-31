from django.db import models


class Theme(models.Model):
    backgound_color_1 = models.CharField(max_length=6, default="02557a")
    backgound_color_2 = models.CharField(max_length=6, default="c7e0f4")
    text_color_1 = models.CharField(max_length=6, default="1b1b1b" )
    text_color_2 = models.CharField(max_length=6, default="1b1b1b")
    text_color_3 = models.CharField(max_length=6, default="ff9001" )

def get_theme():
    return Theme.objects.get_or_create(id=1)[0].id

class Employee(models.Model):
    name_en = models.CharField(max_length=60)
    name_ar = models.CharField(max_length=60)
    file_id = models.CharField(max_length=60)
    finger_print_id = models.CharField(max_length=60)
    department = models.CharField(max_length=60)
    national_id = models.CharField(max_length=60)
    theme = models.ForeignKey(Theme, on_delete=models.SET_DEFAULT, default=get_theme)

    def __str__(self):
        return self.name_ar


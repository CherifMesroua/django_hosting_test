from django.db import models
from django.utils.text import slugify
import os

# 1. Define this renaming function
def sanitize_filename(instance, filename):
    name, ext = os.path.splitext(filename)
    # This turns "décran" into "decran" and keeps it safe
    clean_name = slugify(name) 
    return f"uploads/{clean_name}{ext}"

class Upload(models.Model):
    caption = models.CharField(max_length=100)
    # 2. Use the function here instead of the string 'uploads/'
    image = models.ImageField(upload_to=sanitize_filename) 

    def __str__(self):
        return self.caption
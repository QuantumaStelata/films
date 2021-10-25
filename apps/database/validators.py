import os
from django.core.exceptions import ValidationError

def photo_validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемый формат файла')

def file_validator(instance, filename):
    return f'films/{instance.title}/{filename}'

def video_validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемый формат файла')
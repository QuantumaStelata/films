import os
from django.core.exceptions import ValidationError

def photo_validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемый формат файла')
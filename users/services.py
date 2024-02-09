from django.contrib.auth import authenticate
from users.models import CustomUser




def signin_service(form) -> CustomUser:
    """Проверить данные формы на валидность"""
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(email=email, password=password)
        if user:
            return user
        else:
            return None
    else:
        return None


def generate_context(**kwargs):
    """Генерация контекста для шаблонов"""
    return kwargs
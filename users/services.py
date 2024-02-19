from django.contrib.auth import authenticate
from users.models import CustomUser
from carts.models import Cart




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


def add_anonymous_user_cart(request, user):
    """Функция для привязки корзины анонимного пользователя с только что вошедшим или созданным пользователем"""
    session_key = request.session.session_key
    carts = Cart.objects.filter(session_key=session_key)
    if carts:
        carts.update(user=user)


def signup_service(form) ->CustomUser:
    if form.is_valid():
        form.save()
        return form.instance
    return None

def profile_edit_service(form):
    """Редактирование профиля"""
    if form.is_valid():
        form.save()
        return True
    return False



def generate_context(**kwargs):
    """Генерация контекста для шаблонов"""
    return kwargs
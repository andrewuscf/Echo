from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AbstractUserCreationForm(UserCreationForm):
    class Meta:
        model = User


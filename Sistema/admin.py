from django.contrib import admin


from .models import Mascota
from .models import Adoptante

admin.site.register(Mascota)
admin.site.register(Adoptante)

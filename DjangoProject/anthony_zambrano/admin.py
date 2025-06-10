from django.contrib import admin

from .models import Employed
from .models import Job
from .models import Departament

admin.site.register(Employed)
admin.site.register(Job)
admin.site.register(Departament)
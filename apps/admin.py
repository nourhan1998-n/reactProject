from django.contrib import admin
from .models import certificates,clients,footer,ownedCompanies,aboutUs,seaJob,landJob
# Register your models here.

admin.site.register(certificates)
admin.site.register(clients)
admin.site.register(footer)
admin.site.register(ownedCompanies)
admin.site.register(aboutUs)
admin.site.register(seaJob)
admin.site.register(landJob)
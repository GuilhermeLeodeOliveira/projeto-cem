from django.contrib import admin
from .models import Usuario, ProgramaPosGraduacao, FormInfra, FormTermo, Docente, PosDout, AlunoPosIC

# Register your models here.

admin.site.register(Usuario)
admin.site.register(ProgramaPosGraduacao)
admin.site.register(FormInfra)
admin.site.register(FormTermo)
admin.site.register(Docente)
admin.site.register(PosDout)
admin.site.register(AlunoPosIC)
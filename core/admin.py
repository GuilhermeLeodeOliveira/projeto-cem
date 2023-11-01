from django.contrib import admin
from .models import Usuario, ProgramaPosGraduacao, FormTermo, Docente, PosDout
from .models import AlunoPosIC, preCadDocente, preCadPosDout, preCadUserExterno, UserExterno
# Register your models here.

admin.site.register(Usuario)
admin.site.register(ProgramaPosGraduacao)
admin.site.register(FormTermo)
admin.site.register(Docente)
admin.site.register(PosDout)
admin.site.register(AlunoPosIC)
admin.site.register(preCadDocente)
admin.site.register(preCadPosDout)
admin.site.register(preCadUserExterno)
admin.site.register(UserExterno)
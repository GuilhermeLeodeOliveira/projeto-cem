from django.contrib import admin
from .models import Usuario, ProgramaPosGraduacao, FormTermo, Docente, Login, preLogin
from .models import AlunoPosIC, preCadDocente, preCadUserExterno, UserExterno, preCadAlunoPosIC
# Register your models here.

admin.site.register(Usuario)
admin.site.register(ProgramaPosGraduacao)
admin.site.register(FormTermo)
admin.site.register(Docente)
admin.site.register(AlunoPosIC)
admin.site.register(preCadDocente)
admin.site.register(preCadUserExterno)
admin.site.register(UserExterno)
admin.site.register(Login)
admin.site.register(preLogin)
admin.site.register(preCadAlunoPosIC)
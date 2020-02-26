from django.contrib import admin
from .models import libro,Lista_autores,categoria,presta,estudiante

admin.site.register(libro)#registramos la tabla libros ""
admin.site.register(Lista_autores) 
admin.site.register(categoria) 
admin.site.register(presta) 
admin.site.register(estudiante) 



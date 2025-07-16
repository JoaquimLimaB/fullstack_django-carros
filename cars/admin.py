from django.contrib import admin
from cars.models import Car, Brand
# Register your models here.


class CarAdmin(admin.ModelAdmin):  # Class do tipo ModelAdmin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # list_display é uma configuração herdada do ModelAdmin o mesmo para o  search_fields, o que tem dentro do parentese significa que eu estou subscrevendo o que tem por padrão na class herdadaa
    search_fields = ('model', 'brand__name', 'factory_year', 'model_year',)
    # Não tem nada como padrão, mas mesmo assim tenho que subscrever algo(caso queira). Com esse metodo irei conseguir fazer uma busca pelo meu carro somente com o nome do  modelo.(Aula 37)

admin.site.register(Car, CarAdmin)
# Registrando minha class CarAdmin no site, pede dois parametros: 1-Model no qual  estou falando(minha tabela do Banco de Dados) 2- As configuraçoes de Admin. Lembrar de importar a 1


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Não esquece da virgula miseravel

admin.site.register(Brand, BrandAdmin)

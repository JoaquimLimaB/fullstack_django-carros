from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):  # TABELA PARA GERENCIAR OS CARROS
    id = models.AutoField(primary_key=True)
    # Aqui é pra cadastra o modelo de um carro com no maximo 200 linhas
    model = models.CharField(max_length=200)
    # Aqui é um tipo de chave extrangeira, estou importando dados de uma outra coisa(Nestee caso Tabela) Aula 39
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand')
    # aqui estou adcionado uma data do tipo inteiro (Referente ao ano de frabricação do carro )
    factory_year = models.IntegerField(blank=True, null=True)
    # Data do modelo do carro(tipo inteiro)
    model_year = models.IntegerField(blank=True, null=True)
    # placa do carro
    plate = models.CharField(max_length=10, blank=True, null=True)
    # Aqui é um numero real(valor do carro)
    value = models.FloatField(blank=True, null=True)
    # OBS Sobre blank=True, null=True: significa que os campos que tiverem esses atributos não são obrigatorios.
    # Armazenado imagens (Aula 40)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):  # Função padrão de Model
        return self.model  # Removendo o nome Car Objetc do nosso site, Ese model é referente a  variavel model que guarda o nome do carro


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    # auto_now= qualquer registro que entrar na minha tabela vai ser prenchido esse campo, que indica dia, hora e segudo da criação do registro
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Auterando para prdenar minha lista em ordem decrescente do mais atual ate o mais antigo
        ordering = ['-created_at']

    def __str__(self):
        # Vai mostrar a mesnagem com os campos indicados
        return f'{self.cars_count} - {self.cars_value}'

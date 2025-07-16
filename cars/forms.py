from django import forms
from cars.models import Car

# Tabela onde o usuario cadastra novo carro


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # Significa que  eu quero todos os  campos da tabela Car

    # Uma função de validação sempre vai ser: def clean_nome_do_campoDeValidação(self):
    def clean_value(self):
        # Esse cleaned_data pega os dados limpos
        value = self.cleaned_data.get('value')
        if value < 10000:
            # Esse primeiro  paramentro é  refeerente ao campo do erro,  ja o  seegundo é a mensagem de erro
            self.add_error('value', 'Valor mínimo é de 10 mil reais')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error(
                'factory_year', 'O carro deve ser do ano 2000 para frente')
        return factory_year

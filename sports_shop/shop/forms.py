from django import forms
from .models import *


class EditProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['supplier'].empty_label = 'Поставщик не выбран'
        self.fields['producing_country'].empty_label = 'Страна не выбрана'
        self.fields['name'].label = 'Имя товара'
        self.fields['photo'].label = 'Новое фото'
        self.fields['description'].label = 'Описание'
        self.fields['supplier'].label = 'Поставщик'
        self.fields['price'].label = 'Цена'
        self.fields['category'].label = 'Категория'
        self.fields['producing_country'].label = 'Производящая\nстрана'

    class Meta:
        model = Products
        fields = ['name', 'price', 'category', 'supplier', 'description', 'photo', 'producing_country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 60, 'rows': 10}),
        }

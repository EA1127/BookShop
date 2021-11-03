from django import forms

from .models import Order


class CreateOrderForm(forms.ModelForm):
    # book = forms.ModelChoiceField(Book.objects.all())
    # phone = forms.CharField(max_length=13)
    # address = forms.CharField(widget=forms.Textarea)
    # city = forms.CharField(max_length=100)
    # email = forms.EmailField()
    class Meta:
        model = Order
        fields = '__all__'

    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        # print(phone)
        if not phone.startswith('+996'):
            raise forms.ValidationError('Number should start with +996')
        if len(phone) != 13:
            raise forms.ValidationError('Invalid phone number')
        return phone

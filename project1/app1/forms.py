from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    card_number = forms.CharField(max_length=16, min_length=16)

    def clean_card_number(self):
        card = self.cleaned_data['card_number']

        if not card.isdigit():
            raise forms.ValidationError("Card number must contain only digits.")

        return card
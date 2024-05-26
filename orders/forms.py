from django import forms


class CreateOrderForm(forms.Form):

  first_name = forms.CharField()
  email = forms.EmailField()
  phone_number = forms.CharField()
  requires_delivery = forms.ChoiceField(
    choices=[
      ('0', False),
      ('1', True),
    ],
  )
  delivery_address = forms.CharField(required=False)
  payment_on_get = forms.ChoiceField(
    choices=[
      ('0', False),
      ('1', True),
    ],
  )
  comment = forms.CharField(required=False)

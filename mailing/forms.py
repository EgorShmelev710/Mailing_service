from django import forms

from mailing.models import Client, Mailing, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('next_send_time', 'status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

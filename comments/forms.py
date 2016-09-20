from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))
    # comment = forms.CharField(max_length=148, widget=forms.Textarea, required=False)
    dice = forms.ChoiceField(CHOICES, label='Gi Terningkast')

    class Meta:
        title = 'Gi terningkast'
        model = Comment
        fields = [
            'dice',
            ]
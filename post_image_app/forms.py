from post_image_app.models import Post
from django import forms


class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','text']
        widgets = {
            'text': forms.Textarea(attrs={'rows':6, 'cols':35}),
        }
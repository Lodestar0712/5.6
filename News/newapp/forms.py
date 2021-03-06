from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author','postCategory',
                  'categoryType','title','text'
                  ]
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "description": "Описание не может быть менее 20 символов."
            })
        return cleaned_data



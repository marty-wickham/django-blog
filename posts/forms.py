from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):


    class Meta:
        model = Post
        # We only want form fields that the user can actually edit.
        fields = ('title', 'content', 'image', 'tags', 'published_date' )
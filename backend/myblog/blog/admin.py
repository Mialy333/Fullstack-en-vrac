# blog/admin.py

from django.contrib import admin
from django import forms
from .models import Post, Category, Tag

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'tags': forms.CheckboxSelectMultiple,
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
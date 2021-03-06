from django import forms
from quingenti.models import Gig, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category

class GigForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the title of the gig.")
	price = forms.IntegerField(initial=300, help_text="Please enter a price.")
	description = forms.CharField(max_length=7000, help_text="Please enter a description.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	'''"category_list = forms.ModelMultipleChoiceField(
									queryset=Category.objects.all(),
									help_text="Please enter a category."
									)'''
	#category = Category.objects.get(id=category_list)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Gig

		fields = ('title', 'price', 'description', 'views', 'category')
from django import forms
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from django_select2.forms import Select2MultipleWidget
from .models import Resource, Keyword, Category, Audience, Theme, ResourceGroup, ResourcesGrouped
from authors.models import Author
from PIL import Image
from datetime import datetime, date


class ResourceForm(forms.ModelForm):
    abstract = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'maxTextLength': 1000}}), max_length=1000)
    choices = forms.CharField(widget=forms.HiddenInput(),required=False, initial=())
    choicesSelected = forms.CharField(widget=forms.HiddenInput(),required=False, initial=())
    keywords = forms.MultipleChoiceField(choices=(), widget=Select2MultipleWidget, required=False, label="Keywords (comma separated)")
    category = forms.ModelChoiceField(queryset=Category.objects.filter(parent__isnull=True))
    categorySelected = forms.CharField(widget=forms.HiddenInput(),required=False)
    authorsCollection = forms.CharField(widget=forms.HiddenInput(),required=False, initial=())
    selectedAuthors = forms.CharField(widget=forms.HiddenInput(),required=False, initial=())
    authors = forms.MultipleChoiceField(choices=(), widget=Select2MultipleWidget, required=False,label="Authors (comma separated)")
    audience = forms.ModelMultipleChoiceField(queryset=Audience.objects.all(), widget=Select2MultipleWidget)
    theme = forms.ModelMultipleChoiceField(queryset=Theme.objects.all(), widget=Select2MultipleWidget, required=False)
    image = forms.ImageField(required=False)
    x = forms.FloatField(widget=forms.HiddenInput(),required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(),required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    resource_DOI = forms.CharField(max_length=100)
    year_of_publication = forms.IntegerField()
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'autocomplete':'nope'}))
    license = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete':'nope'}))
    curatedList = forms.ModelMultipleChoiceField(queryset=ResourceGroup.objects.all(), widget=Select2MultipleWidget, required=False,label="Curated lists")

    class Meta:
        model = Resource
        fields = ["name", "abstract", "url", "audience", "theme","keywords", "license", "publisher", "curatedList",
         "category", "authors","author_email", "image", "x", "y", "width", "height", "resource_DOI", "year_of_publication"]
                

    def save(self, args, photo):
        pk = self.data.get('resourceID', '')
        publication_date = datetime.now()
        rsc = super(ResourceForm, self).save(commit=False)
        category = get_object_or_404(Category, id=self.data['categorySelected'])
        
        if pk:
            rsc = get_object_or_404(Resource, id=pk)
            rsc.name = self.data['name']
            rsc.abstract = self.data['abstract']
            rsc.url = self.data['url']
            rsc.license = self.data['license']
            rsc.publisher = self.data['publisher']
        else:
            rsc.dateUploaded = publication_date
            rsc.creator = args.user

        rsc.inLanguage = self.data['language']        
        rsc.author_email = self.data['author_email']
        rsc.resourceDOI = self.data['resource_DOI']
        rsc.datePublished = self.data['year_of_publication']
        rsc.category = category

        if(photo != '/'):
            rsc.image = photo

        rsc.save()

        rsc.audience.set(self.data.getlist('audience'))
        rsc.theme.set(self.data.getlist('theme'))

        curatedList = self.data.getlist('curatedList')
        
        if args.user.is_staff:
            objs = ResourcesGrouped.objects.filter(resource=rsc)
            if objs:
                for obj in objs:
                    obj.delete()        
            for clist in curatedList:
                rscGroup = get_object_or_404(ResourceGroup, id=clist)
                ResourcesGrouped.objects.get_or_create(group=rscGroup,resource=rsc)

        # Keywords
        choices = self.data['choices']
        choices = choices.split(',')
        for choice in choices:
            if(choice != ''):
                keyword = Keyword.objects.get_or_create(keyword=choice)                   
        keywords = Keyword.objects.all()
        keywords = keywords.filter(keyword__in = choices)
        rsc.keywords.set(keywords)

        # Authors
        authors = self.data['authorsCollection']
        authors = authors.split(',')
        for author in authors:
            if(author != ''):
                Author.objects.get_or_create(author=author)
        authorsCollection = Author.objects.all()
        authors = authorsCollection.filter(author__in = authors)
        rsc.authors.set(authors)

        return 'success'

from django.http import HttpResponse
from django.shortcuts import render
from .db_article import article

def home_view(request):
  #return HttpResponse('bonjour le monde again...')  
   return render(request , 'home.html')
def contact_view(request):
   
   #return HttpResponse('contactez nous si possible!!!!...')  
    return render(request ,'contact.html')
    
def article_view(request):
   return render(request ,'article.html', context={'article': article})

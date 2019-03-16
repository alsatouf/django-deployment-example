from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'Hello world', 'number': 100}
    return render(request, 'TemplatesApp/index.html', context_dict)

def other(request):
    return render(request, 'TemplatesApp/other.html')

def relative(request):
    return render(request, 'TemplatesApp/relativeUrlTemplates.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import Project
from .forms import ContactForm

from json import dumps

# Create your views here.
def index(request):
    return HttpResponse("Hello World. I'm back!")


def home(request):
    # Grab all projects for display
    projects = Project.objects.all()
    # Create a project data dictionary and pass the project id to get all data
    project_data = {}
    for project in projects:
        project_data[project.id] = {
            'title': project.title,
            'image': project.image,
            'description': project.description,
            'github_url': project.github_url,
            'live_url': project.live_url,
        }
    project_data_JSON = dumps(project_data)

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']
        
            # Format to send to business email
            subject = f'{name.capitalize()} from {company.upper()}'
            subject_message = email + '\n\n' + message
        else:
            form = ContactForm()
    
    context = {
        'projects': projects,
        'project_data_JSON': project_data_JSON,
        'form': form
    }
    return render(request, 'projects/projects.html', context)
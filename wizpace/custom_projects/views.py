from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from forms import ProjectForm

from models import Project
from custom_reg.models import Skill

def projects_index(request):
    return render(request, 'custom_projects/index.html', {})

class ListProjects(ListView):
    template_name = 'custom_projects/list_projects.html'
    queryset = Project.objects.all()


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                owner=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                nr_of_workers=form.cleaned_data['nr_of_workers'],
                end_date=form.cleaned_data['end_date']
            )
            project.save()
            for s in form.cleaned_data['skills']:
                skill, created = Skill.objects.get_or_create(name=s.lower())
                if created:
                    skill.save()
                project.skills.add(skill)
                project.save()
            # print project.skills
        return redirect(reverse_lazy('projects_index'))
    else:
        form = ProjectForm()
        context_dict = {'form': form}
        return render(request, 'custom_projects/add_project.html', context_dict)




class AddProject(FormView):
    template_name = 'custom_projects/add_project.html'
    form_class = ProjectForm

    success_url = reverse_lazy('projects_index')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()
        project.title = form.cleaned_data['title']
        project.description = form.cleaned_data['description']
        project.nr_of_workers = form.cleaned_data['nr_of_workers']
        for s in form.cleaned_data['skills']:
            skill = Skill.objects.get_or_create(name=s.lower())
            project.skills.add(skill)
        project.save()
        print project.skills


        return super(AddProject, self).form_valid(form)

def search_skill(request):
    query = request.GET.get('q', '').lower
    skills_list = Skill.objects.filter(reduce(lambda x, y: x | y, [Q(name__startswith=query)]))
    json_dicts = []
    for skill in skills_list:
        obj_dict = {}
        obj_dict['id'] = skill.name
        obj_dict['name'] = skill.name
        json_dicts.append(obj_dict)
    return JsonResponse(data=json_dicts, safe=False)
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Link


# Create your views here. instead of def we use class here
class LinkListView(ListView):
    model = Link

    # template called model_list.html --> link_list.html (knows to render)
    '''
          ListView is django class package and creates this LOGIC,just assign model
        # query for all the links link.objects.all
        # context ={'link' : links}
        #return render(request, 'link_link.html, context)
    '''


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')  # redirect the user to the home page
    # template model_form -> link_form.html


"""
if this was a def:
    create forms.py file & form
    check if this was a post/get request
    return an empty form or save the form data

"""


class LinkUpdateView(UpdateView):
    model = Link
    field = ['text', 'url']
    success_url = reverse_lazy('link_list')
    # template model_form -> link_form.html


"""
    if this was a def:
        create a form
        check if this was a post/get request
        either render the form or update and save in db

"""


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')

    # default form to submit to delete the item, link_form_delete.html


"""
    if a def:
        take in id/pk of object
        query to db for that object
        check if it exists -> delete the object
        return some template or forward the user to some url

"""


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
    return render(request, 'link_plant/profile.html', context)

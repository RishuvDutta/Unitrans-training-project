from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.forms.models import inlineformset_factory
from django import forms
from shifts_app.forms import ShiftForm, RunForm, PostForm
from shifts_app.shift import Shift 
from shifts_app.run import Run
from django.contrib.auth.decorators import login_required
from shifts_app.group import Post, History

def home(request):
    return render(request, "home.html")

def display_data(request, data, **kwargs):
    return render_to_response('example/posted-data.html', dict(data=data, **kwargs),
        context_instance=RequestContext(request))

def view_list(request):
    queryset_list = Shift.objects.all().order_by('start_datetime')
    history = History.objects.all()
    context = {
    "object_list": queryset_list,
    "history": history,
    }
    return render(request, "index.html", context)

RunFormSet = inlineformset_factory(Shift, Run, form=RunForm, can_delete=True, extra=1)

def view_delete(request, id=id):
    instance = get_object_or_404(Shift, id=id)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "confirm_delete.html")

def view_detail(request, id=None):
    instance = get_object_or_404(Shift, id=id)
    context = {
        "title": instance.id,
        "instance": instance,
    }
    return render(request, "detail.html", context)

def view_update(request, form_class, template, id=id):
    instance = get_object_or_404(Shift, id=id)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            formset = RunFormSet(request.POST, instance=instance)
            print formset.errors
            if formset.is_valid():
                instance.save()
                formset.save()
                return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ShiftForm(instance=instance)
        formset = RunFormSet(instance=instance)
    return render_to_response(template, {'form': form, 'formset': formset},
        context_instance=RequestContext(request))


def inline_formset(request, form_class, template):
    shift = None
    formset = RunFormSet(instance=Run())
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            formset = RunFormSet(request.POST, instance=info)
            if formset.is_valid():
                info.save()
                formset.save()
                return HttpResponseRedirect(info.get_absolute_url())
    else:
        form = ShiftForm(instance=shift)
        formset = RunFormSet(instance=Run())
    return render_to_response(template, {'form': form, 'formset': formset},
        context_instance=RequestContext(request))

def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.cleaned_data
        context = {"instance": form.cleaned_data,}
        request.session['instance'] = instance
        if Run.objects.filter(user_id=instance['user_id']).exists():
            return HttpResponseRedirect(reverse('shift:creator'))
        else:
            return render(request, "noshift.html")
    context = {"form": form}
    return render(request, "post.html", context)

def cover_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.cleaned_data
        request.session['number'] = instance
        return HttpResponseRedirect(reverse('shift:cover'))
    context = {"form": form}
    return render(request, "pick2.html", context)


def post_creator(request):
    id = request.session['instance']
    runs = Run.objects.filter(user_id = id['user_id'])
    try:
        post = Post.objects.get(current_user = id['user_id'])
        posts = post.runs.all()
    except Post.DoesNotExist:
        post = None
        posts = None
    return render(request, "select.html", {'id': id['user_id'], 'runs': runs, 'posts': posts,})

def cover(request, id, pk, opk, oid):
    t = Post.objects.get(pk=pk).runs.get(pk=opk)
    if request.method == 'POST':
        History.add_history(oid, t)
        t.user_id = id
        t.save()
        Post.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse('shift:cover'))
    return render(request, "confirm_cover.html")

def change_posts(request, operation, id, pk):
    new_post = Run.objects.get(pk=pk)
    if operation == 'add':
        Post.make_post(id, new_post)
    elif operation == 'remove':
        Post.objects.filter(current_user=id)
        Post.delete_post(id, new_post)
    return redirect('shift:creator')

def post_view(request):
    queryset_list = Post.objects.all()
    id = request.session['number']
    context = {
    "object_list": queryset_list, 
    "id": id['user_id']
    }
    return render(request, "posts.html", context)


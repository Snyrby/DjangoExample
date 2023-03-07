from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import course
from .forms import CourseModelForm
# Create your views here.

'''converting a function based view to class based view '''
class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        # get method
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # post method
        form = CourseModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

''' inheritance
class MyListView(CourseListView):
    queryset = course.objects.filter(id=1)'''

'''converting a function based view to class based view '''
class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

class CourseUpdateView(View):
    template_name = 'courses/course_create.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(course, id=id)
        return obj
    def get(self, request, *args, **kwargs):
        # get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # post method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(course, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        # get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # post method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


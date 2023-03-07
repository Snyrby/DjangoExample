from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import course
from .forms import CourseModelForm
# Create your views here.

class CourseObjectMixin(object):
    model = course
    lookup = 'id'

    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=lookup)
        return obj


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
class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_create.html'

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

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

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


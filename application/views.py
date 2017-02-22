from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView

from forms import ApplicationForm
from models import Application

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        return context

class CreateView(FormView):
    template_name = 'create.html'
    form_class = ApplicationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """Returns the create application form"""

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """When create form is submitted, this methods handles post data"""

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        """Saves the form data to the database"""

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        """Return errors to the form if form is invalid"""

        context = self.get_context_data(**kwargs)
        context['form'] = form
        form.save()
        return super(CreateView, self).form_valid(form)

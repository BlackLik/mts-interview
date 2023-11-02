from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
import logging
from . import models as db

logger = logging.getLogger("app")


class ListModelsView(View):
    template_name = './app.html'

    def get_model_class(self, model_name):

        if model_name is None:
            model_name = 'ModelA'

        models = {
            'ModelA': db.ModelA,
            'ModelB': db.ModelB,
            'ModelC': db.ModelC
        }
        return models[model_name]

    def get(self, request):

        model = request.GET.get('model')

        if model is None:
            model = 'ModelA'

        ModelClass = self.get_model_class(model)
        try:
            columns = ModelClass._meta.ordering
            if not columns:
                raise AttributeError("No ordering defined")
            rows = ModelClass.objects.order_by(*columns)
        except Exception as e:
            logger.error(e)
            columns = [f.name for f in ModelClass._meta.fields][1:]
            rows = ModelClass.objects.all()

        context = {
            'model_name': model,
            'columns': columns,
            'rows': rows
        }

        return render(request, self.template_name, context)

    def post(self, request):
        model = request.POST.get('model')

        if model is None:
            return redirect('app')
        
        fields_one = request.POST.get('one')
        fields_two = request.POST.get('two')
        fields_three = request.POST.get('three')
        
        if fields_one is None or fields_two is None or fields_three is None:
            return redirect('app')

        try:
            ModelClass = self.get_model_class(model)
            ModelClass.objects.create(
                one=fields_one,
                two=fields_two,
                three=fields_three
            )
            ModelClass.save()
        except Exception as e:
            logger.error(e)
        redirect_url = reverse('app') + '?model=' + model
        return redirect(redirect_url)

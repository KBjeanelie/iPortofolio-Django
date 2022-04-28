from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views import View

from myCV.models import Profile, Skills, Education, Category


class IndexView(View):
    template_name = "index.html"
    context_object = {"profile": Profile.objects.get(id=1)}
    context_object.update({"skills": Skills.objects.all().order_by('-pourcentage')})
    context_object.update({"educations": Education.objects.all()})
    context_object.update({"categories": Category.objects.all()})

    def get(self, request):
        return render(request, self.template_name, self.context_object)

from django.shortcuts import render

# Create your views here.
# views.py

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
import pytesseract
from PIL import Image
from apps.forms import ImageUploadForm


class ImageUploadView(FormView):
    template_name = 'apps/image_upload.html'
    form_class = ImageUploadForm
    success_url = reverse_lazy('passport_info')

    def form_valid(self, form):
        image = form.cleaned_data['image']
        text = pytesseract.image_to_string(Image.open(image), lang='eng')
        self.request.session['passport_info'] = parse_passport_info(text)
        return super().form_valid(form)


class PassportInfoView(TemplateView):
    template_name = 'apps/passport_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passport_info'] = self.request.session.get('passport_info', {})
        return context


def parse_passport_info(text):
    lines = text.split('\n')
    name = lines[2], lines[4], lines[6]
    series_number = lines[0]
    return {'name': name, 'series_number': series_number}

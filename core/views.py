import io
from django import forms
from django.views.generic import FormView
from django.shortcuts import render
from pdfminer.high_level import extract_text
from .models import UploadedFile


class IndexForm(forms.Form):
    file = forms.FileField(label="PDF")


class IndexView(FormView):
    form_class = IndexForm
    template_name = "core/index.html"

    def form_valid(self, form):
        file = form.files["file"]
        text = extract_text(io.BytesIO(file.read()))
        UploadedFile.objects.create(text=text)
        return render(
            self.request,
            template_name=self.template_name,
            context={"text": text, "form": form},
        )

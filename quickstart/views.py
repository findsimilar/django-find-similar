"""
Quickstart views
"""
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from find_similar import find_similar
from django_find_similar.forms import FindSimilarForm
from django_find_similar.models import CheckResult, TokenTextAdapter, TextToken


class FindSimilarFormView(FormView):
    """
    Quickstart form view
    """
    template_name = 'quickstart/find_similar.html'
    form_class = FindSimilarForm
    success_url = reverse_lazy('quickstart:results')

    def form_valid(self, form):
        data = form.cleaned_data
        text_token = TextToken.objects.create(**data)
        adapter = TokenTextAdapter(text_token)
        adapters = [TokenTextAdapter(item) for item in TextToken.objects.all()]
        result = find_similar(adapter, adapters)
        CheckResult.save_result(text_token, result)
        return super().form_valid(form)


class ResultListView(ListView):
    """
    CheckResults list
    """
    model = CheckResult
    template_name = 'quickstart/checkresult_list.html'

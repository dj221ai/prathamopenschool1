from django.db.models.fields import files
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ExcelUploadModel
from .forms import ExcelUploadModelForm
# from django.views import View
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginRequiredMixin, View):
    template_class = 'core/excel_list.html'

    def get(self ,request, *args, **kwargs):
        check_db = ExcelUploadModel.objects.all()
        request = self.request

        # if not check_db.exists():
        return render(request, self.template_name)


@login_required
def excel_list_view(request):
    files_ = ExcelUploadModel.objects.all()
    context = {}
    context['files'] = files_
    return render(request, 'core/excel_list.html', context=context)

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = ExcelUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:files')
    else:
        form = ExcelUploadModelForm()

    return render(request, 'core/upload.html', {'form': form})

@login_required
def delete_view(request, pk):
    if request.method == 'POST':
        files_ = ExcelUploadModel.objects.get(pk=pk).delete()
    return redirect('core:files')

    




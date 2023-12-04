from .forms import QRForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import QR
from path import Path
from .services import gen_qr_code


# Главная страница
def index(request):
    template = "index.html"
    form = QRForm(request.POST or None, files=request.FILES or None)
    context = {"form": form}
    if request.method == "POST":
        return qr_create(request)
    return render(request, template, context)


def qr_code_detail(request, pk):
    qr = get_object_or_404(QR, pk=pk)
    form = QRForm(request.POST or None, files=request.FILES or None)
    qr_url = qr.qurl

    context = {"qr": qr, "form": form, "qr_url": qr_url}
    if request.method == "POST":
        return qr_create(request)
    return render(request, "qr_code_detail.html", context)


def qr_create(request):
    form = QRForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        qr = form.save(commit=False)
        text = qr.link
        img = str(qr.image)
        # Путь до фона qr кода
        qr_img = img.split(".")[0] + "QR.png"
        qr.qurl = qr_img
        qr.save()
        path_to_download = Path().joinpath("media", img)
        # Куда сохранять результат и под каким именем (обязательно в png)
        path_to_save = Path().joinpath("static", qr_img)
        gen_qr_code(text, path_to_download, path_to_save)
    return redirect("qr_code_detail", pk=qr.id)

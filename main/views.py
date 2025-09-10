from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406343224',
        'nama': 'Galih Nur Rizqy',
        'kelas': 'PBP E',
        'nama_aplikasi': 'adidos'
    }

    return render(request, "main.html", context)
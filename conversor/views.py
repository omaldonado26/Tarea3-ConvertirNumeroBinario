from django.shortcuts import render
from .forms import BinaryForm

def convert_view(request):
    result = None

    if request.method == 'POST':
        if 'clear' in request.POST:
            form = BinaryForm()     
            result = None            
        else:
            form = BinaryForm(request.POST)
            if form.is_valid():
                b = form.cleaned_data['binary']
                dec = int(b, 2)
                octal = oct(dec)[2:]
                hexa = hex(dec)[2:].upper()
                result = {
                    'binary': b,
                    'decimal': dec,
                    'octal': octal,
                    'hexadecimal': hexa,
                }
    else:
        form = BinaryForm()

    return render(request, 'convert.html', {
        'form': form,
        'result': result,
    })

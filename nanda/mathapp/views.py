from django.shortcuts import render 
def powercalc(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('intensity','0')
        R = request.POST.get('resistance','0')
        print('request=',request) 
        print('intensity=',I) 
        print('resistance=',R) 
        power = (int(I) * int(I) ) * int(R) 
        context['power'] = power
        context['intensity'] = I
        context['resistance'] = R 
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

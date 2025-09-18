from django.shortcuts import render

def payment_list(request):
    return render(request, "payment_list.html")

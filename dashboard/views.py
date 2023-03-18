from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        context ={
            "document_title":"Dashboard",
        }
        return render(request, 'dashboard/dashboard.html',context)
    return redirect('/authentication/login/')
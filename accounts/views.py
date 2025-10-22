from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'accounts/login-page.html')

def profile_delete_view(request):
    return render(request, 'accounts/profile-delete-page.html')

def profile_edit_view(request):
    return render(request, 'accounts/profile-edit-page.html')

def profile_details_view(request):
    return render(request, 'accounts/profile-details-page.html')

def register_view(request):
    return render(request, 'accounts/profile-register-page.html')
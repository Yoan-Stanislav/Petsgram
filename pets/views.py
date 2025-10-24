from django.shortcuts import render

def pet_add_view(request):
    return render(request, 'pets/pet-add-page.html')

def pet_delete_view(request):
    return render(request, 'pets/pet-delete-page.html')

def pet_details_view(request):
    return render(request, 'pets/pet-detail-page.html')

def pet_edit_view(request):
    return render(request, 'pet/pet-edit-page.html')

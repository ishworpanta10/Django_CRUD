from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Detail
from .forms import UserDetails


def index(request):
    details = Detail.objects.all()
    context = {'details': details}
    return render(request, 'basic_crud/index.html', context)

# form get and post also update
# def add(request):
#     if request.method == "GET":
#         form = UserDetails()
#         context = {'form': form}
#         return render(request, 'basic_crud/form.html', context)
#     else:
#         form = UserDetails(request.POST)
#         if form.is_valid():
#             form_data = Detail(
#                 fullname=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'])

#             form_data.save()
#         return redirect('home')


def add(request, id=0):
    if request.method == "GET":
        # for update
        if id == 0:
            form = UserDetails()
        else:
            edit_user = Detail.objects.get(pk=id)
            form = UserDetails(instance=edit_user)
        # upto here
        context = {'form': form}
        return render(request, 'basic_crud/form.html', context)
    else:
        if id == 0:
            form = UserDetails(request.POST, request.FILES or None)
        else:
            edit_user = Detail.objects.get(pk=id)
            form = UserDetails(request.POST,request.FILES or None, instance=edit_user)
        if form.is_valid():
            # form_data = Detail(
            #     fullname=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'])

            form.save()
        return redirect('home')


def delete(request, id):
    data = Detail.objects.get(pk=id)
    data.delete()

    return redirect('home')

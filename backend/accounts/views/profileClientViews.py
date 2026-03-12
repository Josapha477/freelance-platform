from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from accounts.models.profileClient import ProfileClient
from accounts.forms.formProfile import ProfileClientForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def createprofileclientview(request):
    if request.user.user_types != "client":
      return redirect("/")
    profile = ProfileClient.objects.get(user=request.user)
    if profile:
      return redirect("/dashboard_client")

    if request.method == "POST":
      form = ProfileClientForm(request.POST, request.FILES)
      if form.is_valid():
         profile = form.save(commit=False)
         profile.user = request.user
         profile.save()
         # messages.success(request, "Votre profile est creer avec success")
         return redirect("/dashboard")
    else:
       form = ProfileClientForm()
    return render(request, "profile/createprofile.html", {'form': form})












# class CreateProfileClientView(CreateView):
#     model = ProfileClient
#     form_class = ProfileClientForm
#     template_name = "profile/createprofile.html"
#     #success_url = reverse_lazy("profile")

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)



# class UpdateProfileClientView(UpdateView):
#     pass






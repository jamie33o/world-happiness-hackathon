from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import ProfileUpdateForm



@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    template_name = 'myprofile/profile.html'

    def get(self, request, **kwargs):

        user_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            
        }

        return render(request, self.template_name, context)

    @method_decorator(require_POST)
    def post(self, request):
      
        user_form = ProfileUpdateForm(request.POST,
                                      request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile Updated!!')
        else:
            messages.error(request, user_form.errors)

        return redirect('profile')

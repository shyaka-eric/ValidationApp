# from django.shortcuts import redirect, render

# from myapp.models import Participant




from django.shortcuts import redirect, render
from django.forms import formset_factory

#from myapp.models import Participant, Vehicle
from .forms import ParticipantForm, VehicleForm

def home_view(request):
    return render(request, 'home.html')

def participant_form_view(request):
    VehicleFormSet = formset_factory(VehicleForm, extra=1, can_delete=True)

    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        vehicle_formset = VehicleFormSet(request.POST, prefix='vehicles')

        if participant_form.is_valid() and vehicle_formset.is_valid():
            participant = participant_form.save()
            for form in vehicle_formset:
                if not form.cleaned_data.get('DELETE', False):
                    vehicle = form.save(commit=False)
                    vehicle.participant = participant
                    vehicle.save()

            # Redirect to a success page
            return redirect('form_success')
    else:
        participant_form = ParticipantForm()
        vehicle_formset = VehicleFormSet(prefix='vehicles')

    return render(request, 'participant_form.html', {'participant_form': participant_form, 'vehicle_formset': vehicle_formset})

def form_success_view(request):
    return render(request, 'form_success.html')

def vehicle_registration(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform any other necessary actions
            form.save()
            # Redirect to a success page or another view
            return redirect('success_page')
    else:
        form = VehicleForm()

    return render(request, 'vehicle_form.html', {'form': form})








import logging

logger = logging.getLogger('django.access')

def some_view(request):
    # Your view logic here

    # Log access information
    ip_address = request.META.get('REMOTE_ADDR')
    logger.info(f"Access from IP: {ip_address}")

    # Rest of your view logic







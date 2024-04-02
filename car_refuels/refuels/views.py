from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import RefuelSession
from .forms import RefuelForm
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def refuels(request):
    if request.method == 'DELETE':
        refuel_id = request.POST.get('refuel_id')
        refuel = get_object_or_404(RefuelSession, pk=refuel_id)
        refuel.delete()
        return JsonResponse({'message': 'Refuel session deleted successfully'}, status=200)
    elif request.method == 'POST':
        form = RefuelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RefuelForm()

    items = RefuelSession.objects.all()
    return render(request, 'refuel_form.html', {'form': form, 'refuels': items})

@require_http_methods(['DELETE'])  # Ensure only DELETE requests are allowed
def delete_refuel(request, refuel_id):
    refuel = get_object_or_404(RefuelSession, pk=refuel_id)
    refuel.delete()
    return JsonResponse({'message': 'Refuel session deleted successfully'}, status=200)





























# def add_refuel(request):
#     items = RefuelSession.objects.all()

#     if request.method == 'POST':

#         # Extract data from the form
#         date = request.POST.get('date')
#         fuel_type = request.POST.get('fuel_type')
#         pence_per_litre = request.POST.get('pence_per_litre')
#         litres_filled = request.POST.get('litres_filled')
#         total_cost = request.POST.get('total_cost')

#         # Save data to the Refuel model
#         refuel = RefuelSession.objects.create(date=date, fuel_type=fuel_type, pence_per_litre=pence_per_litre,
#                                        litres_filled=litres_filled, total_cost=total_cost)
        
#         # Optionally, you can return a JSON response confirming the data addition
#         return render(request, 'refuels.html', {'refuels': items})

#     # If the request method is not POST, render the form template
#     return render(request, 'refuels.html', {'refuels': items})
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import RefuelSession
from .forms import RefuelForm
from django.views.decorators.http import require_POST, require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def refuels(request):
    items = RefuelSession.objects.order_by('-date')  # Sort by date from newest to oldest

    # Pagination
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    try:
        refuels = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        refuels = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        refuels = paginator.page(paginator.num_pages)

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

    return render(request, 'refuel_form.html', {'form': form, 'refuels': refuels})

@require_http_methods(['DELETE'])
def delete_refuel(request, refuel_id):
    refuel = get_object_or_404(RefuelSession, pk=refuel_id)
    refuel.delete()
    return JsonResponse({'message': 'Refuel session deleted successfully'}, status=200)
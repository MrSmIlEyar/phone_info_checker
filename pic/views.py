from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import PhoneRange
from django.views.generic import TemplateView


def validate_phone(phone):
    cleaned = ''.join(filter(str.isdigit, phone))
    if len(cleaned) not in (10, 11) or not cleaned.startswith(('7', '8')):
        return None
    return cleaned[-10:]


@require_GET
def check_phone_api(request):
    phone = validate_phone(request.GET.get('phone', ''))
    if not phone:
        print(phone)
        return JsonResponse({'error': 'Invalid phone format'}, status=400)

    def_code = phone[:3]
    number_part = int(phone[3:])

    try:
        pr = PhoneRange.objects.get(
            def_code=def_code,
            start_range__lte=number_part,
            end_range__gte=number_part
        )
        return JsonResponse({
            'phone': f'7{phone}',
            'operator': pr.operator,
            'region': pr.region,
            'territory': pr.territory,
            'inn': pr.inn
        })
    except PhoneRange.DoesNotExist:
        return JsonResponse({'error': 'Number not found'}, status=404)

class HomeView(TemplateView):
    template_name = 'index.html'
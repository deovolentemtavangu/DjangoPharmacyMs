from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {'GET':'/API/sales'},
        {'GET':'/API/sales/id'},
        {'POST':'/API/sales/id'}
    ]
    return JsonResponse(routes, safe=False)
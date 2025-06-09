from django.http import HttpResponse

from django.shortcuts import render
from django.http import JsonResponse
from services.graph_service import _graph_service


def index(request):
    return HttpResponse("hello world")


def graph_view(request):
    context = {}
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            graph_data = _graph_service.build(text)
            graph_data['edges'] = [list(edge) for edge in graph_data['edges']]
            context['graph'] = graph_data
            context['text'] = text
    else:
        context['text'] = """第一条 为了保护专利权人的合法权益，鼓励发明创造，推动发明创造的应用，提高创新能力，促进科学技术进步和经济社会发展，制定本法。"""

    return render(request, 'graph/graph_form.html', context)


def graph_api(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        graph_data = _graph_service.build(text)
        return JsonResponse(graph_data, safe=False)
    return JsonResponse({'error': 'POST method required'}, status=405)

from django.http import HttpResponse
def list_produto_view(request, id=None):
    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    else: 
        return HttpResponse(f'<h1>produto de id {id} </h1>')


        
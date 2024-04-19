# import time
# from django.http import JsonResponse, HttpResponseBadRequest

# def api(request):
#     time.sleep(1)  # Simula uma pequena demora no processamento, não recomendado para produção
#     payload = {"message": "Hello World"}

#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET['task_id']
#     # else:
#     #     # Retorna uma resposta de erro se a chave 'task_id' não estiver presente
#     #     return HttpResponseBadRequest("task_id is required")

#     return JsonResponse(payload)

# import asyncio
# import httpx

# from django.http import HttpResponse

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)  # Simula um delay, útil para testes.
#         print(num)
#     async with httpx.AsyncClient() as client:
#         # Corrigindo a URL para o valor correto.
#         r = await client.get("https://httpbin.org")
#         print(r)  # Imprime a resposta para debug.

# async def async_view(request):
#     # Espera a conclusão de todas as operações assíncronas.
#     loop = async_view.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse("Non-blocking HTTP request completed")

# import asyncio
import asyncio
import httpx
from time import sleep  # Corrigindo a importação
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print(response.text)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)  # Usando a função sleep importada corretamente
        print(num)
    r = httpx.get("https://httpbin.org/get")  # Corrigindo a URL
    print(r)

async def async_view(request):
    await http_call_async()
    return HttpResponse("Non-blocking HTTP request completed")

def sync_view(request):
    http_call_sync()  # Chamada corrigida para a função síncrona
    return HttpResponse("Blocking HTTP request")

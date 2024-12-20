from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app import file_socket
import json


# Create your views here.

def index(request: HttpRequest):
    return render(request, "app/index.html")


def getAudioData(request: HttpRequest):
    if request.method == "POST":
        file_data = request.FILES.get("file")
        if file_data is not None:
            after_name = file_socket.file_save(file_data.temporary_file_path())
            data = file_socket.socket(after_name)
            if data is not None:
                return HttpResponse(json.dumps(data))
            return HttpResponse(status=503)
        return HttpResponse(status=400)

from rest_framework.response import Response
from rest_framework.decorators import api_view
import subprocess
from rest_framework import status
from .serializers import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['GET', 'POST'])
def run_script(request):
    if request.method == "POST":
        with open ('run.py', 'w') as rsh:
            if len(list(request.data.values())[0]) > 0:
                rsh.write(list(request.data.values())[0])
            else:
                rsh.write(list(request.data.keys())[0])

        result = subprocess.run(['python3','run.py'], stdout=subprocess.PIPE)
        return Response(result.stdout.decode('utf-8'))

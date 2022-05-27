from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import json

def register(request):
    if request.method == 'POST':
        email = json.loads(request.body)['email']
        password = json.loads(request.body)['password']
        if len(password) < 8:
            # messages.warning(request, "비밀번호가 짧습니다.")
            # return render(request, 'index.html')
            return HttpResponse(f'{password}는 너무 짧습니다')
        else:
            if '@' in email:
                return HttpResponse(f'{email}, {password}로 가입이 완료 되었습니다')
            else:
                # messages.warning(request, "이메일 형식이 틀렸습니다.")
                # return render(request, 'index.html')
                return HttpResponse(f'{email}은 양심적으로 너무 합니다.')
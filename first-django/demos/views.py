import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest


# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작입니다. 이게 맞나요?')
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'request.__dict__ = {request.__dict__}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result})


def lotto(request):
    game = 0
    pull_number = None
    lotto_number = None

    ## Case 1
    lotto_number = list()
    for _ in range(6):
        number = random.randint(1, 45)
        lotto_number.append(number)
    print(f'Case 1: {lotto_number}')

    ## Case 2
    pull_number = list()
    for index in range(45):
        pull_number.append(index)

    lotto_number = random.sample(pull_number, 6)
    print(f'Case 2: {lotto_number}')

    ## Case 3
    pull_number = [index for index in range(1, 46)]
    lotto_number = random.sample(pull_number, 6)
    print(f'Case 3: {lotto_number}')

    ## Challenge
    lotto_number = list()
    game = request.GET.get('game', 1)
    pull_number = [index for index in range(1, 46)]

    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number, 6))

    return render(request, 'lotto.html', {'lotto_number': lotto_number, 'game': game})


def lotto_index(request):
    return render(request, 'lotto_index.html')


def lotto_result(request):
    lotto_number = list()
    game = request.GET.get('game', 1)
    pull_number = [index for index in range(1, 46)]

    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number, 6))

    return render(request, 'lotto_result.html', {'lotto_number': lotto_number, 'game': game})

from django.shortcuts import render

def calculator(num1, num2, operation):
    operations = {
        'Addition': num1 + num2,
        'Subtraction' : num1 - num2,
        'Multiplication' : num1 * num2,
        'Division' : num1 / num2
    }
    return operations.get(operation)

def index(request):
    num1 = request.GET.get('num1','')
    num2 = request.GET.get('num2','')
    operation = request.GET.get('operation', '')
    result = {}

    if num1 and num2 and operation:
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = calculator(num1, num2, operation)
        except ValueError:
            result = "Invalid Input, Please Enter Valid Numbers"
    elif num1 or num2 or operation:
        result =  "Please Enter Both Numbers to perform Operaions"

    return render(request, 'index.html', {'num1': num1, 'num2': num2,'operation':operation, 'result':result})

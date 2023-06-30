from django.shortcuts import render,redirect

def index(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        button = request.POST['value']
        if button == 'Addition':
            add1 = add(num1,num2)
            return render(request,'index.html',{'result':add1})
        if button == 'Subtraction':
            sub1 = sub(num1,num2)
            return render(request,'index.html',{'result':sub1})
        if button == 'Multiplication':
            multi1 = multi(num1,num2)
            return render(request,'index.html',{'result':multi1})
        if button == 'Division':
            div1 = div(num1,num2)
            return render(request,'index.html',{'result':div1})
    return render(request,'index.html')

def add(num1,num2):
    result = int(num1)+int(num2)
    return result
def sub(num1,num2):
    result = int(num1)-int(num2)
    return int(result)
def multi(num1,num2):
    result = int(num1)*int(num2)
    return result
def div(num1,num2):
    result = int(num1)/int(num2)
    return result
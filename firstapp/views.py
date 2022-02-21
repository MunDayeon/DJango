from django.shortcuts import render

# index.html을 보여주는 논리를 담당하는 함수를 만들기!
def home(request):  #요청이 들어오면!
    return render(request, 'index.html')   # 요청이 들어오면 'index.html' html을 띄워서 보내줘라(렌더링해줘라!)!

def test(request):
    return render(request, 'test.html')
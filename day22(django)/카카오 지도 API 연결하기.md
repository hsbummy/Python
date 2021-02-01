* 카카오 지도 API 연결하기





![django11](C:\Users\morph\Pictures\django11.png)

```python
    def map(request):
        context = {
        'section': 'shop2/map.html'
        };
        return render(request, 'shop2/shop2.html',context) 

```



* 가장 중요한 건 ~~~지도 API 를 받아오는 일인데 http://apis.map.kakao.com/ 여기서 받아오면 된다. 또한 자세한 설명도 여기에 나와있으니 사이트에서 이용하는게 좋다.!





* 로그



![django12](C:\Users\morph\Pictures\django12.png)





```python
    def loginimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        try:
            user = UserDb().selectone(id)
            if pwd == user.pwd:
                logger.debug(id)
                request.session['suser'] = id;
                context = {
                    'section' : 'shop2/loginok.html',
                    'loginuser' : user
                };
            else:
                
                
         # 이런식으로 로그 파일을 받아올 수 있다.
```


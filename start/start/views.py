# it is created my myself

from django.http import HttpResponse
from django.shortcuts import render,HttpResponse


def index(request):
    
	return render(request, 'temp.html',{"name":"diwas"})

def home(request):
	if request.method=="POST":
		check=["charles","usa"]
		c=0
		for name in check:
			game = request.POST.get(name,'off')
			if game=="on":
				c=c+1   
			else:
				c=c
		return render(request,"result.html",{"result":c})
		
		
	else:
		return HttpResponse("error")


# u='''<ul>
#          <a href="http://127.0.0.1:8000"><li>home</a></li>
# 		 <a href="http://127.0.0.1:8000/rem"><li>removepunc</a></li>
# 		 <a href="http://127.0.0.1:8000/cap"><li>capfirst</a></li>
# 		 <a href="http://127.0.0.1:8000/new"><li>newlineremove</a></li>
# 		 <a href="http://127.0.0.1:8000/char"><li>charcount</a></li>
# 	</ul>'''

# data='''<script>
#          function good(){
#          var x=document.getElementById("uname").value;
#          alert("ohh hii "+x)
#          }
#          </script>
#          <br><input type="text" name="uname" id="uname"><br>
#         <input type="button" value="submit" onclick="good()">'''



# def removepunc(request):
# 	return HttpResponse('''removepuc<br />'''+u)

# def capfirst(request):
# 	return HttpResponse('''capfirst<br />'''+u)


# def newlineremove(request):
# 	return HttpResponse('''newline<br />'''+u)

# def spaceremove(request):
# 	return HttpResponse('''spaceremove<br />'''+u)


# def charcount(request):
# 	return HttpResponse('''charcount<br />'''+ u)
		

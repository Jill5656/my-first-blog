from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
# What is happening in the above 'def'? We created a function (def) called post_list #that takes request and will return the value it gets from callling another function - #render - that will render (put together) our template blog/post_list.html. 

    

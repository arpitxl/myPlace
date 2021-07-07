from django.shortcuts import render, redirect
from django.contrib import messages
from posts.models import Post

# Create your views here.
def posts(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST.get('description')
        price = request.POST['price']
        category = request.POST['category']
        state = request.POST['state']
        city = request.POST['city']
        location = request.POST['location']
        photo = request.FILES['photo']
        if int(price) < 0:
            messages.error(request, 'Price can\'t be negative!')
            return redirect('/post')
        post = Post.objects.create(title=title.title(), desc=desc, price=price, category=category, state=state.title(), city=city.title(), location=location.title(), photo=photo)
        post.save()
        messages.success(request, 'Posted Successfully.')
        return redirect('/post')
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'posts.html')
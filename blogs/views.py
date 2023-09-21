from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from django.http import HttpResponse

# Create your views here.


#blogs
def blogs(request):
  
  try:
    
    post=Post.objects.order_by('-date')
    paginator=Paginator(post,6)
    page=request.GET.get('page')
    paged_posts=paginator.get_page(page)
    return render(request, 'blogs/blogs.html', {"blog_data": paged_posts})

  except Exception as e:
    print('\n\n\n\n\n I am exception -> ',e)

# single blog 
def blog(request,blog_id):
  blog = get_object_or_404(Post, pk=blog_id)

  context = {
    'blog': blog
  }

  return render(request, 'blogs/blog.html', context)
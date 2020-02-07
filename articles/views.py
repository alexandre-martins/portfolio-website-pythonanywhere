from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from articles.models import Post, Category
from django.db.models import Q

def articles(request):
    all_posts = Post.objects.order_by('-timestamp')
    search_post = request.GET.get('search-post')

    categories = Category.objects.all()
    category_search = request.GET.get('cat-search')

    if search_post != '' and search_post is not None:
        all_posts = all_posts.filter(Q(title__icontains=search_post) | Q(overview__icontains=search_post))
    
    if category_search:
        all_posts = all_posts.filter(categories__title__icontains=category_search)

    paginator = Paginator(all_posts, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'categories': categories
    }

    return render(request, 'articles/articles_index.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post
    }

    return render(request, 'articles/post.html', context)

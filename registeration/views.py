from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import Article, Categories
from django.core.paginator import Paginator # how many articles/posts to show per page
#------------------------------------------#
from taggit.models import Tag # tag in view
from django.db.models import Q # Q for search queries
#from hitcount.views import HitCountDetailView # hitcount views for the posts



# paginator Function
def paginate(request, post_list):
    paginator = Paginator(post_list, 3) # Show 3 posts per page.

    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


# Create your views here.
class Posts(View):
    template = 'index.html'

    def get(self, request, slug=None):
        # tags in the Posts
        posts = Article.objects.all()

        page_obj = paginate(request, posts)



        context = {
            "posts":page_obj
        }

        return render(request, self.template, context)

# combine view for chosen tags
class Tagged(View):
    template = 'tagged_blog.html'

    # common tags
    common_tags = Article.tags.most_common()[:4]


    # tagged search
    def get(self, request, slug=None):
        # tags in the Posts
        common_tags = self.common_tags
        tag = get_object_or_404(Tag, slug=slug)
        posts = Article.objects.filter(tags=tag)


        # paginate the posts
        page_obj = paginate(request, posts)


        # html references
        context = {
            'common_tags': common_tags,
            'tag' : tag,
            "posts":page_obj,
        }

        return render(request, self.template, context)


# search view for Results
class SearchView(Tagged):
    template = 'search_results.html'

    # get results and get the database
    def get(self, request):
        # get the common tags from the the tagged class
        common_tags = Tagged.common_tags

        # search results
        # _,query = Tagged.get(request, *args, **kwargs)
        queryset = Article.objects.all()
        query = request.GET.get('q')
        if query:
            queries = queryset.filter(
                Q(title__icontains = query) |
                Q(article__icontains = query) |
                Q(article_1__icontains = query) |
                Q(article_2__icontains = query) |
                Q(article_3__icontains = query) |
                Q(article_4__icontains = query) |
                Q(article_5__icontains = query) |
                Q(article_6__icontains = query) |
                Q(article_7__icontains = query) |
                Q(article_8__icontains = query) |
                Q(article_9__icontains = query) |
                Q(subtitle__icontains = query)
            ).distinct()

        # paginate the posts
        page_obj = paginate(request, queries)

        # html refernecs
        context = {
            'queries':queries,
            'common' : common_tags,
            'page_obj': page_obj,
        }

        return render(request, self.template, context)


# article front page
class PostsAllTogether(Tagged):
    template = 'all-articles.html'

    # get the function get from Tagged view class
    def get(self, request, slug=None):
        common_tags = Tagged.common_tags
        # create a list view in the all posts/articles page
        num_posts = len(Article.objects.all())
        print(num_posts)

        # show the most viewed posts/articles first
        #popular_posts = Article.objects.order_by('-hit_count_generic__hits')[:num_posts]
        posts = Article.objects.all()

        # paginate the posts
        page_obj = paginate(request, posts)

        # html references
        context = {
            'common_tags': common_tags,
            "posts":popular_posts,
            'page_obj' : page_obj,
        }

        return render(request, self.template, context)


# categories view
class CategoriesView(Tagged):
    template = 'categories.html'
    # get the aricles/posts in the category
    def get(self, request, slug=None):
        categories_list = get_object_or_404(Categories, name=slug)
        category = Article.objects.filter(categories=categories_list)
        page_obj = paginate(request, category)
        common_tags = Tagged.common_tags
        print(category)

        context = {
            'common_tags':common_tags,
            'page_obj' : page_obj,
        }

        return render(request, self.template, context)


# detail view for post description
class PostDetail(View):
    template = 'blog-single.html'
    # get the specific posts
    def get(self, request, slug=None):
        categories_view = Categories.objects.all()
        post = get_object_or_404(Article,slug=slug)
        context = {
            'post':post,
            'categories': categories_view,
            'n' : range(1,10),
        }

        return render(request, self.template, context)

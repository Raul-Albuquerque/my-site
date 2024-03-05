from django.views import generic

from blog.models import Post


class PostView(generic.ListViewView):
    queryset = Post.object.filter(status=1).order_by("_created_on")
    template_name = "index.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

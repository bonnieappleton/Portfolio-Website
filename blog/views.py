from django.utils import timezone
from django.views.generic import TemplateView

from blog.models import Post


class Blog(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return context

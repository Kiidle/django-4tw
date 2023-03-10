from django.shortcuts import redirect, render
from django.views import generic

import commentary
from commentary.models import Commentary
from feeds.models import Feed
from django.urls import reverse_lazy


class CommentaryView(generic.DetailView):
    model = Commentary
    template_name = "commentary/commentary.html"

class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ['text']
    template_name = "commentary/create.html"

    def get_success_url(self):
        return reverse_lazy('feed', kwargs={"pk":self.kwargs.get('feed_id')})


    def get_current_feed(self, **kwargs):
        return Feed.objects.get(id = self.kwargs.get('feed_id'))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        feed = self.get_current_feed(**kwargs)
        data.update({'feed': feed})
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.feed = self.get_current_feed(**self.kwargs)
        return super().form_valid(form)
def commentary_edit(request, pk):
    return

def commentary_delete(request, pk):
    commentary = Commentary.objects.get(pk=pk)

    if request.method == 'POST':
        feed_id = commentary.feed.id
        commentary.delete()
        return redirect('feed', pk=feed_id)

    return (request, 'commentary/delete.html', {'commentary': commentary})
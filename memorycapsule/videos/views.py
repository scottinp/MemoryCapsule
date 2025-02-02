from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Video
# Create your views here.

def index(request):
    return render(request, 'videos/index.html')

class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'videos/create_video.html' 

    #def get_success_url(self):
    #    return reverse('video-detail', kwargs={'pk': self.object.pk})
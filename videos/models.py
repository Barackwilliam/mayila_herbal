from django.db import models

UCARECDN_BASE = 'https://ucarecdn.com'

def uc_url(uuid_val, transform=''):
    if not uuid_val:
        return ''
    return f"{UCARECDN_BASE}/{uuid_val}/{transform}"


class VideoAd(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('upload', 'Upload Video (Uploadcare)'),
        ('youtube', 'YouTube Link'),
    ]

    title        = models.CharField(max_length=200)
    description  = models.TextField(blank=True)
    video_type   = models.CharField(max_length=20, choices=VIDEO_TYPE_CHOICES, default='youtube')

    video_file   = models.CharField(max_length=255, blank=True, null=True, help_text='Uploadcare UUID ya video (MP4)')
    thumbnail    = models.CharField(max_length=255, blank=True, null=True, help_text='Uploadcare UUID ya thumbnail image')

    youtube_url  = models.URLField(blank=True, help_text='Paste full YouTube URL')
    product_tag  = models.CharField(max_length=100, blank=True)

    is_active    = models.BooleanField(default=True)
    is_featured  = models.BooleanField(default=False, help_text='Show in top slider')
    order        = models.PositiveIntegerField(default=0)
    views        = models.PositiveIntegerField(default=0, editable=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Video Advertisement'
        verbose_name_plural = 'Video Advertisements'

    def __str__(self):
        return self.title

    def get_youtube_embed_url(self):
        if not self.youtube_url:
            return ''
        url = self.youtube_url
        if 'youtu.be/' in url:
            vid_id = url.split('youtu.be/')[-1].split('?')[0]
        elif 'watch?v=' in url:
            vid_id = url.split('watch?v=')[-1].split('&')[0]
        else:
            vid_id = url.split('/')[-1]
        return f'https://www.youtube.com/embed/{vid_id}?rel=0&modestbranding=1'

    def get_thumbnail_url(self):
        return uc_url(self.thumbnail, '-/resize/640x/-/format/webp/-/quality/smart/')

    def get_video_url(self):
        return uc_url(self.video_file)
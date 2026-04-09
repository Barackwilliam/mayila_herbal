# from django.contrib import admin
# from django.utils.html import format_html
# from .models import VideoAd
# from .forms import VideoAdForm


# @admin.register(VideoAd)
# class VideoAdAdmin(admin.ModelAdmin):
#     form = VideoAdForm
#     list_display  = ('video_thumb', 'title', 'video_type', 'product_tag', 'is_featured', 'is_active', 'order', 'views')
#     list_editable = ('is_featured', 'is_active', 'order')
#     list_filter   = ('is_active', 'is_featured', 'video_type')
#     search_fields = ('title', 'description', 'product_tag')

#     fieldsets = (
#         ('🎬 Video Info', {
#             'fields': ('title', 'description', 'product_tag'),
#         }),
#         ('📹 Video Source', {
#             'fields': ('video_type', 'video_file', 'youtube_url'),
#             'description': (
#                 'Chagua MOJA: Pakia video file AU weka YouTube link. '
#                 'Video zilizopakiwa zinahifadhiwa kwenye Uploadcare CDN.'
#             ),
#         }),
#         ('🖼️ Thumbnail', {
#             'fields': ('thumbnail',),
#         }),
#         ('⚙️ Visibility', {
#             'fields': ('is_active', 'is_featured', 'order'),
#         }),
#     )

#     def video_thumb(self, obj):
#         url = obj.get_thumbnail_url()
#         if url:
#             return format_html(
#                 '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:6px;">',
#                 url
#             )
#         return '🎬'
#     video_thumb.short_description = 'Thumb'
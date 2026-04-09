from django import forms
from .models import VideoAd
from core.widgets import UploadcareWidget


class VideoUploadWidget(UploadcareWidget):
    """
    Widget maalum ya video — inaonyesha kitufe cha kupakia video (MP4/WebM)
    badala ya picha peke yake.
    """

    def render(self, name, value, attrs=None, renderer=None):
        from django.utils.html import format_html
        attrs = attrs or {}
        field_id = attrs.get('id', f'id_{name}')

        return format_html(
            '''
            <div class="uc-upload-wrapper" style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">

              <input type="hidden" name="{name}" id="{field_id}_uuid" value="{value}">

              <input
                type="hidden"
                role="uploadcare-uploader"
                data-public-key="{pub_key}"
                data-mime-types="video/mp4,video/webm,video/quicktime"
                id="{field_id}_uc"
                value="{value}"
              >

              <!-- Video preview (ikiwa ipo) -->
              <div id="{field_id}_preview" style="display:{display_preview};">
                <video width="160" height="90" controls style="border-radius:8px;border:2px solid #ccc;">
                  <source src="{video_url}" type="video/mp4">
                </video>
              </div>

              <button
                type="button"
                id="{field_id}_btn"
                onclick="
                  var widget = uploadcare.Widget('#{field_id}_uc');
                  widget.openDialog(null).done(function(fileInfo){{
                    document.getElementById('{field_id}_uuid').value = fileInfo.uuid;
                    var preview = document.getElementById('{field_id}_preview');
                    preview.style.display = 'block';
                    preview.innerHTML = '<video width=\\'160\\' height=\\'90\\' controls style=\\'border-radius:8px;border:2px solid #ccc;\\'><source src=\\'https://ucarecdn.com/' + fileInfo.uuid + '/\\' type=\\'video/mp4\\'></video>';
                    document.getElementById('{field_id}_filename').textContent = fileInfo.name || fileInfo.uuid.substring(0,8) + '...';
                  }});
                "
                style="background:#417690;color:#fff;border:none;padding:8px 16px;
                       border-radius:6px;cursor:pointer;font-size:13px;
                       display:inline-flex;align-items:center;gap:6px;"
              >
                🎬 Pakia Video
              </button>

              {clear_btn}

              <span id="{field_id}_filename"
                    style="font-size:12px;color:#666;max-width:180px;
                           overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
                {filename_display}
              </span>

            </div>
            ''',
            name=name,
            field_id=field_id,
            value=value or '',
            pub_key='4c3ba9de492e0e0eaddc',
            display_preview='block' if value else 'none',
            video_url=f'https://ucarecdn.com/{value}/' if value else '',
            clear_btn=format_html(
                '''<button type="button"
                    onclick="
                      document.getElementById('{}_uuid').value='';
                      document.getElementById('{}_preview').style.display='none';
                      document.getElementById('{}_filename').textContent='';
                    "
                    style="background:#ba2121;color:#fff;border:none;padding:8px 12px;
                           border-radius:6px;cursor:pointer;font-size:13px;">
                    🗑 Futa
                  </button>''',
                field_id, field_id, field_id
            ) if value else '',
            filename_display=value[:12] + '...' if value else '',
        )


class VideoAdForm(forms.ModelForm):
    class Meta:
        model = VideoAd
        fields = '__all__'

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'thumbnail' in self.fields:
            self.fields['thumbnail'].widget = UploadcareWidget()
        if 'video_file' in self.fields:
            self.fields['video_file'].widget = VideoUploadWidget()
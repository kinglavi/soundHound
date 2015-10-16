import os
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from mutagen.easyid3 import EasyID3
from soundHoundApi.validators import MimetypeValidator


def get_audio_upload_path(obj, filename):
    obj.name = filename
    return os.path.join("audio", obj.user.username, filename)


class Hum(models.Model):
    """
    This model in
    """
    file = models.FileField(upload_to=get_audio_upload_path, validators=[MimetypeValidator(
        ['audio/mpeg', 'audio/x-m4a', 'audio/mp3', 'audio/wav', 'audio/aiff', 'audio/x-wav', 'audio/x-aiff'])])

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


def fetch_id3(sender, instance, created, **kwargs):
    if created == True:

        try:
            id3 = EasyID3("%s/%s" % (settings.MEDIA_ROOT, instance.file))
        except:
            pass

        try:
            instance.title = id3['title'][0]
        except:
            pass

        try:
            instance.artist = id3['artist'][0]
        except:
            pass

        try:
            instance.album = id3['album'][0]
        except:
            pass

        instance.save()


post_save.connect(fetch_id3, sender=Hum, dispatch_uid="fetch_id3")

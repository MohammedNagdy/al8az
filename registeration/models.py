from django.db import models
from taggit.managers import TaggableManager # 3rd party lib for tags
from hitcount.models import HitCountMixin, HitCount # hitcount seeing how many viewes for each post
from django.contrib.contenttypes.fields import GenericRelation # assistant class for hitcount

# import all libs needed for image compression
# import PIL
# from PIL import Image
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.utils.six import StringIO


# main table for categories
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# the articles/posts model
class Article(models.Model):
    #title of the Article
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100, default="hey")
    article = models.TextField()
    published = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="../media/")

    # other parts for the article/posts
    article_1 = models.TextField(default="", blank=True)
    image_1 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_2 = models.TextField(default="", blank=True)
    image_2 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_3 = models.TextField(default="", blank=True)
    image_3 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_4 = models.TextField(default="", blank=True)
    image_4 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_5 = models.TextField(default="", blank=True)
    image_5 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_6 = models.TextField(default="", blank=True)
    image_6 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_7 = models.TextField(default="", blank=True)
    image_7 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_8 = models.TextField(default="", blank=True)
    image_8 = models.ImageField(upload_to="../media/",default="", blank=True)
    article_9 = models.TextField(default="", blank=True)
    image_9 = models.ImageField(upload_to="../media/",default="", blank=True)
    # end of the article


    slug = models.SlugField(unique=True, allow_unicode=True , max_length=100) # for urls slug
    categories = models.ForeignKey('Categories', on_delete=models.PROTECT) # categories ForeignKey
    tags = TaggableManager()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')



    def __str__(self):
        return self.title

    # def get_absolute_url(self, *args, **kwargs):
    #     return

    # slugify in arabic
    # def slugify(self, str):
    #     str = str.replace(" ", "-")
    #     str = str.replace(",", "-")
    #     str = str.replace("(", "-")
    #     str = str.replace(")", "")
    #     str = str.replace("؟", "")
    #     return str

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title

class article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    title=models.CharField(max_length=70)
    body=models.TextField()
    image=models.ImageField(upload_to="images/articles",null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True,unique=True,default=uuid.uuid1)
    like=models.ManyToManyField(User,blank=True,related_name="blog_posts")

#    بجای کلاس متا در ترتیب دهی پستها در ویو اردر ایجاد شد که هر دو قایل اسنفاده میباشد
    class Meta:
       ordering=("-created",)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug=slugify(self.title)
        super(article, self).save()

    def get_absolut_url(self):
        return reverse("article:article_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.title}-{self.body:30}'

class Comment(models.Model):
    Article=models.ForeignKey(article, on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    parent = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

class contact_us(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True)
    Email=models.EmailField()
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

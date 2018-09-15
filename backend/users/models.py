from django.db import models


max_len = 255

class users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=max_len, unique=True)
    password = models.CharField(max_length=300)
    email = models.EmailField()
    is_reader = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)




class books(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=max_len)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(users, on_delete=models.CASCADE)





class chapters(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    chapter = models.IntegerField(unique=True)





class following(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    following = models.ManyToManyField(books)




class read(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    chapter = models.ManyToManyField(chapters)



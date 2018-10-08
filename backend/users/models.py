from django.db import models
from django.contrib.auth.models import User



from books import models as book_model


max_len = 255

class users(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_reader = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'





class following(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    books = models.ManyToManyField(book_model.books, blank=True)

    class Meta:
        verbose_name = 'Books Following'
        verbose_name_plural = 'Books Following'
    





class read(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    book = models.ForeignKey(book_model.books, on_delete=models.CASCADE)
    chapter = models.ManyToManyField(book_model.chapters)

    class Meta:
        verbose_name = 'Books Read'
        verbose_name_plural = 'Books Read'





class author(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    book = models.ManyToManyField(book_model.books)

    class Meta:
        verbose_name = 'Books Written'
        verbose_name_plural = 'Books Written'
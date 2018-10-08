from django.db import models



class books(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.slug





class chapters(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    content = models.TextField()

    class Meta:
        unique_together = ('book', 'chapter')
        verbose_name = 'Book Chapter'
        verbose_name_plural = 'Book Chapter'

    def __str__(self):
        return '{} {}'.format(self.book.slug, self.chapter)
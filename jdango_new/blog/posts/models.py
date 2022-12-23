from django.db import models

# Create your models here.
class Post(models.Model):
    use_in_migration = True
    post_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'blog_posts'
    def __str__(self):
        return f'{self.pk} {self.title} {self.content} {self.created_at} {self.updated_at}'
from django.db import models

# Create your models here.
class Comment(models.Model):
    use_in_migration = True
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    class Meta:
        db_table = 'blog_comments'
    def __str__(self):
        return f'{self.pk} {self.content} {self.created_at} {self.updated_at}'
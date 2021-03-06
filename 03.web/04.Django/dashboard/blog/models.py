from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(verbose_name="TITLE", max_length=50)
    description = models.CharField("DESCRIPTION", max_length=100,
            blank = True, help_text="simple description text")
    content = models.TextField("CONTENT")
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
            verbose_name='OWNER', blank=True, null=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        # 기본 테이블명 : 앱이름_모델명
        db_table = "blog_posts" # 테이블명 재정의;
        # 내림차순 정렬
        ordering = ("-modify_dt", )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return ""
        return reverse("blog:detail", args=(self.id, ))

    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()

    # def save(self, *args, **kwargs):
    #     # 필드 조정 필요 시 작성
    #     super().save(*args, **kwargs)

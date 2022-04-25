from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Faq(models.Model):
    CATEGORY_CHOICES = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]

    title = models.CharField(verbose_name='질문 제목', max_length=80)
    content = models.TextField(verbose_name='질문 내용')
    category = models.CharField(verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICES)

    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='faq_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='faq_updated_by')


class Inquiry(models.Model):
    CATEGORY_CHOICES = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]

    category = models.CharField(verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField(verbose_name='질문 제목', max_length=80)
    email = models.EmailField(verbose_name='이메일', blank=True)
    phone = models.CharField(verbose_name='문자메시지', max_length=11, blank=True)
    is_eamil = models.BooleanField(verbose_name='이메일 수신 여부', default=False)
    is_phone = models.BooleanField(verbose_name='문자메시지 수신 여부', default=False)
    content = models.TextField(verbose_name='문의 내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)

    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquiry_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquiry_updated_by')


class Answer(models.Model):
    content = models.TextField(verbose_name='답변 내용')
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)

    inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answer_updated_by')

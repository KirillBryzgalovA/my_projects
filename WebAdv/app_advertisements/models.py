from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2) # 999.99 max_digits=5, decimal_places=2  || 99999999.99
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def updated_time(self):
        today = timezone.now().date()
        if self.updated_at.date() == today:
            return f"Сегодня в {self.updated_at.strftime('%H:%M')}"
        return self.updated_at.strftime('%d.%m.%Y %H:%M')

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"



from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=False, null=False)
    status = models.TextField(blank=False, null=False)
    class Meta:
        db_table = "user_table"  # 資料庫內表的名稱  #+ __init__ >create tazble name

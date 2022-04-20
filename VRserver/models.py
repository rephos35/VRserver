from django.db import models


# Create your models here.
class StatusDB(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    user1 = models.TextField()
    user2 = models.TextField()
    user3 = models.TextField()
    user4 = models.TextField()
    user5 = models.TextField()
    user6 = models.TextField()

    class Meta:
        db_table = "user_table"  # 資料庫內表的名稱  #+ __init__ >create tazble name

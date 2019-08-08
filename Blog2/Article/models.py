from django.db import models
class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
class Type(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    def __str__(self):
        return self.name

class Article(models.Model): #定义数据表 类名是表名的一部分
    title = models.CharField(max_length=32) #char(32
    date = models.DateField(auto_now=True) #date
    content = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(to=Author,on_delete = models.SET_DEFAULT,default=1)
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title


from django.db import models


class place(models.Model):
    area = models.CharField(max_length=250)
    sub  = models.CharField(max_length=250)

    def __str__(self):
        return self.name
#


#
# class branch(models.Model):
#     district = models(district, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name
# class form(models.Model):
#     name = models.CharField(max_length=250)
#     dob = models.DateField(null=True,blank=True)
#     district = models.ForeignKey(district,on_delete=models.SET_NULL,null=True)
#     branch = models.ForeignKey(bron_delete=models.SET_NULL,null=True)
#     gender = models.CharField(max_length=250)
#     account = models.CharField(max_length=250)
#
#
#     def __str__(self):
#         return self.name

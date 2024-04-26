from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(unique= True, null = True)
    phone = models.CharField(max_length = 50)
    address = models.CharField(max_length= 100)
    city = models.CharField(max_length= 20)
    state = models.CharField(max_length= 20)
    zipcode = models.CharField(max_length= 30, unique= True)
    
    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name}')
    
    
    
    
    
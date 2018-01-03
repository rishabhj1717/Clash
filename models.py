from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
    pname1=models.CharField(max_length=100,blank = True,null=True)
    phone1=models.CharField(max_length=100, blank=False,null=False)
    email1=models.EmailField(max_length=100,blank=False,null=False)
    pname2=models.CharField(max_length=100)
    phone2=models.CharField(max_length=100)
    email2=models.EmailField(max_length=100)
    level = models.IntegerField(default =0)#0 for junior 1 for senior
    total_score = models.IntegerField(default = 0)
    fibonacci_status = models.IntegerField(default=0)    #fibonacci lifeline currently in use or not
    fib_plus= models.IntegerField(default=5)
    fib_minus=models.IntegerField(default=3)
    fibonacci_marks = models.IntegerField(default = 0)  #to calculate the total marks to be awarded
    f_counter = models.IntegerField(default = 3)    #number of times fibonacci used
    coins_status = models.IntegerField(default = 0) #to update the number of coins
    skips = models.IntegerField(default = 0)    #number of skips
    coins=models.IntegerField(default=3)   #number of coins
    user=models.OneToOneField(User,null=True,blank=True)
    start_time=models.IntegerField(default=0)
    end_time=models.IntegerField(default=0)
    right_count=models.IntegerField(default=0) 
    wrong_count=models.IntegerField(default=0)

    def __str__(self):
        return(self.pname1)
##############################################################################################################
class Question(models.Model):
    question=models.TextField(max_length = 1000000)
    option_a = models.CharField(max_length = 500)
    option_b = models.CharField(max_length = 500)
    option_c = models.CharField(max_length = 500)
    option_d = models.CharField(max_length = 500)
    correct_option=models.CharField(max_length = 1)   #Doubt
    level = models.IntegerField(default = 0)#0 for junior 1 for senior
    """def __str__(self):
		return(self.question,self.option_a,self.option_b,self.option_c,self.option_d,self.level)
    """

class Qattempt(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)    
    """def __unicode__(self):
		return(self.status,self.user,self.question)"""
#############################################################################################################


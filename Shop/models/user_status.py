from django.db import models
import smtplib


class User(models.Model) :
    email = models.CharField(max_length=30)
    key = models.CharField(max_length=15)
    visited = models.BooleanField(default=False)
    
    def setVisited(self):
        self.visited = True
        self.save()
    
    def sendMail(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        
        send = "shopzy.supp0rt@gmail.com"
        pass_s = "fkptjaqeqjvlbxxh"
        s.login(send,pass_s)
        
        message = f'''
        Cofirm your account at ShopZy.
        Click on below link to confirm your account.
        http://shopzy-by-ankit.herokuapp.com/auth?key={self.key}&uname={self.email}
        '''  
        message = (f'''Subject: Confirm Account\n\n{message}''')
        
        s.sendmail("Admin.ShopZy@gmail.com", self.email, message)
        s.quit()
        print("Sent")
        
    @staticmethod
    def get_customer_by_email(email):
        try:
            return User.objects.get(email = email)
        except:
            return False

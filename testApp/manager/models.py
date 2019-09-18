from django.db import models

class Manager(models.Model):
    """
    保険会社マスタ
    """

    INSURE_CHOICES = (
        ('A', '生存保険'),
        ('B', '死亡保険'),
        ('C', '養老保険'),
    )
    COMPANY = (
        ('SC', 'seattleconsulting'),
        ('H', 'Hitachi')
    )

    email = models.EmailField()
    password = models.TextField()
    hashed_password = models.TextField(null=True)
    insurance_type = models.CharField(max_length=10, choices=INSURE_CHOICES, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True, null=True)


class Company(models.Model) :
    """
    企業（被保険者）マスタ
    """
    
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True, null=True)


class Employee(models.Model) :
    """
    従業員マスタ
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=50)
    birthday = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    company_id = models.ForeignKey(Company, on_delete=models.PROTECT)
    receiver_name = models.CharField(max_length=50)
    receiver_account = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True, null=True)
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('login/', views.login, name='login'),
    url('create_account/', views.newAcc, name='newAcc'),
    url('reset_pass/', views.resetPass, name="resetPass"),
    url('logged_out/', views.logOut, name="logOut"),
    url('add_done/', views.add, name="add"),
    url('delete_company/', views.delete_company, name="deleteCompany"),
    url('update_company/', views.update_company, name="updateCompany"),
    url('register/', views.registerAccount, name="registerAccount"),
    url('payment/', views.payment, name="payment"),
    url('finished_pay/', views.finished_pay, name="finished_pay"),
    url('detail/', views.employees_detail, name="emp_detail"),
    url('apply_info/', views.apply_info, name="apply_info"),
    url('apply_result/', views.apply_result, name="apply_result"),
    url('', views.index, name='home'),
    
    #url('auth/', include('social_django.urls', namespace='social')),  # <- Here
]
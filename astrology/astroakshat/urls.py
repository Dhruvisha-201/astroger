from django.contrib import admin
from django.urls import path
from astroakshat import views

app_name = "astroakshat"
      

urlpatterns = [
    path('',views.landing_page,name="landing_page"),
    path('client_index/',views.client_index,name="client_index"),
    path('login/',views.login, name='clientlogin'),
    path('clientlogout/',views.clientlogout, name='clientlogout'),
    path('register/',views.register, name='register'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),

    path('daily_horoscope_view',views.daily_horoscope_view,name="daily_horoscope_view"),
    path('daily_panchag',views.daily_panchag,name="daily_panchag"),
    path('daily_article',views.daily_article,name="daily_article"),
    path('contact_us',views.contact_us,name="contact_us"),
    path('takeappointment',views.takeappointment,name="takeappointment"),
    path('poojaappointment',views.poojaappointment,name="poojaappointment"),
    
    path('Kundliview',views.Kundliview,name="Kundliview"),
    path('kundlirequest',views.kundlirequest,name="kundlirequest"),


    path('S_vastushastra/',views.S_vastushastra, name='S_vastushastra'),
    path('s_lalkitab/',views.s_lalkitab, name='s_lalkitab'),
    path('s_tarrotreading/',views.s_tarrotreading, name='s_tarrotreading'),
    path('s_palmreading/',views.s_palmreading, name='s_palmreading'),
    path('birthjournal/',views.birthjournal, name='birthjournal'),
    path('KundliDosh/',views.KundliDosh, name='KundliDosh'),
    path('ManglikDosha/',views.ManglikDosha, name='ManglikDosha'),
    
    path('MakePayment/',views.MakePayment, name='MakePayment'),
]
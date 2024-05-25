from django.contrib import admin
from django.urls import path
from astroadmin import views

app_name = "astroadmin"
      

urlpatterns = [
    path('',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    #daily
    path('daily_horoscope_list/',views.daily_horoscope_list,name="daily_horoscope_list"),
    path('daily_horoscope_insert/',views.daily_horoscope_insert,name="daily_horoscope_insert"),
    path('daily_horoscope_update/<int:id>',views.daily_horoscope_update,name="daily_horoscope_update"),
    path('daily_horoscope_delete/<int:id>',views.daily_horoscope_delete,name="daily_horoscope_delete"),
    
    path('daily_panchag_list/',views.daily_panchag_list,name="daily_panchag_list"),
    path('daily_panchag_insert/',views.daily_panchag_insert,name="daily_panchag_insert"),
    path('daily_panchag_update/<int:id>',views.daily_panchag_update,name="daily_panchag_update"),
    path('daily_panchag_delete/<int:id>',views.daily_panchag_delete,name="daily_panchag_delete"),
    
    path('daily_artile_list/',views.daily_artile_list,name="daily_artile_list"),
    path('daily_artile_insert/',views.daily_artile_insert,name="daily_artile_insert"),
    path('daily_artile_update/<int:id>',views.daily_artile_update,name="daily_artile_update"),
    path('daily_artile_delete/<int:id>',views.daily_artile_delete,name="daily_artile_delete"),
  
    path('astro_admin_list/',views.astro_admin_list,name="astro_admin_list"),
    path('astro_admin_insert/',views.astro_admin_insert,name="astro_admin_insert"),
    path('astro_admin_update/<int:id>',views.astro_admin_update,name="astro_admin_update"),
    path('astro_admin_delete/<int:id>',views.astro_admin_delete,name="astro_admin_delete"),
   
    path('kundli_list/',views.kundli_list,name="kundli_list"),
    path('genrate_kundli/<int:id>',views.genrate_kundli,name="genrate_kundli"),
    path('update_genrate_kundli/<int:id>',views.update_genrate_kundli,name="update_genrate_kundli"),
    path('delete_genrate_kundli/<int:id>',views.delete_genrate_kundli,name="delete_genrate_kundli"),

    path('acceptappoint/<int:id>',views.acceptappoint, name = "acceptappoint"),
    path('rejectappoint/<int:id>',views.rejectappoint, name = "rejectappoint"),
    
    path('acceptpooja/<int:id>',views.acceptpooja, name = "acceptpooja"),
    path('rejectpooja/<int:id>',views.rejectpooja, name = "rejectpooja"),
    
    #services
    path('admin_vastu/',views.admin_vastu, name = "admin_vastu"),
    path('vastu_genrate/',views.vastu_genrate, name = "vastu_genrate"),
    path('vastu_update/<int:id>',views.vastu_update, name = "vastu_update"),
    path('vastudelete/<int:id>',views.vastudelete, name = "vastudelete"),
  
    path('admin_lalkitab/',views.admin_lalkitab, name = "admin_lalkitab"),
    path('lalkitab_genrate/',views.lalkitab_genrate, name = "lalkitab_genrate"),
    path('lalkitab_update/<int:id>',views.lalkitab_update, name = "lalkitab_update"),
    path('lalkitabdelete/<int:id>',views.lalkitabdelete, name = "lalkitabdelete"),
    
    path('admin_tarrot/',views.admin_tarrot, name = "admin_tarrot"),
    path('tarrot_genrate/',views.tarrot_genrate, name = "tarrot_genrate"),
    path('tarrot_update/<int:id>',views.tarrot_update, name = "tarrot_update"),
    path('tarrotdelete/<int:id>',views.tarrotdelete, name = "tarrotdelete"),
    
    path('admin_palm/',views.admin_palm, name = "admin_palm"),
    path('palm_genrate/',views.palm_genrate, name = "palm_genrate"),
    path('palm_update/<int:id>',views.palm_update, name = "palm_update"),
    path('palmdelete/<int:id>',views.palmdelete, name = "palmdelete"),
    
    path('admin_birthjournal/',views.admin_birthjournal, name = "admin_birthjournal"),
    path('genrate_birthjournal/<int:id>',views.genrate_birthjournal, name = "genrate_birthjournal"),
    path('update_birthjournal/<int:id>',views.update_birthjournal, name = "update_birthjournal"),
    path('delete_birthjournal/<int:id>',views.delete_birthjournal, name = "delete_birthjournal"),
    
    path('admin_manglikdosh/',views.admin_manglikdosh, name = "admin_manglikdosh"),
    path('genrate_manglikdosh/<int:id>',views.genrate_manglikdosh, name = "genrate_manglikdosh"),
    path('update_manglikdosh/<int:id>',views.update_manglikdosh, name = "update_manglikdosh"),
    path('delete_manglikdosh/<int:id>',views.delete_manglikdosh, name = "delete_manglikdosh"),
    
    path('admin_kundlidosh/',views.admin_kundlidosh, name = "admin_kundlidosh"),
    path('genrate_kundlikdosh/<int:id>',views.genrate_kundlikdosh, name = "genrate_kundlikdosh"),
    path('update_kundlidosh/<int:id>',views.update_kundlidosh, name = "update_kundlidosh"),
    path('delete_kundlidosh/<int:id>',views.delete_kundlidosh, name = "delete_kundlidosh"),
    
]
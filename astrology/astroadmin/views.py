from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages

from astroakshat.models import *
from .forms import Daily_Horoscopeform
from django.contrib.auth import logout


def admin_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/ad/admin_dashboard/')
        else:
            messages.error(request, 'Invalid credentials!!', extra_tags='loginvalidate')
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')


def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/ad/')
    else:
        return render(request, 'xyz.html')

def admin_dashboard(request):
    if request.user.is_authenticated:
        aid = request.user
        poojarequestlist=book_pooja.objects.all()
        kundlirequestlist=kundli.objects.filter(IsDeleted='0')
        appointmentrequestlist=astro_appointment.objects.all()
        return render(request,"admin_home.html",{'aid':aid,'poojarequestlist':poojarequestlist,'kundlirequestlist':kundlirequestlist,'appointmentrequestlist':appointmentrequestlist})
    else:
        print("Not logged in")
        return redirect('/ad/')

def acceptappoint(request,id):
    appointmentrequest=astro_appointment.objects.get(id=id)
    appointmentrequest.appoint_status = 1
    appointmentrequest.save()
    messages.error(request, 'Appointment Accepted', extra_tags='appoinaccept')
    return redirect('/ad/admin_dashboard/')

def rejectappoint(request,id):
    appointmentrequest=astro_appointment.objects.get(id=id)
    appointmentrequest.appoint_status = 2
    appointmentrequest.save()
    messages.error(request, 'Appointment Rejected!!', extra_tags='appoinreject')
    return redirect('/ad/admin_dashboard/')


def acceptpooja(request,id):
    appointmentrequest=book_pooja.objects.get(id=id)
    appointmentrequest.book_request = 1
    appointmentrequest.save()
    messages.error(request, 'Pooja Accepted', extra_tags='poojaaccept')
    return redirect('/ad/admin_dashboard/')

def rejectpooja(request,id):
    appointmentrequest=book_pooja.objects.get(id=id)
    appointmentrequest.book_request = 2
    appointmentrequest.save()
    messages.error(request, 'Pooja Rejected!!', extra_tags='poojareject')
    return redirect('/ad/admin_dashboard/')
# Daily horoscope Record

def daily_horoscope_list(request):
    if request.user.is_authenticated:
        aid = request.user
        horoscopelist = Daily_Horoscope.objects.filter(IsDeleted='0')
        return render(request,"horoscope_view.html",{'horoscopelist':horoscopelist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_horoscope_insert(request):
    if request.user.is_authenticated:
        aid = request.user
        if request.method == 'POST':
            horosign = request.POST.get('zodicid')
            print("horosign : -----------",horosign)
            horosignid = sign.objects.get(id = horosign)
            horoscopdate = request.POST.get('horodate')
            horoscoptitle = request.POST.get('horotitle')
            horoscopdesc = request.POST.get('horodescription')

            dailyhoro = Daily_Horoscope.objects.create(
                sign_id = horosignid,
                horoscope_date = horoscopdate,
                horoscope_title = horoscoptitle,
                horoscope_description = horoscopdesc,
                IsDeleted='0',
            )
            dailyhoro.save()
            return redirect('/ad/daily_horoscope_list')
        else:
            signlist = sign.objects.all()
            return render(request,"horoscope_add.html",{'signlist':signlist,'aid':aid})

    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_horoscope_update(request,id):
    if request.user.is_authenticated:
        aid = request.user
        selectedhoroid = Daily_Horoscope.objects.get(id=id)
        pdate= selectedhoroid.horoscope_date
        p_date = pdate.strftime("%Y-%m-%d")
        signlist=sign.objects.all()
        if request.method == "POST":
            
            signid=request.POST.get('signid')
            print("signid : ----------------",signid)
            getselectedsign = sign.objects.get(id=signid)
            horodate=request.POST.get('selecteddate')
            print("horodate : ----------------",horodate)
            horotitle=request.POST.get('horotitle')
            horodescription=request.POST.get('horodescription')

            
            selectedhoroid.sign_id=getselectedsign
            selectedhoroid.horoscope_date=horodate
            selectedhoroid.horoscope_title=horotitle
            selectedhoroid.horoscope_description=horodescription
            selectedhoroid.save()
            messages.success(request, 'Horoscope Updated Successfully', extra_tags='horoupdate')
            return redirect("/ad/daily_horoscope_list/")
        else:
            return render(request,"horoscope_update.html",{'p_date':p_date,'selectedhoroid':selectedhoroid,'signlist':signlist,'aid':aid}) 

    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_horoscope_delete(request,id):
    print("id : -----",id)
    selectedid = Daily_Horoscope.objects.get(id=id)
    selectedid.IsDeleted = '1'
    selectedid.save()
    messages.success(request, 'Horoscope Deleted Successfully', extra_tags='horoscopedelete')
    return redirect('/ad/daily_horoscope_list/')

# Daily Panchag Record

def daily_panchag_list(request):
    if request.user.is_authenticated:
        aid = request.user
        panchaglist=panchag.objects.filter(IsDeleted='0')
        return render(request,"panchag_list.html",{'panchaglist':panchaglist,'aid':aid})    

    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_panchag_insert(request):
    if request.user.is_authenticated:
        aid = request.user
        citylist=CityMaster.objects.all()
        monthlist=monthmaster.objects.all()
        if request.method == 'POST':
            panchagdate=request.POST.get('panchagdate')
            panchagday=request.POST.get('panchagday')
            panchagcountry=request.POST.get('panchagcountry')
            panchagstate=request.POST.get('panchagstate')
            cityid=request.POST.get('cityid')
            city=CityMaster.objects.get(id=cityid)
            panchagsunrise=request.POST.get('panchagsunrise')
            panchagset=request.POST.get('panchagset')
            panchagmoonrise=request.POST.get('panchagmoonrise')
            panchagmoonset=request.POST.get('panchagmoonset')
            month=request.POST.get('monthid')
            monthid=monthmaster.objects.get(id=month)
            Panchagtithi=request.POST.get('Panchagtithi')
            vikramsamvat=request.POST.get('vikramsamvat')
            samvatshaka=request.POST.get('samvatshaka')
            panchagnakshatra=request.POST.get('panchagnakshatra')
            panchagyog=request.POST.get('panchagyog')
            Panchagkaran=request.POST.get('Panchagkaran')

            panchagcreate=panchag.objects.create(
                date=panchagdate,
                day=panchagday,
                Country_id=panchagcountry,
                State_id=panchagstate,
                City_id=city,
                sunrise=panchagsunrise,
                sunset=panchagset,
                moonrise=panchagmoonrise,
                moonset=panchagmoonset,
                month=monthid,
                tithi=Panchagtithi,
                vikram_samvat=vikramsamvat,
                samvat_shaka=samvatshaka,
                nakshatra=panchagnakshatra,
                yog=panchagyog,
                karan=Panchagkaran,
                IsDeleted='0',
            )
            panchagcreate.save()
            return redirect('/ad/daily_panchag_list/')
        else:

            return render(request,"panchag_insert.html",{'monthlist':monthlist,'citylist':citylist,'aid':aid})    
    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_panchag_update(request,id):
    if request.user.is_authenticated:
        aid = request.user
        selectedpanchagid = panchag.objects.get(id=id)
        pdate= selectedpanchagid.date
        p_date = pdate.strftime("%Y-%m-%d")
        
        sunrisetime = selectedpanchagid.sunrise
        sunrise_time = sunrisetime.strftime("%H-%M")

        sunsettime = selectedpanchagid.sunrise
        sunset_time = sunsettime.strftime("%H-%M")

        moonrisetime = selectedpanchagid.sunrise
        moonrise_time = moonrisetime.strftime("%H-%M")

        moonsettime = selectedpanchagid.sunrise
        moonset_time = moonsettime.strftime("%H-%M")
    
        
        listofcity=CityMaster.objects.all()
        monthslist=monthmaster.objects.all()
        if request.method == "POST":
            panchagdate=request.POST.get('panchagdate')
            panchagday=request.POST.get('panchagday')
            print("panchagday : ----------------",panchagday)
            panchagcountry=request.POST.get('panchagcountry')
            panchagstate=request.POST.get('panchagstate')
            cityid=request.POST.get('cityid')
            getcity=CityMaster.objects.get(id=cityid)

            panchagsunrise=request.POST.get('panchagsunrise')
            panchagset=request.POST.get('panchagset')
            panchagmoonrise=request.POST.get('panchagmoonrise')
            panchagmoonset=request.POST.get('panchagmoonset')
            monthid=request.POST.get('monthid')
            getmonth=monthmaster.objects.get(id=monthid)

            Panchagtithi=request.POST.get('Panchagtithi')
            vikramsamvat=request.POST.get('vikramsamvat')
            samvatshaka=request.POST.get('samvatshaka')
            panchagnakshatra=request.POST.get('panchagnakshatra')
            panchagyog=request.POST.get('panchagyog')
            Panchagkaran=request.POST.get('Panchagkaran')

            
            selectedpanchagid.date=panchagdate
            selectedpanchagid.day=panchagday
            selectedpanchagid.Country_id=panchagcountry
            selectedpanchagid.State_id=panchagstate
            selectedpanchagid.City_id=getcity
            selectedpanchagid.sunrise=panchagsunrise
            selectedpanchagid.sunset=panchagset
            selectedpanchagid.moonrise=panchagmoonrise
            selectedpanchagid.moonset=panchagmoonset
            selectedpanchagid.month=getmonth
            selectedpanchagid.tithi=Panchagtithi
            selectedpanchagid.vikram_samvat=vikramsamvat
            selectedpanchagid.samvat_shaka=samvatshaka
            selectedpanchagid.nakshatra=panchagnakshatra
            selectedpanchagid.yog=panchagyog
            selectedpanchagid.karan=Panchagkaran
            selectedpanchagid.save()
            messages.success(request, 'Panchag Updated Successfully', extra_tags='horoupdate')
            return redirect("/ad/daily_panchag_list/")
        else:
            return render(request,"panchag_update.html",{'p_date':p_date,'selectedpanchagid':selectedpanchagid,'listofcity':listofcity,'monthslist':monthslist,'sunrise_time':sunrise_time,'sunset_time':sunset_time,'moonrise_time':moonrise_time,'moonset_time':moonset_time,'aid':aid}) 

    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_panchag_delete(request,id):
    print("id : -----",id)
    selectedid = panchag.objects.get(id=id)
    selectedid.IsDeleted = '1'
    selectedid.save()
    messages.success(request, 'Panchag Deleted Successfully', extra_tags='panchagdelete')
    return redirect('/ad/daily_panchag_list/')  

# Daily Article Record
def daily_artile_list(request):
    if request.user.is_authenticated:
        aid = request.user
        articlelist=Daily_Articals.objects.filter(IsDeleted='0')
        return render(request,"article_list.html",{'articlelist':articlelist,'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_artile_insert(request):
    if request.user.is_authenticated:
        aid = request.user
        if request.method == 'POST':
            article_date=request.POST.get('article_date')
            article_title=request.POST.get('article_title')
            artivle_description=request.POST.get('artivle_description')

            dailyarticle = Daily_Articals.objects.create(
                articledate=article_date,
                articletitle=article_title,
                articledescription=artivle_description,
                IsDeleted='0',
            )
            dailyarticle.save()
            return redirect('/ad/daily_artile_list/')
        else:
            return render(request,"article_insert.html",{'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_artile_update(request,id):
    if request.user.is_authenticated:
        aid = request.user
        selectedid = Daily_Articals.objects.get(id=id)
        pdate= selectedid.articledate
        p_date = pdate.strftime("%Y-%m-%d")
        if request.method == "POST":
            article_date=request.POST.get('article_date')
            article_title=request.POST.get('article_title')
            artivle_description=request.POST.get('artivle_description')

            selectedid.articledate=article_date
            selectedid.articletitle=article_title
            selectedid.articledescription=artivle_description
            selectedid.save()
            messages.success(request, 'Article Updated Successfully', extra_tags='Articleupdate')
            return redirect("/ad/daily_artile_list/")
        else:
            return render(request,"article_update.html",{'p_date':p_date,'selectedid':selectedid,'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def daily_artile_delete(request,id):
    print("id : -----",id)
    selectedid = Daily_Articals.objects.get(id=id)
    selectedid.IsDeleted = '1'
    selectedid.save()
    messages.success(request, 'Article Deleted Successfully', extra_tags='Articledelete')
    return redirect('/ad/daily_artile_list/')

# Astro Admin
def astro_admin_list(request):
    if request.user.is_authenticated:
        aid = request.user
        astroadminlist=astro_admin.objects.filter(IsDeleted='0')
        return render(request,"astro_admin_list.html",{'astroadminlist':astroadminlist,'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def astro_admin_insert(request):
    if request.user.is_authenticated:
        aid = request.user
        if request.method == 'POST':
            astroname=request.POST.get('astroname')
            astro_phone_no=request.POST.get('astrophone_no')
            astro_Email=request.POST.get('astroEmail')
            astro_location=request.POST.get('astrolocation')

            newoneadmin = astro_admin.objects.create(
                astro_name=astroname,
                astrophone_no=astro_phone_no,
                astroEmail=astro_Email,
                astrolocation=astro_location,
                IsDeleted='0',
            )
            newoneadmin.save()
            return redirect('/ad/astro_admin_list/')
        else:
            return render(request,"astroger_admin_insert.html",{'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def astro_admin_update(request,id):
    if request.user.is_authenticated:
        aid = request.user
        selectedadmin = astro_admin.objects.get(id=id)
        
        if request.method == "POST":
            astroname=request.POST.get('astro_name')
            astro_phone_no=request.POST.get('astrophone_no')
            astro_Email=request.POST.get('astroEmail')
            astro_location=request.POST.get('astrolocation')

            selectedadmin.astro_name=astroname
            selectedadmin.astrophone_no=astro_phone_no
            selectedadmin.astroEmail=astro_Email
            selectedadmin.astrolocation=astro_location
                # IsDeleted='0',

            selectedadmin.save()
            messages.success(request, 'Admin Updated Successfully', extra_tags='Adminupdate')
            return redirect("/ad/astro_admin_list/")
        else:
            return render(request,"astroger_admin_update.html",{'selectedadmin':selectedadmin,'aid':aid}) 
    else:
        print("Not logged in")
        return redirect('/ad/')

def astro_admin_delete(request,id):
    print("id : -----",id)
    selectedid = astro_admin.objects.get(id=id)
    selectedid.IsDeleted = '1'
    selectedid.save()
    messages.success(request, 'Admin Deleted Successfully', extra_tags='Admindelete')
    return redirect('/ad/astro_admin_list/')

def kundli_list(request):
    if request.user.is_authenticated:
        aid = request.user
        kundlirequestlist=kundli.objects.filter(IsDeleted='0')
        return render(request,"kundli_list.html",{'kundlirequestlist':kundlirequestlist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def genrate_kundli(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        selectedid = kundli.objects.get(id=id)
        if request.method == 'POST':
            kundli_title=request.POST.get('kundli_title')
            kundli_desc=request.POST.get('kundli_desc')
            clientlogid = clientsignup.objects.get(id=selectedid.clientlog.id)

            
            create_kundli.objects.create(
                kundli_id= selectedid,
                clientlog= clientlogid,
                title=kundli_title ,
                description= kundli_desc,
                IsDeleted='0',
            )
            selectedid.IsRequest = '1'
            selectedid.save()
            messages.success(request, 'Kundli Created Successfully', extra_tags='kundlicreate')
            return redirect('/ad/kundli_list/')
        else:
            return render(request,'kundli_genrate.html',{'selectedid':selectedid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def update_genrate_kundli(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        print("id : ---------------------",id)
        selectekundlidid = create_kundli.objects.get(kundli_id =id,IsDeleted=0)
        print('selectekundlidid:---------------',selectekundlidid)
        if request.method == 'POST':
            print("hello if :-----------------")
            kundlititle=request.POST.get('kundli_title')
            kundlidesc=request.POST.get('kundli_desc')


            selectekundlidid.title = kundlititle
            selectekundlidid.description = kundlidesc
            selectekundlidid.save()
            messages.success(request, 'Kundli Updated Successfully', extra_tags='kundliupdate')
            return redirect('/ad/kundli_list/')
        else:

            return render(request, "update_kundli_genrate.html",{'selectekundlidid':selectekundlidid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def delete_genrate_kundli(request,id):
    selectekundlidid = kundli.objects.get(id=id)
    selectekundlidid.IsRequest = '0'
    selectekundlidid.save()
    selectedid = create_kundli.objects.get(kundli_id=id,IsDeleted=0)
    selectedid.IsDeleted = '1'
    selectedid.save()
    messages.success(request, 'Kundli Deleted Successfully', extra_tags='genratedkundlidelete')
    return redirect('/ad/kundli_list/') 



def admin_vastu(request):
    if request.user.is_authenticated:
        aid = request.user
        
        vastulist = vastu.objects.filter(IsDeleted=0)
        return render(request,"s_vastuview.html",{'vastulist':vastulist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def vastu_genrate(request):
    if request.user.is_authenticated:
        aid = request.user
        
        if request.method == 'POST':
            vastu_title=request.POST.get('vastu_title')
            vastu_desc=request.POST.get('vastu_desc')
                    
            vastu.objects.create(
                title= vastu_title,
                description= vastu_desc,
                IsDeleted='0' ,
            )
            messages.success(request, 'Vastu Created Successfully', extra_tags='Vastucreate')
            return redirect('/ad/admin_vastu/')
        else:
            return render(request,'s_vastuinsert.html',{'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')    
    
def vastu_update(request, id):
    if request.user.is_authenticated:
        aid = request.user
        
        print(id)
        selectedvastuid = vastu.objects.get(id=id)
        if request.method == 'POST':
            vastu_title=request.POST.get('vastu_title')
            print("vastu_title: ================", vastu_title)
            vastu_desc=request.POST.get('vastu_desc')
                    
            selectedvastuid.title = vastu_title
            selectedvastuid.description = vastu_desc
            selectedvastuid.save()    
            messages.success(request, 'Vastu Updated Successfully', extra_tags='Vastuupdated')
            return redirect('/ad/admin_vastu/')
        else:
            return render(request,"s_Updatevastu.html",{'selectedvastuid':selectedvastuid,'aid':aid})
    else:   
        print("Not logged in")
        return redirect('/ad/')
def vastudelete(request, id):
    selectedvastuid = vastu.objects.get(id=id)
    selectedvastuid.IsDeleted=1
    selectedvastuid.save()
    messages.success(request, 'Vastu Deleted Successfully', extra_tags='Vastudelete')
    return redirect('/ad/admin_vastu/')    



def admin_lalkitab(request):
    if request.user.is_authenticated:
        aid = request.user
        
        lalkitablist = lalkitab.objects.filter(IsDeleted=0)
        return render(request,"s_lalkitabview.html",{'lalkitablist':lalkitablist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def lalkitab_genrate(request):
    if request.user.is_authenticated:
        aid = request.user
        
        if request.method == 'POST':
            kitab_title=request.POST.get('kitab_title')
            kitab_desc=request.POST.get('kitab_desc')
                    
            lalkitab.objects.create(
                title= kitab_title,
                description= kitab_desc,
                IsDeleted='0' ,
            )
            messages.success(request, 'LalKitab Created Successfully', extra_tags='kitabcreate')
            return redirect('/ad/admin_lalkitab/')
        else:
            return render(request,'s_lalkitabinsert.html',{'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')    
    
def lalkitab_update(request, id):
    if request.user.is_authenticated:
        aid = request.user
        
        print(id)
        selectedlalkitabid = lalkitab.objects.get(id=id)
        if request.method == 'POST':
            kitab_title=request.POST.get('kitab_title')
            print("kitab_title: ================", kitab_title)
            kitab_desc=request.POST.get('kitab_desc')
                    
            selectedlalkitabid.title = kitab_title
            selectedlalkitabid.description = kitab_desc
            selectedlalkitabid.save()    
            messages.success(request, 'LalKitab Updated Successfully', extra_tags='kitabupdated')
            return redirect('/ad/admin_lalkitab/')
        else:
            return render(request,"s_Updatelalkitab.html",{'selectedlalkitabid':selectedlalkitabid,'aid':aid})
    else:   
        print("Not logged in")
        return redirect('/ad/')

def lalkitabdelete(request, id):
    selectedlalkitabid = lalkitab.objects.get(id=id)
    selectedlalkitabid.IsDeleted=1
    selectedlalkitabid.save()
    messages.success(request, 'LalKitab Deleted Successfully', extra_tags='kitabdelete')
    return redirect('/ad/admin_lalkitab/')    

def admin_tarrot(request):
    if request.user.is_authenticated:
        aid = request.user
        
        tarrotlist = tarrot_reading.objects.filter(IsDeleted=0)
        return render(request,"s_tarrotview.html",{'tarrotlist':tarrotlist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def tarrot_genrate(request):
    if request.user.is_authenticated:
        aid = request.user
        
        if request.method == 'POST':
            tarrot_title=request.POST.get('tarrot_title')
            tarrot_desc=request.POST.get('tarrot_desc')
                    
            tarrot_reading.objects.create(
                title= tarrot_title,
                description= tarrot_desc,
                IsDeleted='0' ,
            )
            messages.success(request, 'Tarrot Created Successfully', extra_tags='tarrotcreate')
            return redirect('/ad/admin_tarrot/')
        else:
            return render(request,'s_tarrotinsert.html',{'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')    
    
def tarrot_update(request, id):
    if request.user.is_authenticated:
        aid = request.user
        
        print(id)
        selectedtarrotid = tarrot_reading.objects.get(id=id)
        if request.method == 'POST':
            tarrot_title=request.POST.get('tarrot_title')
            tarrot_desc=request.POST.get('tarrot_desc')
                    
            selectedtarrotid.title = tarrot_title
            selectedtarrotid.description = tarrot_desc
            selectedtarrotid.save()    
            messages.success(request, 'Tarrot Updated Successfully', extra_tags='tarrotupdated')
            return redirect('/ad/admin_tarrot/')
        else:
            return render(request,"s_Updatetarrot.html",{'selectedtarrotid':selectedtarrotid,'aid':aid})
    else:   
        print("Not logged in")
        return redirect('/ad/')

def tarrotdelete(request, id):
    selectedtarrotid = tarrot_reading.objects.get(id=id)
    selectedtarrotid.IsDeleted=1
    selectedtarrotid.save()
    messages.success(request, 'Tarrot Deleted Successfully', extra_tags='tarrotdelete')
    return redirect('/ad/admin_tarrot/') 

def admin_palm(request):
    if request.user.is_authenticated:
        aid = request.user
        palmlist = plam_reading.objects.filter(IsDeleted=0)
        return render(request,"s_palmview.html",{'palmlist':palmlist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def palm_genrate(request):
    if request.user.is_authenticated:
        aid = request.user
        
        if request.method == 'POST':
            palm_title=request.POST.get('palm_title')
            palm_desc=request.POST.get('palm_desc')
                    
            plam_reading.objects.create(
                title= palm_title,
                description= palm_desc,
                IsDeleted='0' ,
            )
            messages.success(request, 'palm Created Successfully', extra_tags='palmcreate')
            return redirect('/ad/admin_palm/')
        else:
            return render(request,'s_palminsert.html',{'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')    
    
def palm_update(request, id):
    if request.user.is_authenticated:
        aid = request.user
        
        print(id)
        selectedplamid = plam_reading.objects.get(id=id)
        if request.method == 'POST':
            palm_title=request.POST.get('palm_title')
            palm_desc=request.POST.get('palm_desc')
                    
            selectedplamid.title = palm_title
            selectedplamid.description = palm_desc
            selectedplamid.save()    
            messages.success(request, 'palm Updated Successfully', extra_tags='palmupdated')
            return redirect('/ad/admin_palm/')
        else:
            return render(request,"s_Updatepalm.html",{'selectedplamid':selectedplamid,'aid':aid})
    else:   
        print("Not logged in")
        return redirect('/ad/')

def palmdelete(request, id):
    selectedplamid = plam_reading.objects.get(id=id)
    selectedplamid.IsDeleted=1
    selectedplamid.save()
    messages.success(request, 'Plam Deleted Successfully', extra_tags='palmdelete')
    return redirect('/ad/admin_palm/') 

def admin_birthjournal(request):
    if request.user.is_authenticated:
        aid = request.user
        birthjournallist=birth.objects.filter(IsDeleted='0')
        return render(request,"ad_s_birthjournal.html",{'birthjournallist':birthjournallist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def genrate_birthjournal(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        selectedid = birth.objects.get(id=id)
        if request.method == 'POST':
            birth_title=request.POST.get('birth_title')
            birth_desc=request.POST.get('birth_desc')
            clientlogid = clientsignup.objects.get(id=selectedid.clientlog.id)

            
            create_birth_journal.objects.create(
                birth_id= selectedid,
                clientlog= clientlogid,
                title=birth_title ,
                description= birth_desc,
                IsDeleted='0',
            )
            selectedid.IsRequest = '1'
            selectedid.save()
            messages.success(request, 'Birth Journal Created Successfully', extra_tags='kundlicreate')
            return redirect('/ad/admin_birthjournal/')
        else:
            return render(request,'ad_s_birthjournalinsert.html',{'selectedid':selectedid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def update_birthjournal(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        print("id : ---------------------",id)
        selectedbirthid = create_birth_journal.objects.get(birth_id =id,IsDeleted=0)
        print('selectedbirthid:---------------',selectedbirthid)
        if request.method == 'POST':
            print("hello if :-----------------")
            kundlititle=request.POST.get('kundli_title')
            kundlidesc=request.POST.get('kundli_desc')


            selectedbirthid.title = kundlititle
            selectedbirthid.description = kundlidesc
            selectedbirthid.save()
            messages.success(request, 'Birth Journal Updated Successfully', extra_tags='kundliupdate')
            return redirect('/ad/admin_birthjournal/')
        else:

            return render(request, "ad_s_birthjounalupdate.html",{'selectedbirthid':selectedbirthid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')


def delete_birthjournal(request,id):
    print("id :-------------- ",id)
    selectedbirthid = birth.objects.get(id=id)
    selectedbirthid.IsRequest = '0'
    selectedbirthid.save()
    selectedbirthjid = create_birth_journal.objects.get(birth_id=id,IsDeleted=0)
    selectedbirthjid.IsDeleted = '1'
    selectedbirthjid.save()
    messages.success(request, 'Birth Journal Deleted Successfully', extra_tags='genratedkundlidelete')
    return redirect('/ad/admin_birthjournal/') 

def admin_manglikdosh(request):
    if request.user.is_authenticated:
        aid = request.user
        manglikdoshllist=manglik.objects.filter(IsDeleted='0')
        return render(request,"ad_s_manglikdosh.html",{'manglikdoshllist':manglikdoshllist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def genrate_manglikdosh(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        selectedid = manglik.objects.get(id=id)
        if request.method == 'POST':
            manglik_title=request.POST.get('manglik_title')
            manglik_desc=request.POST.get('manglik_desc')
            clientlogid = clientsignup.objects.get(id=selectedid.clientlog.id)

            
            create_manglik.objects.create(
                manglik_id= selectedid,
                clientlog= clientlogid,
                title=manglik_title ,
                description= manglik_desc,
                IsDeleted='0',
            )
            selectedid.IsRequest = '1'
            selectedid.save()
            messages.success(request, 'Manglik Dosh Created Successfully', extra_tags='maglikcreate')
            return redirect('/ad/admin_manglikdosh/')
        else:
            return render(request,'ad_s_manglikdoshinsert.html',{'selectedid':selectedid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def update_manglikdosh(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        print("id : ---------------------",id)
        selectedmanglikid = create_manglik.objects.get(manglik_id =id,IsDeleted=0)
        print('selectedmanglikid:---------------',selectedmanglikid)
        if request.method == 'POST':
            print("hello if :-----------------")
            manglik_title=request.POST.get('manglik_title')
            manglik_desc=request.POST.get('manglik_desc')


            selectedmanglikid.title = manglik_title
            selectedmanglikid.description = manglik_desc
            selectedmanglikid.save()
            messages.success(request, 'Mnadlik Dosh Updated Successfully', extra_tags='manglikupdate')
            return redirect('/ad/admin_manglikdosh/')
        else:

            return render(request, "ad_s_manglikdoshupdate.html",{'selectedmanglikid':selectedmanglikid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')


def delete_manglikdosh(request,id):
    print("id :-------------- ",id)
    selectedbirthid = manglik.objects.get(id=id)
    selectedbirthid.IsRequest = '0'
    selectedbirthid.save()
    selectedbirthjid = create_manglik.objects.get(manglik_id=id,IsDeleted=0)
    selectedbirthjid.IsDeleted = '1'
    selectedbirthjid.save()
    messages.success(request, 'Manglik Dosh Deleted Successfully', extra_tags='manglikdoshdelete')
    return redirect('/ad/admin_manglikdosh/') 

def admin_kundlidosh(request):
    if request.user.is_authenticated:
        aid = request.user
        kundlidoshllist=kundli_dosh.objects.filter(IsDeleted='0')
        return render(request,"ad_s_kundlidosh.html",{'kundlidoshllist':kundlidoshllist,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')
    
def genrate_kundlikdosh(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        selectedid = kundli_dosh.objects.get(id=id)
        if request.method == 'POST':
            kundlidosh_title=request.POST.get('kundlidosh_title')
            kundlidosh_desc=request.POST.get('kundlidosh_desc')
            clientlogid = clientsignup.objects.get(id=selectedid.clientlog.id)

            
            create_kundli_dosh.objects.create(
                kundli_dosh_id= selectedid,
                clientlog= clientlogid,
                title=kundlidosh_title ,
                description= kundlidosh_desc,
                IsDeleted='0',
            )
            selectedid.IsRequest = '1'
            selectedid.save()
            messages.success(request, 'Kundli Dosh Created Successfully', extra_tags='kundlidoshcreate')
            return redirect('/ad/admin_kundlidosh/')
        else:
            return render(request,'ad_s_kundlidoshinsert.html',{'selectedid':selectedid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')

def update_kundlidosh(request,id):
    if request.user.is_authenticated:
        aid = request.user
        
        print("id : ---------------------",id)
        selectedkundlidoshid = create_kundli_dosh.objects.get(kundli_dosh_id =id,IsDeleted=0)
        print('selectedkundlidoshid:---------------',selectedkundlidoshid)
        if request.method == 'POST':
            print("hello if :-----------------")
            kundlidosh_title=request.POST.get('kundlidosh_title')
            kundlidosh_desc=request.POST.get('kundlidosh_desc')


            selectedkundlidoshid.title = kundlidosh_title
            selectedkundlidoshid.description = kundlidosh_desc
            selectedkundlidoshid.save()
            messages.success(request, 'Kundli Dosh Updated Successfully', extra_tags='kundliupdate')
            return redirect('/ad/admin_kundlidosh/')
        else:

            return render(request, "ad_s_kundlidoshupdate.html",{'selectedkundlidoshid':selectedkundlidoshid,'aid':aid})
    else:
        print("Not logged in")
        return redirect('/ad/')


def delete_kundlidosh(request,id):
    print("id :-------------- ",id)
    selectedkundlidoshid = kundli_dosh.objects.get(id=id)
    selectedkundlidoshid.IsRequest = '0'
    selectedkundlidoshid.save()
    selectedkundlidoshidd = create_kundli_dosh.objects.get(manglik_id=id,IsDeleted=0)
    selectedkundlidoshidd.IsDeleted = '1'
    selectedkundlidoshidd.save()
    messages.success(request, 'Kundli Dosh Deleted Successfully', extra_tags='kundlidoshdelete')
    return redirect('/ad/admin_kundlidosh/') 

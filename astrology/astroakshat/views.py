from django.shortcuts import render,redirect
from datetime import date
from .models import *
from datetime import datetime
import re
from django.contrib import messages
from django.contrib.auth import logout

 
# Create your views here.
def landing_page(request):
    return render(request,"landingpage.html")
def client_index(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        todaydate = datetime.today().strftime('%Y-%m-%d')
        allcity=CityMaster.objects.all()
        dailyarticle = Daily_Articals.objects.filter(articledate=todaydate)
        print("dailyarticle : -----------------",dailyarticle)
        return render(request,"index.html",{'dailyarticle':dailyarticle,'allcity':allcity,'cid':cid})

    except:
        return redirect('/')


def login(request, message=None):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('Password')
        try:
            val = clientsignup.objects.get(Email = email)
            print("--------------", email)
            if password == val.password:
                request.session['astro_id'] = val.id
                request.session['astro_Email'] = val.Email
                request.session['astro_password'] = val.password
                return redirect('/client_index/')
            
            else:
                messages.error(request, "Invalid user name and password",extra_tags="invalidpass")
                return redirect('/login/')
        except:
            messages.error(request, "Invalid user name and password",extra_tags="invalidpass")
            return redirect('/')
    else:
        return render(request, "sign_in.html")

def clientlogout(request):
    if 'astro_id'  in request.session:
        logout(request)
        return redirect('/')
    else:
        return render(request, "sign_in.html")

def register(request):
    if request.method == "POST":
        citylist = CityMaster.objects.all()
        First_Name = request.POST.get('FirstName')
        print("FirstName : ---------",First_Name)
        LastName = request.POST.get("Last_Name")
        phoneno = request.POST.get("Phone_No")
        email = request.POST.get("signup_email")
        print("email...",email)
        address = request.POST.get("Address")
        city = request.POST.get("City_name")
        print("city : ----[]",city)
        cityid = CityMaster.objects.get(id=city)
        state = request.POST.get("State_name")
        country = request.POST.get("Country_name")
        password = request.POST.get("password")
        print("pass...",password)
        confirm_password = request.POST.get("confirmpassword")
        pincode = request.POST.get("Pincode")
        date = datetime.today()
        print("Today date is: ", date)

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            if clientsignup.objects.filter(Email=email).exists():
                messages.error(request, "Email is Already Taken, Try With Another", extra_tags="loginverify")

                return render(request,"signup.html",{'First_Name':First_Name,'LastName':LastName,'phoneno':phoneno,'email':email,'address':address,'citylist':citylist,'state':state,'country':country,'password':password,'pincode':pincode})
            else:
                pass
        else:
            messages.error(request,'Please Enter Valid Email', extra_tags = 'c_msg')
            return render(request,"signup.html",{'First_Name':First_Name,'LastName':LastName,'phoneno':phoneno,'email':email,'address':address,'citylist':citylist,'state':state,'country':country,'password':password,'pincode':pincode})
        
        passreg = r'\b^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$\b'
        
        if password == confirm_password:
            if(re.fullmatch(passreg , password)):
                pass
            else:
                messages.error(request,'Your password is weak . You should have atleast 8 character, Please including Uppercase, Lowercase, Numbers and Special character', extra_tags = 'c_pass')
                return render(request,"signup.html", {'First_Name':First_Name,'LastName':LastName,'phoneno':phoneno,'email':email,'address':address,'citylist':citylist,'state':state,'country':country,'password':password,'pincode':pincode})
        else:
            messages.error(request,'New Password And Confirm Password Does Not Match', extra_tags = 'strongpassword')
            return render(request,"signup.html", {'First_Name':First_Name,'LastName':LastName,'phoneno':phoneno,'email':email,'address':address,'citylist':citylist,'state':state,'country':country,'password':password,'pincode':pincode})
        
        val = clientsignup.objects.create(
            FirstName =First_Name,
            LastName = LastName,
            phone_no = phoneno,
            Email = email,
            Country_id =country,
            State_id = state,
            City_id = cityid,
            Address = address,
            pincode = pincode,
            password = password,
            IsActive='0',
            IsDeleted='0',
            createby="astrologer",
            CreatedDate=date,
            ModifiedBy="astrologer",
            ModifiedDate=date,
            is_admin='0')
        val.save()
        messages.success(request,'Congratulations!! You Are Successfully Registered Now You Can Login', extra_tags = 'Suc_msg')
        return redirect('/login/')
    else:
        today = datetime.today()
        print("Today date is: ", today)
        citylist = CityMaster.objects.all()
        return render(request,"signup.html",{'citylist':citylist})


def forgot_password(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        if clientsignup.objects.filter(Email=email).exists():
            sendemailvar=clientsignup.objects.get(Email=email)
            print("sendmail..",sendemailvar)

            return render(request,"forgot_password.html")
    else:
        messages.error(request,'Please Enter  Email', extra_tags = 'client_msg')
        return render(request,"forgot_password.html")
    
    company = clientsignup.objects.get(id=id)

    mydict={'email':company.signup_email, 'regno': company.password}
    html_template ='client_email.html'
    html_message = render_to_string(html_template,context=mydict)
    subject="Welcome To swetakshi Applications"
    email_from = EMAIL_HOST_USER

    recipient_list =[company.signup_email,company.password]
    message=EmailMessage(subject,html_message,email_from,recipient_list)
    message.content_subtype ='html'
    message.send()
    company.IsActive = '1'
    company.save()
    messages.error(request,'swtakshi  Accepted.', extra_tags = 'swetakshiaccept')

    return redirect('/login/')


def daily_horoscope_view(request):
    today=datetime.today().strftime('%Y-%m-%d')
    print("today : -----------------------",today)
    today_horoscope=Daily_Horoscope.objects.filter(horoscope_date=today)
    return render(request,"daily_horoscope.html",{'today_horoscope':today_horoscope})

def daily_panchag(request):
    today=datetime.today()
    print("today : -----------------------",today)
    today_panchag=panchag.objects.filter(date=today)
    return render(request,"daily_panchag.html",{'today_panchag':today_panchag})

def daily_article(request):
    today=datetime.today()
    print("today : -----------------------",today)
    today_article=Daily_Articals.objects.filter(articledate=today)
    return render(request,"daily_article.html",{'today_article':today_article})


def contact_us(request):
    return render(request, "contactus.html")

def takeappointment(request):
    try:    
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        clientappoins = astro_appointment.objects.filter(customer_id=cid)

        if request.method == 'POST':
            clientname=request.POST.get('clientname')
            clientemail=request.POST.get('clientemail')
            clientno=request.POST.get('clientno')
            pdate=request.POST.get('pdate')
            ptime=request.POST.get('ptime')
            resoanappoint=request.POST.get('resoanappoint')

            astro_appointment.objects.create(
                customer_id = cid,
                c_name = clientname,
                c_Email = clientemail,
                c_phoneno = clientno,
                preferred_date = pdate,
                preferred_time = ptime,
                reason_for_appoint = resoanappoint,
                appoint_status = '0',
            )
            messages.success(request,"appointment request genrated successfully", extra_tags='appoinreq')

            return redirect('/takeappointment')
        else:
            return render(request,"requestappointment.html",{'cid':cid,'clientappoins':clientappoins})
    except:
        return redirect('/login/')

def Kundliview(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        allcity = CityMaster.objects.all()
        logkundli = kundli.objects.filter(clientlog=cid.id,IsRequest=0)
        logcreate_kundli = create_kundli.objects.filter(clientlog=cid.id,IsDeleted=0)

        return render(request, "kundliview.html",{'allcity':allcity,'logkundli':logkundli,'logcreate_kundli':logcreate_kundli})
    except:
        return redirect('/login/')

def kundlirequest(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        if request.method == "POST":
            name=request.POST.get('kundli_name')
            dob=request.POST.get('kundli_DOB')
            tob=request.POST.get('kundli_time_of_birth')
            cityname=request.POST.get('kundli_City')
            cityid = CityMaster.objects.get(id=cityname)

            kundlireq = kundli.objects.create(
                kundli_name=name,
                kundli_DOB=dob,
                kundli_time_of_birth=tob,
                kundli_City=cityid,
                clientlog= cid,
                IsRequest='0',
                IsDeleted='0',
            )
            kundlireq.save()
            messages.success(request,'Request genrated successfully', extra_tags = 'kundligenrates')
            return redirect('/Kundliview')
        else:
            allcity = CityMaster.objects.all()
            return render(request, "kundliview.html", {'allcity':allcity})
    except:
        return redirect('/login/')

def poojaappointment(request):
    try:    
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        clientappoins = book_pooja.objects.filter(customer_id=cid)
        poojalist = astro_pooja.objects.all()

        if request.method == 'POST':
            poojaname=request.POST.get('poojaname')
            print("poojaname :---------------",poojaname)
            poojaid = astro_pooja.objects.get(id=poojaname)
            cname=request.POST.get('cname')
            cemail=request.POST.get('cemail')
            cnumber=request.POST.get('cnumber')
            pdate=request.POST.get('pdate')
            ptime=request.POST.get('ptime')
            resoanappoint=request.POST.get('resoanappoint')

            book_pooja.objects.create(
                customer_id = cid,
                pooja_name = poojaid,
                c_name = cname,
                c_Email = cemail,
                c_phoneno = cnumber,
                preferred_date = pdate,
                preferred_time = ptime,
                reason_for_appoint = resoanappoint,
                book_request = '0',
            )
            messages.success(request,"appointment request genrated successfully", extra_tags='appoinreq')

            return redirect('/poojaappointment')
        else:
            return render(request,"requestpooja.html",{'cid':cid,'clientappoins':clientappoins, 'poojalist':poojalist})
    except:
        return redirect('/login/')

def S_vastushastra(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        vastulist=vastu.objects.filter(IsDeleted=0)
        return render(request,"s_vastushastra.html",{'cid':cid,'vastulist':vastulist})

    except:
        return redirect('/login/')
    # return render(request,"vastushastra.html")

def s_lalkitab(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        lalkitablist=lalkitab.objects.filter(IsDeleted=0)
        return render(request,"s_lalkitab.html",{'cid':cid,'lalkitablist':lalkitablist})

    except:
        return redirect('/login/')

def s_tarrotreading(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        tarotlist=tarrot_reading.objects.filter(IsDeleted=0)
        return render(request,"s_tarot.html",{'cid':cid,'tarotlist':tarotlist})

    except:
        return redirect('/')

def s_palmreading(request):
    try:
        user=request.session['astro_id']
        cid = clientsignup.objects.get(id=user)
        palmlist=plam_reading.objects.filter(IsDeleted=0)
        return render(request,"s_palm.html",{'cid':cid,'palmlist':palmlist})

    except:
        return redirect('/')

def birthjournal(request):
    user=request.session['astro_id']
    cid = clientsignup.objects.get(id=user)
    bcity = CityMaster.objects.all()
    if request.method == 'POST':
        birthj_name=request.POST.get('birthj_name')
        print("birthj_name......",birthj_name)
        birthj_DOB=request.POST.get('birthj_DOB')
        birthj_time_of_birth=request.POST.get('birthj_time_of_birth')
        b_cityname=request.POST.get('birthj_City')
        cityid = CityMaster.objects.get(id=b_cityname)

        birth.objects.create(
            name = birthj_name,
            DOB = birthj_DOB,
            time_of_birth = birthj_time_of_birth,
            City = cityid,
            clientlog = cid,
            IsRequest='0',
            IsDeleted='0',
            )
        messages.success(request,'Request genrated successfully', extra_tags = 'birthjournal')
                
        return redirect('/birthjournal/')

    else:
         
        birthj_id = birth.objects.filter(clientlog=cid)
        print("birthj_id_____________",birthj_id)

        return render(request,"birthjournal.html",{'bcity':bcity,'birthj_id':birthj_id})
    
def KundliDosh(request):
    user=request.session['astro_id']
    cid = clientsignup.objects.get(id=user)
    kundlicity = CityMaster.objects.all()
    if request.method == 'POST':
        Kundli_name = request.POST.get('name')
        Kundli_dob = request.POST.get('DOB')
        Kundli_time = request.POST.get('time_of_birth')
        Kundli_place = request.POST.get('City')
        cityid = CityMaster.objects.get(id=Kundli_place)
   
        kundli_dosh.objects.create(
            name = Kundli_name,
            DOB = Kundli_dob,
            time_of_birth = Kundli_time,
            City = cityid,
            clientlog = cid,
            IsRequest='0',
            IsDeleted='0',
            )
        messages.success(request,'Request genrated successfully', extra_tags = 'birthjournal')
                
        return redirect('/KundliDosh/')

    else:
         
        kundli_id = kundli_dosh.objects.filter(clientlog=cid)
        print("kundli_id_____________",kundli_id)

        return render(request,"kundlidosh.html",{'kundlicity':kundlicity,'kundli_id':kundli_id})

def ManglikDosha(request):
    user=request.session['astro_id']
    cid = clientsignup.objects.get(id=user)
    mcity = CityMaster.objects.all()
    if request.method == 'POST':
        Manglik_name=request.POST.get('Manglik_name')
        Manglik_DOB=request.POST.get('Manglik_DOB')
        Manglik_time_of_birth=request.POST.get('Manglik_time_of_birth')
        m_cityname=request.POST.get('City')
        cityid = CityMaster.objects.get(id=m_cityname)

        manglik.objects.create(
            name = Manglik_name,
            DOB = Manglik_DOB,
            time_of_birth = Manglik_time_of_birth,
            City = cityid,
            clientlog = cid,
            IsRequest='0',
            IsDeleted='0',
            )
        messages.success(request,'Request genrated successfully', extra_tags = 'ManglikDosha')
                
        return redirect('/ManglikDosha/')

    else:
         
        manglik_id = manglik.objects.filter(clientlog=cid)

        return render(request,"ManglikDosha.html",{'mcity':mcity,'manglik_id':manglik_id})
    
def MakePayment(request):
    try:    
        user=request.session['astro_id']
    
        return render(request,"Makepayment.html")
    except:
        return redirect('/')
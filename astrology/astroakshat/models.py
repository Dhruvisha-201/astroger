from django.db import models

# Create your models here.


class CityMaster(models.Model):
    City_Name = models.CharField(max_length=30)


class monthmaster(models.Model):
    month_name = models.CharField(max_length=200)

    def __str__(self):
        return self.month_name
    
class clientsignup(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    phone_no = models.IntegerField()
    Email = models.EmailField()
    Country_id = models.CharField(max_length=500)
    State_id = models.CharField(max_length=500)
    City_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    Address = models.TextField()
    pincode = models.IntegerField()
    password = models.CharField(max_length=15)
    IsActive = models.IntegerField()
    IsDeleted = models.IntegerField()
    createby = models.CharField(max_length=30)
    CreatedDate = models.DateField()
    ModifiedBy = models.CharField(max_length=30)
    ModifiedDate = models.DateField()
    is_admin= models.IntegerField()

class sign(models.Model):
    sign_name = models.CharField(max_length=200)
    

    def __int__(self):
        return self.id

class Daily_Horoscope(models.Model):
    sign_id = models.ForeignKey(sign, on_delete=models.CASCADE)
    horoscope_date =models.DateField()
    horoscope_title = models.CharField(max_length=200)
    horoscope_description = models.TextField()
    IsDeleted = models.IntegerField()

class moon_sign(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    time_of_birth  = models.TimeField()
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    birth_city = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()

class create_moonsign(models.Model):
    moon_id = models.ForeignKey(moon_sign, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class kundli(models.Model):
    kundli_name = models.CharField(max_length=200)
    kundli_DOB = models.DateField()
    kundli_time_of_birth  = models.TimeField()
    kundli_City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()

class create_kundli(models.Model):
    kundli_id = models.ForeignKey(kundli, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class panchag(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=200)
    Country_id = models.CharField(max_length=200)
    State_id = models.CharField(max_length=200)
    City_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    sunrise =models.TimeField()
    sunset =models.TimeField()
    moonrise =models.TimeField()
    moonset =models.TimeField()
    month = models.ForeignKey(monthmaster, on_delete=models.CASCADE)
    tithi = models.CharField(max_length=200)
    vikram_samvat = models.CharField(max_length=200)
    samvat_shaka = models.CharField(max_length=200)
    nakshatra = models.CharField(max_length=200)
    yog = models.CharField(max_length=200)
    karan = models.CharField(max_length=200)
    IsDeleted = models.IntegerField()

class male_Horoscope_Matching(models.Model):
    m_name = models.CharField(max_length=200)
    m_DOB = models.DateField()
    m_time_of_birth  = models.TimeField()
    m_City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)

class female_Horoscope_Matching(models.Model):
    f_name = models.CharField(max_length=200)
    f_DOB = models.DateField()
    f_time_of_birth  = models.TimeField()
    f_City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)

class astro_admin(models.Model):
    astro_name = models.CharField(max_length=200)
    astrophone_no = models.IntegerField()
    astroEmail = models.EmailField()
    astrolocation = models.CharField(max_length=5000)
    IsDeleted = models.IntegerField()
    
def __str__(self):
        return self.astro_name

class astro_appointment(models.Model):
    customer_id = models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=500)
    c_Email = models.EmailField()
    c_phoneno = models.IntegerField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    reason_for_appoint = models.CharField(max_length=1000000)
    appoint_status = models.IntegerField()

    
class Daily_Articals(models.Model):
    articledate = models.DateField()
    articletitle = models.CharField(max_length=50000)
    articledescription = models.TextField()
    IsDeleted = models.IntegerField()

class astro_pooja(models.Model):
    pooja_name = models.CharField(max_length=300)

def __str__(self):
        return self.pooja_name

class book_pooja(models.Model):
    customer_id = models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    pooja_name = models.ForeignKey(astro_pooja, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=500)
    c_Email = models.EmailField()
    c_phoneno = models.IntegerField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    reason_for_appoint = models.CharField(max_length=1000000)
    book_request = models.IntegerField()

class vastu(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class birth(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    time_of_birth  = models.TimeField()
    City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()

class create_birth_journal(models.Model):
    birth_id = models.ForeignKey(birth, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class manglik(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    time_of_birth  = models.TimeField()
    City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()

class create_manglik(models.Model):
    manglik_id = models.ForeignKey(manglik, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class lalkitab(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class match_matching(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    time_of_birth  = models.TimeField()
    City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()
    
class create_match(models.Model):
    match_matching_id = models.ForeignKey(match_matching, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()
    
class kundli_dosh(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    time_of_birth  = models.TimeField()
    City = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    IsRequest = models.IntegerField()
    IsDeleted = models.IntegerField()

class create_kundli_dosh(models.Model):
    kundli_dosh_id = models.ForeignKey(kundli_dosh, on_delete=models.CASCADE)
    clientlog= models.ForeignKey(clientsignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class tarrot_reading(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()

class plam_reading(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    IsDeleted = models.IntegerField()
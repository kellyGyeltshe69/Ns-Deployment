from django.db import models

# Create your models here.
class BloodType(models.Model):
    bg_id = models.IntegerField(db_column='BG_ID', primary_key=True)  # Field name made lowercase.
    blood_group = models.TextField(db_column='Blood_Group')  # Field name made lowercase.
    def __str__(self):
        return self.blood_group
    class Meta:
        managed = False
        db_table = 'Blood_Type'


class DzongkhagList(models.Model):
    dzo_id = models.AutoField(db_column='Dzo_ID', primary_key=True)  # Field name made lowercase.
    dzongkhag = models.TextField(db_column='Dzongkhag')  # Field name made lowercase.
    def __str__(self):
        return self.dzongkhag
    class Meta:
        managed = False
        db_table = 'Dzongkhag_List'

class GewogList(models.Model):
    gewog_id = models.IntegerField(db_column='Gewog_ID', primary_key=True)  # Field name made lowercase.
    gewogs = models.CharField(db_column='Gewogs', max_length=100)  # Field name made lowercase.
    dzo_id = models.ForeignKey(DzongkhagList, models.DO_NOTHING, db_column='Dzo_ID')  # Field name made lowercase.
    def __str__(self):
        return self.gewogs
    class Meta:
        managed = False
        db_table = 'Gewog_List'


class Gender(models.Model):
    g_id = models.AutoField(db_column='G_ID', primary_key=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender')  # Field name made lowercase.
    def __str__(self):
        return self.gender
    class Meta:
        managed = False
        db_table = 'Gender'


class EmploymentStatus(models.Model):
    emp_id = models.IntegerField(db_column='Emp_ID', primary_key=True)  # Field name made lowercase.
    employment_status = models.TextField(db_column='Employment_Status')  # Field name made lowercase.
    def __str__(self):
        return self.employment_status
    class Meta:
        managed = False
        db_table = 'Employment_Status'



class QualificationLevel(models.Model):
    q_id = models.IntegerField(db_column='Q_ID', primary_key=True)  # Field name made lowercase.
    level = models.TextField(db_column='Level')  # Field name made lowercase.
    def __str__(self):
        return self.level
    class Meta:
        managed = False
        db_table = 'Qualification_Level'

class Scheme(models.Model):
    scheme_id = models.IntegerField(db_column='Scheme_ID', primary_key=True)  # Field name made lowercase.
    scheme = models.TextField(db_column='Scheme')  # Field name made lowercase.
    def __str__(self):
        return self.scheme
    class Meta:
        managed = False
        db_table = 'Scheme'

class WaterProjectStatus(models.Model):
    status_id = models.IntegerField(db_column='Status_ID', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.
    def __str__(self):
        return self.status
    class Meta:
        managed = False
        db_table = 'Water_Project_Status'

class Marital(models.Model):
    m_id = models.IntegerField(db_column='M_ID', primary_key=True)  # Field name made lowercase.
    marital = models.TextField(db_column='Marital')  # Field name made lowercase.
    def __str__(self):
        return self.marital
    class Meta:
        managed = False
        db_table = 'Marital'



class DesuupProfileDetail(models.Model):
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length= 50)  # Field name made lowercase.
    cid = models.BigIntegerField(db_column='CID', primary_key=True)  # Field name made lowercase.
    g = models.ForeignKey('Gender', models.DO_NOTHING, db_column='G_ID', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    m = models.ForeignKey('Marital', models.DO_NOTHING, db_column='M_ID', blank=True, null=True)  # Field name made lowercase.
    emp = models.ForeignKey('EmploymentStatus', models.DO_NOTHING, db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    bg = models.ForeignKey(BloodType, models.DO_NOTHING, db_column='BG_ID', blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='Mobile_No',max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_ID',max_length= 250, blank=True, null=True)  # Field name made lowercase.
    profession = models.TextField(db_column='Profession', blank=True, null=True)  # Field name made lowercase.
    q = models.ForeignKey('QualificationLevel', models.DO_NOTHING, db_column='Q_ID', blank=True, null=True)  # Field name made lowercase.
    year_of_completion = models.CharField(db_column='Year_of_Completion',max_length=50, blank=True, null=True)  # Field name made lowercase.
    present_address = models.TextField(db_column='Present_Address', blank=True, null=True)  # Field name made lowercase.
    dzo = models.ForeignKey('DzongkhagList', models.DO_NOTHING, db_column='Dzo_ID', blank=True, null=True)  # Field name made lowercase.
    gewog = models.ForeignKey('GewogList', models.DO_NOTHING, db_column='Gewog_ID', blank=True, null=True)  # Field name made lowercase.
    village = models.TextField(db_column='Village', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.cid)
    class Meta:
        managed = False
        db_table = 'Desuup_Profile_Detail'


class DeployedList(models.Model):
    deployed_id = models.AutoField(db_column='Deployed_ID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey('DesuupProfileDetail', models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    project = models.ForeignKey('WaterProjectDetail', models.DO_NOTHING, db_column='Project_ID')  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    no_of_days_served = models.IntegerField(db_column='No_of_Days_Served', blank=True, null=True)  # Field name made lowercase.
    actual_days = models.IntegerField(db_column='Actual_Days', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.cid)
      
    class Meta:
        managed = False
        db_table = 'Deployed_List'



class WaterProjectDetail(models.Model):
    project_id = models.AutoField(db_column='Project_ID', primary_key=True)  # Field name made lowercase.
    project_site = models.CharField(db_column='Project_Site', max_length=100)  # Field name made lowercase.
    gewog = models.ForeignKey(GewogList, models.DO_NOTHING, db_column='Gewog_ID', blank=True, null=True)  # Field name made lowercase.
    dzo = models.ForeignKey(DzongkhagList, models.DO_NOTHING, db_column='Dzo_ID', blank=True, null=True)  # Field name made lowercase.
    scheme = models.ForeignKey(Scheme, models.DO_NOTHING, db_column='Scheme_ID', blank=True, null=True)  # Field name made lowercase.
    tentative_launch_date = models.CharField(db_column=' Tentative_Launch_Date', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    launch_date = models.CharField(db_column='Launch_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    progress = models.CharField(db_column='Progress', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    project_duration = models.CharField(db_column='Project_Duration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expected_date_of_completion = models.CharField(db_column='Expected_Date_of_Completion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_of_completion = models.CharField(db_column='Date_of_Completion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    beneficiaries_households_field = models.CharField(db_column='Beneficiaries_Households ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    trenching_distance_field = models.CharField(db_column='Trenching_Distance ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    distribution_distance_field = models.CharField(db_column='Distribution_Distance ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    estd_budget_m_field = models.FloatField(db_column='Estd_Budget_(m)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    desuup_male_engaged = models.IntegerField(db_column='Desuup_Male_Engaged', blank=True, null=True)  # Field name made lowercase.
    desuup_female_engaged = models.IntegerField(db_column='Desuup_Female_Engaged', blank=True, null=True)  # Field name made lowercase.
    total_desuup = models.IntegerField(db_column='Total_Desuup', blank=True, null=True)  # Field name made lowercase.
    rba = models.IntegerField(db_column='RBA', blank=True, null=True)  # Field name made lowercase.
    civil = models.IntegerField(db_column='Civil', blank=True, null=True)  # Field name made lowercase.
    desuup_requirement = models.IntegerField(db_column='Desuup_Requirement', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('WaterProjectStatus', models.DO_NOTHING, db_column='Status_ID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.project_site
    class Meta:
        managed = False
        db_table = 'Water_Project_Detail'


class WaterProjectWithdralList(models.Model):
    withdral_id = models.AutoField(db_column='WIthdral_ID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(DesuupProfileDetail, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    project = models.ForeignKey(WaterProjectDetail, models.DO_NOTHING, db_column='Project_ID')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=False, null=False)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Water_Project_Withdral_List'


class SearchModel(models.Model):
    cid = models.BigIntegerField(db_column='CID', primary_key=True)  # Field name made lowercase.
    
    def __str__(self):
        return str(self.cid)
    class Meta:
        managed = False
        db_table = 'Desuup_Profile_Detail'


class WaterProjectLeaveList(models.Model):
    leave_id = models.AutoField(db_column='Leave_ID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(DesuupProfileDetail, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    project_id= models.ForeignKey(WaterProjectDetail, models.DO_NOTHING, db_column='Project_ID')  # Field name made lowercase.
    startdate = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cid)
    class Meta:
        managed = False
        db_table = 'Water_Project_Leave_List'


class ProfileModel(models.Model):
    name = models.TextField()  # Field name made lowercase.
    did = models.CharField( max_length= 50)  # Field name made lowercase.
    cid = models.BigIntegerField(primary_key=True)  # Field name made lowercase.
    g = models.ForeignKey('Gender', models.DO_NOTHING,blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(blank =True, null=True)  # Field name made lowercase.
    m = models.ForeignKey('Marital', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    emp = models.ForeignKey('EmploymentStatus', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    bg = models.ForeignKey(BloodType, models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(max_length= 250, blank=True, null=True)  # Field name made lowercase.
    profession = models.TextField( blank=True, null=True)  # Field name made lowercase.
    q = models.ForeignKey('QualificationLevel', models.DO_NOTHING,blank=True, null=True)  # Field name made lowercase.
    year_of_completion = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    present_address = models.TextField(blank=True, null=True)  # Field name made lowercase.
    dzo = models.ForeignKey('DzongkhagList', models.DO_NOTHING,blank=True, null=True)  # Field name made lowercase.
    gewog = models.ForeignKey('GewogList', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    village = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def _str_(self):
        return str(self.cid)
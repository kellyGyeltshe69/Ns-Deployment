from django.forms import ModelForm
from django import forms
from.import models
from django.contrib.admin import widgets
from .models import GewogList
from django.forms.widgets import DateInput


class GewogForm(ModelForm):
    class Meta:
        model = GewogList
        fields = ['gewogs', 'dzo_id',]
        labels = {
         'gewogs':'Gewog',
         'dzo_id':'Dzongkhag',
        }

    def __init__(self, *args,** kwargs):
            super(GewogForm,self).__init__(*args,** kwargs)
            self.fields['dzo_id'].empty_label = "Select Dzongkhang"

from.models import DeployedList
class DeployForm(forms.ModelForm):
    class Meta:
        model = DeployedList
        fields = ['cid','project','start_date','end_date','no_of_days_served','actual_days']
        labels = {
         'cid':'Cid',
         'project':'Project Site',
         'start_date':'Start Date',
         'end_date':'End date',
         'no_of_days_served':'No of days Served',
         'actual_days':'Actual Days of Project',
        }
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args,** kwargs):
        super(DeployForm,self).__init__(*args,** kwargs)
        self.fields['cid'].empty_label = "Select CID"
        self.fields['project'].empty_label = "Select Project Site"


from.models import WaterProjectWithdralList
class WithdrawForm(forms.ModelForm):
    class Meta:
        model = WaterProjectWithdralList
        fields = ['cid','project','date','remarks']
        labels = {
         'cid':'Cid',
         'project':'Project Site',
         'date':'Date',
         'remarks':'Remarks'
        }
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args,** kwargs):
        super(WithdrawForm,self).__init__(*args,** kwargs)
        self.fields['cid'].empty_label = "Select"
        self.fields['project'].empty_label = "Select"

from.models import WaterProjectLeaveList
class LeaveForm(forms.ModelForm):
    class Meta:
        model = WaterProjectLeaveList
        fields = ['cid','project_id','startdate','enddate','remarks']
        labels = {
         'cid':'Cid',
         'project_id':'Project Site',
         'startdate':'Start Date',
         'enddate':'End date',
         'remarks':'Remarks'
        }
        widgets = {
            'startdate': DateInput(attrs={'type': 'date'}),
            'enddate': DateInput(attrs={'type': 'date'}),

        }
    def __init__(self, *args,** kwargs):
        super(LeaveForm,self).__init__(*args,** kwargs)
        self.fields['cid'].empty_label = "Select"
        self.fields['project_id'].empty_label = "Select"


from.models import WaterProjectDetail
class ProjectForm(forms.ModelForm):
    class Meta:
        model = WaterProjectDetail
        fields = ['project_site','gewog','dzo','scheme','tentative_launch_date',
              'launch_date','progress','project_duration','expected_date_of_completion','date_of_completion',
              'beneficiaries_households_field','trenching_distance_field','distribution_distance_field','estd_budget_m_field',
              'desuup_male_engaged','desuup_female_engaged','total_desuup','rba','civil','desuup_requirement','status',
              'remarks']
        labels = {
         'project_site':'Project Site',
         'gewog':'Gewog',
         'dzo':'Dzongkhag',
         'scheme':'Scheme',
         'tentative_launch_date':'Tentative Launch Date',
         'launch_date':'Launch Date',
         'progress':'Progress',
         'project_duration':'Project Duration',
         'expected_date_of_completion':'Expected Date of completion',
         'date_of_completion':'Date of Completion',
         'beneficiaries_households_field':'Beneficiaries Households',
         'trenching_distance_field':'Trenching Distance',
         'distribution_distance_field':'Distribution Distance',
         'estd_budget_m_field':'Estd. Budget(m)',
         'desuup_male_engaged':'Desuup Male Engaged',
         'desuup_female_engaged':'Desuup Female Engaged',
         'total_desuup':'Total Desuup',
         'rba':'RBA',
         'civil':'Civil',
         'desuup_requirement':'Desuup Requirement',
         'status':'Status',
         'remarks':'Remarks'
        }
        widgets = {
            'launch_date': DateInput(attrs={'type': 'date'}),
            'tentative_launch_date': DateInput(attrs={'type': 'date'}),
            'expected_date_of_completion': DateInput(attrs={'type': 'date'}),
            'date_of_completion': DateInput(attrs={'type': 'date'}),

        }
    def __init__(self, *args,** kwargs):
        super(ProjectForm,self).__init__(*args,** kwargs)
        self.fields['gewog'].empty_label = "Select"
        self.fields['dzo'].empty_label = "Select Dzongkhag"
        self.fields['scheme'].empty_label = "Select Scheme"
        self.fields['status'].empty_label = "Select Status"

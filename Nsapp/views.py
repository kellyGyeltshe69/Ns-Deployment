from math import remainder
from django.shortcuts import render, redirect
from django.contrib import messages
from.import forms
from django.db.models import Sum, Avg, Count, Q, Max, F, ExpressionWrapper
from datetime import datetime, date
from django.utils import timezone
from django.db.models.functions import ExtractYear
from itertools import groupby
from operator import itemgetter

# Create your views here.

from .models import BloodType
def blood(request):
    bloods = BloodType.objects.all
    return render(request, 'blood.html', {'all_types':bloods})


def base(request):
    return render(request, 'base.html',{})


# views and crude for Gender
from .models import Gender
def gender(request):
    genders = Gender.objects.all
    return render(request, 'gender.html', {'all_gender':genders})

def addgender(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        genders = Gender(
                gender = gender
        )
        genders.save()
        return redirect('gender')
    return render(request, 'gender.html')

def editgender(request):
    gender = Gender.objects.all()
    context = {
        'gender':gender
    }
    return redirect(request, 'gender.html', context)

def updategender(request,g_id):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        genders = Gender(
                g_id = g_id,
                gender = gender,
        )
        genders.save()
        return redirect('gender')
    return redirect(request, 'gender.html')

def deletegender(request, g_id):
    genders = Gender.objects.filter(g_id = g_id)
    genders.delete()
    context = {
        'gender':gender,
    }
    return redirect('gender')

# crud for Employment_Status
from .models import EmploymentStatus
def employment(request):
    employments = EmploymentStatus.objects.all
    return render(request, 'employment.html', {'all_employment':employments})

def addemployment(request):
    if request.method == 'POST':
        employment_status = request.POST.get('employment_status')

        employments = EmploymentStatus(

                employment_status = employment_status,
        )

        employments.save()
        return redirect('employment')

    return render(request, 'employment.html')

def editemployment(request):
    employments = EmploymentStatus.objects.all()

    context = {
        'employments':employments,
    }
    return redirect(request, 'employment.html', context)

def updateemployment(request,emp_id):
    if request.method == 'POST':
        employment_status = request.POST.get('employment_status')
        employments = EmploymentStatus(
                emp_id = emp_id,
                employment_status = employment_status,
        )

        employments.save()
        return redirect('employment')

    return redirect(request, 'employment.html')

def deleteemployment(request, emp_id):
    employments = EmploymentStatus.objects.filter(emp_id = emp_id)
    employments.delete()

    context = {
        'employments':employments,
    }

    return redirect('employment')


# crud for QualificationLevel
from .models import QualificationLevel
def qualification(request):
    qualifications = QualificationLevel.objects.all
    return render(request, 'qualification.html', {'qualifications':qualifications})

def addqualification(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        qualifications = QualificationLevel(
                level = level,
        )
        qualifications.save()
        return redirect('qualification')
    return render(request, 'qualification.html')

def editqualification(request):
    qualifications = QualificationLevel.objects.all()
    context = {'qualifications':qualifications}
    return redirect(request, 'qualification.html', context)

def updatequalification(request,q_id):
    if request.method == 'POST':
        level = request.POST.get('level')
        qualifications = QualificationLevel(
                q_id = q_id,
                level = level,
        )
        qualifications.save()
        return redirect('qualification')
    return redirect(request, 'qualification.html')

def deletequalification(request, q_id):
    qualifications = QualificationLevel.objects.filter(q_id = q_id)
    qualifications.delete()
    context = {
        'qualifications':qualifications,
    }
    return redirect('qualification')


# Display and crud for scheme
from .models import Scheme
def scheme(request):
    schemes = Scheme.objects.all
    return render(request, 'scheme.html', {'all_scheme':schemes})

def addscheme(request):
    if request.method == 'POST':
        scheme = request.POST.get('scheme')
        schemes = Scheme(
                scheme = scheme,
        )
        schemes.save()
        return redirect('scheme')
    return render(request, 'scheme.html')

def editscheme(request):
    schemes = Scheme.objects.all()
    context = {
        'schemes':schemes
    }
    return redirect(request, 'scheme.html', context)

def updatescheme(request,scheme_id):
    if request.method == 'POST':
        scheme = request.POST.get('scheme')
        schemes = Scheme(
                scheme_id = scheme_id,
                scheme = scheme,
        )
        schemes.save()
        return redirect('scheme')
    return redirect(request, 'scheme.html')

def deletescheme(request, scheme_id):
    schemes = Scheme.objects.filter(scheme_id = scheme_id)
    schemes.delete()

    context = {
        'schemes':schemes,
    }

    return redirect('scheme')


from .models import WaterProjectStatus
def waterprojectstatus(request):
    waterprojectstatus = WaterProjectStatus.objects.all
    return render(request, 'waterprojectstatus.html',{'all_waterprojectstatus':waterprojectstatus})

from .models import Marital
def marital_type(request):
    maritals = Marital.objects.all
    return render(request, 'marital.html', {'all_marital':maritals})

from .models import DesuupProfileDetail
def desuupprofiledetail(request):
    desuupprofiledetails = DesuupProfileDetail.objects.all
    return render(request, 'desuupprofiledetails.html', {'all_desuupprofiledetail':desuupprofiledetails})


# from .models import DeployedList
# def deployedlist(request):
#     deployedlists = DeployedList.objects.all
#     return render(request, 'deployedlist.html', {'all_deployedlists':deployedlists})

from .models import WaterProjectDetail
def waterprojectdetail(request):
    waterprojectdetails = WaterProjectDetail.objects.all
    return render(request, 'waterprojectdetail.html', {'all_waterprojectdetail':waterprojectdetails})


from .models import WaterProjectWithdralList
def withdraw(request):
    withdraws = WaterProjectWithdralList.objects.all
    return render(request, 'withdrawlist.html', {'all_withdraws':withdraws})

from .models import DzongkhagList
def dzongkhag(request):
    dzongkhags = DzongkhagList.objects.all
    return render(request, 'dzongkhag.html', {'all_dzongkhag':dzongkhags})


def ADD(request):
    if request.method == 'POST':
        dzongkhag = request.POST.get('dzongkhag')

        dzongkhags = DzongkhagList(

                dzongkhag = dzongkhag,
        )

        dzongkhags.save()
        return redirect('dzongkhag')

    return render(request, 'dzongkhag.html')


def Edit(request):
    dzongkhag = DzongkhagList.objects.all()

    context = {
        'dzongkhag':dzongkhag
    }
    return redirect(request, 'dzongkhag.html', context)

def Update(request,dzo_id):
    if request.method == 'POST':
        dzongkhag = request.POST.get('dzongkhag')
        dzongkhags = DzongkhagList(
                dzo_id = dzo_id,
                dzongkhag = dzongkhag,
        )

        dzongkhags.save()
        return redirect('dzongkhag')

    return redirect(request, 'dzongkhag.html')

def Delete(request, dzo_id):
    dzongkhags = DzongkhagList.objects.filter(dzo_id = dzo_id)
    dzongkhags.delete()

    context = {
        'dzongkhags':dzongkhags,
    }

    return redirect('dzongkhag')


#     # views for creating forms
# from .forms import DeployedForm
# def deployedform(request):
#     if request.method == "POST":
#         deployedform = DeployedForm(request.POST or None)
#         if deployedform.is_valid():
#             add_deployed = deployedform.save(commit=False)
#             add_deployed.save()
#         else:
#             # messages.success(request, (" There Was An Error, Please Try Again! "))
#             return render(request, "deployedform.html", {'deployedforms':deployedform})
#         messages.success(request, "Your DeployedForm Has Been Successfully Save!")
#         return redirect("deployedlist")
#     else:
#         deployedform = DeployedForm()
#     return render(request, "deployedform.html", {'deployedforms':deployedform})

from .models import SearchModel
def searchmodel(request):
    searchmodels = SearchModel.objects.all
    return render(request, 'search.html', {'searchmodels':searchmodels})

# from django.http import HttpResponse
# def Addcid(request):
#     if request.method == 'POST':
#         cid = request.POST.getlist('selectedcid')
#         # print(cid)
#         # cid = SearchModel(

#         #         cid = cid,
#         # )
#         return render(request, 'search.html', {'cid':cid})

   
def overallsummary(request):
    return render(request, 'overallsummary.html',{})

def projectsummary(request):
    details = WaterProjectDetail.objects.all().values('project_site','desuup_male_engaged','desuup_female_engaged','total_desuup','estd_budget_m_field')
    return render(request, 'projectsummary.html',{'details':details})

def dashboard(request):
    male = DeployedList.objects.distinct('cid').filter(cid__g=1)
    totalmale = male.count()
    female = DeployedList.objects.distinct('cid').filter(cid__g=2)
    totalfemale = female.count()
    total = totalmale + totalfemale
    drinkingcompleted = WaterProjectDetail.objects.filter(status=3,scheme=1)
    y = drinkingcompleted.count()
    irrigationcompleted = WaterProjectDetail.objects.filter(status=3,scheme=2)
    x = irrigationcompleted.count()
    integratedcompleted = WaterProjectDetail.objects.filter(status=3,scheme=3)
    z = integratedcompleted.count()
    completed = x+y+z

    drinkingongoing = WaterProjectDetail.objects.filter(status=1,scheme=1)
    a = drinkingongoing.count()
    irrigationongoing = WaterProjectDetail.objects.filter(status=1,scheme=2)
    b = irrigationongoing.count()
    integratedongoing = WaterProjectDetail.objects.filter(status=1,scheme=3)
    c = integratedongoing.count()
    ongoing = a+b+c

    drinkingupcoming = WaterProjectDetail.objects.filter(status=2,scheme=1)
    d = drinkingupcoming.count()
    irrigationupcoming = WaterProjectDetail.objects.filter(status=2,scheme=2)
    e = irrigationupcoming.count()
    integratedupcoming = WaterProjectDetail.objects.filter(status=2,scheme=3)
    f = integratedupcoming.count()
    upcoming = d+e+f

    drinkingunexecuted = WaterProjectDetail.objects.filter(status=4,scheme=1)
    g = drinkingunexecuted.count()
    irrigationunexecuted = WaterProjectDetail.objects.filter(status=4,scheme=2)
    h = irrigationunexecuted.count()
    integratedunexecuted = WaterProjectDetail.objects.filter(status=4,scheme=3)
    i = integratedunexecuted.count()
    unexecuted = g+h+i

    totalproject = unexecuted + upcoming + ongoing + completed
    context={'totalmale':totalmale,'totalfemale':totalfemale,'total':total,'x':x,'y':y,'completed':completed,'z':z,'a':a,'b':b,'c':c,'ongoing':ongoing,'d':d,'e':e,'upcoming':upcoming,
    'f':f,'unexecuted':unexecuted,'g':g,'h':h,'i':i,'totalproject':totalproject}
    return render(request, 'dashboard.html',context)

from .models import ProfileModel
def profile(request):
    profiles = ProfileModel.objects.all
    return render(request, 'profile.html',{'profiles':profiles})


def ViewAll(request):
    profiles = ProfileModel.objects.all
    return render(request, 'viewall.html',{'profiles':profiles})


def viewDetails(request):
    profiles = ProfileModel.objects.all()
    context = {
        'profiles':profiles
    }
    return redirect(request, 'profile.html', context)

def viewDetailsView(request,cid):
    if request.method == 'POST':
        cid = request.POST.get('cid')
        name = request.POST.get('name')
        did = request.POST.get('did')
        profiles = ProfileModel(
                cid = cid,
                name = name,
        )
        # return redirect('scheme')
    return redirect(request, 'profile.html')


# views and crud for Gewogs
from .models import GewogList
def gewog(request):
    gewogs = GewogList.objects.all()
    return render(request, 'gewog.html', {'gewogs':gewogs})

from .forms import GewogForm
def gewogform(request,gewog_id =0):
    if request.method == "GET":
        gewogforms = GewogForm()
        return render(request,'gewogform.html',{'gewogforms':gewogforms})
    else:
        gewogforms= GewogForm(request.POST,)
        if gewogforms.is_valid():
            gewogforms.save()
        return redirect('gewog')

def updategewog(request,gewog_id=None):
    instance = GewogList.objects.get(gewog_id=gewog_id)
    gewogforms = GewogForm(request.POST or None,instance=instance)
    if gewogforms.is_valid():
        instance = gewogforms.save(commit=False)
        instance.save()
        return redirect('gewog')
    context = {"gewogforms":gewogforms}
    return render(request,'gewogform.html',context)

def deletegewog(request,gewog_id):
    gewogs = GewogList.objects.filter(gewog_id=gewog_id)
    gewogs.delete()
    return redirect('gewog')

# views and crud for blood
from .models import BloodType
def blood(request):
    bloods =  BloodType.objects.all()
    context = {'bloods':bloods}
    return render(request, 'blood.html', context)

def addblood(request):
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        bloods = BloodType(
                blood_group = blood_group,
        )
        bloods.save()
        return redirect('blood')
    return render(request, 'blood.html')
def editblood(request):
    bloods = BloodType.objects.all()
    context = {
        'bloods':bloods
    }
    return redirect(request, 'blood.html', context)

def updateblood(request, bg_id):
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        bloods = BloodType(
                bg_id = bg_id,
                blood_group = blood_group,
        )
        bloods.save()
        return redirect('blood')
    return redirect(request, 'blood.html', context)

def deleteblood(request, bg_id):
    bloods = BloodType.objects.filter(bg_id = bg_id)
    bloods.delete()
    context = {
        'bloods':bloods,
    }
    return redirect('blood')


    # views and crud for Marital
from .models import Marital
def marital_type(request):
    maritals = Marital.objects.all
    return render(request, 'marital.html', {'maritals':maritals})

def addmarital_type(request):
    if request.method == 'POST':
        marital = request.POST.get('marital')
        maritals = Marital(
                marital = marital,
        )
        maritals.save()
        return redirect('marital_type')
    return render(request, 'marital.html')

def editmarital_type(request):
    maritals = Marital.objects.all()
    context = {
        'maritals':maritals
    }
    return redirect(request, 'marital.html', context)

def updatemarital_type(request,m_id):
    if request.method == 'POST':
        marital = request.POST.get('marital')
        maritals = Marital(
                m_id = m_id,
                marital = marital,
        )
        maritals.save()
        return redirect('marital_type')
    return redirect(request, 'marital.html')

def deletemarital_type(request, m_id):
    maritals = Marital.objects.filter(m_id = m_id)
    maritals.delete()
    context = {
        'maritals':maritals,
    }
    return redirect('marital_type',context)


    #crud for Waterproject status
from .models import WaterProjectStatus
def waterprojectstatus(request):
    waterprojectstatus = WaterProjectStatus.objects.all
    return render(request, 'waterprojectstatus.html',{'all_waterprojectstatus':waterprojectstatus})

def addstatus(request):
    if request.method == 'POST':
        status = request.POST.get('status')

        status = WaterProjectStatus(

                status = status,
        )

        status.save()
        return redirect('waterprojectstatus')

    return render(request, 'waterprojectstatus.html')

def editstatus(request):
    status = WaterProjectStatus.objects.all()

    context = {
        'status':status
    }
    return redirect(request, 'waterprojectstatus.html', context)

def updatestatus(request,status_id):
    if request.method == 'POST':
        status = request.POST.get('status')
        status = WaterProjectStatus(
                status_id = status_id,
                status = status,
        )

        status.save()
        return redirect('waterprojectstatus')

    return redirect(request, 'waterprojectstatus.html')

def deletestatus(request, status_id):
    status = WaterProjectStatus.objects.filter(status_id = status_id)
    status.delete()

    context = {
        'status':status,
    }

    return redirect('waterprojectstatus')

# crud for Deployed list
from .models import DeployedList
def deploy(request):
    deploys = DeployedList.objects.all()
    return render(request, 'deployedlist.html', {'deploys':deploys})

from .forms import DeployForm
def deployform(request,deployed_id=0):
    if request.method == "GET":
        deployforms = DeployForm()
        return render(request,'deployform.html',{'deployforms':deployforms})
    else:
        deployforms= DeployForm(request.POST,)
        if deployforms.is_valid():
            deployforms.save()
        return redirect('deploy')

def updatedeploy(request,deployed_id=None):
    instance = DeployedList.objects.get(deployed_id=deployed_id)
    deployforms = DeployForm(request.POST or None,instance=instance)
    if deployforms.is_valid():
        instance = deployforms.save(commit=False)
        instance.save()
        return redirect('deploy')
    context = {"deployforms":deployforms}
    return render(request,'deployform.html',context)

def deletedeploy(request,deployed_id):
    deployforms = DeployedList.objects.filter(deployed_id=deployed_id)
    deployforms.delete()
    return redirect('deploy')


# crud for withdrawlist
from .models import WaterProjectWithdralList
def withdraw(request):
    withdraws = WaterProjectWithdralList.objects.all
    return render(request, 'withdrawlist.html', {'withdraws':withdraws})

from .forms import WithdrawForm
def withdrawform(request,withdral_id =0):
    if request.method == "GET":
        withdrawforms = WithdrawForm()
        return render(request,'withdrawform.html',{'withdrawforms':withdrawforms})
    else:
        withdrawforms= WithdrawForm(request.POST,)
        if withdrawforms.is_valid():
            withdrawforms.save()
        return redirect('withdraw')

def updatewithdraw(request,withdral_id=None):
    instance = WaterProjectWithdralList.objects.get(withdral_id=withdral_id)
    withdrawforms = WithdrawForm(request.POST or None,instance=instance)
    if withdrawforms.is_valid():
        instance = withdrawforms.save(commit=False)
        instance.save()
        return redirect('withdraw')
    context = {"withdrawforms":withdrawforms}
    return render(request,'withdrawform.html',context)

def deletewithdraw(request,withdral_id):
    withdraws = WaterProjectWithdralList.objects.filter(withdral_id=withdral_id)
    withdraws.delete()
    return redirect('withdraw')


# crud for leave Records
from .models import WaterProjectLeaveList
def leave(request):
    leaves = WaterProjectLeaveList.objects.all()
    return render(request, 'leave.html', {'leaves':leaves})

from .forms import LeaveForm
def leaveform(request,leave_id =0):
    if request.method == "GET":
        leaveforms = LeaveForm()
        return render(request,'leaveform.html',{'leaveforms':leaveforms})
    else:
        leaveforms= LeaveForm(request.POST,)
        if leaveforms.is_valid():
            leaveforms.save()
        return redirect('leave')

def updateleaveform(request,leave_id=None):
    instance = WaterProjectLeaveList.objects.get(leave_id=leave_id)
    leaveforms = LeaveForm(request.POST or None,instance=instance)
    if leaveforms.is_valid():
        instance = leaveforms.save(commit=False)
        instance.save()
        return redirect('leave')
    context = {"leaveforms":leaveforms}
    return render(request,'leaveform.html',context)

def deleteleaveform(request,leave_id):
    leaves = WaterProjectLeaveList.objects.filter(leave_id=leave_id)
    leaves.delete()
    return redirect('leave')


    # crud for waterproject Detail
from .models import WaterProjectDetail
def waterprojectdetail(request):
    waterprojectdetails = WaterProjectDetail.objects.all
    return render(request, 'waterprojectdetail.html', {'waterprojectdetails':waterprojectdetails})

from .forms import ProjectForm
def projectform(request,project_id =0):
    if request.method == "GET":
        projectforms = ProjectForm()
        return render(request,'waterprojectform.html',{'projectforms':projectforms})
    else:
        projectforms= ProjectForm(request.POST,)
        if projectforms.is_valid():
            projectforms.save()
        return redirect('waterprojectdetail')

def updatewaterprojectdetail(request,project_id=None):
    instance = WaterProjectDetail.objects.get(project_id=project_id)
    projectforms = ProjectForm(request.POST or None,instance=instance)
    if projectforms.is_valid():
        instance = projectforms.save(commit=False)
        instance.save()
        return redirect('waterprojectdetail')
    context = {"projectforms":projectforms}
    return render(request,'waterprojectform.html',context)

def deletewaterprojectdetail(request,project_id):
    waterprojectdetails = WaterProjectDetail.objects.filter(project_id=project_id)
    waterprojectdetails.delete()
    return redirect('waterprojectdetail')

# Overallsummary Report
def overallsummary(request):
    male = WaterProjectDetail.objects.filter(status=1).aggregate(Male=Sum('desuup_male_engaged'))
    male = str(male)[1:-1]
    female = WaterProjectDetail.objects.filter(status=1).aggregate(Female=Sum('desuup_female_engaged'))
    female = str(female)[1:-1]
    malefemale = WaterProjectDetail.objects.filter(status=1).aggregate( Total =Sum('total_desuup'))
    malefemale = str(malefemale)[1:-1]

    # Queryset for estinated budget with complted updatewaterprojectdetail
    expenditure = WaterProjectDetail.objects.filter(status=3).aggregate(Budget=Sum('estd_budget_m_field'))
    totalexpenditure = str(expenditure)[1:-1]
    # Queryset for Qualification
    master = DeployedList.objects.distinct('cid').filter(cid__q=1)
    masterlevel = master.count()
    degree = DeployedList.objects.distinct('cid').filter(cid__q=2)
    degreelevel = degree.count()
    diploma = DeployedList.objects.distinct('cid').filter(cid__q=3)
    diplomalevel = diploma.count()
    classxii = DeployedList.objects.distinct('cid').filter(cid__q=4)
    classxiilevel = classxii.count()
    classx = DeployedList.objects.distinct('cid').filter(cid__q=5)
    classxlevel = classx.count()
    monk = DeployedList.objects.distinct('cid').filter(cid__q=8)
    monklevel = monk.count()
    other = DeployedList.objects.distinct('cid').filter(cid__q=6)
    otherlevel = other.count()
    doctoral = DeployedList.objects.distinct('cid').filter(cid__q=7)
    doctorallevel = doctoral.count()

    # Query set for Maximum, Minimum, And Average Age
    current_year = timezone.now().year
    x = DeployedList.objects.values('cid__name','cid').annotate(Age=(current_year - ExtractYear('cid__dob')))
    max_age = max(x, key=lambda x:x['Age'])
    maximumage = str(max_age)[1:-1]
    min_age = min(x, key=lambda x:x['Age'])
    minimumage = str(min_age)[1:-1]
    AverageAge = DeployedList.objects.values('cid').aggregate(Average=Avg(current_year - ExtractYear('cid__dob')))
    AverageAge = str(AverageAge)[1:-1]

    # highest served desuup
    highestserved = DeployedList.objects.all().values('cid','cid__name').annotate(TotalDays=Sum('no_of_days_served'))
    max_days = max(highestserved, key=lambda x:x['TotalDays'])
    highest = str(max_days)[1:-1]

    context={
    'female':female,'male':male,'malefemale':malefemale,'masterlevel':masterlevel,'degreelevel':degreelevel,
    'diplomalevel':diplomalevel,'classxiilevel':classxiilevel,'classxlevel':classxlevel,'otherlevel':otherlevel,
    'monklevel':monklevel,'doctorallevel':doctorallevel,'highest':highest,'totalexpenditure':totalexpenditure,
    'maximumage':maximumage, 'minimumage': minimumage, 'AverageAge':AverageAge
    }
    return render(request, 'overallsummary.html',context)

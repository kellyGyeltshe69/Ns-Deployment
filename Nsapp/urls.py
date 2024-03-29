from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('base/', views.base, name = "base"),
    path('blood/', views.blood, name = "blood"),
    path('addblood/', views.addblood, name = "addblood"),
    path('editblood/', views.editblood, name = "editblood"),
    path('updateblood/<str:bg_id>',views.updateblood, name='updateblood'),
    path('deleteblood/<str:bg_id>',views.deleteblood, name='deleteblood'),
    path('dzongkhag/', views.dzongkhag, name = "dzongkhag"),
    path('add', views.ADD, name='add'),
    path('edit',views.Edit, name='edit'),
    path('update/<str:dzo_id>',views.Update, name='update'),
    path('delete/<str:dzo_id>',views.Delete, name='delete'),
    path('desuupprofiledetail/', views.desuupprofiledetail, name = "desuupprofiledetail"),
    path('withdraw/', views.withdraw, name = "withdraw"),
    path('searchmodel/', views.searchmodel, name = "searchmodel"),
    # path('addacid', views.Addcid, name='add'),
    path('overallsummary/', views.overallsummary, name = "overallsummary"),
    path('projectsummary/', views.projectsummary, name = "projectsummary"),
    path('', views.dashboard, name = "dashboard"),
    path('profile/', views.profile, name = "profile"),
    path('ViewAll/', views.ViewAll, name = "ViewAll"),
    path('gewog/', views.gewog, name = "gewog"),
    path('gewogform/', views.gewogform, name = "gewogform"),
    path('updategewog/<str:gewog_id>', views.updategewog, name = "updategewog"),
    path('deletegewog/<str:gewog_id>',views.deletegewog, name='deletegewog'),
    path('employment/', views.employment, name = "employment"),
    path('addemployment/', views.addemployment, name = "addemployment"),
    path('editemployment/', views.editemployment, name = "editemployment"),
    path('updateemployment/<str:emp_id>', views.updateemployment, name = "updateemployment"),
    path('deleteemployment/<str:emp_id>', views.deleteemployment, name = "deleteemployment "),
    path('qualification/', views.qualification, name = "qualification"),
    path('addqualification/', views.addqualification, name = "addqualification"),
    path('editqualification/', views.editqualification, name = "editqualification"),
    path('updatequalification/<str:q_id>', views.updatequalification, name = "updatequalification"),
    path('deletequalification/<str:q_id>',views.deletequalification, name='deletequalification'),
    path('scheme/', views.scheme, name = "scheme"),
    path('addscheme/', views.addscheme, name = "addscheme"),
    path('editscheme/', views.editscheme, name = "editscheme"),
    path('updatescheme/<str:scheme_id>', views.updatescheme, name = "updatescheme"),
    path('deletescheme/<str:scheme_id>', views.deletescheme, name = "deletescheme"),
    path('gender/', views.gender, name = "gender"),
    path('addgender/', views.addgender, name = "addgender"),
    path('editgender',views.editgender, name='editgender'),
    path('updategender/<str:g_id>',views.updategender, name='updategender'),
    path('deletegender/<str:g_id>',views.deletegender, name='deletegender'),
    path('marital_type/', views.marital_type, name = "marital_type"),
    path('addmarital_type/', views.addmarital_type, name = "addmarital_type"),
    path('editmarital_type/', views.editmarital_type, name = "editmarital_type"),
    path('updatemarital_type/<str:m_id>', views.updatemarital_type, name = "updatemarital_type"),
    path('deletemarital_type/<str:m_id>',views.deletemarital_type, name='deletemarital_type'),
    path('waterprojectstatus/', views.waterprojectstatus, name = "waterprojectstatus"),
    path('addstatus/', views.addstatus, name = "addstatus"),
    path('editstatus/', views.editstatus, name = "editstatus"),
    path('updatestatus/<str:status_id>', views.updatestatus, name = "updatestatus"),
    path('deletestatus/<str:status_id>', views.deletestatus, name = "deletestatus"),
    path('deploy/', views.deploy, name = "deploy"),
    path('deployform/', views.deployform, name = "deployform"),
    path('updatedeploy/<str:deployed_id>', views.updatedeploy, name = "updatedeploy"),
    path('deletedeploy/<str:deployed_id>', views.deletedeploy, name = "deletedeploy"),
    path('withdraw/', views.withdraw, name = "withdraw"),
    path('withdrawform/', views.withdrawform, name = "withdrawform"),
    path('updatewithdraw/<str:withdral_id>', views.updatewithdraw, name = "updatewithdraw"),
    path('deletewithdraw/<str:withdral_id>', views.deletewithdraw, name = "deletewithdraw"),
    path('leave/', views.leave, name = "leave"),
    path('leaveform/', views.leaveform, name = "leaveform"),
    path('updateleaveform/<str:leave_id>', views.updateleaveform, name = "updateleaveform"),
    path('deleteleaveform/<str:leave_id>', views.deleteleaveform, name = "deleteleaveform"),
    path('waterprojectdetail/', views.waterprojectdetail, name = "waterprojectdetail"),
    path('projectform/', views.projectform, name = "projectform"),
    path('updatewaterprojectdetail/<str:project_id>', views.updatewaterprojectdetail, name = "updatewaterprojectdetail"),
    path('deletewaterprojectdetail/<str:project_id>', views.deletewaterprojectdetail, name = "deletewaterprojectdetail"),
    path('viewDetails/', views.viewDetails, name = "viewDetails"),




    # path('showlist/', views.showlist, name='showlist'),


]

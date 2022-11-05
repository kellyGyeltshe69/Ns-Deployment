from django.contrib import admin

# Register your models here.

from .models import BloodType
admin.site.register(BloodType)

from .models import DzongkhagList
admin.site.register(DzongkhagList)


from .models import GewogList
admin.site.register(GewogList)


from .models import Gender
admin.site.register(Gender)

from .models import EmploymentStatus
admin.site.register(EmploymentStatus)

from .models import QualificationLevel
admin.site.register(QualificationLevel)

from .models import Scheme
admin.site.register(Scheme)

from .models import WaterProjectStatus
admin.site.register(WaterProjectStatus)

from .models import DesuupProfileDetail
admin.site.register(DesuupProfileDetail)

from .models import Marital
admin.site.register(Marital)

from .models import DeployedList
admin.site.register(DeployedList)

from .models import WaterProjectDetail
admin.site.register(WaterProjectDetail)

from .models import WaterProjectWithdralList
admin.site.register(WaterProjectWithdralList)

from .models import SearchModel
admin.site.register(SearchModel)

from .models import ProfileModel
admin.site.register(ProfileModel)


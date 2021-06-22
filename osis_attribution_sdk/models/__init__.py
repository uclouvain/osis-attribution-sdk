# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_attribution_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_attribution_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_attribution_sdk.model.application import Application
from osis_attribution_sdk.model.application_course_calendar import ApplicationCourseCalendar
from osis_attribution_sdk.model.application_create_command import ApplicationCreateCommand
from osis_attribution_sdk.model.application_list import ApplicationList
from osis_attribution_sdk.model.application_update_command import ApplicationUpdateCommand
from osis_attribution_sdk.model.attribution import Attribution
from osis_attribution_sdk.model.attribution_about_to_expire import AttributionAboutToExpire
from osis_attribution_sdk.model.attribution_about_to_expire_list import AttributionAboutToExpireList
from osis_attribution_sdk.model.attribution_function_enum import AttributionFunctionEnum
from osis_attribution_sdk.model.attribution_links import AttributionLinks
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.learning_unit_type_enum import LearningUnitTypeEnum
from osis_attribution_sdk.model.my_charge_summary import MyChargeSummary
from osis_attribution_sdk.model.my_charge_summary_list import MyChargeSummaryList
from osis_attribution_sdk.model.renew_attribution_about_to_expire_command import RenewAttributionAboutToExpireCommand
from osis_attribution_sdk.model.tutor_attribution import TutorAttribution
from osis_attribution_sdk.model.vacant_course import VacantCourse
from osis_attribution_sdk.model.vacant_course_list import VacantCourseList
from osis_attribution_sdk.model.vacant_declaration_type_enum import VacantDeclarationTypeEnum

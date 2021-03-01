# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_attribution_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_attribution_sdk.model.application_course_calendar import ApplicationCourseCalendar
from osis_attribution_sdk.model.attribution import Attribution
from osis_attribution_sdk.model.attribution_function_enum import AttributionFunctionEnum
from osis_attribution_sdk.model.attribution_links import AttributionLinks
from osis_attribution_sdk.model.error import Error

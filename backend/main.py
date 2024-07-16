
from backend.bundle_builder import combine_bundle_js
from backend.schedule_fetcher import *
from backend.utils import fetch_kst_datetime


# build schedule json file
today = fetch_kst_datetime()
interpark_schedules = fetch_schedule_from_interpark(today)
print(interpark_schedules)

# write_schedule_in_json(my_schedules)
#
# # build bundle.js file
# combine_bundle_js()

from datetime import datetime

from backend.bundle_builder import combine_bundle_js
from backend.schedule_json_builder import *

# build schedule json file
today = datetime.now().strftime("%Y%m%d")
interpark_schedules = fetch_schedule_from_interpark(today)

my_schedules = parse_schedule(interpark_schedules)
write_schedule_in_json(my_schedules)

# build bundle.js file
combine_bundle_js()

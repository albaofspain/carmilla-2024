EN_CARMILLA = 'carmilla'
EN_LAURA = 'laura'
EN_NICK = 'nick'
EN_SPIELSDORF = 'spielsdorf'

FIELD_PLAYDATE = 'playDate'
FIELD_WEEK = 'weekDay'
FIELD_PLAYTIME = 'playTime'
FIELD_CASTINGS = 'castings'
FILED_CHARACTER = 'characterName'
FIELD_ACTOR = 'manName'

REQUEST_END_DATE = '20240908'
REQUEST_URL = (f'https://api-ticketfront.interpark.com/v1/goods/casting/schedule?endDate={REQUEST_END_DATE}&goodsCode'
               f'=24006970&placeCode=24000105&startDate=')

SCHEDULE_JSON_FILE = 'resources/schedule.json'
TOP_COMPONENT_FILE = 'component/top.js'
BOTTOM_COMPONENT_FILE = 'component/bottom.js'
BUNDLE_JS_FILE = '../docs/bundle.js'

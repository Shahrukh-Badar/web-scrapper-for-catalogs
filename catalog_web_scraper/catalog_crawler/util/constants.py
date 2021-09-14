### Global #####
SPIDER_NAME = 'catalog'
BASE_URL = 'https://www.urparts.com/'
START_URL = f'{BASE_URL}index.cfm/page/catalogue'
PARSER = 'html.parser'
MANUFACTURER = 'manufacturer'
CATEGORY = 'category'
MODEL = 'model'
PART = 'part'
PART_CATEGORY = 'part_category'

### HTML SELECTORS ###
MANUFACTURER_SELECTOR = 'div.c_container.allmakes'
CATEGORY_SELECTOR = 'div.c_container.allmakes.allcategories'
MODEL_SELECTOR = 'div.c_container.allmodels'
PART_SELECTOR = 'div.c_container.allparts'
UNORDERED_LIST = 'ul'
LIST_ITEM = 'li'
ANCHOR = 'a'

### Others ###
FIRST_ELEMENT = 0
OUTPUT_FOLDER_NAME = 'storage'
OUTPUT_FILE_NAME = 'output.csv'

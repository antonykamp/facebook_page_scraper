from facebook_page_scraper import Facebook_scraper
import json

#instantiate the Facebook_scraper class

page_name = "alternativefuerde"
posts_count = 3000
timeout=360000
browser = "firefox"

facebook_ai = Facebook_scraper(page_name,posts_count,browser, timeout=timeout)
filename = "test"  #file name without CSV extension,where data will be saved
directory = "/Users/antonykamp/Projects/charly-facebook-analysis" #directory where CSV file will be saved
facebook_ai.scrap_to_csv("alternativefuerde_3000.json")

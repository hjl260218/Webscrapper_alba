from extract import extract_brand_info,extract_jobs
from save import save

def get_brand_jobs():
  brand_info = extract_brand_info()
  for num in range(len(brand_info['url'])):
    
    jobs = extract_jobs(brand_info["url"][num])
    save(brand_info["brand"][num],jobs)
    
  return
  
get_brand_jobs()
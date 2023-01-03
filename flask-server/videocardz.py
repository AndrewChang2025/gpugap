from scrape import * 
from firebase import *

# retrieved links to specific gpu models
amd_gpus_links = get_GPUs(amd)
nvidia_gpus_links = get_GPUs(nvidia)
intel_gpus_links = get_GPUs(intel)

# scrape each page, generate list of dataclasses for amd, nvidia, intel
amd_gpus = scrape_page(amd_gpus_links)
nvidia_gpus = scrape_page(nvidia_gpus_links)
intel_gpus = scrape_page(intel_gpus_links)

# convert dataclass lists to JSON array of objects 
amd_json = data_to_json(amd_gpus)
nvidia_json = data_to_json(nvidia_gpus)
intel_json = data_to_json(intel_gpus)

# write to firebase 
amd_db_ref.set(amd_json)
nvidia_db_ref.set(nvidia_json)
intel_db_ref.set(intel_json)

driver.quit()


from scrape import * 

# retrieved links to specific gpu models
amd_gpus_links = get_GPUs(amd)
nvidia_gpus_links = get_GPUs(nvidia)
intel_gpus_links = get_GPUs(intel)

# scrape each page 
amd_gpus = scrape_page(amd_gpus_links)
nvidia_gpus = scrape_page(nvidia_gpus_links)
intel_gpus = scrape_page(intel_gpus_links)

print('-' * 10 + 'AMD GPUS' + '-' * 10)
for amd_gpu in amd_gpus:
    print(amd_gpu.name)

print('-' * 10 + 'NVIDIA GPUS' + '-' * 10)
for nvidia_gpu in nvidia_gpus:
    print(nvidia_gpu.name)

print('-' * 10 + 'INTEL GPUS' + '-' * 10)
for intel_gpu in intel_gpus:
    print(intel_gpu.name)

driver.quit()


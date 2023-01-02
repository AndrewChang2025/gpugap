from dataclasses import dataclass
from dataclasses_json import dataclass_json

# store gpus as dataclass then export them as json to database
@dataclass
class GPU:
    # overview
    name: str
    manufacturer: str
    series: str
    announced: str
    released: str
    msrp: str

    # graphics processing unit
    model: str
    architecture: str
    fab: str
    die: str
    transistors: str
    stream_processors: str
    rt_cores: str
    tmu: str
    rop: str

    # clocks
    base_clock: str
    game_clock: str
    boost_clock: str
    memory_clock: str
    eff_memory_clock: str

    # memory configuration 
    mem_size: str
    mem_type: str
    mem_bus_width: str
    mem_bandwidth: str

    # api support
    directx: str
    vulkan: str
    openGL: str
    openCL: str

    # performance 
    pixel_fillrate : str
    texture_fillrate: str
    peak_FP32: str
    fp32_perf_per_watt: str
    fp32_perf_per_mm2: str

    # physical 
    interface: str
    length: str
    height: str
    power_connectors: str
    tdp_tbp: str
    psu_rec: str

    # display outputs
    display_port: str
    hdmi: str

    # image 
    img_src: str 

    def __init__(self):
        pass

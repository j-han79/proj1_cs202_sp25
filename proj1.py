#complete your tasks in this file
#Task 1
from dataclasses import dataclass
import math
from math import radians, sin, cos, sqrt
@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float #lower latitude in degrees
    hi_lat: float #upper latitude in degrees
    west_long: float #western longitude in degrees
    east_long: float #eastern longitude in degrees
@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str #string with name of region
    terrain: str #terrain should be these types: "ocean", "mountains", "forest", or "other"
@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int #year of observation
    pop: int #population in that year
    ghg_rate: float #greenhouse gas emissions

#Task 2
region_conditions = [
    RegionCondition(Region(GlobeRect(39.8, 41.7, -74.6, -72.9), "Tri-State", "other"), 2019, 19200000, 2.7918e8),
    RegionCondition(Region(GlobeRect(-7.5, -5.9, 106.33, 107.92), "Greater Jakarta","other"), 2013, 28000000, 5.2e7),
    RegionCondition(Region(GlobeRect(-23.5, 23.5, 100.0, 180.0), "Western Pacific Ocean", "ocean"), 2011, 0, 0.0),
    RegionCondition(Region(GlobeRect(35.03, 35.75, -121.2, -119.5), "San Luis Obispo County", "other"), 2021, 279464, 2.4e6)]

#Task 3
def emissions_per_capita(rc: RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    return rc.ghg_rate / rc.pop

def area(gr: GlobeRect) -> float:
    r = 6378.1 #earth radius in km
    lo = radians(gr.lo_lat)
    hi = radians(gr.hi_lat)
    west = radians(gr.west_long)
    east = radians(gr.east_long)
    a = (r**2) * abs(east - west) * abs(sin(hi) - sin(lo))
    return a
def emissions_per_square_km(rc: RegionCondition) -> float:
    pass
def densest(rc_list: list[RegionCondition]) -> str:
    pass

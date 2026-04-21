#complete your tasks in this file
#Task 1
from dataclasses import dataclass
import math
from math import radians, sin, cos, sqrt, pi
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
    longitude_diff = east - west
    if longitude_diff < 0:
        longitude_diff = longitude_diff + 2 * pi
    return (r**2) * longitude_diff * abs(sin(hi) - sin(lo))
def emissions_per_square_km(rc: RegionCondition) -> float:
    region_area = area(rc.region.rect)
    if region_area == 0:
        return 0.0
    return rc.ghg_rate / region_area
def densest(rc_list: list[RegionCondition]) -> str:
    return densest_rc(rc_list).region.name
def densest_rc(rc_list: list[RegionCondition]) -> RegionCondition:
    if len(rc_list) == 1:
        return rc_list[0]
    densest_rest = densest_rc(rc_list[1:])
    first_density = rc_list[0].pop / area(rc_list[0].region.rect)
    rest_density = densest_rest.pop / area(densest_rest.region.rect)
    if first_density >= rest_density:
        return rc_list[0]
    else:
        return densest_rest
#Task 4
def growth_rate(terrain:str)->float:
    if terrain == "ocean":
        return 0.0001
    elif terrain == "mountains":
        return 0.0005
    elif terrain == "forest":
        return -0.00001
    else:
        return 0.0003

def project_condition(rc: RegionCondition, years:int) -> RegionCondition:
    rate = growth_rate(rc.region.terrain)
    new_pop = int(rc.pop * ((1 + rate) ** years))
    if rc.pop == 0:
        new_ghg = 0.0
    else:
        new_ghg = rc.ghg_rate * (new_pop / rc.pop)
    return RegionCondition(rc.region, rc.year + years, new_pop, new_ghg)

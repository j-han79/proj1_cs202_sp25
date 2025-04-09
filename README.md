## 🌍 CSC 202 – Assignment 1: Modeling and Projecting the Earth's Surface

### Overview

In this assignment, we’re building a system to **rank and analyze regular slices of the Earth’s surface**. Your job is to design the data structures, create example data, and implement functions that help reason about climate-related changes over time.

Your work will be organized into **four tasks**.

You must use:
- `@dataclass(frozen=True)` for all your data definitions
- **External functions only** (no class methods)
- **Recursive functions** for list processing

---

## ✅ Task 1: Define the Data Classes

Define **three immutable data classes** using `@dataclass(frozen=True)`. These will model the basic geographic and environmental information about regions on Earth.

---

### `GlobeRect`

Represents a rectangular region of the globe. It should contain the following attributes:

- `lo_lat`: the lower latitude in degrees (between -90 and 90 inclusive)
- `hi_lat`: the upper latitude in degrees (greater than `lo_lat`)
- `west_long`: the western longitude in degrees (between -180 and 180)
- `east_long`: the eastern longitude in degrees (between -180 and 180)

> Note: `west_long` may be greater than `east_long` for regions crossing the international date line.

---

### `Region`

Describes the identity and terrain of a region. It should contain:

- `rect`: a `GlobeRect` object describing the physical boundaries
- `name`: a string with the name of the region (e.g., `"Tokyo"`)
- `terrain`: a string representing the terrain type — one of:
  - `"ocean"`
  - `"mountains"`
  - `"forest"`
  - `"other"`

---

### `RegionCondition`

Describes the current state of a region in a specific year. It should include:

- `region`: a `Region` object
- `year`: the year of observation (as an integer)
- `pop`: the population in that year (as an integer)
- `ghg_rate`: the greenhouse gas emissions for that year (as a float, in tons of CO₂-equivalent per year)

---

## ✅ Task 2: Create Example Data

Create **four instances** of `RegionCondition`. These will be used to test your functions in later tasks.

Store them in a list called:

```python
region_conditions = [...]
```

Your list must include:
1. A major metropolitan area from anywhere in the world
2. A second major metro from a different continent
3. A substantial ocean region (not a whole ocean)
4. A region that includes Cal Poly, but excludes:
   - San Jose
   - Santa Barbara
   - Bakersfield
   - and too much ocean

> Use rough estimates. Approximate within:
> - ~5% for latitude/longitude
> - Factor of 10 for population or emissions  
> Don’t spend more than 5–10 minutes researching numbers.

---

## ✅ Task 3: Implement External Functions

You must implement **external functions only** (do not define any methods inside the classes).  
Functions that process lists **must be recursive**.

---

### Function: `emissions_per_capita(rc)`

Takes a `RegionCondition` and returns the tons of CO₂-equivalent **emitted per person** in the region per year. Avoid division by zero.

---

### Function: `area(gr)`

Takes a `GlobeRect` and returns the estimated **area in square kilometers**, using this formula:

- ignore curvature, of the earth treat as a rectangle. 
- Each degree ≈ 111 km on the Earth.

---

### Function: `emissions_per_square_km(rc)`

Takes a `RegionCondition` and returns the **tons of CO₂-equivalent per square kilometer**.  
hint: (Uses the area of the region.)

---

### Function: `densest(rc_list)`

Takes a list of `RegionCondition` values and returns the **name of the region with the highest population density**, calculated as:

```
population / area
```

> Must be implemented **recursively**.  
> You may not use `max`, `for`, `while`, or list comprehensions.

---

## ✅ Task 4: Simulate Future Projections

Now we’ll simulate how regions change over time based on terrain-specific population growth.

---

### Function: `project_condition(rc, years)`

Takes a `RegionCondition` and a number of years.  
Returns a **new RegionCondition** that represents the state of the region after that many years have passed.

Rules:
- Population grows exponentially each year based on terrain type.
- Emissions grow proportionally to population.
- The region and terrain remain unchanged.
- The `year` should be updated by the given number of years.

Growth rates per terrain:
| Terrain     | Annual growth rate |
|-------------|--------------------|
| `"ocean"`     | +0.0001           |
| `"mountains"` | +0.0005           |
| `"forest"`    | -0.00001          |
| `"other"`     | +0.0003           |

> You are encouraged to write **helper functions** to make testing easier.  
> This function must return a **new object** — do **not mutate** the original `RegionCondition`.

---

## 🔧 Setup and Restrictions

Use the following imports only:

```python
import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10**6)
```

- **Do not import anything else**
- Use **recursion**, not loops or comprehensions, for list processing
- Follow the design recipe (purpose, type comment, examples/tests, definition)

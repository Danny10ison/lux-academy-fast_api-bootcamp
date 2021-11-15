from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum  # for gender enum

# enum of gender for staff members
class Gender(str, Enum):
    male = "male"
    female = "female"

# enum for staff roles
class Role(str, Enum):
    admin = "admin"
    head = "head"
    hod = "hod"
    teacher = "teacher"

# setting the structure for every staff
class Staff(BaseModel):
    id         : Optional[UUID] = uuid4() # generate id
    first_name : str
    middle_name: Optional[str]
    last_name  : str
    gender     : Gender
    roles      : List[Role]

# use this model when updating staff details
# Optional so that not everything is required
class StaffUpdateRequest(BaseModel):
    first_name : Optional[str]
    middle_name: Optional[str]
    last_name  : Optional[str]
    roles      : Optional[List[Role]]

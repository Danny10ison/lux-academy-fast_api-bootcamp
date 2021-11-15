from fastapi import FastAPI, HTTPException 
from typing import List
from   models import Staff, Gender, Role, StaffUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

# fake database to store users
fake_db: List[Staff] = [
    Staff(
        id=uuid4(), # will change anytime u reload app
        first_name="John", 
        middle_name="Kofi", 
        last_name="Osei",
        gender=Gender.male,
        roles=[Role.admin] 
    ),
    Staff(
        id=uuid4(), # will change anytime u reload app
        first_name="Ellen",  
        last_name="Bortey",
        gender=Gender.female,
        roles=[Role.head, Role.hod] 
    )
]

# root of api
@app.get("/")
async def get_index():
    return {
        "App"     : "Staff Portal for Imaginary School",
        "Version" : "1.0.0",
        "Date"    : "12-11-2021"
    }

@app.get("/school/staff")
async def get_staff_members():
    return fake_db

@app.post("/school/staff")
async def add_staff_member(staff: Staff):
    fake_db.append(staff)
    return {"staff_id": staff.id}

# update staff details using staff id
@app.put("/school/staff/{staff_id}")
async def update_staff_details(staff_updater: StaffUpdateRequest, staff_id: UUID):
    for staff in fake_db:
        if staff.id == staff_id:
            if staff_updater.first_name is not None:
                staff.first_name = staff_updater.first_name
            if staff_updater.middle_name is not None:
                staff.middle_name = staff_updater.middle_name
            if staff_updater.last_name is not None:
                staff.last_name = staff_updater.last_name
            if staff_updater.roles is not None:
                staff.roles = staff_updater.roles
            return
    raise HTTPException( # if id does not exits
        status_code = 404,
        detail=f"Staff with id: {staff_id} does not exist"
    )

# delete staff with id
@app.delete("/school/staff/{staff_id}")
async def delete_staff(staff_id: UUID):
    for staff in fake_db:
        if staff.id == staff_id:
            fake_db.remove(staff)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Staff with id: {staff_id} does not exist"
    )
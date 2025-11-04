# OOD amazon locker 
"""
Requirements:
Users can ship packages to lockers instead of home.

A locker has size (small/medium/large), location, status (available, occupied).

A package is assigned a locker based on its size and location.

The courier deposits a package, generating a pickup code.

The user retrieves the package using the pickup code.

Lockers become available again after pickup.
"""
# package
class Package:
    def __init__(self, package_id: int, size: float):
        self.package_id = package_id
        self.size =  size # enum: small, medium, large

# Locker
class LockerSize(Enum):
    SMALL = 1 
    MEDIUM = 2 
    LARGE = 3 

class Locker:
    def __init__(self, locker_id: int, size: LockerSize, location):
        self.locker_id = locker_id 
        self.size = size 
        self.location = location 
        self.package = None 
        self.is_occupied = True

    def store_package(self, package: Package):
        self.package = package
        self.is_occupied = False

    def retrieve_package(self):
        pkg = self.package
        self.package = None 
        self.is_occupied = True
        return pkg

# PickupCodeManager 
import uuid 

class PickupCodeManager:
    def __init__(self):
        self.code_map = {} # code : locker

    def generate_code(self, locker: Locker):
        code = str(uuid.uuid4())
        self.code_map[code] = locker
        return code 

    def get_locker(self, code):
        return self.code_map.get(code,0)

# LockerSystme
class LockerSystem:
    def __init__(self, lockers: list[locker]):
        self.lockers = lockers 
        self.code_manager = PickupManager()
    
    

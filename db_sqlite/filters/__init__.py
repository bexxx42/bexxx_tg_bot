from loader import dp
from .IsAdmin import IsAdmin
from .IsUser  import IsUser

if __name__ == "__filters__":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsUser)
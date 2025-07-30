def pond_water_volume():
    radius = 84  
    pi = 3.14
    water_per_sq_meter = 1.4  

    area = pi * radius ** 2
    total_water = int(area * water_per_sq_meter)  
    print("Total water in pond (liters):", total_water)

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 1 - Original Justice League:")
print(justice_league)

print("\nStep 2 - Number of members:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nStep 3 - After adding Batgirl and Nightwing:")
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nStep 4 - Wonder Woman moved to the beginning:")
print(justice_league)

aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

if aquaman_index > flash_index:
    aquaman_index, flash_index = flash_index, aquaman_index

justice_league.remove("Superman")  
print("\nStep 5 - Superman inserted between Aquaman and Flash:")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nStep 6 - New Justice League after crisis:")
print(justice_league)

# assign new leader
justice_league.sort()
print("\nStep 7 - Justice League sorted alphabetically:")
print(justice_league)

print("\nNew leader (0th index):", justice_league[0])

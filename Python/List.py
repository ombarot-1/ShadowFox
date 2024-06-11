justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
# Perform the following tasks:
# 1. Calculate the number of members in the Justice League.
print('Number of members in the Justice League:',len(justice_league),'\n')

# 2. Batman recruited Batgirl and Nightwing as new members. 
justice_league.extend(['Batgirl','Nightwing'])
print(justice_league,'\n')

# 3. Wonder Woman is now the leader of the Justice League.
justice_league.remove('Wonder Woman')
justice_league.insert(0,'Wonder Woman')
print(justice_league,'\n')

# 4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman"
# and move them in between Aquaman and Flash.
justice_league.remove('Superman')
justice_league.insert(3,'Superman')
print(justice_league,'\n')

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the 
# following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
NewTeam = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = NewTeam
print(justice_league,'\n')

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print(justice_league)

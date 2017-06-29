import json, hashlib, uuid, os

def personalInfo(): #define personal account information

    # gather profile data into JSON format
    data = {
        "Name": name.replace("\n", "").replace("/", ""),
        "DateOfBirth": dateOfBirth.replace("\n", "").replace("/", ""),
        "Address": address.replace("\n", "").replace("/", ""),
        "City": city.replace("\n", "").replace("/", ""),
        "State": state.replace("\n", "").replace("/", ""),
        "Zip": zip.replace("\n", "").replace("/", ""),
        "Phone": phone.replace("\n", "").replace("/", ""),
        "Email": email.replace("\n", "").replace("/", ""),
        "UserName": userName.replace("\n", "").replace("/", ""),
        "Password": hashedPwd.replace("\n", "").replace("/", "")
    }

    #result = json.dumps(data, indent=4, sort_keys=True) #format as JSON for screen printing
    #print result
    print "\n Your Profile has been created!"

    with open(profileName, 'w') as f:  #create JSON file
        json.dump([data], f, indent=4, sort_keys=True)


def playerAchievements(): # Gather player achievements and add to profile

    ach2 = raw_input("You awaken with no memory at a dark cave entrance.  Do you Enter? (Y/N): ")

    if (ach2 == 'Y'):
        ach2Score = '1'
        ach2Desc = 'Achievement Unlocked!! You have entered your first Dungeon!'
        print ach2Desc
        ach3 = raw_input("Immediately a fierce furry creature jumps from the shadows!  Do you attack with your sword? (Y/N)")
    else:
        ach2Score ='0'
        ach2Desc = ''
        ach3 = raw_input("An assassin has been following you and confronts you!  Do you attack with your sword? (Y/N): ")

    if ach3 =='Y':
        ach3Score = '1'
        ach3Desc = 'Achievement Unlocked!! You have defeated your first enemy!'
        ach4Score = '0'
        ach4Desc = ''
        print ach3Desc
    else:
        ach3Score = '0'
        ach3Desc = 'You are a coward and have perished in battle!'
        ach4Score = '1'
        ach4Desc = 'You have died your first death!'
        print ach3Desc

    with open(profileName) as f:
        profile = json.load(f)

    achievements = {
        "Achievement 1": '1',
        "Achievement 1 Name": "Create Profile",
        "Achievement 1 Description": 'Achievement Unlocked!! You have created your Profile!!',
        "Achievement 2 Name": "Enter Dungeon",
        "Achievement 2": ach2Score,
        "Achievement 2 Description": ach2Desc,
        "Achievement 3 Name": "First Battle",
        "Achievement 3": ach3Score,
        "Achievement 3 Description": ach3Desc,
        "Achievement 4 Name": "First Death",
        "Achievement 4": ach4Score,
        "Achievement 4 Description": ach4Desc,
    }

    #result = json.dumps(achievements, indent=4, sort_keys=True)  # format as JSON for screen printing
    #print result

    with open(profileName, 'r+') as data_file:
        profile.append(achievements)
        json.dump(profile, data_file, indent=4, sort_keys=True)

def playerBattles(): #this randomizes battles, wins and losses since there is no actual game to get actual data for this.
    with open(profileName, 'r+') as battles:

        prof = json.load(battles)

        battle1 = int(prof[1]["Achievement 3"])
        battle2 = int(prof[1]["Achievement 4"])

        battlesWon = battle1+battle2

        print "You have won ", battlesWon, " of 2 battles!"

#gather profile information from the user

name = raw_input("Name: ")
profileName = name.replace(" ", "_") + "_profile.json"

if os.path.exists(profileName):  #check to see if this user exists!
    start = raw_input("Your Profile Already Exists, would you like to start the game? (Y/N): ") #play game for achievements Y or N
    if (start == 'Y'): #start game
        playerAchievements()
        playerBattles()
    else: #exit if N is chosen
        sys.exit(1)
else: # complete the profile first

    dateOfBirth = raw_input("DOB (MM-DD-YYYY): ")
    address = raw_input("Street: ")
    city = raw_input("City: ")
    state = raw_input("State: ")
    zip = raw_input("Zip: ")
    email = raw_input("Email: ")
    phone = raw_input("Phone: ")
    userName = raw_input("Username: ")
    password = raw_input("Password: ")
    salt = uuid.uuid4().hex
    hashedPwd = hashlib.sha512(password + salt).hexdigest()

    personalInfo()
    playerAchievements()
    playerBattles()
from pyscript import document

# Stores my hobbies and interests
interests_hobbies = [
    "Listening to music", 
    "Watching movies and TV series", 
    "Reading books",
    "Traveling and exploring new places",
    "Spending time with family and friends",
    "Playing mobile games",
    "Problem solving",
    "Playing badminton",
    "Singing",
    "Playing instruments (Piano and Ukulele)",
]

# Stores my dreams
dreams = [
    "Become a better version of myself",
    "Make my family proud",
    "Visit more places around the world",
    "To live a happy and fulfilling life",
    "Become more confident and independent",
    "Create unforgettable memories with my loved ones",
    "Graduate with excellent achievements",
    "Study at my dream university (UP)",
    "Become successful in my chosen profession",
    "Develop skills that will help me in the future" ,
    "Become financially independent",
    "Attend concerts of my favorite artists",
    "Try new adventures and activities",
    "Meet inspiring people",
]

# Stores my favorites
favorites = {
    'Food': ' Instant Noodles',
    'Color': ' Pink',
    'Singer/Artist': ' Taylor Swift',
}

# Stores my favorite activities
favorite_activities = {
    "Listening to Taylor Swift",
    "Playing the Piano and Ukulele",
    "Traveling",
    "Watching Movies and TV Shows",
    "Playing Badminton"
}

# Stores personal information
about_me = {
    'Birthday': 'Sept. 7, 2011',
    'Nationality': 'Filipino (With Chinese and Spanish ancestry)',
    'Zodiac Sign': 'Virgo',
    'Mbti personality': 'ENFP',
}

# Stores my favorite quotes
quotes = [
    "To me, fealess is not the absence of fear. It's not being completely unafraid. To me, fearless is having fears. Fearless is living in spite of those things that scare you to death. - Taylor Swift",
    "What, like it's hard - Elle Woods",
    "Fire is cathing, and if we burn, you burn with us! - Katniss Everdeen"
]

# The HTML output for hobbies
hobby_output = ""

# Goes through each item in the list
for hobby in interests_hobbies:
    hobby_output += f"<li>{hobby}</li>"

# Displays list
document.getElementById("hobbies").innerHTML = hobby_output

# The HTML output for dreams
dream_output = ""

# Goes through each item in the list
for dream in dreams:
    dream_output += f"<li>{dream}</li>"

# Displays list
document.getElementById("dreams").innerHTML = dream_output

# The HTML output for favorites
favorite_output = ""

# Access both key and value of the dictionary
for key, value in favorites.items():
    favorite_output += f"<div class='info'><b>{key}:</b>{value}</div>"

# Displays dictionary
document.getElementById("favorites").innerHTML = favorite_output

# The HTML output for favorite activities
activity_output = ""

# Arranges the set values alphabetically
for activity in sorted(favorite_activities):
    activity_output += f"<li>{activity}</li>"

# Displays set
document.getElementById("activities").innerHTML = activity_output

# The HTML output for personal information
about_output = ""

# Access both key and value of the dictionary
for key, value in about_me.items():
    about_output += f"<div class='info'><b>{key}:</b> {value}</div>"

# Displays dictionary
document.getElementById("about-me").innerHTML = about_output

# The HTML output for quotes
quote_output = ""

# Goes through each item in the list
for quote in quotes:
    quote_output += f"<div class='quote'>“{quote}”</div>"

# Displays list
document.getElementById("quotes").innerHTML = quote_output
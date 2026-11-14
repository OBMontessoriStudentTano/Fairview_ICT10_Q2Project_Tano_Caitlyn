from pyscript import document

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

favorites = {
    'Food': 'Instant Noodles',
    'Color': 'Pink',
    'Singer/Artist': 'Taylor Swift',
}

favorite_activities = {
    "Listening to Taylor Swift",
    "Playing the Piano and Ukulele",
    "Traveling",
    "Watching Movies and TV Shows",
    "Playing Badminton"
}

about_me = {
    'Birthday': 'Sept. 7, 2011',
    'Nationality': 'Filipino',
    'Zodiac Sign': 'Virgo',
    'Mbti personality': 'ENFP',
}

quotes = [
    "To me, fealess is not the absence of fear. It's not being completely unafraid. To me, fealess is having fears. Fearless is living in spite of those things that scare you to death. - Taylor Swift",
    "What, like it's hard - Elle Woods",
    "Fire is cathing, and if we burn, you burn with us! - Katniss Everdeen"
]

about_output = ""

for key, value in about_me.items():
    about_output += f"<div class='info><b>{key}:</b> {value}</div>"

document.getElementById("about-me").innerHTML = about_output

me_output = ""

for detail in personal_details:
    abome_output += f"<li>{detail}</li>"

document.getElementById("me").innerHTML = about_output

hobby_output = ""

for hobby in interests_hobbies:
    hobby_output += f"<li>{hobby}</li>"

document.getElementById("hobbies").innerHTML = hobby_output

dream_output = ""

for dream in dreams:
    dream_output += f"<li>{dream}</li>"

document.getElementById("dreams").innerHTML = dream_output

favorite_output = ""

for key, value in favorite.items():
    favorite_output += f"<li><b>{key}:</b>{value}</li>"

document.getElementById("favorites").innerHTML = favorite_output

activity_output = ""

for activity in sorted(favorite_activities):
    activity_output += f"<li>{activity}</li>"

document.getElementById("activities").innerHTML = activity_output

quote_output = ""

for quote in quotes:
    quote_output += f"<div class='quote'>“{quote}”</div>"

document.getElementById("quotes").innerHTML = quote_output
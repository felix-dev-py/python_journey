profile = { 
    "name": "Rustam",
    "age": 30,
    "city": "Mayami",
    "skills": ["Python", "JS", "Abelton"]
}

profile["age"] = 31
profile["email"] = "rustam@gmail.com"
for key, value in profile.items():
    print(f"{key}: {value}")

def describe(profile):
    skills = ", ".join(profile.get("skills"))
    return f"{profile.get('name')}, {profile.get('age')} years, from {profile.get('city')}. Skills: {skills}"

print()
print(describe(profile))
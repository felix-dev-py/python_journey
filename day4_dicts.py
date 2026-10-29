profile = { 
    "name": "Rustam",
    "age": 30,
    "city": "Mayami",
    "skills": ["Python", "JS", "Abelton"]
}

profile["age"] = 31
profile["email"] = "rustam@gmail.com"
print(profile.items())

def describe(profl):
    skills = ", ".join(profl.get("skills"))
    return f"{profl.get('name')}, {profl.get('age')} years, from {profl.get('city')}. Skills: {skills}"

print()
print(describe(profile))
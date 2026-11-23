python_workshop = ["olena@mail.com", "taras@mail.com", "olena@mail.com", "marta@mail.com"]
git_workshop = ["marta@mail.com", "petro@mail.com", "taras@mail.com", "petro@mail.com"]

python_people = set()
git_people = set()
git_python_people = set()

i = 0
j = 0
while i < len(python_workshop):
    python_people.add(python_workshop[i])
    i += 1

while j < len(git_workshop):
    git_people.add(git_workshop[j])
    j += 1

print(f"Python: {len(python_people)} учасники")
print(f"Git: {len(git_people)} учасники")
print(f"На обох: {sorted(git_people & python_people)}")
print(f"Лише на Python: {python_people - git_people}")
print(f"Лише на Git: {git_people - python_people}")
print(f"Усього різних людей: {len(git_people | python_people)}")
print(f"Усі учасники: {sorted(git_people | python_people)}")
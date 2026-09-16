# Lab-2_C-2

# create two sets of developer skills
dev_skills_1 = {
    "python",
    "git",
    "sql",
    "docker"
    }

dev_skills_2 = {
    "javascript",
    "git",
    "html",
    "docker"
}

# find skill they share
print(dev_skills_1 & dev_skills_2)
# find skills only the first has
print(dev_skills_1 - dev_skills_2)
# all skills by either person
print(dev_skills_1 | dev_skills_2)

import sys
import os
import shutil
import json
from github import Github
import git

config = {""}

root = os.path.dirname(os.path.realpath(__file__))

with open(root + "\\config.json", "r") as read_file:
    config = json.load(read_file)

userToken = config["github"]["token"]
template = ""
if(len(sys.argv) <= 2):
    template = "/defaulttemplate"
else:
    template = "/" + sys.argv[2]

print("Logging in. . .")
g = Github(userToken)

print("Copying template. . .")
if(not os.path.isdir("./" + sys.argv[1])):
    shutil.copytree(root + template, "./" + sys.argv[1])

print("Creating Github repo. . .")
user = g.get_user()
repo = user.create_repo(sys.argv[1], has_wiki=False)
tree = os.listdir("./" + sys.argv[1])

for i in range(len(tree)):
    tree[i] = os.getcwd() + "\\" + sys.argv[1] + "\\" + tree[i]

print("Initializing git repo. . .")

os.chdir("./" + sys.argv[1])
r = git.Repo.init(os.getcwd())
print("Adding files to git repo. . .")
r.index.add(tree)
r.index.add("README.md")
print("Commiting. . .")
r.index.commit("initial commit")

print("Pushing git repo to Github repo. . .")

os.system("git branch -M main")
os.system("git remote add origin https://github.com/" + user.name +"/" + repo.name)
os.system("git push -u origin main")

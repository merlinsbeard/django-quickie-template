from jinja2 import Template
import os, shutil

def read_file(file, **kwargs):
    with open(file, 'r') as f:
        t = Template(f.read())
        return t.render(**kwargs)

def save_file(file, data):
    with open(file, 'w') as f:
        f.write(data)
        return f

# Create New Dockerfile

project_name = input("Project Name: ")
cwd = os.getcwd()
data = {"project_name": project_name}
print("Saving File")
save_file(f"{cwd}/Dockerfile", read_file(f"{cwd}/docker-template", **data))
print("Done")

# Create entrypoint
ep = os.path.join(os.getcwd(), "entrypoint.sh")
print("Updating entrypoint")
save_file(ep, read_file(ep, **data))
print("Done")

# Rename Project Folder
print("Rename Project Folder")
project_folder = os.path.join(os.getcwd(), "{{ project_name }}")
os.rename(project_folder, data['project_name'])
print("DONEEEEEEEEEE")

# Delete Git
print("Removing .git")
git_folder = os.path.join(os.getcwd(), ".git/")
shutil.rmtree(git_folder)
print("DONEEEEEEEEEE")

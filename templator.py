from jinja2 import Template
import os

def read_file(file, **kwargs):
    with open(file, 'r') as f:
        t = Template(f.read())
        return t.render(**kwargs)

def save_file(file, data):
    with open(file, 'w') as f:
        f.write(data)
        return f

# Create New Dockerfile

project_name = input("Project Name")
data = {"project_name": project_name}
print("Saving File")
save_file("Dockerfile", read_file("docker-template", **data))
print("Done")

# Create entrypoint
print("Updating entrypoint")
save_file("entrypoint.sh", read_file("entrypoint.sh", **data))
print("Done")

# Rename Project Folder
print("Rename Project Folder")
os.rename("{{ project_name }}", data['project_name'])
print("DONEEEEEEEEEE")

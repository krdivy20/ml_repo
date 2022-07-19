## Start Machine Learning Project

## Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda environment
'''
conda create -p venv python==3.7 -y
'''

Conda activate 
'''
conda activate venv/
'''

pip install -r requirements.txt

Git commands

git add <file_name> 

To check git status
'''
git status
'''

to check all version maintained by git
'''
git log
'''

To create verison/commit all changes by git
''' git commit -m "message"
'''

To send changes/version to github
'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

To setup CI/CD pipeline in heroku we need 3 information
a. Heroku Email = divyanshukumar3@gmail.com
b. Heroku API key = <GET API KEY FROM HEROKU>
c. Heroku App Name = first-ml-regression

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname>
'''
> Note: Image name for docker must be lowercase

To list docker images
'''
docker images
'''

Run Docker Image
'''
docker run -p 5000:5000 -e PORT=5000 <image_id>
'''

To check running container in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''


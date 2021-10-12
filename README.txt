# django_REST-API-s
## Version control commands
```
git init
git branch (view the branch)
git checkout main (switch the branch from existing to main)
git branch -v
git remote add origin/main <githut remote repository url>
git add . && git commit -m "initial commit" && git push -f origin man
```
## Dependency/software installations
```
midir <project folder name>
cd <project folder>
python -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
pip install markdown # to provide support for browsable api
pip install django-filter # filtering support
pip freeze > requirements.txt

```
# Production: Deploy into Heroku Cloud Server

```
sudo apt-get install software-properties-common # debian only
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
```
git add .
git commit -m "$1"
python3 src/main.py test/test.oto
git push
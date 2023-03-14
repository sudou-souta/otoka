gcc src/main.c -o bin/main
./bin/main
git checkout gcc
git add .
git commit -m "$1"
git push
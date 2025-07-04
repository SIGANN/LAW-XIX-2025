# LAW-XIX-2025
The 19th Linguistic Annotation Workshop

This is the `main` branch; it contains sources for building the website.
The [website](https://sigann.github.io/LAW-XIX-2025) itself lives on the `gh-pages` branch.


### create gh-pages branch:

git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
echo "My GitHub Page" > index.html
git add .
git commit -a -m "First pages commit"
git push origin gh-pages
# first time: git push --set-upstream origin gh-pages


To deploy changes:

    $ git checkout main
    # ...make, commit, and push changes...
    $ python3 build.py deploy
    # ...make, commit, and push changes...
    $ git checkout gh-pages
    #$ git checkout main -- deploy/* 
    # (logan added the command to move deploy/* files from main to gh-pages)
    $ mv deploy/* .
    $ rmdir deploy
    $ git commit -a -m "deploy changes"
    $ git push


How to test the website locally:

https://kbroman.org/simple_site/pages/local_test.html


NB: Only edit the files under `pages/`, since these are the ones used by the build script. Any HTML files in the repository root will be overwritten on deployment.

NB: The two branches have been cleaned up to avoid confusion since the directory structure gets flattened during build, but used to still be present in `gh-pages`. Now the directory structure (`pages/`, `images/`, etc.) only lives on this branch (the `main` branch). The live page at `gh-pages` does not have any directories, and thus paths to, e.g., images from any html pages should not specify a directory, just the base file name.


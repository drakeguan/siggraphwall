#! /bin/bash
#
# update-gh-pages.sh
# Copyright (C) 2013 drake <drake.guan@gmail.com>
#
# Distributed under terms of the MIT license.
#


if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
	echo -e "Starting to update gh-pages\n"
	#copy data we're interested in to other place
	mkdir $HOME/tmp
	cp -R static $HOME/tmp
	cp -R teaser_images $HOME/tmp
	cp -R index.html $HOME/tmp
	#go to home and setup git
	cd $HOME
	git config --global user.email "drake.guan@gmail.com"
	git config --global user.name "Drake"
	#using token clone gh-pages branch
	git clone --quiet --branch=gh-pages https://drakeguan:${GH_TOKEN}@github.com/drakeguan/siggraphwall.git gh-pages > /dev/null
	#go into diractory and copy data we're interested in to that directory
	cd gh-pages
	cp -Rf $HOME/tmp/* .
	#add, commit and push files
	git add -f .
	git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to gh-pages"
	git push -fq origin gh-pages > /dev/null
	echo -e "Done the magic with gh-pages\n"
fi

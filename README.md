SIGGRAPH Image Wall
===================

> Let's try to make a image wall for SIGGRAPH (2013) technical papers!

![](https://pbs.twimg.com/media/BQ8-n1XCcAAsjcE.jpg:large)



Motivation
----------
[SIGGRAPH][1] is really great, and those published technical papers keeps pushing it to the un-explored limit.
It is easy to get a list of great work through [official website][1].
However, if you don't like to wait til the last minute,
you can visit [Ken-Sen Huang's collection (ex, for SIG'13)][4] frequently and get surprised.
You can get something really refresh there, and study papers prior to attending the conference.

[This year][2], there is a compilation of the 1st page of all technical papers,
[Technical Papers First Pages][3].
I think it would be great to have a image wall, a pinterest-like website,
which dedicates to provide ease-to-read, inspiring and a ToC-like functionality.

I need your help.



Goal
----

* An image wall of technical papers in nearly all SIGGRAPH or other related conferences.
* As easy as possible to browse for human beings and to parse for machine programs.
* No license issues or copyright conflict/fight for using.
* Coop with other great ideas or similar services to help inspiring research in
  computer graphics and computer vision fields.
* Be friendly.



Test run
--------

* Fork the repo recursively or
* Fork the repo and init submodules by `git submodule init; git submodule update`
* Do some modifcation or addition on data. That is, bibtex/ and teaser_images/ (optional)
* Re-generate index.html by `python index_gen.py`
* Open *index.html* in your browser!



Task
----
* First and the most important one, to figure out the suitable license for this work.
  I don't like to get into trouble like [this][5] or make issues to people providing help.
  Right now, I use [CC0, Public Domain Dedication][6].
* Secondly, I need your help :)
* To compile a human-friendly and machine-readable format of papers.
  I think [BibJSON][7] should be a great choice.
* Upload better teaser images if you do have one.
* To build a pinterest-like website for human browsing and machine parsing.
* To design a website, not just a pinterest-like one,
  but in consideration of researchers.
  Of course, it should be as elegant as possible.



Example: Teaser Images
----------------------
A4: Asynchronous Adaptive Anti-Aliasing using Shared Memory
![a4_asynchronous_adaptive_anti-aliasing_using_shared_memory.jpg](teaser_images/a4_asynchronous_adaptive_anti-aliasing_using_shared_memory.jpg)  

Acquiring Reflectance and Shape from Continuous Shperical Harmonic Illumination
![acquiring_reflectance_and_shape_from_continuous_spherical_harmonic_illumination.jpg](teaser_images/acquiring_reflectance_and_shape_from_continuous_spherical_harmonic_illumination.jpg)  

Adaptive Fracture Simulation of Multi-Layered Thin Plates
![adaptive_fracture_simulation_of_multi-layered_thin_plates.jpg](teaser_images/adaptive_fracture_simulation_of_multi-layered_thin_plates.jpg)  

Adaptive Image Synthesis for Compressive Displays
![adaptive_image_synthesis_for_compressive_displays.jpg](teaser_images/adaptive_image_synthesis_for_compressive_displays.jpg)  

Aireal Interactive Tactile Experiences in Free Air
![aireal_interactive_tactile_experiences_in_free_air.jpg](teaser_images/aireal_interactive_tactile_experiences_in_free_air.jpg)  

For more teaser images, check *teaser_images/* folder.



Dependencies
-------------
* [bibtexparser][101], Bibtex parser.
* [MixItUp][102], a light-weight but powerful jQuery plugin that provides beautiful 
  animated filtering and sorting of categorized and ordered content.
* [Bootstrap 3][103], a sleek, intuitive, and powerful mobile-first 
  front-end framework for faster and easier web development.
* [Bootstrap Image Gallery][104], an extension to the Modal dialog of Twitter's Bootstrap toolkit, to ease navigation between a set of gallery images.


References
----------
* [SIGGRAPH 2013 Technical Papers][2]
* [SIGGRAPH 2013 Technical Papers First Pages (44 MB PDF)][3]
* [SIGGRAPH 2013 papers on the web][4]
* [Official SIGGRAPH][1]
* [ACM copyright policy and Ke-Sen Huang's pages][5]



[1]: http://www.siggraph.org/ "ACM SIGGRAPH"
[2]: http://s2013.siggraph.org/attendees/technical-papers "SIGGRAPH 2013 Technical Papers"
[3]: http://s2013.siggraph.org/sites/default/files/firstpages-lores.pdf "SIGGRAPH 2013 Technical Papers First Pages (44 MB PDF)"
[4]: http://kesen.realtimerendering.com/sig2013.html "SIGGRAPH 2013 papers on the web"
[5]: https://groups.google.com/d/topic/ray-tracing-news/ndaSHwvfTEE/discussion "ACM copyright policy and Ke-Sen Huang's pages"
[6]: http://creativecommons.org/publicdomain/zero/1.0/ "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
[7]: http://www.bibjson.org/ "BibJSON"

[101]: https://pypi.python.org/pypi/bibtexparser "bibtexparser"
[102]: http://mixitup.io/ "MixItUp"
[103]: http://getbootstrap.com/ "Bootstrap 3"
[104]: http://blueimp.github.io/Bootstrap-Image-Gallery/ "Bootstrap Image Gallery"

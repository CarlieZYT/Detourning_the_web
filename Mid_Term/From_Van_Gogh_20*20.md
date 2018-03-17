Pinterest Visual Research is a new visual discovery tool to identify what something is and aiming to show people how it can fit into your life. From their research paper, they say:

"By sharing our implementation details and learnings from launching a commercial visual search engine from scratch, we hope visual search becomes more widely incorporated into today's commercial applications."

So how could art work with that? Since art pieces today are also seen as products in some way(and very expensive ones), how do the visual search identify the brushes and pixels of the painting? What will I get when I take a closer look at it? So I scraped Pinterest Visual Rearch page on Van Gogh self portrait, divided the painting into 20x20 grids and download the results of that. I also saved the descriptions into a json file. Here's the [python code](pin_visualsearch.py) and [json file](result_imgs.json)

I got 8644 images out of it and how can I use them. I decide to generate a video and flay the images very fast to see what impression the "machine learning" could get after reading artwork square by square and the result is suprising to me. 

* [The Video](https://youtu.be/AI-kSbmHNRU) Please look straight at it and see what impression you get.

* [The code resizing the images](resize_imgs.py)
* [The code generate a txt file for ffmpeg to read images in an order](imgtovid.py)
* [The txt result](vidsequence.txt)
* Command Line: >>ffmpeg -r 25 -f concat -safe 0 -i vidsequence.txt -vsync vfr fast_output.mp4

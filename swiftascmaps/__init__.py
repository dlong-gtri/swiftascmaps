"""
Taylor Swift color map collection.

Includes color maps based on the following albums:

+ Red (red, red_r)
+ 1989 (nineteen_eighty_nine, nineteen_eighty_nine_r)
+ Reputation (reputation, reputation_r)
+ Lover (lover, lover_r)
+ Folklore (folklore, folklore_r)
+ Evermore (evermore, evermore_r, evermore_shifted, evermore_shifted_r)
+ Fearless: Taylor's Version (fearless_tv, fearless_tv_r)
+ Midnights (midnights, midnights_r)
+ Speak Now: Taylor's Version (speak_now_tv, speak_now_rv_r)
+ 1989: Taylor's Version (nineteen_eighty_nine_tv, nineteen_eighty_nine_tv_r)

License: LGPLv3
Author: Josh Borrow (josh.borrow@gmail.com)

Usage
-----

To use these, you can import them and use them
with matplotlib as you would with any other color map.

.. code-block:: python

    from swiftascmaps import red
    from matplotlib.pyplot import imshow
    from numpy import random

    imshow(random.rand(128, 128), cmap=red)

"""

import swiftascmaps.colors as colors
from swiftascmaps.make_cmap import make_custom_cmap
from swiftascmaps.__version__ import __version__

debut, debut_r = make_custom_cmap("debut", colors.debut)
fearless, fearless_r = make_custom_cmap("fearless", colors.fearless)
speak_now, speak_now_r = make_custom_cmap("speak_now", colors.speak_now)
speak_now_live, speak_now_live_r = make_custom_cmap("speak_now_live", colors.speak_now_live)
red, red_r = make_custom_cmap("red", colors.red)
nineteen_eighty_nine, nineteen_eighty_nine_r = make_custom_cmap(
    "nineteen_eighty_nine", colors.nineteen_eighty_nine
)
reputation, reputation_r = make_custom_cmap("reputation", colors.reputation)
lover, lover_r = make_custom_cmap("lover", colors.lover)
folklore, folklore_r = make_custom_cmap("folklore", colors.folklore)
evermore, evermore_r = make_custom_cmap("evermore", colors.evermore)
evermore_shifted, evermore_shifted_r = make_custom_cmap(
    "evermore_shifted", colors.evermore_shifted
)
fearless_tv, fearless_tv_r = make_custom_cmap("fearless_tv", colors.fearless_tv)
red_tv, red_tv_r = make_custom_cmap("red_tv", colors.red_tv)
midnights, midnights_r = make_custom_cmap("midnights", colors.midnights)
midnights_blood_moon, midnights_blood_moon_r = make_custom_cmap("midnights_blood_moon", colors.midnights_blood_moon)
midnights_jade_green, midnights_jade_green_r = make_custom_cmap("midnights_jade_green", colors.midnights_jade_green)
midnights_mahogany, midnights_mahogany_r = make_custom_cmap("midnights_mahogany", colors.midnights_mahogany)
speak_now_tv, speak_now_tv_r = make_custom_cmap("speak_now_tv", colors.speak_now_tv)
nineteen_eighty_nine_tv, nineteen_eighty_nine_tv_r = make_custom_cmap(
    "nineteen_eighty_nine_tv", colors.nineteen_eighty_nine_tv
)
nineteen_eighty_nine_tv_sunrise_boulevard, nineteen_eighty_nine_tv_sunrise_boulevard_r = make_custom_cmap("nineteen_eighty_nine_tv_sunrise_boulevard", colors.nineteen_eighty_nine_tv_sunrise_boulevard)
nineteen_eighty_nine_tv_aquamarine_green, nineteen_eighty_nine_tv_aquamarine_green_r = make_custom_cmap("nineteen_eighty_nine_tv_aquamarine_green", colors.nineteen_eighty_nine_tv_aquamarine_green)
nineteen_eighty_nine_tv_rose_garden_pink, nineteen_eighty_nine_tv_rose_garden_pink_r = make_custom_cmap("nineteen_eighty_nine_tv_rose_garden_pink", colors.nineteen_eighty_nine_tv_rose_garden_pink)

ttpd, ttpd_r = make_custom_cmap("ttpd", colors.ttpd)

"""
add_attribution.py
==================
Utility to add an official C3S/ECMWF attribution bar to matplotlib figures.

Usage in notebooks
------------------
    from add_attribution import save_with_attribution

    # Call just before plt.show():
    save_with_attribution(fig, 'my_figure.png', dpi=150)

Logo setup (one-time)
---------------------
Download the official C3S four-logo line from the Copernicus branding page:
  https://climate.copernicus.eu/branding-guidelines -> Logolines -> C3S -> positive .png

Save it as:  logos/logoline_c3s.png  (in your project root)

If the logo file is not found the bar renders with text fallback: still valid attribution.

For notebooks one level below the project root (e.g. notebooks/), add this before importing:
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path().resolve().parent))
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path


ATTRIBUTION_TEXT = "© Copernicus / ECMWF 2026  |  CC BY 4.0"

DEFAULT_LOGO_PATH = str(Path(__file__).parent.parent / "logos" / "logoline_c3s.png")

BAR_HEIGHT_INCHES = 0.5
BAR_COLOR         = "#FFFFFF"
# TEXT_COLOR        = "#444444"
# TEXT_FONTSIZE     = 8

def add_attribution_bar(fig, logo_path=DEFAULT_LOGO_PATH, text=ATTRIBUTION_TEXT,
                        bar_height=BAR_HEIGHT_INCHES):
    fig_w, fig_h = fig.get_size_inches()
    new_h = fig_h + bar_height
    fig.set_size_inches(fig_w, new_h)

    scale    = fig_h / new_h
    bar_frac = bar_height / new_h

    for ax in fig.get_axes():
        pos = ax.get_position()
        ax.set_position([
            pos.x0,
            pos.y0 * scale + bar_frac,
            pos.width,
            pos.height * scale,
        ])

    bar_ax = fig.add_axes([0, 0, 1, bar_frac])
    bar_ax.set_xlim(0, 1)
    bar_ax.set_ylim(0, 1)
    bar_ax.axis('off')
    bar_ax.set_facecolor(BAR_COLOR)
    bar_ax.axhline(1.0, color='#CCCCCC', linewidth=0.8)

    if os.path.exists(logo_path):
        try:
            logo_img = mpimg.imread(logo_path)
            img_h, img_w = logo_img.shape[:2]
            img_aspect = img_w / img_h

            # Logo occupies top 65% of bar height, text bottom 25%
            logo_h_inches = bar_height * 0.58
            logo_w_inches = logo_h_inches * img_aspect

            # Cap at 50% of figure width
            max_logo_w = fig_w * 0.50
            if logo_w_inches > max_logo_w:
                logo_w_inches = max_logo_w
                logo_h_inches = logo_w_inches / img_aspect

            # Convert to figure fractions and centre horizontally
            logo_w_frac = logo_w_inches / fig_w
            logo_h_frac = logo_h_inches / new_h
            logo_x_frac = 0.5 - logo_w_frac / 2
            logo_y_frac = (bar_height - logo_h_inches) / 2 / new_h

            logo_ax = fig.add_axes([logo_x_frac, logo_y_frac, logo_w_frac, logo_h_frac])
            logo_ax.set_facecolor(BAR_COLOR)
            logo_ax.imshow(logo_img, aspect='auto')
            logo_ax.axis('off')
        except Exception as e:
            print(f"Logo load failed: {e}")

    # # Attribution text centred below logo
    # bar_ax.text(
    #     0.5, 0.015, text,
    #     transform=bar_ax.transAxes,
    #     fontsize=TEXT_FONTSIZE, color=TEXT_COLOR,
    #     va='bottom', ha='center',
    # )

    return fig


def save_with_attribution(fig, filepath, logo_path=DEFAULT_LOGO_PATH,
                          text=ATTRIBUTION_TEXT, dpi=150, **kwargs):
    add_attribution_bar(fig, logo_path=logo_path, text=text)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight', **kwargs)
    print(f"Saved: {filepath}")

"""
Generate before/after mockups for the OSU Moritz Law public website migration.
- osu-website-before.png: 2017-era hard-coded site (cluttered, dated)
- osu-website-after.png: modern CMS redesign (clean, conversion-focused)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np

W, H = 14, 9
DPI = 140

def fig():
    f, ax = plt.subplots(figsize=(W, H), facecolor='#FFFFFF')
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis('off')
    return f, ax

def rect(ax, x, y, w, h, color, zorder=2, radius=0, alpha=1, ec='none', lw=1):
    if radius:
        p = FancyBboxPatch((x, y), w, h,
                           boxstyle=f"round,pad=0,rounding_size={radius}",
                           facecolor=color, edgecolor=ec, linewidth=lw,
                           zorder=zorder, alpha=alpha)
    else:
        p = patches.Rectangle((x, y), w, h,
                               facecolor=color, edgecolor=ec, linewidth=lw,
                               zorder=zorder, alpha=alpha)
    ax.add_patch(p)

def txt(ax, x, y, s, size=9, color='#333333', ha='left', va='bottom', bold=False, zorder=20, wrap=False):
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va,
            fontweight=weight, zorder=zorder,
            fontfamily='DejaVu Sans',
            wrap=wrap)

def divider(ax, y, color='#CCCCCC', lw=0.5):
    ax.axhline(y, color=color, linewidth=lw, zorder=3)


# ─── BEFORE (2017 legacy site) ───────────────────────────────────────────────
def build_before():
    f, ax = fig()

    BG = '#F5F4F0'
    NAV_BG = '#666666'
    ACCENT = '#BB0000'  # dark red (OSU colours, dated)
    TEXT_DARK = '#222222'
    TEXT_MID = '#555555'
    BORDER = '#BBBBBB'

    # Background
    rect(ax, 0, 0, W, H, BG)

    # ── Top utility bar (very narrow, cramped)
    rect(ax, 0, H - 0.4, W, 0.4, '#333333')
    txt(ax, 0.25, H - 0.27, 'THE OHIO STATE UNIVERSITY', size=6.5, color='#CCCCCC', bold=True)
    txt(ax, W - 0.25, H - 0.27, 'Buckeye Link  |  Webmail  |  Map  |  Find People', size=6, color='#AAAAAA', ha='right')

    # ── Nav bar
    rect(ax, 0, H - 1.05, W, 0.65, NAV_BG)
    nav_items = ['Home', 'About', 'Academics', 'Admissions', 'Faculty', 'Students', 'Alumni', 'Giving', 'Contact']
    spacing = W / len(nav_items)
    for i, item in enumerate(nav_items):
        cx = spacing * i + spacing / 2
        is_home = item == 'Home'
        if is_home:
            rect(ax, spacing * i + 0.05, H - 1.0, spacing - 0.1, 0.55, ACCENT)
        txt(ax, cx, H - 0.77, item, size=7.5, color='#FFFFFF' if is_home else '#DDDDDD', ha='center', bold=is_home)

    # ── Hero (static image placeholder, dated look with text overlay)
    rect(ax, 0, H - 3.4, W, 2.35, '#8B7355')  # brownish photo placeholder
    # Simulate old photo texture
    for i in range(0, 14, 2):
        rect(ax, i, H - 3.4, 1.8, 2.35, '#7A6848', alpha=0.3)
    # Text overlay box (old-school semi-transparent box)
    rect(ax, 0.3, H - 3.15, 5.5, 1.8, '#000000', alpha=0.55)
    txt(ax, 0.6, H - 1.85, 'Moritz College of Law', size=15, color='#FFFFFF', bold=True)
    txt(ax, 0.6, H - 2.25, 'The Ohio State University', size=9, color='#DDDDDD')
    txt(ax, 0.6, H - 2.75, 'Ranked #34 Nationally', size=8, color='#CCCCCC')

    # ── No clear CTA — just a link list in top corner
    rect(ax, 10.2, H - 2.85, 3.5, 1.3, '#EEEEEE', ec=BORDER, lw=0.5)
    txt(ax, 10.35, H - 1.75, 'Quick Links', size=7.5, color=ACCENT, bold=True)
    links = ['- Admissions Info', '- Course Schedule', '- Faculty Directory', '- Law Library', '- Student Portal']
    for i, l in enumerate(links):
        txt(ax, 10.35, H - 1.95 - i * 0.2, l, size=6.5, color='#0044BB')

    # ── Three-column content area (cluttered, no visual hierarchy)
    COL_Y = 0.4
    COL_H = H - 3.4 - COL_Y - 0.2
    col_w = W / 3 - 0.15

    for col_i, (title, items) in enumerate([
        ('News & Announcements', [
            'Faculty Spotlight: Prof. Smith publishes new paper on...',
            'Upcoming: Law Review Symposium — Feb 14',
            'Career Services: On-Campus Recruiting Spring 2017',
            'Congratulations to the Moot Court team...',
            'Spring semester registration now open',
            'Library hours updated for holidays'
        ]),
        ('Events', [
            'Feb 14 — Law Review Symposium',
            'Feb 17 — Alumni Happy Hour',
            'Feb 21 — Career Fair (all 1Ls)',
            'Feb 28 — Faculty Colloquium',
            'Mar 03 — Spring Break begins',
            'Mar 15 — Classes resume'
        ]),
        ('Announcements', [
            'New clinic offerings for 3L students...',
            'Tuition payment deadline: Jan 30',
            'Spring commencement details TBA',
            'Bar Exam prep resources available',
            'Office hours suspended Feb 20',
            'Important: email list updates'
        ]),
    ]):
        cx = col_i * (W / 3) + 0.12
        rect(ax, cx, COL_Y, col_w, COL_H, '#FFFFFF', ec=BORDER, lw=0.5)
        # Column header — ugly coloured stripe
        rect(ax, cx, COL_Y + COL_H - 0.38, col_w, 0.38, ACCENT if col_i == 0 else '#888888')
        txt(ax, cx + 0.12, COL_Y + COL_H - 0.2, title, size=7, color='#FFFFFF', bold=True)
        for j, item in enumerate(items):
            txt(ax, cx + 0.12, COL_Y + COL_H - 0.65 - j * 0.38,
                item[:52] + ('...' if len(item) > 52 else ''), size=6.5, color='#0044BB')
            divider(ax, COL_Y + COL_H - 0.72 - j * 0.38, color='#DDDDDD')

    # ── Footer
    rect(ax, 0, 0, W, 0.4, '#444444')
    txt(ax, W / 2, 0.15, '55 W 12th Ave, Columbus OH 43210  |  (614) 292-2631  |  moritz.osu.edu  |  © 2017 The Ohio State University', size=6, color='#AAAAAA', ha='center')

    # Label
    rect(ax, 0.15, H - 3.4 - 0.42, 1.1, 0.35, '#CC3333', radius=0.04)
    txt(ax, 0.7, H - 3.4 - 0.27, 'BEFORE  2017', size=7.5, color='#FFFFFF', bold=True, ha='center')

    f.savefig('assets/images/work/osu-website-before.png', dpi=DPI, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(f)
    print("Saved osu-website-before.png")


# ─── AFTER (modern CMS redesign) ────────────────────────────────────────────
def build_after():
    f, ax = fig()

    BG = '#FFFFFF'
    NAV_BG = '#FFFFFF'
    SCARLET = '#BB0000'
    DARK = '#1A1A1A'
    MID = '#555555'
    LIGHT_BG = '#F8F7F5'
    BORDER = '#E5E5E5'
    PILL_BG = '#FFF1F1'

    # Background
    rect(ax, 0, 0, W, H, BG)

    # ── Top utility bar (slim, clean)
    rect(ax, 0, H - 0.35, W, 0.35, '#F5F5F5')
    txt(ax, 0.25, H - 0.19, 'The Ohio State University', size=6.5, color='#666666')
    txt(ax, W - 0.25, H - 0.19, 'Buckeye Link  |  Webmail  |  Search', size=6.5, color='#666666', ha='right')

    # ── Clean nav bar
    rect(ax, 0, H - 0.95, W, 0.6, NAV_BG, ec=BORDER, lw=0.5)
    # Logo
    rect(ax, 0.2, H - 0.88, 0.08, 0.5, SCARLET)  # scarlet bar
    txt(ax, 0.45, H - 0.68, 'MORITZ', size=10, color=SCARLET, bold=True)
    txt(ax, 0.45, H - 0.87, 'COLLEGE OF LAW', size=5.5, color='#555555', bold=True)

    nav_items = ['Admissions', 'Academics', 'Student Life', 'Faculty & Research', 'Careers', 'About']
    for i, item in enumerate(nav_items):
        txt(ax, 3.2 + i * 1.75, H - 0.68, item, size=7.5, color=DARK)

    # Apply Now button
    rect(ax, 12.4, H - 0.88, 1.4, 0.46, SCARLET, radius=0.06)
    txt(ax, 13.1, H - 0.68, 'Apply Now', size=7.5, color='#FFFFFF', bold=True, ha='center')

    # ── Hero — full-bleed, strong photography feel
    rect(ax, 0, H - 3.7, W, 2.75, '#2C2C2C')
    # Simulate hero image with gradients
    for xi in range(14):
        shade = '#1a1a1a' if xi < 7 else '#2a3520'
        rect(ax, xi, H - 3.7, 1.05, 2.75, shade, alpha=0.8)

    # Left-aligned hero text (modern convention)
    txt(ax, 0.7, H - 1.35, 'Ranked #34 Nationally.', size=22, color='#FFFFFF', bold=True)
    txt(ax, 0.7, H - 1.8, 'Law school designed for the real world.', size=11, color='#CCCCCC')

    # Two clear CTAs
    rect(ax, 0.7, H - 2.55, 1.8, 0.5, SCARLET, radius=0.07)
    txt(ax, 1.6, H - 2.35, 'Apply Now', size=9, color='#FFFFFF', bold=True, ha='center')
    rect(ax, 2.65, H - 2.55, 2.0, 0.5, '#FFFFFF', radius=0.07, alpha=0.15, ec='#FFFFFF', lw=1)
    txt(ax, 3.65, H - 2.35, 'Explore Programs', size=9, color='#FFFFFF', bold=True, ha='center')

    # Stats on hero right side
    stats = [('11,000+', 'Alumni worldwide'), ('8', 'Hands-on clinics'), ('50+', 'Student orgs')]
    for i, (num, label) in enumerate(stats):
        sx = 9.5 + i * 1.55
        txt(ax, sx, H - 1.55, num, size=18, color='#FFFFFF', bold=True, ha='center')
        txt(ax, sx, H - 1.95, label, size=6.5, color='#AAAAAA', ha='center')
        if i < 2:
            ax.axvline(sx + 1.3, ymin=(H - 3.7) / H, ymax=(H - 0.95) / H, color='#888888', lw=0.8, zorder=5)

    # ── Three clean feature cards
    card_y = 0.7
    card_h = H - 3.7 - card_y - 0.3
    cards = [
        (PILL_BG, SCARLET, 'Admissions', 'Find your path to Moritz. Review requirements, deadlines,\nand scholarship opportunities.', 'Learn More ->'),
        ('#F0F7F0', '#1A5C1A', 'Academics', 'Explore 50+ specialisations, clinics, and dual-degree\nprogrammes built for legal careers.', 'Explore ->'),
        ('#F0F4FF', '#1A2C6B', 'Faculty & Research', 'Work with nationally recognised scholars across\nenvironmental law, IP, and criminal justice.', 'Meet the Faculty ->'),
    ]
    cw = (W - 0.6) / 3 - 0.15
    for i, (bg, accent, title, desc, cta) in enumerate(cards):
        cx = 0.2 + i * (cw + 0.15)
        rect(ax, cx, card_y, cw, card_h, bg, radius=0.1, ec=BORDER, lw=0.5)
        rect(ax, cx, card_y + card_h - 0.04, cw, 0.04, accent, radius=0.1)
        txt(ax, cx + 0.25, card_y + card_h - 0.3, title, size=10, color=accent, bold=True)
        txt(ax, cx + 0.25, card_y + card_h - 0.6, desc, size=7, color=MID, wrap=False)
        # CTA link
        txt(ax, cx + 0.25, card_y + 0.2, cta, size=7.5, color=accent, bold=True)

    # ── Footer
    rect(ax, 0, 0, W, 0.7, '#1A1A1A')
    txt(ax, 0.4, 0.42, 'Moritz College of Law', size=7.5, color='#FFFFFF', bold=True)
    txt(ax, 0.4, 0.22, '55 W 12th Ave, Columbus OH 43210', size=6.5, color='#999999')
    for j, link in enumerate(['Admissions', 'Academics', 'Careers', 'Library', 'Alumni']):
        txt(ax, 3.5 + j * 1.6, 0.32, link, size=6.5, color='#CCCCCC')

    # After label
    rect(ax, 0.15, H - 3.7 - 0.42, 1.1, 0.35, '#1A5C1A', radius=0.04)
    txt(ax, 0.7, H - 3.7 - 0.27, 'AFTER  2024', size=7.5, color='#FFFFFF', bold=True, ha='center')

    f.savefig('assets/images/work/osu-website-after.png', dpi=DPI, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(f)
    print("Saved osu-website-after.png")


if __name__ == '__main__':
    import os
    os.chdir('/Users/katrinab/ktrnab.github.io')
    build_before()
    build_after()
    print("Done.")

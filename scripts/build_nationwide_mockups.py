#!/usr/bin/env python3
"""
Build Nationwide Insurance intranet case study mockup images:
1. Editorial content calendar (Figma-style)
2. Proposed intranet IA / site map
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

IMG_DIR = "/Users/katrinab/ktrnab.github.io/assets/images/work"
os.makedirs(IMG_DIR, exist_ok=True)

# ── PALETTE ──────────────────────────────────────────────────────────────────
C_DARK    = "#2a5c27"
C_MID     = "#3d7a39"
C_LIGHT   = "#cae896"
C_CREAM   = "#edf0e5"
C_SURFACE = "#f5f7f0"
C_MUTED   = "#6a8c65"
C_TEXT    = "#1e2a1c"
C_BORDER  = "#d4dace"
C_WHITE   = "#ffffff"
C_GRAY    = "#f0f0f0"

# Content type colors
TYPE_COLORS = {
    "Email Newsletter":   ("#2a5c27", "#e8f5e9"),
    "Intranet Post":      ("#1565c0", "#e3f2fd"),
    "Manager Briefing":   ("#6a1b9a", "#f3e5f5"),
    "Town Hall / Event":  ("#e65100", "#fff3e0"),
    "Survey / Feedback":  ("#558b2f", "#f1f8e9"),
    "Policy Update":      ("#37474f", "#eceff1"),
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
})

# ════════════════════════════════════════════════════════════════════════════
# IMAGE 1: EDITORIAL CONTENT CALENDAR
# ════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(C_WHITE)
ax.set_facecolor(C_WHITE)
ax.axis("off")
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)

# ── Header bar ───────────────────────────────────────────────────────────────
ax.add_patch(FancyBboxPatch((0, 9.0), 16, 1.0,
    boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none"))

ax.text(0.4, 9.55, "Nationwide Insurance — Internal Comms Content Calendar",
        fontsize=13, fontweight="bold", color=C_WHITE, va="center")
ax.text(0.4, 9.18, "March 2018  ·  Q1 Planning View",
        fontsize=9, color="#cae896", va="center")

# Month label (right)
ax.text(15.6, 9.38, "March", fontsize=18, fontweight="bold",
        color=C_LIGHT, va="center", ha="right", alpha=0.4)

# ── Week columns ─────────────────────────────────────────────────────────────
col_x     = [1.8, 5.0, 8.2, 11.4]
col_w     = 3.0
week_labels = ["Week 1  (Mar 1–7)", "Week 2  (Mar 8–14)",
               "Week 3  (Mar 15–21)", "Week 4  (Mar 22–31)"]

for i, (x, label) in enumerate(zip(col_x, week_labels)):
    bg = C_SURFACE if i % 2 == 0 else C_WHITE
    ax.add_patch(FancyBboxPatch((x - 0.1, 0.3), col_w + 0.1, 8.5,
        boxstyle="square,pad=0", facecolor=bg, edgecolor=C_BORDER, linewidth=0.5))
    ax.text(x + col_w/2 - 0.05, 8.65, label,
            fontsize=8.5, fontweight="bold", color=C_MUTED,
            ha="center", va="center")

# ── Row labels (channels) ─────────────────────────────────────────────────────
rows = [
    ("Email Newsletter",  7.6),
    ("Intranet Post",     6.3),
    ("Manager Briefing",  5.0),
    ("Town Hall / Event", 3.7),
    ("Survey / Feedback", 2.4),
    ("Policy Update",     1.1),
]

# Row label column background
ax.add_patch(FancyBboxPatch((0, 0.3), 1.75, 8.5,
    boxstyle="square,pad=0", facecolor=C_SURFACE, edgecolor=C_BORDER, linewidth=0.5))

ax.text(0.875, 8.65, "Channel", fontsize=8.5, fontweight="bold",
        color=C_MUTED, ha="center", va="center")

for label, y in rows:
    dot_color = TYPE_COLORS[label][0]
    ax.add_patch(plt.Circle((0.22, y + 0.55), 0.06, color=dot_color))
    ax.text(0.35, y + 0.55, label, fontsize=8, color=C_TEXT,
            va="center", fontweight="500")
    # Horizontal divider
    ax.plot([0, 16], [y - 0.05, y - 0.05], color=C_BORDER, linewidth=0.5)

# ── Content blocks ────────────────────────────────────────────────────────────
# Format: (channel_label, week_index 0-3, content_title, span_weeks)
content_blocks = [
    # Email Newsletter
    ("Email Newsletter",   0, "Welcome Back: Q1 Kick-Off",       1),
    ("Email Newsletter",   1, "Benefits Open Enrolment Reminder", 1),
    ("Email Newsletter",   2, "Town Hall Recap",                  1),
    ("Email Newsletter",   3, "March Wrap-Up",                    1),
    # Intranet Post
    ("Intranet Post",      0, "IT System Update Notice",          1),
    ("Intranet Post",      1, "New HR Policy: Remote Work",       2),
    ("Intranet Post",      3, "Q2 Planning Resources Live",       1),
    # Manager Briefing
    ("Manager Briefing",   0, "Q1 OKR Alignment Brief",          1),
    ("Manager Briefing",   2, "Performance Review Guidance",      2),
    # Town Hall / Event
    ("Town Hall / Event",  1, "All-Hands Town Hall",              2),
    # Survey / Feedback
    ("Survey / Feedback",  0, "Intranet UX Survey Launch",       2),
    ("Survey / Feedback",  3, "Survey Close & Results",          1),
    # Policy Update
    ("Policy Update",      1, "Data Privacy Policy Update",      1),
    ("Policy Update",      3, "Updated Travel & Expense Policy", 1),
]

row_y = {label: y for label, y in rows}

for ch, week_idx, title, span in content_blocks:
    x_start = col_x[week_idx] + 0.08
    width   = col_w * span - 0.16 + (col_x[min(week_idx + span, 3)] - col_x[week_idx] if span > 1 else 0)
    if span > 1:
        width = col_x[min(week_idx + span - 1, 3)] + col_w - col_x[week_idx] - 0.16
    y_base  = row_y[ch] + 0.08
    h       = 0.88

    fc, bc = TYPE_COLORS[ch][1], TYPE_COLORS[ch][0]

    ax.add_patch(FancyBboxPatch((x_start, y_base), width, h,
        boxstyle="round,pad=0.04", facecolor=fc,
        edgecolor=bc, linewidth=1.2, zorder=3))

    # Left accent
    ax.add_patch(FancyBboxPatch((x_start, y_base), 0.12, h,
        boxstyle="square,pad=0", facecolor=bc, edgecolor="none", zorder=4))

    # Title text
    max_chars = int(width * 11)
    display = title if len(title) <= max_chars else title[:max_chars - 1] + "…"
    ax.text(x_start + 0.22, y_base + h/2, display,
            fontsize=7.5, color=bc, va="center", fontweight="600",
            zorder=5, clip_on=True)

# ── Legend ────────────────────────────────────────────────────────────────────
legend_x = 0.05
ax.text(legend_x, 0.22, "Content type:", fontsize=7.5, color=C_MUTED, va="center")
lx = 1.1
for label, (dark, light) in TYPE_COLORS.items():
    ax.add_patch(FancyBboxPatch((lx, 0.09), 0.14, 0.24,
        boxstyle="round,pad=0.02", facecolor=light, edgecolor=dark, linewidth=1))
    short = label.split(" ")[0]
    ax.text(lx + 0.19, 0.22, short, fontsize=7, color=dark, va="center", fontweight="600")
    lx += 0.95 + len(short) * 0.055

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-calendar.png", dpi=160, bbox_inches="tight",
            facecolor=C_WHITE)
plt.close()
print(f"✓ Saved: {IMG_DIR}/nationwide-calendar.png")


# ════════════════════════════════════════════════════════════════════════════
# IMAGE 2: PROPOSED INTRANET IA / SITEMAP
# ════════════════════════════════════════════════════════════════════════════

fig2, ax2 = plt.subplots(figsize=(16, 9))
fig2.patch.set_facecolor(C_WHITE)
ax2.set_facecolor(C_WHITE)
ax2.axis("off")
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 9)

# ── Title ─────────────────────────────────────────────────────────────────────
ax2.add_patch(FancyBboxPatch((0, 8.2), 16, 0.8,
    boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none"))
ax2.text(0.5, 8.62, "Nationwide Insurance Intranet — Proposed Information Architecture",
         fontsize=12, fontweight="bold", color=C_WHITE, va="center")
ax2.text(0.5, 8.32, "Based on findings from employee surveys and user interviews  ·  March 2018",
         fontsize=8.5, color=C_LIGHT, va="center")

def node(ax, x, y, w, h, label, sublabel=None, level=0):
    colors = [C_DARK, C_MID, "#e8f5e9", C_SURFACE]
    text_colors = [C_WHITE, C_WHITE, C_TEXT, C_MUTED]
    edge_colors = [C_DARK, C_MID, C_MID, C_BORDER]
    lw = [0, 0, 1.5, 1]

    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.06",
        facecolor=colors[level], edgecolor=edge_colors[level],
        linewidth=lw[level], zorder=3))

    fs = [10, 9, 8, 7.5][level]
    fw = ["bold", "bold", "600", "normal"][level]
    ax.text(x, y + (0.06 if sublabel else 0), label,
            fontsize=fs, fontweight=fw, color=text_colors[level],
            ha="center", va="center", zorder=4)
    if sublabel:
        ax.text(x, y - 0.18, sublabel,
                fontsize=6.5, color=text_colors[level], alpha=0.75,
                ha="center", va="center", zorder=4)

def connector(ax, x1, y1, x2, y2, color=C_BORDER):
    mid_y = (y1 + y2) / 2
    ax.plot([x1, x1, x2, x2], [y1, mid_y, mid_y, y2],
            color=color, linewidth=1.2, zorder=1, solid_capstyle="round")

# ── Root node ─────────────────────────────────────────────────────────────────
root_x, root_y = 8, 7.4
node(ax2, root_x, root_y, 2.8, 0.55, "Intranet Home", level=0)

# ── Level 1: main sections ────────────────────────────────────────────────────
l1_nodes = [
    (2.2,  5.9, "For Employees"),
    (6.0,  5.9, "For Managers"),
    (10.0, 5.9, "News & Updates"),
    (13.8, 5.9, "Quick Links"),
]
for x, y, label in l1_nodes:
    connector(ax2, root_x, root_y - 0.28, x, y + 0.28, C_MID)
    node(ax2, x, y, 2.8, 0.52, label, level=1)

# ── Level 2: sub-pages ───────────────────────────────────────────────────────
l2_map = {
    2.2: [
        (0.8,  4.4, "HR &\nBenefits"),
        (2.2,  4.4, "IT &\nSystems"),
        (3.6,  4.4, "Policies &\nForms"),
    ],
    6.0: [
        (4.8,  4.4, "Team\nResources"),
        (6.0,  4.4, "Reporting\n& OKRs"),
        (7.2,  4.4, "Comms\nToolkit"),
    ],
    10.0: [
        (8.8,  4.4, "Company\nNews"),
        (10.0, 4.4, "Department\nUpdates"),
        (11.2, 4.4, "Events &\nCalendar"),
    ],
    13.8: [
        (12.8, 4.4, "IT Help\nDesk"),
        (13.8, 4.4, "Directory"),
        (14.8, 4.4, "Facilities"),
    ],
}

for parent_x, children in l2_map.items():
    parent_y = 5.9
    for cx, cy, label in children:
        connector(ax2, parent_x, parent_y - 0.26, cx, cy + 0.28, C_BORDER)
        node(ax2, cx, cy, 1.08, 0.52, label, level=2)

# ── Level 3: sample leaf nodes (just under HR & News) ────────────────────────
l3_map = {
    (0.8, 4.4): [(0.3, 3.1, "Benefits\nEnrolment"), (1.3, 3.1, "Pay &\nPayroll")],
    (8.8, 4.4): [(8.3, 3.1, "All-Staff\nAnnouncements"), (9.3, 3.1, "Leadership\nMessages")],
}

for (px, py), children in l3_map.items():
    for cx, cy, label in children:
        connector(ax2, px, py - 0.26, cx, cy + 0.26, C_BORDER)
        node(ax2, cx, cy, 0.9, 0.46, label, level=3)

# ── Legend ────────────────────────────────────────────────────────────────────
legend_items = [
    (C_DARK,    C_DARK,   "Homepage"),
    (C_MID,     C_MID,    "Primary section"),
    ("#e8f5e9", C_MID,    "Sub-page"),
    (C_SURFACE, C_BORDER, "Leaf page"),
]
lx2 = 0.4
ly2 = 0.45
ax2.text(lx2, ly2, "Node key:", fontsize=7.5, color=C_MUTED, va="center")
lx2 += 0.9
for fc, ec, label in legend_items:
    ax2.add_patch(FancyBboxPatch((lx2, ly2 - 0.14), 0.26, 0.26,
        boxstyle="round,pad=0.03", facecolor=fc, edgecolor=ec, linewidth=1))
    ax2.text(lx2 + 0.34, ly2, label, fontsize=7.5, color=C_TEXT, va="center")
    lx2 += 1.55

# Research note
ax2.text(15.6, 0.45,
         "IA derived from\n12 employee interviews\n& 84-response survey",
         fontsize=7, color=C_MUTED, ha="right", va="center",
         linespacing=1.5)

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-ia.png", dpi=160, bbox_inches="tight",
            facecolor=C_WHITE)
plt.close()
print(f"✓ Saved: {IMG_DIR}/nationwide-ia.png")

print("\nAll Nationwide mockups generated.")

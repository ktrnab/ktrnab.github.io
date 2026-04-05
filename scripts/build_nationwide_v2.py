#!/usr/bin/env python3
"""
Nationwide case study visuals v2:
1. IA Before & After
2. User Journey Map
3. Editorial Calendar (polished)
4. Quick Links Panel
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

IMG_DIR = "/Users/katrinab/ktrnab.github.io/assets/images/work"

# Palette
C_DARK    = "#2a5c27"
C_MID     = "#3d7a39"
C_LIGHT   = "#cae896"
C_CREAM   = "#edf0e5"
C_SURFACE = "#f5f7f0"
C_MUTED   = "#6a8c65"
C_TEXT    = "#1e2a1c"
C_BORDER  = "#d4dace"
C_WHITE   = "#ffffff"
C_RED     = "#c0392b"
C_RED_BG  = "#fdf0ee"
C_ORANGE  = "#e67e22"

plt.rcParams.update({"font.family": "sans-serif"})

def box(ax, x, y, w, h, fc, ec, lw=1.2, radius=0.06, zorder=3):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle=f"round,pad={radius}", facecolor=fc, edgecolor=ec,
        linewidth=lw, zorder=zorder))

def label(ax, x, y, text, size=8.5, color=C_TEXT, weight="normal",
          ha="center", va="center", zorder=5):
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=zorder, linespacing=1.4)

def arrow(ax, x1, y1, x2, y2, color=C_BORDER, lw=1.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>", color=color,
                        lw=lw, mutation_scale=10))

def section_header(ax, x, y, w, text):
    ax.add_patch(FancyBboxPatch((x, y), w, 0.45,
        boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none", zorder=4))
    ax.text(x + 0.18, y + 0.225, text, fontsize=9, fontweight="bold",
            color=C_WHITE, va="center", zorder=5)

# ════════════════════════════════════════════════════════════════════════════
# 1. IA BEFORE & AFTER
# ════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(16, 9))
fig.patch.set_facecolor(C_WHITE)

for ax in axes:
    ax.axis("off")
    ax.set_facecolor(C_WHITE)

ax_b = axes[0]
ax_a = axes[1]

ax_b.set_xlim(0, 8)
ax_b.set_ylim(0, 9)
ax_a.set_xlim(0, 8)
ax_a.set_ylim(0, 9)

# ── BEFORE (left) ────────────────────────────────────────────────────────────
section_header(ax_b, 0.2, 8.3, 7.6, "BEFORE  ·  Organisation-Centric Model")

# Root
box(ax_b, 4, 7.4, 3.0, 0.52, C_RED_BG, C_RED, lw=1.8)
label(ax_b, 4, 7.4, "Intranet Home", 9, C_RED, "bold")

# L1 departments
depts = ["Claims", "Underwriting", "Finance\n& Risk", "Human\nResources",
         "IT &\nSystems", "Legal", "Marketing", "Corporate\nAffairs"]
xs = np.linspace(0.6, 7.4, len(depts))
for x, dept in zip(xs, depts):
    # connector
    ax_b.plot([4, x], [7.14, 6.22], color="#e0b0a8", lw=1, zorder=1)
    box(ax_b, x, 5.9, 0.82, 0.58, C_RED_BG, C_RED, lw=1.2, radius=0.04)
    label(ax_b, x, 5.9, dept, 7, C_RED)

# Sub-pages (just under HR)
hr_x = xs[3]
sub_hr = ["Pay &\nPayroll", "Benefits", "Forms &\nPolicies", "Training"]
sub_xs = np.linspace(hr_x - 1.2, hr_x + 1.2, 4)
for sx, sub in zip(sub_xs, sub_hr):
    ax_b.plot([hr_x, sx], [5.61, 4.72], color="#e0b0a8", lw=0.8, zorder=1)
    box(ax_b, sx, 4.44, 0.68, 0.48, C_RED_BG, C_RED, lw=0.8, radius=0.03)
    label(ax_b, sx, 4.44, sub, 6.5, C_RED)

# Problem annotation
ax_b.add_patch(FancyBboxPatch((0.3, 0.4), 7.4, 2.5,
    boxstyle="round,pad=0.1", facecolor=C_RED_BG, edgecolor=C_RED,
    linewidth=1, zorder=2, alpha=0.7))
label(ax_b, 4, 3.55, "Pain Points", 9, C_RED, "bold")
pain = [
    "4+ clicks to reach most resources",
    "Navigation mirrors org chart, not daily tasks",
    "Content siloed across departments & SharePoint",
    "Repeat support tickets for \"lost\" information",
]
for i, p in enumerate(pain):
    label(ax_b, 0.65, 3.1 - i * 0.46, f"✕  {p}", 8, C_RED, ha="left")

# ── AFTER (right) ─────────────────────────────────────────────────────────────
section_header(ax_a, 0.2, 8.3, 7.6, "AFTER  ·  Task-Based Model")

# Root
box(ax_a, 4, 7.4, 3.0, 0.52, C_DARK, "none")
label(ax_a, 4, 7.4, "Intranet Home", 9, C_WHITE, "bold")

# L1 - 4 paths
l1 = [("For\nEmployees", 1.5), ("For\nManagers", 3.5),
      ("News &\nUpdates", 5.5), ("Quick\nLinks", 7.0)]
for name, x in l1:
    ax_a.plot([4, x], [7.14, 6.22], color=C_LIGHT, lw=1.2, zorder=1)
    box(ax_a, x, 5.9, 1.5, 0.58, C_MID, "none", radius=0.05)
    label(ax_a, x, 5.9, name, 8, C_WHITE, "bold")

# Sub-pages under Employees
emp_subs = ["Pay &\nPayroll", "Benefits", "HR\nForms", "Policies"]
emp_xs = np.linspace(0.5, 2.5, 4)
for ex, sub in zip(emp_xs, emp_subs):
    ax_a.plot([1.5, ex], [5.61, 4.72], color=C_LIGHT, lw=0.8, zorder=1)
    box(ax_a, ex, 4.44, 0.75, 0.48, "#e8f5e9", C_MID, lw=1, radius=0.04)
    label(ax_a, ex, 4.44, sub, 6.5, C_MID)

# Sub-pages under Managers
mgr_subs = ["Team\nMetrics", "Capacity\nPlanning", "Approvals"]
mgr_xs = np.linspace(2.7, 4.3, 3)
for mx, sub in zip(mgr_subs, mgr_subs):
    ax_a.plot([3.5, mgr_xs[list(mgr_subs).index(sub)]], [5.61, 4.72],
              color=C_LIGHT, lw=0.8, zorder=1)
    box(ax_a, mgr_xs[list(mgr_subs).index(sub)], 4.44, 0.82, 0.48,
        "#e8f5e9", C_MID, lw=1, radius=0.04)
    label(ax_a, mgr_xs[list(mgr_subs).index(sub)], 4.44, sub, 6.5, C_MID)

# Outcome annotation
ax_a.add_patch(FancyBboxPatch((0.3, 0.4), 7.4, 2.5,
    boxstyle="round,pad=0.1", facecolor="#e8f5e9", edgecolor=C_MID,
    linewidth=1, zorder=2, alpha=0.8))
label(ax_a, 4, 3.55, "Outcomes", 9, C_MID, "bold")
outcomes = [
    "2 clicks to any key resource",
    "Navigation reflects employee workflows",
    "Persistent Quick Links surface top-tier requests",
    "Centralised content planning across all channels",
]
for i, o in enumerate(outcomes):
    label(ax_a, 0.65, 3.1 - i * 0.46, f"✓  {o}", 8, C_DARK, ha="left")

# Divider
fig.add_artist(plt.Line2D([0.5, 0.5], [0.05, 0.95],
    transform=fig.transFigure, color=C_BORDER, lw=1))

plt.tight_layout(pad=1.5)
plt.savefig(f"{IMG_DIR}/nationwide-ia-before-after.png", dpi=160,
            bbox_inches="tight", facecolor=C_WHITE)
plt.close()
print("✓ IA before/after saved")


# ════════════════════════════════════════════════════════════════════════════
# 2. USER JOURNEY MAP
# ════════════════════════════════════════════════════════════════════════════
fig2, ax = plt.subplots(figsize=(16, 7))
fig2.patch.set_facecolor(C_WHITE)
ax.set_facecolor(C_WHITE)
ax.axis("off")
ax.set_xlim(0, 16)
ax.set_ylim(0, 7)

# Title
ax.add_patch(FancyBboxPatch((0, 6.3), 16, 0.7,
    boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none"))
label(ax, 8, 6.65, "Employee Journey: Finding HR Benefits Information",
      12, C_WHITE, "bold")

# Lane labels
ax.add_patch(FancyBboxPatch((0, 3.4), 1.5, 2.65,
    boxstyle="square,pad=0", facecolor=C_RED_BG, edgecolor=C_BORDER, lw=0.5))
ax.add_patch(FancyBboxPatch((0, 0.5), 1.5, 2.65,
    boxstyle="square,pad=0", facecolor="#e8f5e9", edgecolor=C_BORDER, lw=0.5))

label(ax, 0.75, 4.72, "BEFORE", 8.5, C_RED, "bold")
label(ax, 0.75, 4.4, "Org-chart\nmodel", 7.5, C_RED)
label(ax, 0.75, 1.82, "AFTER", 8.5, C_MID, "bold")
label(ax, 0.75, 1.5, "Task-based\nmodel", 7.5, C_MID)

# ── BEFORE journey ────────────────────────────────────────────────────────────
before_steps = [
    (2.5,  4.7, "Homepage",         "Starting\npoint",       C_RED_BG, C_RED),
    (4.5,  4.7, "Human\nResources", "Wrong\ndepartment",     C_RED_BG, C_RED),
    (6.5,  4.7, "HR Sub-page",      "Still\nsearching",      C_RED_BG, C_RED),
    (8.5,  4.7, "Benefits\nHome",   "Found it?\nMaybe…",     C_RED_BG, C_RED),
    (10.5, 4.7, "Dead End",         "Wrong\npage",           "#c0392b", "none"),
    (12.8, 4.7, "IT Support\nTicket", "Gave up",             "#c0392b", "none"),
]

for i, (x, y, title, sub, fc, ec) in enumerate(before_steps):
    is_end = ec == "none"
    box(ax, x, y, 1.55, 0.72, fc, C_RED if is_end else ec,
        lw=2 if is_end else 1.2, radius=0.05)
    tc = C_WHITE if is_end else C_RED
    label(ax, x, y + 0.1, title, 8, tc, "bold" if is_end else "600")
    label(ax, x, y - 0.22, sub, 6.5, tc)
    if i < len(before_steps) - 1:
        next_x = before_steps[i+1][0]
        arrow(ax, x + 0.78, y, next_x - 0.78, y, C_RED)
    # Step number
    ax.add_patch(plt.Circle((x - 0.62, y + 0.28), 0.14,
        color=C_RED, zorder=6))
    label(ax, x - 0.62, y + 0.28, str(i+1), 6.5, C_WHITE, "bold")

# Click count labels above
for i, (x, y, *_) in enumerate(before_steps[:-1]):
    ax.text(before_steps[i][0] + (before_steps[i+1][0]-before_steps[i][0])/2,
            y + 0.55, f"click {i+1}", fontsize=6.5, color=C_RED,
            ha="center", va="center", style="italic")

# ── AFTER journey ─────────────────────────────────────────────────────────────
after_steps = [
    (2.5,  1.8, "Homepage",      "Starting\npoint",    "#e8f5e9", C_MID),
    (5.2,  1.8, "For\nEmployees","Right\npath",        "#e8f5e9", C_MID),
    (7.9,  1.8, "HR &\nBenefits","Found it.",          C_MID,     "none"),
]

for i, (x, y, title, sub, fc, ec) in enumerate(after_steps):
    is_end = ec == "none"
    box(ax, x, y, 1.8, 0.72, fc, C_MID if is_end else ec,
        lw=2.5 if is_end else 1.5, radius=0.05)
    tc = C_WHITE if is_end else C_MID
    label(ax, x, y + 0.1, title, 8.5, tc, "bold")
    label(ax, x, y - 0.22, sub, 7, tc)
    if i < len(after_steps) - 1:
        next_x = after_steps[i+1][0]
        arrow(ax, x + 0.9, y, next_x - 0.9, y, C_MID, lw=1.8)
    ax.add_patch(plt.Circle((x - 0.74, y + 0.28), 0.14,
        color=C_MID, zorder=6))
    label(ax, x - 0.74, y + 0.28, str(i+1), 6.5, C_WHITE, "bold")

for i, (x, y, *_) in enumerate(after_steps[:-1]):
    ax.text(after_steps[i][0] + (after_steps[i+1][0]-after_steps[i][0])/2,
            y + 0.55, f"click {i+1}", fontsize=6.5, color=C_MID,
            ha="center", va="center", style="italic")

# ✓ badge on final after step
label(ax, 10.2, 1.8, "✓  2 clicks vs 4+", 9, C_MID, "bold")
label(ax, 10.2, 1.45, "No dead ends · No support ticket", 8, C_MUTED)

# Horizontal divider between lanes
ax.plot([0, 16], [3.35, 3.35], color=C_BORDER, lw=1)

plt.tight_layout(pad=0.5)
plt.savefig(f"{IMG_DIR}/nationwide-journey.png", dpi=160,
            bbox_inches="tight", facecolor=C_WHITE)
plt.close()
print("✓ Journey map saved")


# ════════════════════════════════════════════════════════════════════════════
# 3. EDITORIAL CALENDAR v2 (polished)
# ════════════════════════════════════════════════════════════════════════════
TYPE_COLORS = {
    "Email Newsletter":  ("#2a5c27", "#e8f5e9", "◆"),
    "Intranet Post":     ("#1565c0", "#e3f2fd", "●"),
    "Manager Briefing":  ("#6a1b9a", "#f3e5f5", "■"),
    "Town Hall":         ("#e65100", "#fff3e0", "▲"),
    "Survey":            ("#00695c", "#e0f2f1", "★"),
    "Policy Update":     ("#37474f", "#eceff1", "◉"),
}

weeks = ["Week 1\nMar 1–7", "Week 2\nMar 8–14",
         "Week 3\nMar 15–21", "Week 4\nMar 22–31"]
channels = list(TYPE_COLORS.keys())

fig3, ax3 = plt.subplots(figsize=(16, 9.5))
fig3.patch.set_facecolor(C_WHITE)
ax3.set_facecolor(C_WHITE)
ax3.axis("off")
ax3.set_xlim(0, 16)
ax3.set_ylim(0, 9.5)

# Top header bar
ax3.add_patch(FancyBboxPatch((0, 8.8), 16, 0.7,
    boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none"))
label(ax3, 5, 9.15, "Internal Comms — Content Calendar", 13, C_WHITE, "bold", ha="left")
label(ax3, 5, 8.93, "Nationwide Insurance  ·  March 2018  ·  Q1 Planning View",
      8.5, C_LIGHT, ha="left")
label(ax3, 15.6, 9.05, "March 2018", 20, C_LIGHT, ha="right")
ax3.text(15.6, 9.05, "March 2018", fontsize=20, fontweight="bold",
         color=C_LIGHT, ha="right", va="center", alpha=0.25, zorder=2)

# Column setup
label_col_w = 2.2
col_start = label_col_w + 0.1
col_w = (16 - col_start - 0.2) / 4
row_h = 1.15
top_y = 8.55
header_h = 0.45

# Week headers
for i, week in enumerate(weeks):
    cx = col_start + i * col_w + col_w / 2
    bg = C_SURFACE if i % 2 == 0 else "#f0f3ec"
    ax3.add_patch(FancyBboxPatch((col_start + i * col_w, top_y - header_h),
        col_w - 0.05, header_h,
        boxstyle="square,pad=0", facecolor=bg, edgecolor=C_BORDER, lw=0.5))
    label(ax3, cx, top_y - header_h / 2, week, 8, C_MUTED, "bold")

# Channel label column header
ax3.add_patch(FancyBboxPatch((0, top_y - header_h), label_col_w, header_h,
    boxstyle="square,pad=0", facecolor=C_SURFACE, edgecolor=C_BORDER, lw=0.5))
label(ax3, label_col_w / 2, top_y - header_h / 2, "Channel", 8, C_MUTED, "bold")

# Rows
for r, ch in enumerate(channels):
    dark, light, icon = TYPE_COLORS[ch]
    y_top = top_y - header_h - r * row_h
    y_mid = y_top - row_h / 2

    # Alternating row bg
    row_bg = C_WHITE if r % 2 == 0 else C_SURFACE
    ax3.add_patch(FancyBboxPatch((0, y_top - row_h), 16, row_h,
        boxstyle="square,pad=0", facecolor=row_bg, edgecolor="none"))
    ax3.plot([0, 16], [y_top - row_h, y_top - row_h], color=C_BORDER, lw=0.4)

    # Channel label
    ax3.add_patch(plt.Circle((0.3, y_mid), 0.1, color=dark, zorder=4))
    label(ax3, 0.5, y_mid, icon, 8, dark, ha="left")
    label(ax3, 0.65, y_mid, ch, 8.5, C_TEXT, ha="left")

    # Week column backgrounds
    for i in range(4):
        col_bg = C_WHITE if i % 2 == 0 else "#f9faf7"
        ax3.add_patch(FancyBboxPatch((col_start + i * col_w, y_top - row_h),
            col_w - 0.05, row_h,
            boxstyle="square,pad=0", facecolor=col_bg, edgecolor=C_BORDER, lw=0.3))

# Content blocks
content = [
    (0, 0, 1, "Welcome Back: Q1 Kick-Off"),
    (0, 1, 1, "Benefits Enrolment Reminder"),
    (0, 2, 1, "Town Hall Recap"),
    (0, 3, 1, "March Wrap-Up"),
    (1, 0, 1, "IT System Update Notice"),
    (1, 1, 2, "New HR Policy: Remote Work"),
    (1, 3, 1, "Q2 Planning Resources Live"),
    (2, 0, 1, "Q1 OKR Alignment Brief"),
    (2, 2, 2, "Performance Review Guidance"),
    (3, 1, 2, "All-Hands Town Hall"),
    (4, 0, 2, "Intranet UX Survey Launch"),
    (4, 3, 1, "Survey Close & Results"),
    (5, 1, 1, "Data Privacy Policy Update"),
    (5, 3, 1, "Updated Travel Policy"),
]

for ch_idx, week_idx, span, title in content:
    ch = channels[ch_idx]
    dark, light, icon = TYPE_COLORS[ch]
    y_top = top_y - header_h - ch_idx * row_h
    y_mid = y_top - row_h / 2

    x_start = col_start + week_idx * col_w + 0.08
    width = col_w * span - 0.16
    if span > 1:
        width = col_w * span - 0.16

    pad = 0.12
    bh = row_h * 0.68
    by = y_mid - bh / 2

    # Shadow
    ax3.add_patch(FancyBboxPatch((x_start + 0.04, by - 0.04), width, bh,
        boxstyle="round,pad=0.04", facecolor="#00000010", edgecolor="none", zorder=3))
    # Block
    ax3.add_patch(FancyBboxPatch((x_start, by), width, bh,
        boxstyle="round,pad=0.04", facecolor=light, edgecolor=dark,
        linewidth=1.2, zorder=4))
    # Left accent
    ax3.add_patch(FancyBboxPatch((x_start, by), 0.1, bh,
        boxstyle="square,pad=0", facecolor=dark, edgecolor="none", zorder=5))
    # Title
    max_w = int(width * 13)
    disp = title if len(title) <= max_w else title[:max_w - 1] + "…"
    label(ax3, x_start + 0.22, y_mid, disp, 7.5, dark, "600", ha="left")

# Legend
lx = 0.15
ly = 0.35
label(ax3, lx, ly, "Content type:", 7.5, C_MUTED, ha="left")
lx += 1.05
for ch, (dark, light, icon) in TYPE_COLORS.items():
    short = ch.split(" ")[0]
    ax3.add_patch(FancyBboxPatch((lx, ly - 0.13), 0.22, 0.24,
        boxstyle="round,pad=0.03", facecolor=light, edgecolor=dark, lw=1))
    label(ax3, lx + 0.11, ly, icon, 7, dark)
    label(ax3, lx + 0.3, ly, short, 7.5, dark, ha="left")
    lx += 1.35

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-calendar-v2.png", dpi=160,
            bbox_inches="tight", facecolor=C_WHITE)
plt.close()
print("✓ Calendar v2 saved")


# ════════════════════════════════════════════════════════════════════════════
# 4. QUICK LINKS PANEL
# ════════════════════════════════════════════════════════════════════════════
fig4, ax4 = plt.subplots(figsize=(14, 8))
fig4.patch.set_facecolor(C_SURFACE)
ax4.set_facecolor(C_SURFACE)
ax4.axis("off")
ax4.set_xlim(0, 14)
ax4.set_ylim(0, 8)

# Outer card
ax4.add_patch(FancyBboxPatch((0.5, 0.5), 13, 7,
    boxstyle="round,pad=0.1", facecolor=C_WHITE,
    edgecolor=C_BORDER, linewidth=1, zorder=1))

# Card header
ax4.add_patch(FancyBboxPatch((0.5, 6.6), 13, 0.9,
    boxstyle="square,pad=0", facecolor=C_DARK, edgecolor="none", zorder=2))
label(ax4, 7, 7.05, "Quick Links", 14, C_WHITE, "bold")
label(ax4, 7, 6.76, "Persistent panel — available on every page of the intranet",
      8.5, C_LIGHT)

# Description strip
ax4.add_patch(FancyBboxPatch((0.5, 5.9), 13, 0.68,
    boxstyle="square,pad=0", facecolor=C_SURFACE, edgecolor="none", zorder=2))
label(ax4, 7, 6.25,
      "The Quick Links panel surfaces the 8 most-requested resources, reducing depth-to-resource from 4 clicks to 2 on every page.",
      8.5, C_MUTED)

# Quick link items: (icon_char, label, sublabel, row, col)
links = [
    ("$", "Pay & Payroll",       "View payslips · Tax docs",       0, 0),
    ("♥", "Benefits",           "Health · Dental · Wellness",      0, 1),
    ("✎", "HR Forms",           "Requests · Leave · Policies",     0, 2),
    ("⚙", "IT Help Desk",       "Raise a ticket · FAQs",          0, 3),
    ("☎", "Staff Directory",    "Search by name or team",          1, 0),
    ("◉", "Room Booking",       "Reserve a space",                 1, 1),
    ("▶", "Learning Hub",       "Courses · Certifications",        1, 2),
    ("✱", "Policy Library",     "Compliance · Travel · Expenses",  1, 3),
]

card_w = 2.8
card_h = 1.9
start_x = 1.0
start_y = 4.8
gap_x = 3.05
gap_y = 2.15

for icon, name, sub, row, col in links:
    cx = start_x + col * gap_x
    cy = start_y - row * gap_y

    # Card shadow
    ax4.add_patch(FancyBboxPatch((cx + 0.06, cy - card_h + 0.06 - 0.06),
        card_w, card_h,
        boxstyle="round,pad=0.08", facecolor="#00000010",
        edgecolor="none", zorder=2))

    # Card
    ax4.add_patch(FancyBboxPatch((cx, cy - card_h + 0.06), card_w, card_h,
        boxstyle="round,pad=0.08", facecolor=C_WHITE,
        edgecolor=C_BORDER, linewidth=1.2, zorder=3))

    # Icon circle
    icon_y = cy - 0.45
    ax4.add_patch(plt.Circle((cx + 0.55, icon_y), 0.28,
        color=C_LIGHT, zorder=4))
    label(ax4, cx + 0.55, icon_y, icon, 11, C_DARK, "bold")

    # Text
    label(ax4, cx + 1.05, icon_y + 0.08, name, 9, C_TEXT, "bold", ha="left")
    label(ax4, cx + 1.05, icon_y - 0.28, sub, 7.5, C_MUTED, ha="left")

    # Top accent line
    ax4.add_patch(FancyBboxPatch((cx, cy - 0.02 + 0.06), card_w, 0.08,
        boxstyle="square,pad=0", facecolor=C_MID, edgecolor="none", zorder=4))

    # "Used by X employees" note
    uses = [847, 612, 491, 388, 275, 244, 198, 156]
    label(ax4, cx + card_w - 0.15, cy - card_h + 0.3,
          f"{uses[links.index((icon, name, sub, row, col))]:,} uses/mo",
          6.5, C_MUTED, ha="right")

# Footer note
label(ax4, 7, 0.32,
      "Click frequency data drawn from 3-month intranet analytics audit  ·  Used to prioritise panel placement",
      7.5, C_MUTED)

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-quicklinks.png", dpi=160,
            bbox_inches="tight", facecolor=C_SURFACE)
plt.close()
print("✓ Quick Links panel saved")

print("\nAll visuals generated.")

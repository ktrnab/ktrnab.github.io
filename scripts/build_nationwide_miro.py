#!/usr/bin/env python3
"""
Nationwide case study — Miro board aesthetic (refined)
Dot-grid canvas, polished frames, sticky notes, clean connectors
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

IMG_DIR = "/Users/katrinab/ktrnab.github.io/assets/images/work"

CANVAS = "#F0F0EF"; WHITE = "#FFFFFF"; FBD = "#CACAC8"; DOT = "#D8D8D5"

S_YELLOW="#FFF9C4"; S_YELLOW_D="#E6A817"
S_GREEN="#DCEDC8";  S_GREEN_D="#558B2F"
S_BLUE="#BBDEFB";   S_BLUE_D="#1565C0"
S_RED="#FFCDD2";    S_RED_D="#C62828"
S_ORANGE="#FFE0B2"; S_ORANGE_D="#E65100"
S_PURPLE="#E1BEE7"; S_PURPLE_D="#6A1B9A"
S_TEAL="#B2DFDB";   S_TEAL_D="#00695C"
S_GRAY="#ECEFF1";   S_GRAY_D="#455A64"

G_DARK="#2A5C27"; G_MID="#3D7A39"; G_LIGHT="#CAE896"
T_DARK="#1A1A1A"; T_MID="#4A4A4A"; T_MUTED="#909090"

plt.rcParams.update({"font.family": "sans-serif"})


def dot_grid(ax, xlim, ylim, spacing=0.55):
    xs = np.arange(spacing, xlim - spacing/2, spacing)
    ys = np.arange(spacing, ylim - spacing/2, spacing)
    gx, gy = np.meshgrid(xs, ys)
    ax.scatter(gx.ravel(), gy.ravel(), s=1.2, color=DOT, zorder=0, linewidths=0)


def txt(ax, x, y, s, size=8.5, color=T_DARK, weight="normal",
        ha="center", va="center", style="normal", zorder=20):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, style=style, zorder=zorder, linespacing=1.4)


def shadow(ax, x, y, w, h, r=0.06, zorder=4):
    ax.add_patch(FancyBboxPatch((x+0.055, y-0.055), w, h,
        boxstyle=f"round,pad={r}", facecolor="#00000016",
        edgecolor="none", zorder=zorder))


def card(ax, x, y, w, h, fc=WHITE, ec=FBD, lw=1.1, r=0.06,
         zorder=5, do_shadow=True):
    if do_shadow: shadow(ax, x, y, w, h, r, zorder)
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad={r}", facecolor=fc,
        edgecolor=ec, linewidth=lw, zorder=zorder+1))


def frame(ax, x, y, w, h, title, tc=G_DARK, zorder=2):
    # Outer white card
    card(ax, x, y, w, h, WHITE, FBD, 1.0, 0.12, zorder, do_shadow=True)
    # Title pill
    tw = len(title) * 0.112 + 0.55
    card(ax, x+0.25, y+h+0.04, tw, 0.36, tc, "none", 0, 0.04, zorder+3, False)
    txt(ax, x+0.25+tw/2, y+h+0.22, title, 8.5, WHITE, "bold", zorder=zorder+4)


def sticky(ax, x, y, w, h, text, fc, ec, size=8, weight="bold",
           subtext=None, zorder=6):
    shadow(ax, x-w/2, y-h/2, w, h, 0.04, zorder)
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle="round,pad=0.045", facecolor=fc,
        edgecolor=ec, linewidth=1.2, zorder=zorder+1))
    ty = y + 0.07 if subtext else y
    txt(ax, x, ty, text, size, T_DARK, weight, zorder=zorder+2)
    if subtext:
        txt(ax, x, y-0.23, subtext, 6.5, T_MUTED, zorder=zorder+2)


def annot_sticky(ax, x, y, w, h, text, fc, ec, rotate=0, zorder=6):
    """Annotation sticky — slightly rotated using a separate axes trick"""
    shadow(ax, x-w/2, y-h/2, w, h, 0.04, zorder)
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle="round,pad=0.04", facecolor=fc,
        edgecolor=ec, linewidth=1.1, zorder=zorder+1))
    txt(ax, x, y, text, 7.5, T_DARK, zorder=zorder+2)


def elbow(ax, x1, y1, x2, y2, color=T_MUTED, lw=1.0, zorder=4):
    mid_y = (y1+y2)/2
    ax.plot([x1,x1,x2,x2],[y1,mid_y,mid_y,y2],
            color=color, lw=lw, zorder=zorder,
            solid_capstyle="round", solid_joinstyle="round")
    ax.annotate("", xy=(x2,y2), xytext=(x2, mid_y+0.01),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=8))


def harrow(ax, x1, y, x2, color=T_MUTED, lw=1.1, zorder=4):
    ax.annotate("", xy=(x2,y), xytext=(x1,y),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=9))


def miro_watermark(ax, xlim, ylim):
    # Small Miro-style logo mark + text
    ax.add_patch(FancyBboxPatch((xlim-1.45, ylim-0.38), 1.22, 0.28,
        boxstyle="round,pad=0.04", facecolor=WHITE,
        edgecolor=FBD, lw=0.8, zorder=30))
    # Yellow square (Miro logo colour)
    ax.add_patch(FancyBboxPatch((xlim-1.38, ylim-0.32), 0.18, 0.18,
        boxstyle="square,pad=0", facecolor="#FFD02F",
        edgecolor="none", zorder=31))
    txt(ax, xlim-1.05, ylim-0.23, "Made in Miro", 6.5, T_MID,
        ha="center", zorder=32)


# ════════════════════════════════════════════════════════════════════════════
# 1. IA BEFORE & AFTER
# ════════════════════════════════════════════════════════════════════════════
W, H = 18, 10
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor(CANVAS); ax.set_facecolor(CANVAS); ax.axis("off")
ax.set_xlim(0, W); ax.set_ylim(0, H)
dot_grid(ax, W, H)
miro_watermark(ax, W, H)

# ── BEFORE frame ─────────────────────────────────────────────────────────────
frame(ax, 0.35, 0.5, 7.9, 8.85, "BEFORE  --  Org-Chart Model", S_RED_D)

sticky(ax, 4.3, 8.72, 2.7, 0.52, "Intranet Home", S_RED, S_RED_D, 9)

depts = ["Claims","Underwriting","Finance &\nRisk","Human\nResources",
         "IT &\nSystems","Legal","Marketing","Corporate\nAffairs"]
xs = np.linspace(0.92, 7.68, 8)
for name, x in zip(depts, xs):
    elbow(ax, 4.3, 8.46, x, 7.1, S_RED_D, 0.65)
    sticky(ax, x, 6.8, 0.82, 0.52, name, S_RED, S_RED_D, 6.5, weight="normal")

hr_x = xs[3]
for name, sx in [("Pay &\nPayroll", hr_x-0.56), ("Benefits", hr_x), ("Forms", hr_x+0.56)]:
    elbow(ax, hr_x, 6.54, sx, 5.65, S_RED_D, 0.55)
    sticky(ax, sx, 5.38, 0.72, 0.46, name, S_ORANGE, S_ORANGE_D, 6.5, weight="normal")

# Pain point annotation stickies (placed at slight visual angles via position)
pain = [
    ("4+ clicks to\nreach resources",    1.25, 4.1),
    ("Navigation mirrors\norg chart,\nnot daily tasks", 3.75, 3.45),
    ("Content siloed\nacross SharePoint", 6.3,  4.1),
    ("Avoidable\nsupport tickets",        2.3,  2.5),
]
for text, x, y in pain:
    annot_sticky(ax, x, y, 1.55, 0.82, text, S_YELLOW, S_YELLOW_D)

txt(ax, 4.3, 1.2, "Employees must know the org chart to find what they need.",
    8, S_RED_D, style="italic")

# ── AFTER frame ───────────────────────────────────────────────────────────────
frame(ax, 9.75, 0.5, 7.9, 8.85, "AFTER  --  Task-Based Model", G_DARK)

sticky(ax, 13.7, 8.72, 2.7, 0.52, "Intranet Home", S_GREEN, S_GREEN_D, 9)

l1 = [("For\nEmployees",11.1,S_GREEN,S_GREEN_D),
      ("For\nManagers",12.95,S_TEAL,S_TEAL_D),
      ("News &\nUpdates",14.8,S_BLUE,S_BLUE_D),
      ("Quick\nLinks",16.65,S_GREEN,G_DARK)]
for name, x, fc, ec in l1:
    elbow(ax, 13.7, 8.46, x, 7.1, G_MID, 0.9)
    sticky(ax, x, 6.8, 1.45, 0.55, name, fc, ec, 8)

for name, ex in [("Pay &\nPayroll",10.3),("Benefits",11.1),("HR Forms",11.9)]:
    elbow(ax, 11.1, 6.52, ex, 5.63, S_GREEN_D, 0.6)
    sticky(ax, ex, 5.38, 0.78, 0.46, name, S_GREEN, S_GREEN_D, 6.5, weight="normal")

for name, mx in [("Team\nMetrics",12.45),("Capacity\nPlanning",13.45)]:
    elbow(ax, 12.95, 6.52, mx, 5.63, S_TEAL_D, 0.6)
    sticky(ax, mx, 5.38, 0.86, 0.46, name, S_TEAL, S_TEAL_D, 6.5, weight="normal")

outcomes = [
    ("2 clicks to\nany resource",  10.5, 4.05),
    ("Task-oriented\nnavigation",   12.5, 3.45),
    ("Persistent\nQuick Links",     14.6, 4.05),
    ("Support tickets\ndown",       16.5, 3.45),
]
for text, x, y in outcomes:
    annot_sticky(ax, x, y, 1.55, 0.82, text, S_GREEN, S_GREEN_D)

txt(ax, 13.7, 1.8, "Navigation now matches how employees actually work.",
    8, G_DARK, style="italic")

# Research tag
card(ax, 10.0, 0.62, 4.2, 0.38, S_YELLOW, S_YELLOW_D, 1, 0.04, 7, False)
txt(ax, 12.1, 0.81, "Grounded in 12 interviews  +  84-person survey", 7.5, T_DARK)

# Centre divider line
ax.plot([9.05, 9.05], [0.7, 9.1], color=FBD, lw=1, zorder=1, linestyle="--", alpha=0.6)

plt.tight_layout(pad=0.2)
plt.savefig(f"{IMG_DIR}/nationwide-ia-before-after.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v IA before/after saved")


# ════════════════════════════════════════════════════════════════════════════
# 2. USER JOURNEY MAP
# ════════════════════════════════════════════════════════════════════════════
W2, H2 = 18, 8
fig2, ax2 = plt.subplots(figsize=(W2, H2))
fig2.patch.set_facecolor(CANVAS); ax2.set_facecolor(CANVAS); ax2.axis("off")
ax2.set_xlim(0, W2); ax2.set_ylim(0, H2)
dot_grid(ax2, W2, H2)
miro_watermark(ax2, W2, H2)

frame(ax2, 0.3, 0.3, 17.4, 7.2,
      "Employee Journey Map  --  Finding HR Benefits", G_DARK)

# Lane divider
ax2.plot([0.3, 17.7], [3.95, 3.95], color=FBD, lw=1.2, zorder=5)

# Lane labels
card(ax2, 0.48, 4.1, 1.5, 2.78, S_RED, S_RED_D, 1, 0.04, 5, False)
txt(ax2, 1.23, 5.6,  "BEFORE",        9, S_RED_D, "bold")
txt(ax2, 1.23, 5.22, "Org-chart\nmodel", 7.5, S_RED_D)

card(ax2, 0.48, 0.5, 1.5, 3.2, S_GREEN, S_GREEN_D, 1, 0.04, 5, False)
txt(ax2, 1.23, 2.12, "AFTER",          9, S_GREEN_D, "bold")
txt(ax2, 1.23, 1.74, "Task-based\nmodel", 7.5, S_GREEN_D)

# Phase header strip (before)
phases_b = ["Discovery","Navigation","Search","Confusion","Failure","Escalation"]
phase_xs = [3.0, 5.25, 7.5, 9.75, 12.0, 14.25]
for ph, px in zip(phases_b, phase_xs):
    txt(ax2, px, 6.82, ph, 7, T_MUTED, style="italic")
    ax2.plot([px, px], [6.68, 6.56], color=FBD, lw=0.7, zorder=4)

# BEFORE steps
before = [
    (3.0,  5.5, "Homepage",         "Start",              S_GRAY,   S_GRAY_D,   "Neutral"),
    (5.25, 5.5, "Human\nResources", "Wrong dept?",        S_ORANGE, S_ORANGE_D, "Unsure"),
    (7.5,  5.5, "HR Sub-page",      "Still searching...", S_ORANGE, S_ORANGE_D, "Frustrated"),
    (9.75, 5.5, "Benefits Home",    "Found it? Maybe.",   S_ORANGE, S_ORANGE_D, "Confused"),
    (12.0, 5.5, "Dead End",         "Wrong page.",        S_RED,    S_RED_D,    "Annoyed"),
    (14.25,5.5, "IT Ticket",        "Gave up.",           S_RED,    S_RED_D,    "Defeated"),
]
for i, (x, y, title, sub, fc, ec, mood) in enumerate(before):
    sticky(ax2, x, y, 1.75, 0.88, title, fc, ec, 8.5, subtext=sub)
    txt(ax2, x, y+0.6, mood, 6.5, ec, style="italic")
    if i < len(before)-1:
        harrow(ax2, x+0.88, y, before[i+1][0]-0.88, S_RED_D, 1.2)
        mx = (x+before[i+1][0])/2
        txt(ax2, mx, y+0.22, f"click {i+1}", 6.5, S_RED_D, style="italic")

# AFTER steps
after = [
    (3.0, 2.2, "Homepage",      "Start",       S_GRAY,  S_GRAY_D,  "Neutral"),
    (6.2, 2.2, "For Employees", "Right path.", S_GREEN, S_GREEN_D, "Confident"),
    (9.4, 2.2, "HR & Benefits", "Found it.",   S_GREEN, G_DARK,    "Success"),
]
for i, (x, y, title, sub, fc, ec, mood) in enumerate(after):
    sticky(ax2, x, y, 1.9, 0.88, title, fc, ec, 9, subtext=sub)
    txt(ax2, x, y+0.6, mood, 6.5, ec, style="italic")
    if i < len(after)-1:
        harrow(ax2, x+0.95, y, after[i+1][0]-0.95, G_MID, 1.6)
        mx = (x+after[i+1][0])/2
        txt(ax2, mx, y+0.22, f"click {i+1}", 7, G_MID, style="italic")

# Result callout
card(ax2, 11.3, 1.35, 5.7, 1.58, S_GREEN, S_GREEN_D, 1.8, 0.1, 7)
txt(ax2, 14.15, 2.42, "2 clicks vs 4+", 15, G_DARK, "bold")
txt(ax2, 14.15, 1.98, "No dead ends  ·  No support ticket", 9, G_DARK)
txt(ax2, 14.15, 1.62, "Navigation aligned to employee workflows", 8, T_MUTED, style="italic")

plt.tight_layout(pad=0.3)
plt.savefig(f"{IMG_DIR}/nationwide-journey.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v Journey map saved")


# ════════════════════════════════════════════════════════════════════════════
# 3. EDITORIAL CALENDAR
# ════════════════════════════════════════════════════════════════════════════
TYPE_CFG = {
    "Email Newsletter":  (S_GREEN,  S_GREEN_D,  "E"),
    "Intranet Post":     (S_BLUE,   S_BLUE_D,   "I"),
    "Manager Briefing":  (S_PURPLE, S_PURPLE_D, "M"),
    "Town Hall":         (S_ORANGE, S_ORANGE_D, "T"),
    "Survey":            (S_TEAL,   S_TEAL_D,   "S"),
    "Policy Update":     (S_GRAY,   S_GRAY_D,   "P"),
}
channels = list(TYPE_CFG.keys())
weeks = ["Week 1  ·  Mar 1-7","Week 2  ·  Mar 8-14",
         "Week 3  ·  Mar 15-21","Week 4  ·  Mar 22-31"]

W3, H3 = 18, 10.5
fig3, ax3 = plt.subplots(figsize=(W3, H3))
fig3.patch.set_facecolor(CANVAS); ax3.set_facecolor(CANVAS); ax3.axis("off")
ax3.set_xlim(0, W3); ax3.set_ylim(0, H3)
dot_grid(ax3, W3, H3)
miro_watermark(ax3, W3, H3)

frame(ax3, 0.3, 0.3, 17.4, 9.85,
      "Internal Comms -- Editorial Content Calendar  ·  March 2018", G_DARK)

# Dark header strip
ax3.add_patch(FancyBboxPatch((0.3, 9.3), 17.4, 0.68,
    boxstyle="square,pad=0", facecolor=G_DARK, edgecolor="none", zorder=6))
txt(ax3, 0.95, 9.65, "Nationwide Insurance  ·  Q1 Planning View",
    9, G_LIGHT, ha="left")
txt(ax3, 17.5, 9.65, "March 2018", 14, G_LIGHT, "bold", ha="right")

label_w = 2.3
col_start = label_w + 0.65
col_w = (17.1 - col_start) / 4
row_h = 1.22
header_y = 9.18

# Week headers
for i, week in enumerate(weeks):
    cx = col_start + i*col_w
    bg = WHITE if i % 2 == 0 else "#F6F6F4"
    ax3.add_patch(FancyBboxPatch((cx+0.04, header_y-0.36), col_w-0.08, 0.36,
        boxstyle="square,pad=0", facecolor=bg, edgecolor=FBD, lw=0.6, zorder=6))
    txt(ax3, cx+col_w/2, header_y-0.18, week, 7.5, T_MUTED, "bold")

ax3.add_patch(FancyBboxPatch((0.48, header_y-0.36), label_w, 0.36,
    boxstyle="square,pad=0", facecolor=WHITE, edgecolor=FBD, lw=0.6, zorder=6))
txt(ax3, 0.48+label_w/2, header_y-0.18, "Channel", 7.5, T_MUTED, "bold")

for r, ch in enumerate(channels):
    fc, ec, letter = TYPE_CFG[ch]
    y_top = header_y - 0.36 - r*row_h
    y_mid = y_top - row_h/2
    row_bg = WHITE if r % 2 == 0 else "#FAFAF8"

    ax3.add_patch(FancyBboxPatch((0.48, y_top-row_h), 17.12, row_h,
        boxstyle="square,pad=0", facecolor=row_bg, edgecolor=FBD, lw=0.35, zorder=5))

    ax3.add_patch(plt.Circle((0.78, y_mid), 0.13, color=ec, zorder=7))
    txt(ax3, 0.78, y_mid, letter, 7.5, WHITE, "bold")
    txt(ax3, 1.02, y_mid, ch, 8.5, T_DARK, "600", ha="left")

    for i in range(4):
        cx = col_start + i*col_w
        col_bg = WHITE if i % 2 == 0 else "#F6F6F4"
        ax3.add_patch(FancyBboxPatch((cx+0.04, y_top-row_h), col_w-0.08, row_h,
            boxstyle="square,pad=0", facecolor=col_bg, edgecolor=FBD, lw=0.3, zorder=5))

blocks = [
    (0,0,1,"Welcome Back:\nQ1 Kick-Off"),
    (0,1,1,"Benefits\nEnrolment Reminder"),
    (0,2,1,"Town Hall\nRecap"),
    (0,3,1,"March Wrap-Up"),
    (1,0,1,"IT System\nUpdate Notice"),
    (1,1,2,"New HR Policy:\nRemote Work"),
    (1,3,1,"Q2 Planning\nResources Live"),
    (2,0,1,"Q1 OKR\nAlignment Brief"),
    (2,2,2,"Performance\nReview Guidance"),
    (3,1,2,"All-Hands\nTown Hall"),
    (4,0,2,"Intranet UX\nSurvey Launch"),
    (4,3,1,"Survey Close\n& Results"),
    (5,1,1,"Data Privacy\nPolicy Update"),
    (5,3,1,"Updated\nTravel Policy"),
]
for ch_i, wk_i, span, title in blocks:
    ch = channels[ch_i]
    fc, ec, _ = TYPE_CFG[ch]
    y_top = header_y - 0.36 - ch_i*row_h
    y_mid = y_top - row_h/2
    x0 = col_start + wk_i*col_w + 0.12
    bw = col_w*span - 0.24
    bh = row_h*0.68
    by = y_mid - bh/2

    shadow(ax3, x0, by, bw, bh, 0.04, 7)
    ax3.add_patch(FancyBboxPatch((x0, by), bw, bh,
        boxstyle="round,pad=0.04", facecolor=fc,
        edgecolor=ec, linewidth=1.3, zorder=8))
    ax3.add_patch(FancyBboxPatch((x0, by+bh-0.1), bw, 0.11,
        boxstyle="square,pad=0", facecolor=ec, edgecolor="none", zorder=9))
    txt(ax3, x0+bw/2, y_mid, title, 7.5, T_DARK, "600", zorder=10)

# Legend
lx = 0.6; ly = 0.6
txt(ax3, lx, ly, "Content type:", 7.5, T_MUTED, ha="left")
lx += 1.12
for ch, (fc, ec, letter) in TYPE_CFG.items():
    short = ch.split(" ")[0]
    ax3.add_patch(FancyBboxPatch((lx, ly-0.15), 0.26, 0.28,
        boxstyle="round,pad=0.03", facecolor=fc, edgecolor=ec, lw=1.1, zorder=7))
    txt(ax3, lx+0.13, ly, letter, 7.5, ec, "bold", zorder=8)
    txt(ax3, lx+0.34, ly, short, 7.5, T_MID, ha="left", zorder=8)
    lx += 1.38

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-calendar-v2.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v Calendar saved")


# ════════════════════════════════════════════════════════════════════════════
# 4. QUICK LINKS PANEL
# ════════════════════════════════════════════════════════════════════════════
W4, H4 = 16, 9
fig4, ax4 = plt.subplots(figsize=(W4, H4))
fig4.patch.set_facecolor(CANVAS); ax4.set_facecolor(CANVAS); ax4.axis("off")
ax4.set_xlim(0, W4); ax4.set_ylim(0, H4)
dot_grid(ax4, W4, H4)
miro_watermark(ax4, W4, H4)

frame(ax4, 0.3, 0.3, 15.4, 8.15, "Quick Links -- Persistent Navigation Panel", G_DARK)

# Description sticky
card(ax4, 0.65, 7.08, 14.7, 0.75, S_YELLOW, S_YELLOW_D, 1.3, 0.06, 6, False)
txt(ax4, 8.0, 7.65,
    "Available on every page of the intranet  --  Reduces depth-to-resource from 4 clicks to 2",
    10, T_DARK, "bold")
txt(ax4, 8.0, 7.25, "Items ordered by click frequency from a 3-month analytics audit", 8.5, T_MID)

links = [
    ("$",  "Pay & Payroll",   "View payslips / Tax docs",      S_GREEN,  S_GREEN_D,  847),
    ("H",  "Benefits",        "Health / Dental / Wellness",    S_BLUE,   S_BLUE_D,   612),
    ("#",  "HR Forms",        "Requests / Leave / Policies",   S_PURPLE, S_PURPLE_D, 491),
    ("@",  "IT Help Desk",    "Raise a ticket / FAQs",         S_ORANGE, S_ORANGE_D, 388),
    ("T",  "Staff Directory", "Search by name or team",        S_TEAL,   S_TEAL_D,   275),
    ("[]", "Room Booking",    "Reserve a meeting space",       S_YELLOW, S_YELLOW_D, 244),
    (">",  "Learning Hub",    "Courses / Certifications",      S_GREEN,  S_GREEN_D,  198),
    ("*",  "Policy Library",  "Compliance / Travel / Expenses",S_GRAY,   S_GRAY_D,   156),
]

cw, ch_h = 3.35, 2.18
sx, sy = 0.7, 6.72
gx, gy = 3.68, 2.44

for i, (icon, name, sub, fc, ec, uses) in enumerate(links):
    col = i % 4; row = i // 4
    cx = sx + col*gx; cy = sy - row*gy

    card(ax4, cx, cy-ch_h, cw, ch_h, WHITE, FBD, 1.1, 0.09, 6)

    # Top colour strip
    ax4.add_patch(FancyBboxPatch((cx, cy-0.18), cw, 0.2,
        boxstyle="square,pad=0", facecolor=ec, edgecolor="none", zorder=8))

    # Icon circle
    ax4.add_patch(plt.Circle((cx+0.52, cy-0.74), 0.28, color=fc, zorder=9))
    txt(ax4, cx+0.52, cy-0.74, icon, 11, ec, "bold", zorder=10)

    # Rank badge
    ax4.add_patch(plt.Circle((cx+cw-0.24, cy-0.3), 0.19, color=G_DARK, zorder=9))
    txt(ax4, cx+cw-0.24, cy-0.3, str(i+1), 7.5, WHITE, "bold", zorder=10)

    # Name & subtitle
    txt(ax4, cx+0.97, cy-0.60, name,  9.5, T_DARK, "bold", ha="left", zorder=10)
    txt(ax4, cx+0.97, cy-0.96, sub,   7.5, T_MUTED, ha="left", zorder=10)

    # Divider
    ax4.plot([cx+0.2, cx+cw-0.2], [cy-1.38, cy-1.38],
             color=FBD, lw=0.8, zorder=8)

    # Uses badge
    card(ax4, cx+0.2, cy-ch_h+0.14, cw-0.4, 0.38, fc, "none", 0, 0.04, 9, False)
    txt(ax4, cx+cw/2, cy-ch_h+0.33, f"{uses:,} clicks / month",
        7.5, ec, "bold", zorder=10)

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-quicklinks.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v Quick Links saved")

print("\nAll refined Miro visuals done.")

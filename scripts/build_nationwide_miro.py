#!/usr/bin/env python3
"""
Nationwide case study visuals — Miro board aesthetic (fixed)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

IMG_DIR = "/Users/katrinab/ktrnab.github.io/assets/images/work"

# Miro palette
CANVAS    = "#F0F0EF"
WHITE     = "#FFFFFF"
FBD       = "#D8D8D6"   # frame border

S_YELLOW  = "#FFF9C4";  S_YELLOW_D= "#F9A825"
S_GREEN   = "#DCEDC8";  S_GREEN_D = "#558B2F"
S_BLUE    = "#BBDEFB";  S_BLUE_D  = "#1565C0"
S_RED     = "#FFCDD2";  S_RED_D   = "#C62828"
S_ORANGE  = "#FFE0B2";  S_ORANGE_D= "#E65100"
S_PURPLE  = "#E1BEE7";  S_PURPLE_D= "#6A1B9A"
S_TEAL    = "#B2DFDB";  S_TEAL_D  = "#00695C"
S_GRAY    = "#ECEFF1";  S_GRAY_D  = "#37474F"

G_DARK = "#2A5C27"; G_MID = "#3D7A39"; G_LIGHT = "#CAE896"
T_DARK = "#1A1A1A"; T_MID = "#444444"; T_MUTED = "#888888"

plt.rcParams.update({"font.family": "sans-serif"})


def txt(ax, x, y, s, size=8.5, color=T_DARK, weight="normal",
        ha="center", va="center", style="normal", zorder=20, wrap=False):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, style=style, zorder=zorder, linespacing=1.35)


def card(ax, x, y, w, h, fc=WHITE, ec=FBD, lw=1.2, r=0.06, zorder=5, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch((x+0.05, y-0.05), w, h,
            boxstyle=f"round,pad={r}", facecolor="#00000014",
            edgecolor="none", zorder=zorder-1))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad={r}", facecolor=fc,
        edgecolor=ec, linewidth=lw, zorder=zorder))


def frame(ax, x, y, w, h, title, tc=G_DARK, zorder=2):
    card(ax, x, y, w, h, WHITE, FBD, 1.2, 0.1, zorder)
    tw = max(len(title)*0.115 + 0.5, 1.2)
    ax.add_patch(FancyBboxPatch((x+0.22, y+h+0.02), tw, 0.38,
        boxstyle="round,pad=0.04", facecolor=tc,
        edgecolor="none", zorder=zorder+1))
    txt(ax, x+0.22+tw/2, y+h+0.21, title, 8.5, WHITE, "bold", zorder=zorder+2)


def elbow(ax, x1, y1, x2, y2, color=T_MUTED, lw=1.0, zorder=4):
    mid_y = (y1+y2)/2
    ax.plot([x1,x1,x2,x2],[y1,mid_y,mid_y,y2],
            color=color,lw=lw,zorder=zorder,
            solid_capstyle="round",solid_joinstyle="round")
    ax.annotate("",xy=(x2,y2),xytext=(x2,mid_y+0.01),
        arrowprops=dict(arrowstyle="-|>",color=color,lw=lw,mutation_scale=8))


def hline_arrow(ax, x1, y, x2, color=T_MUTED, lw=1.0, zorder=4):
    ax.annotate("",xy=(x2,y),xytext=(x1,y),
        arrowprops=dict(arrowstyle="-|>",color=color,lw=lw,mutation_scale=9))


def sticky_node(ax, x, y, w, h, text, fc, ec, size=8, weight="bold", zorder=6):
    card(ax, x-w/2, y-h/2, w, h, fc, ec, 1.3, 0.05, zorder)
    txt(ax, x, y, text, size, T_DARK, weight, zorder=zorder+2)


def miro_tag(ax, x, y):
    txt(ax, x, y, "Made in Miro", 7, T_MUTED, style="italic", ha="right", zorder=20)


# ════════════════════════════════════════════════════════════════════════════
# 1. IA BEFORE & AFTER
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(CANVAS); ax.set_facecolor(CANVAS); ax.axis("off")
ax.set_xlim(0, 18); ax.set_ylim(0, 10)
miro_tag(ax, 17.7, 9.7)

# BEFORE frame
frame(ax, 0.3, 0.5, 7.8, 8.8, "BEFORE  --  Org-Chart Model", S_RED_D, zorder=2)

# Root node
sticky_node(ax, 4.2, 8.7, 2.6, 0.52, "Intranet Home", S_RED, S_RED_D, 9)

depts = ["Claims","Underwriting","Finance &\nRisk","Human\nResources",
         "IT &\nSystems","Legal","Marketing","Corporate\nAffairs"]
xs = np.linspace(0.85, 7.55, 8)
for name, x in zip(depts, xs):
    elbow(ax, 4.2, 8.44, x, 7.05, S_RED_D, 0.7)
    sticky_node(ax, x, 6.75, 0.82, 0.52, name, S_RED, S_RED_D, 6.5, weight="normal")

hr_x = xs[3]
for name, sx in [("Pay &\nPayroll", hr_x-0.55), ("Benefits", hr_x), ("Forms", hr_x+0.55)]:
    elbow(ax, hr_x, 6.49, sx, 5.6, S_RED_D, 0.6)
    sticky_node(ax, sx, 5.32, 0.72, 0.46, name, S_ORANGE, S_ORANGE_D, 6.5, weight="normal")

# Pain point stickies
pain = [
    ("4+ clicks to\nreach resources", 1.3, 4.1, -1.5),
    ("Navigation mirrors\norg chart,\nnot daily tasks", 3.8, 3.5, 1.2),
    ("Content siloed\nacross SharePoint", 6.2, 4.1, -1.0),
    ("Avoidable\nsupport tickets", 2.2, 2.4, 0.6),
]
for text, x, y, rot in pain:
    from matplotlib.transforms import Affine2D
    p = FancyBboxPatch((x-0.75, y-0.42), 1.5, 0.82,
        boxstyle="round,pad=0.05", facecolor=S_YELLOW,
        edgecolor=S_YELLOW_D, linewidth=1.1, zorder=6)
    t = Affine2D().rotate_deg_around(x, y, rot) + ax.transData
    p.set_transform(t); ax.add_patch(p)
    txt(ax, x, y, text, 7, T_DARK, zorder=7)

txt(ax, 4.2, 1.15, "Employees must know the org chart to find what they need.",
    8, S_RED_D, style="italic", zorder=8)

# AFTER frame
frame(ax, 9.6, 0.5, 8.1, 8.8, "AFTER  --  Task-Based Model", G_DARK, zorder=2)

sticky_node(ax, 13.65, 8.7, 2.6, 0.52, "Intranet Home", S_GREEN, S_GREEN_D, 9)

l1 = [("For\nEmployees",11.0,S_GREEN,S_GREEN_D),
      ("For\nManagers",12.9,S_TEAL,S_TEAL_D),
      ("News &\nUpdates",14.8,S_BLUE,S_BLUE_D),
      ("Quick\nLinks",16.7,S_GREEN,G_DARK)]
for name, x, fc, ec in l1:
    elbow(ax, 13.65, 8.44, x, 7.05, G_MID, 0.9)
    sticky_node(ax, x, 6.75, 1.4, 0.55, name, fc, ec, 8)

for name, ex in [("Pay &\nPayroll",10.2),("Benefits",11.1),("HR Forms",12.0)]:
    elbow(ax, 11.0, 6.47, ex, 5.58, S_GREEN_D, 0.65)
    sticky_node(ax, ex, 5.32, 0.78, 0.46, name, S_GREEN, S_GREEN_D, 6.5, weight="normal")

for name, mx in [("Team\nMetrics",12.4),("Capacity\nPlanning",13.4)]:
    elbow(ax, 12.9, 6.47, mx, 5.58, S_TEAL_D, 0.65)
    sticky_node(ax, mx, 5.32, 0.85, 0.46, name, S_TEAL, S_TEAL_D, 6.5, weight="normal")

# Outcome stickies
outcomes = [
    ("2 clicks to\nany resource", 10.5, 4.0, 1.3),
    ("Task-oriented\nnavigation", 12.5, 3.4, -1.0),
    ("Persistent\nQuick Links", 14.5, 4.0, 0.8),
    ("Support tickets\ndown", 16.5, 3.4, -0.7),
]
for text, x, y, rot in outcomes:
    p = FancyBboxPatch((x-0.75, y-0.42), 1.5, 0.82,
        boxstyle="round,pad=0.05", facecolor=S_GREEN,
        edgecolor=S_GREEN_D, linewidth=1.1, zorder=6)
    t = Affine2D().rotate_deg_around(x, y, rot) + ax.transData
    p.set_transform(t); ax.add_patch(p)
    txt(ax, x, y, text, 7, T_DARK, zorder=7)

txt(ax, 13.65, 1.8, "Navigation now matches how employees actually work.",
    8, G_DARK, style="italic", zorder=8)

# Research tag
card(ax, 9.85, 0.65, 3.8, 0.38, S_YELLOW, S_YELLOW_D, 1, 0.04, zorder=6, shadow=False)
txt(ax, 11.75, 0.84, "Based on 12 interviews + 84-person survey",
    7.5, T_DARK, zorder=7)

plt.tight_layout(pad=0.3)
plt.savefig(f"{IMG_DIR}/nationwide-ia-before-after.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v IA before/after saved")


# ════════════════════════════════════════════════════════════════════════════
# 2. USER JOURNEY MAP
# ════════════════════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(18, 8))
fig2.patch.set_facecolor(CANVAS); ax2.set_facecolor(CANVAS); ax2.axis("off")
ax2.set_xlim(0, 18); ax2.set_ylim(0, 8)
miro_tag(ax2, 17.7, 7.75)

frame(ax2, 0.3, 0.3, 17.4, 7.2, "Employee Journey Map  --  Finding HR Benefits", G_DARK)

ax2.plot([0.3,17.7],[3.95,3.95], color=FBD, lw=1.2, zorder=5)

# Lane label tabs
card(ax2, 0.48, 4.1, 1.5, 2.8, S_RED, S_RED_D, 1, 0, zorder=5, shadow=False)
txt(ax2, 1.23, 5.6, "BEFORE", 9, S_RED_D, "bold", zorder=6)
txt(ax2, 1.23, 5.22, "Org-chart\nmodel", 7.5, S_RED_D, zorder=6)

card(ax2, 0.48, 0.5, 1.5, 3.2, S_GREEN, S_GREEN_D, 1, 0, zorder=5, shadow=False)
txt(ax2, 1.23, 2.1, "AFTER", 9, S_GREEN_D, "bold", zorder=6)
txt(ax2, 1.23, 1.72, "Task-based\nmodel", 7.5, S_GREEN_D, zorder=6)

# BEFORE steps
before = [
    (3.0,  5.5, "Homepage",       "Start",              S_GRAY,   S_GRAY_D,   "Neutral"),
    (5.3,  5.5, "Human\nResources","Wrong dept?",       S_ORANGE, S_ORANGE_D, "Unsure"),
    (7.6,  5.5, "HR Sub-page",    "Still searching...", S_ORANGE, S_ORANGE_D, "Frustrated"),
    (9.9,  5.5, "Benefits Home",  "Found it? Maybe.",   S_ORANGE, S_ORANGE_D, "Confused"),
    (12.2, 5.5, "Dead End",       "Wrong page.",        S_RED,    S_RED_D,    "Annoyed"),
    (14.5, 5.5, "IT Ticket",      "Gave up.",           S_RED,    S_RED_D,    "Defeated"),
]
for i,(x,y,title,sub,fc,ec,mood) in enumerate(before):
    card(ax2, x-0.88, y-0.45, 1.76, 0.9, fc, ec, 1.5, 0.05, 7)
    txt(ax2, x, y+0.12, title, 8.5, T_DARK, "bold", zorder=9)
    txt(ax2, x, y-0.2, sub, 7, T_MUTED, zorder=9)
    txt(ax2, x, y+0.58, mood, 6.5, ec, style="italic", zorder=9)
    if i < len(before)-1:
        hline_arrow(ax2, x+0.88, y, before[i+1][0]-0.88, S_RED_D, 1.2)
        mx = (x+before[i+1][0])/2
        txt(ax2, mx, y+0.2, f"click {i+1}", 6.5, S_RED_D, style="italic", zorder=9)

# Phase labels
phases = ["Discovery","Navigation","Search","Confusion","Failure","Escalation"]
for (x,y,*_), ph in zip(before, phases):
    txt(ax2, x, 6.72, ph, 7, T_MUTED, style="italic", zorder=9)

# AFTER steps
after = [
    (3.0, 2.2, "Homepage",      "Start",       S_GRAY,  S_GRAY_D,  "Neutral"),
    (6.2, 2.2, "For Employees", "Right path.", S_GREEN, S_GREEN_D, "Confident"),
    (9.4, 2.2, "HR & Benefits", "Found it.",  S_GREEN, G_DARK,    "Success"),
]
for i,(x,y,title,sub,fc,ec,mood) in enumerate(after):
    card(ax2, x-0.95, y-0.45, 1.9, 0.9, fc, ec, 1.8, 0.05, 7)
    txt(ax2, x, y+0.12, title, 9, T_DARK, "bold", zorder=9)
    txt(ax2, x, y-0.2, sub, 7.5, T_MUTED, zorder=9)
    txt(ax2, x, y+0.58, mood, 6.5, ec, style="italic", zorder=9)
    if i < len(after)-1:
        hline_arrow(ax2, x+0.95, y, after[i+1][0]-0.95, G_MID, 1.6)
        mx = (x+after[i+1][0])/2
        txt(ax2, mx, y+0.2, f"click {i+1}", 7, G_MID, style="italic", zorder=9)

# Result callout
card(ax2, 11.2, 1.35, 5.8, 1.6, S_GREEN, S_GREEN_D, 1.8, 0.08, 7)
txt(ax2, 14.1, 2.42, "2 clicks vs 4+", 14, G_DARK, "bold", zorder=9)
txt(ax2, 14.1, 2.0, "No dead ends  ·  No support ticket", 9, G_DARK, zorder=9)
txt(ax2, 14.1, 1.65, "Navigation aligned to employee workflows", 8, T_MUTED, style="italic", zorder=9)

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

fig3, ax3 = plt.subplots(figsize=(18, 10))
fig3.patch.set_facecolor(CANVAS); ax3.set_facecolor(CANVAS); ax3.axis("off")
ax3.set_xlim(0, 18); ax3.set_ylim(0, 10)
miro_tag(ax3, 17.7, 9.75)

frame(ax3, 0.3, 0.3, 17.4, 9.2,
      "Internal Comms -- Editorial Content Calendar  *  March 2018", G_DARK)

# Dark header strip
ax3.add_patch(FancyBboxPatch((0.3, 8.65), 17.4, 0.65,
    boxstyle="square,pad=0", facecolor=G_DARK, edgecolor="none", zorder=5))
txt(ax3, 1.0, 9.0, "Nationwide Insurance  *  Q1 Planning View", 9, G_LIGHT,
    ha="left", zorder=6)
txt(ax3, 17.5, 9.0, "March 2018", 14, G_LIGHT, "bold", ha="right", zorder=6)

label_w = 2.3
col_start = label_w + 0.6
col_w = (17.1 - col_start) / 4
row_h = 1.18
header_y = 8.52

# Week headers
for i, week in enumerate(weeks):
    cx = col_start + i*col_w
    bg = WHITE if i % 2 == 0 else "#F5F5F3"
    ax3.add_patch(FancyBboxPatch((cx+0.04, header_y-0.34), col_w-0.08, 0.34,
        boxstyle="square,pad=0", facecolor=bg,
        edgecolor=FBD, lw=0.6, zorder=5))
    txt(ax3, cx+col_w/2, header_y-0.17, week, 7.5, T_MUTED, "bold", zorder=6)

ax3.add_patch(FancyBboxPatch((0.48, header_y-0.34), label_w, 0.34,
    boxstyle="square,pad=0", facecolor=WHITE, edgecolor=FBD, lw=0.6, zorder=5))
txt(ax3, 0.48+label_w/2, header_y-0.17, "Channel", 7.5, T_MUTED, "bold", zorder=6)

# Rows
for r, ch in enumerate(channels):
    fc, ec, letter = TYPE_CFG[ch]
    y_top = header_y - 0.34 - r*row_h
    y_mid = y_top - row_h/2
    row_bg = WHITE if r % 2 == 0 else "#FAFAF8"

    ax3.add_patch(FancyBboxPatch((0.48, y_top-row_h), 17.12, row_h,
        boxstyle="square,pad=0", facecolor=row_bg,
        edgecolor=FBD, lw=0.4, zorder=4))

    # Channel dot + label
    ax3.add_patch(plt.Circle((0.76, y_mid), 0.13, color=ec, zorder=6))
    txt(ax3, 0.76, y_mid, letter, 7.5, WHITE, "bold", zorder=7)
    txt(ax3, 1.0, y_mid, ch, 8.5, T_DARK, "600", ha="left", zorder=6)

    for i in range(4):
        cx = col_start + i*col_w
        col_bg = WHITE if i % 2 == 0 else "#F5F5F3"
        ax3.add_patch(FancyBboxPatch((cx+0.04, y_top-row_h),
            col_w-0.08, row_h,
            boxstyle="square,pad=0", facecolor=col_bg,
            edgecolor=FBD, lw=0.3, zorder=4))

# Content blocks
blocks = [
    (0,0,1,"Welcome Back:\nQ1 Kick-Off"),
    (0,1,1,"Benefits\nEnrolment Reminder"),
    (0,2,1,"Town Hall\nRecap"),
    (0,3,1,"March\nWrap-Up"),
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
    y_top = header_y - 0.34 - ch_i*row_h
    y_mid = y_top - row_h/2
    x0 = col_start + wk_i*col_w + 0.12
    bw = col_w*span - 0.24
    bh = row_h*0.68
    by = y_mid - bh/2

    # Shadow + card
    ax3.add_patch(FancyBboxPatch((x0+0.04, by-0.04), bw, bh,
        boxstyle="round,pad=0.04", facecolor="#00000011",
        edgecolor="none", zorder=7))
    ax3.add_patch(FancyBboxPatch((x0, by), bw, bh,
        boxstyle="round,pad=0.04", facecolor=fc,
        edgecolor=ec, linewidth=1.3, zorder=8))
    # Top strip
    ax3.add_patch(FancyBboxPatch((x0, by+bh-0.09), bw, 0.1,
        boxstyle="square,pad=0", facecolor=ec,
        edgecolor="none", zorder=9))
    txt(ax3, x0+bw/2, y_mid, title, 7.5, T_DARK, "600", zorder=10)

# Legend
lx = 0.6; ly = 0.6
txt(ax3, lx, ly, "Content type:", 7.5, T_MUTED, ha="left", zorder=6)
lx += 1.1
for ch, (fc, ec, letter) in TYPE_CFG.items():
    short = ch.split(" ")[0]
    ax3.add_patch(FancyBboxPatch((lx, ly-0.14), 0.26, 0.28,
        boxstyle="round,pad=0.03", facecolor=fc,
        edgecolor=ec, lw=1.1, zorder=7))
    txt(ax3, lx+0.13, ly, letter, 7.5, ec, "bold", zorder=8)
    txt(ax3, lx+0.34, ly, short, 7.5, T_MID, ha="left", zorder=8)
    lx += 1.35

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-calendar-v2.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v Calendar saved")


# ════════════════════════════════════════════════════════════════════════════
# 4. QUICK LINKS PANEL
# ════════════════════════════════════════════════════════════════════════════
fig4, ax4 = plt.subplots(figsize=(16, 9))
fig4.patch.set_facecolor(CANVAS); ax4.set_facecolor(CANVAS); ax4.axis("off")
ax4.set_xlim(0, 16); ax4.set_ylim(0, 9)
miro_tag(ax4, 15.7, 8.75)

frame(ax4, 0.3, 0.3, 15.4, 8.1, "Quick Links -- Persistent Navigation Panel", G_DARK)

# Description sticky
card(ax4, 0.65, 7.05, 14.7, 0.72, S_YELLOW, S_YELLOW_D, 1.3, 0.06, 6, shadow=False)
txt(ax4, 8.0, 7.62, "Available on every page of the intranet  --  Reduces depth-to-resource from 4 clicks to 2",
    10, T_DARK, "bold", zorder=8)
txt(ax4, 8.0, 7.24, "Items ordered by click frequency from a 3-month analytics audit",
    8.5, T_MID, zorder=8)

links = [
    ("$",  "Pay & Payroll",   "View payslips / Tax docs",     S_GREEN,  S_GREEN_D,  847),
    ("H",  "Benefits",        "Health / Dental / Wellness",   S_BLUE,   S_BLUE_D,   612),
    ("#",  "HR Forms",        "Requests / Leave / Policies",  S_PURPLE, S_PURPLE_D, 491),
    ("@",  "IT Help Desk",    "Raise a ticket / FAQs",        S_ORANGE, S_ORANGE_D, 388),
    ("T",  "Staff Directory", "Search by name or team",       S_TEAL,   S_TEAL_D,   275),
    ("[]", "Room Booking",    "Reserve a meeting space",      S_YELLOW, S_YELLOW_D, 244),
    (">",  "Learning Hub",    "Courses / Certifications",     S_GREEN,  S_GREEN_D,  198),
    ("*",  "Policy Library",  "Compliance / Travel / Expenses",S_GRAY,  S_GRAY_D,   156),
]

cw, ch_h = 3.3, 2.15
sx, sy = 0.7, 6.7
gx, gy = 3.65, 2.4

for i, (icon, name, sub, fc, ec, uses) in enumerate(links):
    col = i % 4; row = i // 4
    cx = sx + col*gx; cy = sy - row*gy

    # Card
    card(ax4, cx, cy-ch_h, cw, ch_h, WHITE, FBD, 1.2, 0.08, 6)

    # Top colour strip
    ax4.add_patch(FancyBboxPatch((cx, cy-0.17), cw, 0.18,
        boxstyle="square,pad=0", facecolor=ec, edgecolor="none", zorder=7))

    # Icon circle
    ax4.add_patch(plt.Circle((cx+0.5, cy-0.72), 0.28,
        color=fc, zorder=8))
    txt(ax4, cx+0.5, cy-0.72, icon, 11, ec, "bold", zorder=9)

    # Rank badge
    ax4.add_patch(plt.Circle((cx+cw-0.22, cy-0.28), 0.18,
        color=G_DARK, zorder=8))
    txt(ax4, cx+cw-0.22, cy-0.28, str(i+1), 7.5, WHITE, "bold", zorder=9)

    # Name and subtitle
    txt(ax4, cx+0.95, cy-0.58, name, 9.5, T_DARK, "bold", ha="left", zorder=9)
    txt(ax4, cx+0.95, cy-0.94, sub, 7.5, T_MUTED, ha="left", zorder=9)

    # Divider
    ax4.plot([cx+0.18, cx+cw-0.18], [cy-1.35, cy-1.35],
             color=FBD, lw=0.8, zorder=7)

    # Uses badge
    card(ax4, cx+0.18, cy-ch_h+0.12, cw-0.36, 0.38, fc, "none", 0, 0.04, 8, shadow=False)
    txt(ax4, cx+cw/2, cy-ch_h+0.31,
        f"{uses:,} clicks / month", 7.5, ec, "bold", zorder=9)

plt.tight_layout(pad=0)
plt.savefig(f"{IMG_DIR}/nationwide-quicklinks.png", dpi=160,
            bbox_inches="tight", facecolor=CANVAS)
plt.close(); print("v Quick Links saved")

print("\nAll Miro-style visuals done.")

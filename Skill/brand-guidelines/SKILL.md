---
name: lensmor-brand-guidelines
description: Applies Lensmor's official brand identity. Use this for generating UI mockups, presentations, or documents that need to look like official Lensmor artifacts. Focuses on a modern, dark-mode SaaS aesthetic.
license: Proprietary
---

# Lensmor Brand Styling

## Overview

Use these guidelines to apply Lensmor's distinct visual identity. Lensmor uses a modern, high-contrast dark mode aesthetic suitable for an AI-native SaaS platform.

**Keywords**: Lensmor, dark mode, violet, SaaS, AI, clean, minimalistic, Plus Jakarta Sans

## Brand Guidelines

### Colors (Dark Mode System)

Lensmor is designed "Dark Mode First".

**Primary Colors:**
- **Primary (Violet)**: `#6B75FF` (Main action color, Logo, Links)
- **Primary Hover**: `#8088FF` (Interactive states)
- **Primary Dark**: `#2C317A` (Subtle backgrounds / Accents)

**Neutral / Backgrounds:**
- **App Background**: `#16161F` (Main canvas, Neutral-950)
- **Surface / Card**: `#1E1E29` (Secondary background, Neutral-900)
- **Border / Divider**: `#262733` (Neutral-800)

**Typography Colors:**
- **Headlines / Primary**: `#FAFAFA` (Neutral-50, High contrast)
- **Body / Secondary**: `#9496A8` (Neutral-400, Readable gray)
- **Muted / Disabled**: `#66687A` (Neutral-500)

**Semantic Colors:**
- **Success**: `#4CB782` (Green)
- **Warning**: `#F09F43` (Orange)
- **Danger**: `#EB5757` (Red)

### Typography

- **Headings**: **Plus Jakarta Sans** (Weights: 600 SemiBold, 700 Bold)
  - Fallback: `Inter`, `system-ui`, `sans-serif`
- **Body**: **Inter** (Weights: 400 Regular, 500 Medium)
  - Fallback: `system-ui`, `sans-serif`

### Visual Design Tokens

- **Corner Radius**:
  - `sm`: 8px
  - `md`: 12px (Standard for cards/inputs)
  - `lg`: 16px (Standard for modals/containers)
  - `full`: 9999px (Buttons/Badges)

- **Shadows (Dark Mode)**:
  - Deep and subtle to create depth on dark backgrounds.
  - *Example*: `box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5)`

## Features & Application

### For UI Generation
When generating generic UI or HTML:
1. Initialize the body with `bg-[#16161F]` and `text-[#FAFAFA]`.
2. Use `font-sans` (Inter) for copy and `font-display` (Plus Jakarta Sans) for headers if available.
3. Use `#6B75FF` for primary CTAs.

### For Presentations / Images
- **Backgrounds**: Use `#16161F` (Deep Dark) generally. Avoid pure black `#000000`.
- **Accents**: Use the Primary Violet `#6B75FF` for key data points or visual interest.
- **Charts**: Use the Semantic colors (Green/Orange/Red) combined with the Primary Violet.

## CSS Variables Reference

```css
:root {
  /* Brand */
  --primary: #6B75FF;
  --primary-foreground: #FFFFFF;

  /* Backgrounds */
  --background: #16161F;
  --surface: #1E1E29;
  --border: #262733;

  /* Text */
  --text-main: #FAFAFA;
  --text-muted: #9496A8;

  /* Radii */
  --radius-md: 12px;
}
```

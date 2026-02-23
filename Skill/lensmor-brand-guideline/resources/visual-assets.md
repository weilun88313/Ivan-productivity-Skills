# Lensmor Visual Assets Reference

## Logo Files

**File Locations:**
[TODO: Add paths or URLs to logo files]

### Primary Logo
- Full color: `[path/to/lensmor-logo-color.svg]`
- Monochrome: `[path/to/lensmor-logo-mono.svg]`
- White version: `[path/to/lensmor-logo-white.svg]`
- Black version: `[path/to/lensmor-logo-black.svg]`

### Logo Icon/Mark
- Full color: `[path/to/lensmor-icon-color.svg]`
- Monochrome: `[path/to/lensmor-icon-mono.svg]`

### Logo Variants
- Horizontal lockup: `[path/to/lensmor-logo-horizontal.svg]`
- Stacked version: `[path/to/lensmor-logo-stacked.svg]`

## Color Swatches

### Digital Color Palette

**Primary Brand Color:**
```css
/* Main brand color - use for CTAs, links, focus states */
--lensmor-primary: #6B75FF;
--lensmor-primary-hover: #5563E6;    /* Darker on hover */
--lensmor-primary-active: #4451CC;   /* Even darker when clicked */
--lensmor-primary-light: #8B95FF;    /* Lighter variant for backgrounds */
--lensmor-primary-subtle: #E8EAFF;   /* Very light for subtle highlights */
```

**Surface Colors:**
```css
/* Background and foreground colors */
--lensmor-background-dark: #16161F;  /* Main dark background */
--lensmor-foreground-light: #FAFAFA; /* Light text/surfaces */
--lensmor-divider: #DCDDE5;          /* Borders and separators */
```

**Semantic Colors:**
```css
/* Status and feedback colors */
--lensmor-success: #00C853;          /* Green for success states */
--lensmor-success-light: #E8F5E9;    /* Light green background */

--lensmor-warning: #FF9800;          /* Orange for warnings */
--lensmor-warning-light: #FFF3E0;    /* Light orange background */

--lensmor-error: #FF5252;            /* Red for errors */
--lensmor-error-light: #FFEBEE;      /* Light red background */

--lensmor-info: #2196F3;             /* Blue for info */
--lensmor-info-light: #E3F2FD;       /* Light blue background */
```

**Neutral Grayscale:**
```css
/* Grayscale for text, backgrounds, and UI elements */
--lensmor-gray-900: #1A1A1A;         /* Darkest gray - primary text on light */
--lensmor-gray-800: #2D2D2D;
--lensmor-gray-700: #404040;
--lensmor-gray-600: #666666;         /* Secondary text */
--lensmor-gray-500: #808080;         /* Disabled text */
--lensmor-gray-400: #999999;
--lensmor-gray-300: #CCCCCC;         /* Subtle borders */
--lensmor-gray-200: #E5E5E5;         /* Light borders, dividers */
--lensmor-gray-100: #F5F5F5;         /* Light backgrounds */
--lensmor-gray-50: #FAFAFA;          /* Lightest backgrounds */
```

**Complete CSS Variable Set:**
```css
:root {
  /* Brand Colors */
  --lensmor-primary: #6B75FF;
  --lensmor-primary-hover: #5563E6;
  --lensmor-primary-active: #4451CC;
  --lensmor-primary-light: #8B95FF;
  --lensmor-primary-subtle: #E8EAFF;

  /* Surface Colors */
  --lensmor-background-dark: #16161F;
  --lensmor-foreground-light: #FAFAFA;
  --lensmor-divider: #DCDDE5;

  /* Semantic */
  --lensmor-success: #00C853;
  --lensmor-success-light: #E8F5E9;
  --lensmor-warning: #FF9800;
  --lensmor-warning-light: #FFF3E0;
  --lensmor-error: #FF5252;
  --lensmor-error-light: #FFEBEE;
  --lensmor-info: #2196F3;
  --lensmor-info-light: #E3F2FD;

  /* Grays */
  --lensmor-gray-900: #1A1A1A;
  --lensmor-gray-800: #2D2D2D;
  --lensmor-gray-700: #404040;
  --lensmor-gray-600: #666666;
  --lensmor-gray-500: #808080;
  --lensmor-gray-400: #999999;
  --lensmor-gray-300: #CCCCCC;
  --lensmor-gray-200: #E5E5E5;
  --lensmor-gray-100: #F5F5F5;
  --lensmor-gray-50: #FAFAFA;
}
```

### Print Color Palette

**CMYK Values:**
[TODO: Add CMYK values for print materials]
- Primary: C__% M__% Y__% K__%
- Secondary: C__% M__% Y__% K__%

**Pantone Values:**
[TODO: If applicable]
- Primary: Pantone ____
- Secondary: Pantone ____

## Typography Assets

**Web Font Files:**
- Primary font: `[path/to/font-files]`
- Fallback fonts: `[system font stack]`

**Font Loading:**
```css
@font-face {
  font-family: '[Primary Font]';
  src: url('[path]') format('[format]');
  font-weight: [weight];
  font-style: [style];
}
```

**Typography Scale:**
```css
--font-size-xs: 12px;
--font-size-sm: 14px;
--font-size-base: 16px;
--font-size-lg: 18px;
--font-size-xl: 20px;
--font-size-2xl: 24px;
--font-size-3xl: 30px;
--font-size-4xl: 36px;
--font-size-5xl: 48px;
```

## Icon Library

**Icon Set:** [TODO: Specify icon library used]
- Source: [Link to icon library or custom icon files]
- Style: [Outline, filled, duotone, etc.]
- Format: [SVG, icon font, etc.]

**Custom Icons:**
[TODO: List any custom Lensmor-specific icons]
- Icon name: `[path/to/icon.svg]`

## Design Templates

**Figma/Sketch Files:**
[TODO: Add links to design files]
- UI component library: `[link]`
- Marketing templates: `[link]`
- Presentation template: `[link]`

**Document Templates:**
- One-pager template: `[link]`
- Case study template: `[link]`
- Blog post template: `[link]`

## Image Library

**Brand Photography:**
[TODO: Links to approved stock photos or brand photoshoots]
- Hero images: `[path/to/folder]`
- Team photos: `[path/to/folder]`
- Product screenshots: `[path/to/folder]`

**Illustrations:**
[TODO: Links to illustration assets]
- Onboarding illustrations: `[path/to/folder]`
- Empty state illustrations: `[path/to/folder]`
- Marketing illustrations: `[path/to/folder]`

## UI Components

**Component Specifications:**
[TODO: Document key UI component specs]

### Buttons
- Primary button: Height [X]px, Padding [X]px, Border radius [X]px
- Secondary button: [specs]
- Text button: [specs]

### Input Fields
- Height: [X]px
- Border radius: [X]px
- Focus state: [border color and shadow]

### Cards
- Border radius: [X]px
- Shadow: [shadow specs]
- Padding: [X]px

## Spacing System

```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
--space-3xl: 64px;
```

## Border Radius Scale

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-full: 9999px;
```

## Shadows

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
```

## Animation/Motion

**Timing Functions:**
```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

**Duration:**
```css
--duration-fast: 150ms;
--duration-normal: 300ms;
--duration-slow: 500ms;
```

## Asset Usage Notes

**File Formats:**
- Logos: Use SVG for web, PNG for raster needs (300dpi for print)
- Icons: SVG preferred for scalability
- Images: WebP for web (with JPG/PNG fallback), PNG for transparency

**Optimization:**
- Always optimize images before use
- Use appropriate compression levels
- Consider responsive image sizes

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

**Primary Colors:**
```css
--lensmor-primary: #______;
--lensmor-primary-hover: #______;
--lensmor-primary-active: #______;

--lensmor-secondary: #______;
--lensmor-secondary-hover: #______;
--lensmor-secondary-active: #______;
```

**Accent Colors:**
```css
--lensmor-accent-1: #______;
--lensmor-accent-2: #______;
--lensmor-accent-3: #______;
```

**Semantic Colors:**
```css
--lensmor-success: #______;
--lensmor-warning: #______;
--lensmor-error: #______;
--lensmor-info: #______;
```

**Neutral Colors:**
```css
--lensmor-gray-900: #______;
--lensmor-gray-800: #______;
--lensmor-gray-700: #______;
--lensmor-gray-600: #______;
--lensmor-gray-500: #______;
--lensmor-gray-400: #______;
--lensmor-gray-300: #______;
--lensmor-gray-200: #______;
--lensmor-gray-100: #______;
--lensmor-gray-50: #______;
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

from ..dependencies.colors import colors, themes


def staticBadgeGenerate(
    label: str = "Belg", text: str = ".dev", color: str = "rose", theme: str = "dark"
):
    text, label = text.replace("%20", " "), label.replace("%20", " ")

    if theme not in themes:
        theme = "dark"

    themeColors = themes[theme]

    colorScheme = colors.get(color, colors["rose"])[theme]

    labelWidth = len(label) * 8 + 24
    textWidth = len(text) * 8 + 24
    totalWidth = labelWidth + textWidth
    height = 32

    svg = f'''
    <svg width="{totalWidth}" height="{height}" viewBox="0 0 {totalWidth} {height}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <clipPath id="outerClip">
          <rect width="{totalWidth}" height="{height}" rx="8" />
        </clipPath>
      </defs>
      <rect width="{totalWidth}" height="{height}" rx="8" fill="{themeColors["bg"]}" />
      <g clip-path="url(#outerClip)">
        <rect x="0" y="0" width="{labelWidth}" height="{height}" fill="{colorScheme["bg"]}" />
        <line x1="{labelWidth}" y1="0" x2="{labelWidth}" y2="{height}" stroke="{themeColors["border"]}" stroke-width="1" />
        <text x="{labelWidth / 2}" y="{height / 2}" text-anchor="middle" dominant-baseline="central" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="{colorScheme["text"]}">{label}</text>
        <text x="{labelWidth + textWidth / 2}" y="{height / 2}" text-anchor="middle" dominant-baseline="central" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="{themeColors["text"]}">{text}</text>
      </g>
    </svg>
    '''

    return svg

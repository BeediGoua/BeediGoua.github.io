def lum(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]

    def f(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


pairs = [
    ("text on bg", "#E9EDF2", "#0E1319"),
    ("muted on bg", "#A6B0BB", "#0E1319"),
    ("accent on bg", "#8EA2B5", "#0E1319"),
    ("bg on accent btn", "#0E1319", "#8EA2B5"),
    ("text on surface", "#E9EDF2", "#171D25"),
    ("muted on surface", "#A6B0BB", "#171D25"),
    ("strong on bg", "#A3B6C7", "#0E1319"),
    # Graphite light
    ("light text on bg", "#12171E", "#F4F6F8"),
    ("light muted on bg", "#5C6773", "#F4F6F8"),
    ("light accent on bg", "#5B6F82", "#F4F6F8"),
    ("light btn text", "#F4F6F8", "#5B6F82"),
]

for name, fg, bg in pairs:
    r = ratio(fg, bg)
    print(
        f"{name:22} {r:5.2f}:1  AA-text={r >= 4.5} AA-large/UI={r >= 3.0}"
    )

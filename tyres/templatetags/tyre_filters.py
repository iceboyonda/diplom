from django import template

register = template.Library()

def format_radius_ranges(radii):
    if not radii:
        return ''
    radii = sorted(set(float(r) for r in radii))
    result = []
    start = prev = radii[0]
    for r in radii[1:]:
        if r == prev + 1:
            prev = r
        else:
            if start == prev:
                result.append(f'{int(start)}')
            else:
                result.append(f'{int(start)}-{int(prev)}')
            start = prev = r
    if start == prev:
        result.append(f'{int(start)}')
    else:
        result.append(f'{int(start)}-{int(prev)}')
    return ', '.join(result)

@register.filter
def tyre_radius_range(variants):
    """
    Принимает QuerySet или список вариантов шин,
    возвращает строку с диапазонами радиусов: 15-17, 19
    """
    radii = [v.radius for v in variants]
    return f'R{format_radius_ranges(radii)}' 
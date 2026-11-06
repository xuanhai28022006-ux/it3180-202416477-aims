def search_by_category(items, category):
    return [dvd for dvd in items if category in dvd.category]


def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword in dvd.title]
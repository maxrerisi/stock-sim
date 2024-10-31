import arrow


def get_date():
    return arrow.utcnow()


def date_to_vis(date):
    return date.humanize()

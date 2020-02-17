import re


class ExtractFilmIds:
    REGEX = '/films/([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})'
    url = ''

    def __init__(self, url):
        self.url = url

    def export_film_uuid(self):
        idList = re.findall(self.REGEX, self.url)
        if 0 == len(idList):
            return ''

        return idList[0]

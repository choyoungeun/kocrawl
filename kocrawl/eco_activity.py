from kocrawl.base import BaseCrawler
from kocrawl.searcher.eco_searcher import EcoSearcher


class EcoCrawler(BaseCrawler):

    def __init__(self):
        self.searcher = EcoSearcher()

    def request(self, top_n: int):
        try:
            return self.request_debug(top_n)
        except:
            return "에러가 발생했어요."

    def request_dict(self, top_n: int):
        try:
            out, urls = self.request_debug(top_n)
            return {
                "output": out,
                "urls": urls
            }
        except:
            return "에러가 발생했어요."

    def request_debug(self, top_n: int):
        return self.searcher.search_eco_activity(top_n)

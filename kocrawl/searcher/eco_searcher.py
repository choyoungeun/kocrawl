"""
@auther Youngeun
@since {4/4/2022}
@see : https://github.com/choyoungeun/kocrawl
"""
import random
from random import randint

from kocrawl.searcher.base_searcher import BaseSearcher


class EcoSearcher(BaseSearcher):

    def __init__(self):

        self.selectors = [[".bg-box"], [".wisdom-list > ul"]]

    def _make_query(self, category: str):
        """
        검색할 쿼리를 만듭니다.

        :param category: 수단
        :return: "수단(카테고리)"로 만들어진 쿼리
        """

        query = ' '.join([category])
        return query

    def search_eco_act(self, category: str) -> tuple:
        """
        해당 카테고리에 맞는 탄소중립 활동을 검색합니다.

        :param category: 수단
        :return: "수단(카테고리)"로 만들어진 쿼리
        """

        query = self._make_query(category)

        slogan = self._bs4_documents(url=self.url['eco_info'],selectors=self.selectors[0],query=query)
        way = self._bs4_documents(url=self.url['eco_info'],selectors=self.selectors[1],query=query)
        #print(way[0])
        data_dict = {'slogan': slogan[0].getText(), 'way': way[0].getText()}

        result = data_dict['way'].split('\n\n\n\n\n')

        #랜덤으로 해당 카테고리에 해당하는 저탄소 실천방법 뽑아와서 저장하기
        random_result = random.choice(result)

        data_dict['way'] = random_result

        return data_dict

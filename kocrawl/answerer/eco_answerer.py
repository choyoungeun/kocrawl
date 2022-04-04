from kocrawl.answerer.base_answerer import BaseAnswerer


class EcoAnswerer(BaseAnswerer):

    def eco_form(self,result: dict) -> str:
        msg = '일상에서 실천할 수 있는 저탄소 실천 방법에 대해 알려드릴께요! 😄 {slogan} \n {way}\n'.format(slogan = result['slogan'], way = result['way'])
        #msg += '비슷한 단어인 {sim_term}에 대해서도 알아볼까요?\n{sim_meaning}\n'.format(sim_term = result['sim_term'], sim_meaning = result['sim_meaning'])
        return msg
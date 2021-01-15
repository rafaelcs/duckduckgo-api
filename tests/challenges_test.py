import pytest
from common.methods import Methods
from pyquery import PyQuery as pq


class TestChallenges:
    def setup_class(self):
        self.methods = Methods()

    def test_challenge_one(self):
        response = self.methods.get()
        json_response = response.json()
        related_topics_list = json_response['RelatedTopics']

        for url_icon in related_topics_list:
            print(f'Icon URL: https://duckduckgo.com{url_icon["Icon"]["URL"]}')

    def test_challenge_two(self):
        response = self.methods.get()
        json_response = response.json()
        related_topics_list = json_response['RelatedTopics']

        for result in related_topics_list:
            result_content = result["Result"]
            character_name = pq(result_content)
            print(character_name('a').text(), end=', ')

    def test_challenge_three(self):
        response = self.methods.get()
        json_response = response.json()
        min_abstract_length = json_response['meta']['src_options']['min_abstract_length']

        assert min_abstract_length is not None
        assert isinstance(min_abstract_length, int), 'The value is not an integer'

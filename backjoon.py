import os
import sys
import requests


class Backjoon:
    def __init__(self):
        self.api = 'https://solved.ac/api/v3/problem/show'
        self.dir_path = './백준/'
        self.dir_name = {
            'Unrated': '0_Unrated',
            'Bronze': '1_Bronze',
            'Silver': '2_Silver',
            'Gold': '3_Gold',
            'Platinum': '4_Platinum',
            'Diamond': '5_Diamond',
            'Ruby': '6_Ruby'
        }
        self.study_members= {
            '예주': '.swift', 
            '하경': '.py', 
            '다영': '.py'
        }

        self.problem_id = 0
        self.level = ''
        self.title = ''
        self.title_raw = ''

    def get_level(self, level):
        if level < 1:
            return 'Unrated'
        elif level < 6:
            return 'Bronze'
        elif level < 11:
            return 'Silver'
        elif level < 16:
            return 'Gold'
        elif level < 21:
            return 'Platinum'
        elif level < 26:
            return 'Diamond'
        else:
            return 'Ruby'

    def get_problem_info(self, problem_id):
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get(self.api, params={'problemId': problem_id}, headers=headers).json()

        self.problem_id = problem_id
        self.level = self.get_level(response['level'])
        self.title_raw = response['titleKo']
        # title에 '/', ' ' 가 있으면 파일명으로 사용할 수 없으므로 '_'로 변경 
        self.title = response['titleKo'].replace('/', '_').replace(' ', '_')

    def make_problem_dir(self):
        # Level 디렉토리 여부 확인 후 없으면 생성
        if self.dir_name[self.level] not in os.listdir(self.dir_path):
            os.mkdir(self.dir_path + self.dir_name[self.level])

        # 문제 디렉토리 생성
        problem_dir = self.dir_path + self.dir_name[self.level] + '/' + str(self.problem_id) + '_' + str(self.title) + '/'
        if not os.path.exists(problem_dir):
            os.mkdir(problem_dir)

        # 스터디 멤버 별 문제 디렉토리 여부 확인 후 없으면 생성
        for (member, ex)in self.study_members.items():
            member_dir = problem_dir + member + '/'
            if not os.path.exists(member_dir):
                os.mkdir(member_dir)
            # 문제 디렉토리에 README.md 파일 생성
            with open(member_dir + '/README.md', 'w') as f:
                f.write(f'# [{self.problem_id}. {self.title_raw}](https://www.acmicpc.net/problem/{self.problem_id})\n\n')
            # 문제 디렉토리에 python 파일 생성
            with open(member_dir + self.problem_id + ex, 'w') as f:
                f.write('')

    def run(self, problem_id):
        self.get_problem_info(problem_id)
        self.make_problem_dir()

if __name__ == '__main__':
    # 스크립트 실행 시 argv로 problem info 받기
    # ex) python backjoon.py 1000
    if len(sys.argv) > 1:
        Backjoon().run(sys.argv[1])

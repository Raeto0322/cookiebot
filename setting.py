"""

Github GNU General Public License version 3.0 (GPLv3)

Copyright 매리 2018, All Rights Reserved
"""

class set:
    def __init__(self):
        #공지할 사람의 디스코드 ID 입력
        self.owner = "361091925266137089"
        #봇의 토큰 입력
        self.token = "NTE5ODIyMjEzNDY2MDMwMDgx.DyAubQ.RdqZSxt0SG4iAE7Iwx5Gm_BZw_4"
        #봇의 접두사 입력
        self.first = "$sudo "
        #봇의 공지 명령어 입력
        self.no = "Cookie-Notice"

        #콘솔 채팅 로깅 기능 설정입니다. (True : 켜짐, False : 꺼짐)
        self.log = False
        
        #공지 채널을 찾을 수 없을 시
        self.nfct = True # ( True : 채널 생성후 발송, False : 아무것도 안함 )
        #생성할 채널 이름
        self.nfctname = "쿠키봇-공지"

        """ 공지 채널 설정입니다. (자신없으면 기본으로) 반드시 List 형이여야 합니다. """

        #허용 공지 채널 접두사
        self.allowprefix = ["notice", "공지", "공고"]

        #허용 공지 채널 접두사가 들어있다 하더라도 이 접두사가 들어가 있으면 공지 하지 않습니다.
        self.disallowprefix = ["밴", "경고", "제재", "길드", "ban", "worry", "warn", "guild","원더봇","슷칼봇","레토봇","래토봇"]

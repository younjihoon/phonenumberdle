import json
class Numberdle():
    def __init__(self):
        try:
            with open('number.json', 'r') as f:
                self.numbers = json.load(f)
        except:
            raise Exception('number.json 파일이 없습니다.')
        self.log = []
    
    def set_name(self, name):
        def phone_to_list(phone):
            return [int(i) for i in phone.replace('-', '')]
        self.name = name
        self.phone = phone_to_list(self.numbers.get(name))[3:]
        if len(self.phone) != 8:
            raise Exception('전화번호가 형식이 알맞지 않습니다.')
        

    def _check(self, trial):
        if len(trial) != 4:
            raise Exception('4자리를 입력해주세요.')
        trial = [int(i) for i in trial]
        strike = [0,0]
        ball = [0,0]
        for i in range(4):
            if trial[i] == self.phone[i]:
                strike[0] += 1
            elif trial[i] in self.phone[:4]:
                ball[0] += 1
            if trial[i] == self.phone[i+4]:
                strike[1] += 1
            elif trial[i] in self.phone[4:]:
                ball[1] += 1
        return {'strike': strike, 'ball': ball}
    
    def result(self,trial):
        sb = self._check(trial)
        strike = sb['strike']
        ball = sb['ball']

        res = [f'{strike[0]}S {ball[0]}B',f'{strike[1]}S {ball[1]}B']
        if strike[0] == 4:
            res[0] = 'HOME RUN!'
        elif strike[1] == 4:
            res[1] = 'HOME RUN!'
        if strike[0] == 0 and ball[0] == 0:
            res[0] = 'OUT'
        elif strike[1] == 0 and ball[1] == 0:
            res[1] = 'OUT'
        self._log(trial, res)
        return res
    
    def get_names(self):
        return list(self.numbers.keys())
    
    def _log(self, trial, res):
        self.log.append(f'{trial} : {res[0]} | {res[1]}')

    def get_log(self):
        return self.log


# -*- coding: utf-8 -*- 
from string import digits  
from random import randint, choice  
class GuessNumber(object) :  
    #������  
    def __init__(self) :  
        self.count = 0      #����ͳ�Ʋ²����  
        self.usrNums = []   #�û���������  
        self.sysNum = ''    #ϵͳ��������  
        self.results = []   #�²���  
        self.isWinner = False  
    #��ӡ����  
    def printRules(self) :  
        print """��ϵͳ������ɲ��ظ�����λ���֣��û��£�֮��ϵͳ������ʾ�� 
                 A����������ȷλ����ȷ��B����������ȷλ�ô��� 
                 ����ȷ��Ϊ 5234�����µ��˲� 5346������ 1A2B��������һ��5��λ�ö��� 
                 ����Ϊ1A;3��4���������ֶ��ˣ���λ��û�ԣ���˼�Ϊ 2B������������ 1A2B�� 
                 ���Ųµ����ٸ��ݳ����ߵļ�A��B�����£�ֱ�����У��� 4A0B��Ϊֹ"""  
    #�����������  
    def randNumGen(self) :  
        numStr = '0123456789'  
        randNum = ''  
        for i in range(4) :  
            n = choice(numStr)  
            randNum += n  
            numStr = numStr.replace(n, '')  
        self.sysNum = randNum  
        #print 'Debug >> SysNum::', self.sysNum  
    #��������  
    def numInput(self) :  
        self.count += 1  
        while True:  
            num = raw_input('��������Ҫ�µ�����:')  
            print 'Debug >> num::',num  
            if len(num) < 4 :  
                print '***���� λ��С����λ������������'  
                continue  
            elif len(num) > 4:  
                print '***����: λ��������λ������������'  
                continue  
            if not self.isAllNumber(num) :  
                print '***����: �������˷������ַ�������������'  
                continue  
            elif self.hasSameDigit(num) :  
                print '***����: �������˺�����ͬ���ֵ����ִ�������������'  
                continue  
            else :  
                self.usrNums.append(num)  
                return num  
    #�ж��Ƿ�������  
    def isAllNumber(self, num) :  
        for ch in num :  
            if ch not in digits :  
                return False  
        return True  
          
    #�ж��Ƿ�����ͬ���ַ�  
    def hasSameDigit(self, num) :  
        for i in range(len(num)) :  
            pos = num[i + 1 :].find(num[i])  
            if pos >= 0 :  
                return True  
        return False  
    #�ж�  
    def numJudge(self, sysNum, usrNum) :  
        countA = 0  
        countB = 0  
        for i in range(4) :  
            if usrNum[i] in sysNum :  
                if i == sysNum.find(usrNum[i]) :  
                    countA += 1  
                else :  
                    countB += 1  
        result = '%dA%dB' % (countA, countB)  
        self.results.append(result)  
        if countA == 4 :  
            self.isWinner = True  
    #��ʾ����Ϊֹ���в²���  
    def showResults(self, usrNums, results) :  
        print '-' * 20  
        for i in range(self.count) :  
            print '(%d)/t%s/t%s' % (i + 1, usrNums[i], results[i])  
        print '-' * 20  
        if self.isWinner :  
            print 'Total: %d times' % self.count  
            print 'Congratulations�� Your are winner !!'  
    #����  
    def run(self) :  
        self.printRules()  
        self.randNumGen()  
        while not self.isWinner:  
            num = self.numInput()  
            self.numJudge(self.sysNum, num)  
            self.showResults(self.usrNums, self.results)  
#������  
def main() :  
    guessNumber = GuessNumber()  
    guessNumber.run()  
if __name__ == '__main__' :  
    main()  

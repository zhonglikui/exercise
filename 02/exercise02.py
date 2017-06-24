'''
生成200个邀请码，参考自：http://ju.outofmemory.cn/entry/142048
'''
import string,random


poolOfchars=string.ascii_letters+string.digits
random_codes=lambda x,y:''.join([random.choice(x) for i in range(y)])

def pad_zero_to_left(inputNumberString,totalLength):
    lengthOfInput=len(inputNumberString)
    if lengthOfInput > totalLength:
        raise IndexError('the length of input is greater than the totalLength')
    else:
        return '0'*(totalLength-lengthOfInput)+inputNumberString

def invitation_code_generator(quantity,lengthOfRandom,LengthOfkey):
    placeHoldChar="L"
    for index in range(quantity):
        try:
            yield random_codes(poolOfchars,lengthOfRandom)+placeHoldChar+pad_zero_to_left(str(index),LengthOfkey)
        except IndexError:
            print('index exceeds the length of master key')


for invitationCode in invitation_code_generator(20, 15, 4):
    print(invitationCode)
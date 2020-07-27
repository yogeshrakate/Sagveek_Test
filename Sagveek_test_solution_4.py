'''
Question No. 4
Run-length encoding is fast and simple method of encoding string.
The string 'AAAABBBCCCCCCDAA' would be encoded as '4A3B6C1D2A'
'''

def EncodeDecode(s):
    if s[0].isalpha():
        '''Encode'''
        s_e=''
        st=str(s)
        for i in range(len(s)):
            ns=st.lstrip(s[i])
            if len(st)-len(ns)!=0:
                s_e+=(str(len(st)-len(ns))+s[i])
            st=ns
        return s_e                
    else:
        '''Decode'''
        s_d=''
        for i in range(len(s)):
            if s[i].isdigit():
                s_d+=(int(s[i])*s[i+1])
        return s_d
print(EncodeDecode('AAAABBBCCCCCCDAA'))
print(EncodeDecode('4A3B6C1D2A'))

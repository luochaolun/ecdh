from ctypes import *

# ECDH key
EcdhPriKey = b''
EcdhPubKey = b''
'''
global EcdhPriKey, EcdhPubKey
loader = cdll.LoadLibrary
lib = loader("./libecdh_x64.so")
priKey = bytes(bytearray(2048))
pubKey = bytes(bytearray(2048))
lenPri = c_int(0)
lenPub = c_int(0)
pri = c_char_p(priKey)
pub = c_char_p(pubKey)
pLenPri = pointer(lenPri)
pLenPub = pointer(lenPub)
nid = 713
bRet = lib.GenEcdh(nid, pri, pLenPri, pub, pLenPub)
if bRet:
    EcdhPriKey = priKey[:lenPri.value]
    EcdhPubKey = pubKey[:lenPub.value]
else:
    print('error')
'''
# 使用c接口生成ECDH本地密钥对
def GenEcdhKey():
    global EcdhPriKey, EcdhPubKey
    # 载入c模块
    loader = cdll.LoadLibrary
    #lib = loader("./ecdh_x64.dll")
    lib = loader("./libecdh_x64.so")
    # 申请内存
    priKey = bytes(bytearray(2048))                                                         # 存放本地DH私钥
    pubKey = bytes(bytearray(2048))                                                         # 存放本地DH公钥
    lenPri = c_int(0)                                                                       # 存放本地DH私钥长度
    lenPub = c_int(0)                                                                       # 存放本地DH公钥长度
    # 转成c指针传参
    pri = c_char_p(priKey)
    pub = c_char_p(pubKey)
    pLenPri = pointer(lenPri)
    pLenPub = pointer(lenPub)
    # secp224r1 ECC算法
    nid = 713
    # c函数原型:bool GenEcdh(int nid, unsigned char *szPriKey, int *pLenPri, unsigned char *szPubKey, int *pLenPub);
    bRet = lib.GenEcdh(nid, pri, pLenPri, pub, pLenPub)
    if bRet:
        # 从c指针取结果
        EcdhPriKey = priKey[:lenPri.value]
        EcdhPubKey = pubKey[:lenPub.value]
        #print(EcdhPriKey)
        #print(EcdhPubKey)
    else:
        print('aa')
    return bRet

# 使用c接口生成ECDH本地密钥对
def GenEcdhKeyaa():
    global EcdhPriKey, EcdhPubKey
    # 载入c模块
    loader = cdll.LoadLibrary
    #lib = loader("./ecdh_x64.dll")
    lib = loader("./libecdh_x64.so")
    print(lib.add(1,2))

GenEcdhKey()

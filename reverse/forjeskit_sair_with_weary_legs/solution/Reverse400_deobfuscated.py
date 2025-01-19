lllllllllllllll,llllllllllllllI,lllllllllllllIl,lllllllllllllII,llllllllllllIll,llllllllllllIlI,llllllllllllIIl=bytearray,print,enumerate,chr,ord,len,bytes
from Crypto.Cipher import AES as IIIIlIIlIIllII
from Crypto.Util.Padding import pad as IIlIlIIllllIlI
def lIlIIIlllllIlllIll(IlIlIlIIlllIIlIlll):return''.join(lllllllllllllII(llllllllllllIll(A)^42)for A in IlIlIlIIlllIIlIlll)
def lllIIllllIIIIlllll(lIIllllllIlllIIIll,llIllIIlllIlIIllII):B=llIllIIlllIlIIllII;A=lIIllllllIlllIIIll;return A<<B&255|A>>8-B
def IllIlllIIlllIIIIlI(lIlIllIlllIlIlIIIl,IlllIIlIIIllIlIlII,lIIIIllIllllIIIlII):
	B=lIIIIllIllllIIIlII;A=IlllIIlIIIllIlIlII;C=lllllllllllllll();E=llllllllllllIlI(A);F=llllllllllllIlI(B)
	for(D,G)in lllllllllllllIl(lIlIllIlllIlIlIIIl):H=(A[D%E]+B[D%F])%8;C.append(lllIIllllIIIIlllll(G,H))
	return C
def IIIllIlIIIIlIlIlIl(IIIIlllIIIIIlIIIll,llIllIlllIIIlllIll,IIllIlllIIIlIIlIlI):A=IIIIlIIlIIllII.new(llIllIlllIIIlllIll,IIIIlIIlIIllII.MODE_CBC,IIllIlllIIIlIIlIlI);return A.encrypt(IIlIlIIllllIlI(IIIIlllIIIIIlIIIll,IIIIlIIlIIllII.block_size))
def lIlIlIllIlIlIlIIll(lIIIIlIlIIIIIIIIIl):return llllllllllllIIl.fromhex(lIIIIlIlIIIIIIIIIl)
IIllIllIlIllIIIIIl='[redacted]'
IIllIIlIllIlIIlIll='fa21c9c2596099915dbc7845c941c14e81594b5c4f69177cc4059da11e782e0b'
IlllIlIlllIIIIIIll='504f43544632303234'
llIllIIlllIlIIllII='437261636b3430302d58'
IllIllllllIIIllIIl=lIlIIIlllllIlllIll(IIllIllIlIllIIIIIl)
IIllllIlIlIIIIIIll=lIlIlIllIlIlIlIIll(IlllIlIlllIIIIIIll)
if llllllllllllIlI(IIllllIlIlIIIIIIll)<16:IIllllIlIlIIIIIIll=IIllllIlIlIIIIIIll.ljust(16,b'\x00')
IlllIIlIIIllIlIlII=llIllIIlllIlIIllII[:32]if llllllllllllIlI(llIllIIlllIlIIllII)>=32 else llIllIIlllIlIIllII.ljust(32,'0')
lIIIIllIllllIIIlII=llllllllllllIIl.fromhex(IlllIIlIIIllIlIlII)
lllllIIllllIlIllll=IllIlllIIlllIIIIlI(IllIllllllIIIllIIl.encode('utf-8'),IIllllIlIlIIIIIIll,lIIIIllIllllIIIlII)
IIIlIIllllIlllIlII=IIIllIlIIIIlIlIlIl(lllllIIllllIlIllll,IIllllIlIlIIIIIIll,lIIIIllIllllIIIlII)
llllllllllllllI('Encrypted flag:',IIIlIIllllIlllIlII.hex())
__import__('sys').exit()
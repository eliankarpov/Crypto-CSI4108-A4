import sympy
import hashlib

p = 134796622252495208738574021465844661062239290534052132012639741978205229775558094949191891517752025977182349866988849483492003542922096414869433206759007623589928006700376654580423682607807596138585649238236273081604068591769467064849278875629165375417476702954222035092297882579075036594985556127414637023627
q = 1095879381793297477132942924236119161835765003959

h = 64921783012
g = pow(h, (int)((p-1)//q), p)

x = 697662301
y = pow(g, x, p)

m = b'522346828557612'
k = 86230045723597503457297108103843235798

print("p is prime: " + str(sympy.isprime(p)))
print("p is a 1024 bit number: " + str((2**1023)<p<(2**1024)))

print("q is prime: " + str(sympy.isprime(q)))
print("q is a 160 bit number: "+ str((2**159)<q<(2**160)))

print("q|(p-1): " + str((p-1)%q==0))
print("q^2 !| (p-1): "+str((p-1)%(q**2)!=0))

############################################
# signing

r = pow(g, k, p) % q
s = ((pow(k, -1, q)) * (int(hashlib.sha1(m).hexdigest(), base=16) + (x*r))) % q

# verification

w = pow(s, -1, q)
u1 = (int(hashlib.sha1(m).hexdigest(), base=16)*w) % q
u2 = (r*w) % q
v = ((pow(g, u1, p)*pow(y, u2, p)) % p) % q

print("v: "+str(v))
print("r: "+str(r))

print("r and v are the same value: " + str(r==v))
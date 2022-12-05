import sympy
import hashlib

p = 134796622252495208738574021465844661062239290534052132012639741978205229775558094949191891517752025977182349866988849483492003542922096414869433206759007623589928006700376654580423682607807596138585649238236273081604068591769467064849278875629165375417476702954222035092297882579075036594985556127414637023627
q = 1095879381793297477132942924236119161835765003959

h = 64921783012
g = pow(h, (int)((p-1)//q), p)

x = 697662301
y = pow(g, x, p)

m1 = b'8161474912883'
m2 = b'522346828557612' # from q2
k = 86230045723597503457297108103843235798


############################################
# signing

r = pow(g, k, p) % q
s1 = ((pow(k, -1, q)) * (int(hashlib.sha1(m1).hexdigest(), base=16) + (x*r))) % q # using m1
s2 = ((pow(k, -1, q)) * (int(hashlib.sha1(m2).hexdigest(), base=16) + (x*r))) % q # using m2

# verification

w1 = pow(s1, -1, q)
u11 = (int(hashlib.sha1(m1).hexdigest(), base=16)*w1) % q
u21 = (r*w1) % q
v1 = ((pow(g, u11, p)*pow(y, u21, p)) % p) % q

w2 = pow(s2, -1, q)
u12 = (int(hashlib.sha1(m2).hexdigest(), base=16)*w2) % q
u22 = (r*w2) % q
v2 = ((pow(g, u12, p)*pow(y, u22, p)) % p) % q

# find k as the observer

calculated_k = ((int(hashlib.sha1(m1).hexdigest(), base=16) - int(hashlib.sha1(m2).hexdigest(), base=16)) * pow(s1-s2, -1, q)) % q

print("The k the observer calculated: " + str(calculated_k))
print("The actual value of k: " + str(k))
print("The two values of k are the same: " + str(calculated_k==k))
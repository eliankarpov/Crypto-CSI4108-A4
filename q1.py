import hashlib
import hmac

key = b'eli key'
msg = b'I am using this input string to test my own implementation of HMAC-SHA-512.'


# using my own hmac implementation

b = 128 # blocksize in bytes
padded_key = key
ipad = 0x36
opad = 0x5c
s1 = bytearray()
s2 = bytearray()

# append zeros to the left end of k to create b-bit string k+

for i in range(b - len(key)):
    padded_key += b'\x00'

# xor new_k with ipad to produce b-bit block s[i]

for i in range(b):
    s1.append(ipad ^ padded_key[i])

# concat s with the msg

inner_hash = hashlib.sha512(bytes(s1)+msg).digest()

# padded_key xor with opad

for i in range(b):
    s2.append(opad ^ padded_key[i])

res = hashlib.sha512(s2+inner_hash).digest()

print("My own implementation: " + str(res))


# using built in hmac
built_in_h = hmac.new(key, msg, hashlib.sha512).digest()
print("Result from built-in library: " + str(built_in_h))

print("My own implementation and the built-in library have the same output: " + str(res==built_in_h))
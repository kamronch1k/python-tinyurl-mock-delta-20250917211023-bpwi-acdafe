import hashlib
s='deltajamol'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])

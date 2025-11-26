from itertools import imap

def KSA(key):
  S = range(256)
  j = 0
  for i in range(256):
    j = (j + S[i] + key[i % len(key)]) % 256
    S[i], S[j] = S[j], S[i]
  return S
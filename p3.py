# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0
#netacad email cth: 'abcd@gmail.com'
email='descampwarnaaji@gmail.com'

# Graded
def caesar_encript(txt,shift):
  shift2 = shift % 26
  teks_encript = ''
  pass
  for char in txt :
    if char.isalpha() :
      huruf = ord(char) + shift2
      if huruf > ord('Z') :
        huruf = ord('A') + shift2 - (ord('Z') - ord(char))-1
      if huruf < ord('A') :
        huruf = ord('Z') - shift2 - (ord(char) - ord('A')) +1 
      if char.islower():
        huruf = ord(char)+shift2
        if huruf > ord('z') :
          huruf = ord('a') + shift2 - (ord('z') - ord(char))-1
        if huruf < ord('a') :
          huruf = ord('z') - shift2 - (ord(char) - ord('a')) +1 
      teks_encript += chr(huruf)
    else :
      teks_encript += char
  return teks_encript
# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  return caesar_encript(chiper,-shift)

# Sanity check!!!
msg = 'Haloz DTS mania, MANTAPSZZZ!'
cpr = caesar_encript(msg,4)
txt = caesar_decript(cpr,4)
print('plain text:',txt)
print('chiper text:',cpr)

# Graded
# Fungsi mengacak urutan
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
  
# Fungsi untuk mengurutkan return ''.join([txt[i] for i in order])kembali sesuai order
def deshuffle_order(sftxt,order):
  pass
  sort_index = sorted(order)
  dictionary = dict(zip(order,sftxt))
  huruf_awal = ''
  for i in range(len(sort_index)) :
    huruf_awal += dictionary[sort_index[i]]
  return huruf_awal
  
# Sanity check!!!
print(shuffle_order('abcd',[2,1,3,0]))
print(deshuffle_order('cbda',[2,1,3,0]))

# Graded
import math
#fungsi send batch
def send_batch(txt,batch_order,shift=3):
  pass
  list_batch = []
  encrypt_cpr = []
  batch_cpr = []
  len_batch = len(batch_order)
  for i in range(math.ceil(len(txt)/len_batch)) :
    idx = i*len_batch
    list_batch.append(txt[idx:idx+len_batch])
  for i in range(len(list_batch)) :
    if len(list_batch[i]) < len_batch :
      list_batch[i] = list_batch[i] + '_'*(len_batch-len(list_batch[i]))
  for i in range(len(list_batch)) :
    encrypt_cpr.append(caesar_encript(list_batch[i],shift))
  for i in range(len(encrypt_cpr)) :
    batch_cpr.append(shuffle_order(encrypt_cpr[i],batch_order))
  return batch_cpr
#fungsi receive batch
def receive_batch(batch_cpr,batch_order,shift=3):
  batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
  return ''.join(batch_txt).strip('_')

# Sanity check!!!
msg_cpr = send_batch('halo DTS mania, mantaaap!!!',[2,1,3,0],4)
msg_txt = receive_batch(msg_cpr,[2,1,3,0],4)
print(msg_txt,msg_cpr,sep='\n')
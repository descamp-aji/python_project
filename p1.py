# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='descampwarnaaji@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  pass
  ist2 = []
  for i in range(len(items)):
    for huruf in items[i] :
      if huruf == letter :
        ist2.append(items[i])
  return ist2
print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A'))

#Graded
def counter_item(items):
  pass
  unique_list = []
  jumlah = []
  dictionary = {}
  for buah in items :
    if buah not in unique_list :
      unique_list.append(buah) #membuat data unik dari total data di list 
  for i in range(len(unique_list)):
    jumlah.append(items.count(unique_list[i])) #menghitung jumlah masing2 dari data unik 
  for i in range(len(unique_list)) :
    dictionary[unique_list[i]] = jumlah[i] #membuat dictionary
  return dictionary
print(counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries','water melon']))

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = None 
fruit_price = {}
for i in range(len(fruits)):
  fruit_price[fruits[i]] = prices[i]

def total_price(dcounter,fprice):
  pass
  total_bayar = 0
  for i in dcounter.keys() :
    total_bayar += dcounter[i] * fprice[i]
  return total_bayar
print(total_price(counter_item(chart),fruit_price))

#Graded

def discounted_price(total,discount,minprice=100):
  pass
  if total >= 100 :
    harga_diskon = total - (total * discount/100)
  else :
    harga_diskon = total
  return harga_diskon
print(discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))

#Graded

def print_summary(items,fprice):
  pass
  nama_buah = []
  jumlah_buah = []
  harga_perbuah = []
  sorted_dict ={}
  daftar_items = counter_item(items)
  for key in sorted(daftar_items.keys()):
    sorted_dict[key] = daftar_items[key] #menyortir Dictionary
  for buah in sorted_dict.keys() :
    nama_buah.append(buah) #Nama macam Buah
  for jumlah in sorted_dict.values():
    jumlah_buah.append(jumlah) #jumlah Macam Buah
  for buah in nama_buah :
    harga_perbuah.append(fruit_price[buah]) #harga per Buah
  for i in range(len(nama_buah)):
    print(jumlah_buah[i],nama_buah[i],":", (harga_perbuah[i] * jumlah_buah[i]), sep=" ") #print summary

  print("Total :",total_price(counter_item(chart),fruit_price))
  print("Discount Price :",discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100))

print_summary(chart,fruit_price)
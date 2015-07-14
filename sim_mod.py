from PIL import Image
import imagehash
import urllib
import argparse

# module input res1 and res2 are image locations
# module output 1-Similar -1-Different

class sim:

   def __init__(self,res1,res2):
      urllib.urlretrieve(res1, "data1")
      urllib.urlretrieve(res2, "data2")
      self.hash = imagehash.dhash(Image.open("data1"))
      self.otherhash = imagehash.dhash(Image.open("data2"))

   def ham_dist(self):
                                       # Hamming_dist calc
      h1=str(self.hash)
      h2=str(self.otherhash)
      h_size = len(h1) * 4
      h = (bin(int(h1, 16))[2:]).zfill(h_size)
      h_size = len(h2) * 4
      h_1 = (bin(int(h2, 16))[2:]).zfill(h_size)
      x= len(h_1)
      for i in range(64):
         if h[i]!= h_1[i] :
            x=x-1

      if (64 - x < 10):                     # hamming distance threshold
         word='Similar'
      else :
         word='Different'

      per=(x/64.0*100.0)
      return per,word



if __name__=='__main__' :
   parser = argparse.ArgumentParser()
   parser.add_argument("link1", help="Link of first Image")
   parser.add_argument("link2", help="Link of second Image")
   args = parser.parse_args()

   obj=sim(args.link1,args.link2)
   scale,word=obj.ham_dist()
   print word,'\nScale =',scale

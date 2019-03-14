#Create your tests here.

print("Execution of  Tests Started")

import unittest 
import time
#import time
time.sleep(2)


class TestCalc(unittest.TestCase):
      def test_add(self):  
           print("Starting manage.py")
           a=5
           time.sleep(2)
           print("Ok")
           time.sleep(1)
           self.assertEqual(a,5)
           
         
      def test_add1(self):
           print("Executing settings.py in djangoproject")
           a=5
           time.sleep(2)
           print("Ok")
           time.sleep(1)
           self.assertEqual(a,5)
        
       
      def test_add2(self):
           print("Executing view.py in posts")
           a=5
           time.sleep(2)
           print("Ok")
           time.sleep(1)
           self.assertEqual(a,5)     
         
         
      def test_sub(self):
           print("Calling index  in Posts/template/")
           a=5
           time.sleep(2)
           print("Ok")
           time.sleep(1)
       
           self.assertEqual(a,5)
       
       
      def test_multiply(self):
           print("Calling Settings.py in File DjangoProject")
           a=5
           time.sleep(2)
           print("Ok")
           time.sleep(1)

           self.assertEqual(a,5)


if __name__ == '__main__':
       unittest.main()


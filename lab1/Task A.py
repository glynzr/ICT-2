#Task A:Qiymetin hesablanmasi
notebookquantity=int(input("How many notebooks do you want? "))
notebookprice1=float(input("notebookprice1: "))
pencilquantity=int(input("How many pencils do you want? "))
pencilprice1=float(input("pencilprice1: "))
notebooktotal=notebookquantity*notebookprice1
penciltotal=pencilquantity*pencilprice1
print("{} defterin qiymeti {} manatdir".format(notebookquantity,notebooktotal))
print("{} qelemin qiymeti {} manatdir".format(pencilquantity,penciltotal))

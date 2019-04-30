a=int(input("Input A value: "))
b=int(input("Input B value: "))
operation_check=["+","-","*","/","%"]
while True:
  oper=input("Input operation: ")
  if oper in operation_check:
    break
  else:
    print("Unsupported operation")
if(oper=="/" and b==0):
  print("Division by zero")
  exit()
operation_dictionary={
  "+": a+b,
  "-": a-b,
  "/": a/b,
  "*": a*b,  
}
print("A %s B = %s" % (oper,operation_dictionary.get(oper)))
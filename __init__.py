from colorama import Fore, Style

print(Fore.CYAN+"Loading.......")
print("It may take Little while !")
print(Style.RESET_ALL)
from .main import crop_model


print(Fore.GREEN+"""
      Tomato Model - 1
      Potato Disease - 2
      Fruit Health - 3
      
      """)
print(Style.RESET_ALL)

model = int(input("Enter The Model You Want To Use: "))

if model == 1:
    vid = input("Input Feed Enter None for demo Video: ").lower()
    if vid == "none" or vid=="":

        crop_model()
        
        
        
        
    else:
        try:
            crop_model(vid)

            
            
        except Exception as e:
            
                print(Fore.RED+"Invalid Video path")
                print(Style.RESET_ALL)
         

else:
    print("This Model Is Currently In Working Phase")
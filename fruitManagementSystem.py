'''
================= INSTALLATION COMMAND==============
|
|   1. pip install colorama
|   2. pip install pandas
| 
=====================================================
'''


import colorama
from colorama import Back, Fore, Style
import xlsxwriter
import pandas as pd

colorama.init(autoreset=True)

#================== FUNCITON DECLARETION ==================== 


def insertProduct():
    print(f"{Back.CYAN}|\n|\t{Fore.RED}{Style.DIM}INSERT PRODUCT (ADMIN):")
    pNmae = str(input(f"{Back.CYAN}|\t{Fore.RED}Product Name : "))
    stockQty = str(input(f"{Back.CYAN}|\t{Fore.RED}Product Stock : "))
    proPrice = int(input(f"{Back.CYAN}|\t{Fore.RED}Product Price : "))
    proSupplier = str(input(f"{Back.CYAN}|\t{Fore.RED}Supplier Name : "))

    df = pd.DataFrame({
        'NAME' : [f"{pNmae}"],
        'QUANTITY' : [f"{stockQty}"],
        'PRICE' : [f"{proPrice}"],
        'SUPPLIER' : [f"{proSupplier}"],
    })

    df.to_csv("productList.csv")

    addMore = str(input(f"{Back.CYAN}|\t{Fore.RED}Do you want to add more product? (y/n) : "))
    if addMore == 'y':
        insertProduct()
    else:
        print(f"|{Back.MAGENTA}{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
        admin()


#========== Seller Function ==========
def Addseller():
    sellerId = str(input(f"{Back.WHITE}|\t{Fore.BLUE}Seller ID : "))
    sellerName = str(input(f"{Back.WHITE}|\t{Fore.BLUE}Seller Name : "))
    sellerEmail = str(input(f"{Back.WHITE}|\t{Fore.BLUE}Seller Email : "))
    sellerPhone = str(input(f"{Back.WHITE}|\t{Fore.BLUE}Seller Phone Number : "))
    print(f"{Back.WHITE}|\t{Fore.BLUE}Seller Username is : {Fore.RED}Seller")
    print(f"{Back.WHITE}|\t{Fore.BLUE}Seller Password is : {Fore.RED}seller")

    sellerCSV = pd.DataFrame({
        'ID' : [f"{sellerId}"],
        'NAME' : [f"{sellerName}"],
        'EMAIL' : [f"{sellerEmail}"],
        'PHONE NUMBER' : [f"{sellerPhone}"],
    })
    sellerCSV.to_csv("sellerDetails.csv")

    addMore = str(input(f"{Back.WHITE}|\t{Fore.RED}Do you want to add more product? (y/n) : "))
    if addMore == 'y':
        Addseller()
    else:
        print(f"|{Back.MAGENTA}{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
        admin()




def checkSeller():
    print(f"{Back.MAGENTA}|\n|{Fore.WHITE} ===========================|  C H E C K   S E L L E R  |===========================")
    checkSeller = pd.read_csv("sellerDetails.csv")
    print(f"{Back.MAGENTA}|\n{Fore.WHITE}{checkSeller}")

    print(f"|{Back.MAGENTA}{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
    admin()


def orderProducts():
    print(f"{Back.MAGENTA}|\n|{Fore.WHITE} ===========================|  O R D E R   P R O D U C T S  |===========================")
    orderProduct = pd.read_csv("OrderProduct.csv")
    print(f"{Back.MAGENTA}|\n{Fore.WHITE}{orderProduct}")
    print(f"|{Back.MAGENTA}{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
    admin()


# ================== CHECK PRODUCT FUNCTION =======================
def checkProducts():
    df = pd.read_csv("productList.csv")
    print(f"{Back.BLUE}|\n{Fore.WHITE}{df}")


def admin():
    print(f"{Back.RED}|{Fore.WHITE}===========================| A D M I N |===========================")
    print(f"{Back.RED}|{Fore.WHITE}\t\t1. INSERT PRODUCT\n|{Fore.WHITE}\t\t2. ADD SELLER\n|{Fore.WHITE}\t\t3. CHECK SELLERLIST\n|{Fore.WHITE}\t\t4. CHECK PRODUCTS\n|{Fore.WHITE}\t\t5. ORDERED PRODUCT\t\t6. BACK")
    userInputAdmin = int(input(f"{Back.RED}|\n|\t{Fore.WHITE}Enter your sellected number : "))

    if userInputAdmin == 1:
        insertProduct()
    
    elif userInputAdmin == 2:
        Addseller()

    elif userInputAdmin == 3:
        checkSeller()
    
    elif userInputAdmin == 4:
        checkProducts()

    elif userInputAdmin == 5:
        orderProducts()

    else:
        print(f"{Back.MAGENTA}|\n{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
        main()

def seller():
    print(f"{Back.GREEN}||===========================|  S E L L E R   S E C T I O N  |===========================")

    df = pd.read_csv("productList.csv")
    print(f"{Back.GREEN}|\n{Fore.YELLOW}{df}")

    print(f"{Back.GREEN}{Fore.YELLOW}|\n|\n|")
    print(f"{Back.GREEN}|\t{Fore.YELLOW}PRODUCT SELLECTION : ")

    print(f"{Back.GREEN}|\n|\t{Fore.YELLOW}You have to follow the product list when you will enter product details!")

    try:
        orderProduct = str(input(f"{Back.GREEN}|\n|\t{Fore.YELLOW}Product name : "))
        productPrice = int(input(f"{Back.GREEN}|\t{Fore.YELLOW}Product Price : "))
        orderQuantity = int(input(f"{Back.GREEN}|\t{Fore.YELLOW}Product Order Quantity : "))


    except Exception as ex:
        print(f"{Back.GREEN}|\t\t{Fore.RED}== Your error due {ex} ==")
        print(f"{Back.MAGENTA}|\n{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
        seller()

    totalPrice = productPrice*orderQuantity

    print(f"{Back.GREEN}{Fore.RED}|\n|\t===========================|  O R D E R   S U M M A R Y  |===========================")
    print(f"{Back.GREEN}|\t{Fore.RED}YOUR PRODUCT IS : {orderProduct}")
    print(f"{Back.GREEN}|\t{Fore.RED}PRODUCT -per PRICE : {productPrice}")
    print(f"{Back.GREEN}|\t{Fore.RED}TOTAL COST : {totalPrice}")

    orderProductCSV = pd.DataFrame({
        'PRODUCT ' : [f"{orderProduct}"],
        'PRODUCT PRICE ' : [f"{productPrice}"],
        'QUANTITY ' : [f"{orderQuantity}"],
        'TOTAL PRICE ' : [f"{totalPrice}"],
        })
    orderProductCSV.to_csv("OrderProduct.csv")

    orderMore = str(input(f"{Back.GREEN}|\n|\t{Fore.YELLOW}Do you want to order more product? (y/n) :"))

    
    if orderMore == 'y':
        seller()
    else:
        print(f"{Back.MAGENTA}|\n{Fore.WHITE} ->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
        main()




def main():

    print(f"{Back.RED}{Fore.WHITE}|\t\t\t\t\tH E L L O   F R I E N D S")
    print(f"{Back.RED}{Fore.WHITE}|\t\t\t\t->  THIS SYSTEM DEVELOPED BY TAHAMIDUR TAIEF  <-")
    print(f"{Back.YELLOW}|\n|\tSELLECT ONE OPTION:\n|{Fore.RED}\t\t1. LOGIN AS ADMIN\n|{Fore.BLUE}\t\t2. LOGIN AS seller\n|{Fore.BLACK}\t\t3. EXIT")

    try:
        option_in = int(input(f"{Back.YELLOW}|\n|\tEnter your sellected number : "))

    except Exception as ex:
        print(f"|{Back.YELLOW}{Fore.RED}\t\tYour error due to {ex}")
        main()



    #................... Redirect to the ADMIN or SELLER function.......................

    if option_in == 1:
        admin()
    elif option_in == 2:
        seller()
    else:
        print(f"{Back.WHITE}\n|\t\t\t\t\t{Fore.BLUE}Y{Fore.RED}o{Fore.YELLOW}u{Fore.GREEN}r {Fore.CYAN}s{Fore.MAGENTA}y{Fore.BLUE}s{Fore.RED}t{Fore.YELLOW}e{Fore.GREEN}m {Fore.RED}i{Fore.BLUE}s {Fore.CYAN}E{Fore.MAGENTA}X{Fore.YELLOW}I{Fore.GREEN}S{Fore.RED}T{Fore.BLUE}I{Fore.CYAN}N{Fore.MAGENTA}G ...")
        exit()

main()











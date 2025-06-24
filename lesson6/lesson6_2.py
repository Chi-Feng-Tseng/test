
#import tools
#from lesson6.tools import calculate_BMI, get_state
#import edu
#from edu.tools import calculate_BMI, get_state
from edu.tools import calculate_BMI as a
from edu.tools import get_state as b
def main():
    #計算BMI
    try:
        weight:int = int(input("請輸入體重:"))
        print(f"體重:{weight} Kg")
        
        height:int = int(input("請輸入身高:")) 
        print(f'身高:{height} cm')
        BMI = a(height, weight)

        print(f'BMI:{BMI:.2f}')
        print(b(BMI))
        
    except ValueError:
        print("輸入數值非int型態")

    except Exception as e:
        print(e)
        
    print("應用程式結束")

if __name__ == "__main__":
    main()

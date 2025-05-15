
import tools
def main():
    #計算BMI
    try:
        weight:int = int(input("請輸入體重:"))
        print(f"體重:{weight} Kg")
        
        height:int = int(input("請輸入身高:")) 
        print(f'身高:{height} cm')
        BMI = tools.calculate_BMI(height, weight)

        print(f'BMI:{BMI:.2f}')
        print(tools.get_state(BMI))
        

    except ValueError:
        print("輸入數值非int型態")

    except Exception as e:
        print(e)
        
    print("應用程式結束")

if __name__ == "__main__":
    main()

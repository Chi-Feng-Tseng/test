def calculate_BMI(height:int, weight:int):
    if weight < 30 or weight > 200:
            raise Exception("輸入體重低於30或高於200")
    if height < 120 or height > 220:
            raise Exception("輸入身高低於120或高於220")
    
    BMI = weight/(height/100)**2
    return BMI

def get_state(BMI:float)->str:
    if BMI >=18.5 and BMI < 24:
        message = "BMI為正常範圍"
    elif BMI < 18.5:
        message = "體重過輕"
    elif  BMI >= 24 and BMI < 27:
        message = "體重過重"
    elif BMI >= 27 and BMI < 30:
        message = "輕度肥胖"
    elif BMI >= 30 and BMI < 35:
        message = "中度肥胖"
    else:
        message = "重度肥胖"
    return message

def main():
    #計算BMI
    try:
        weight:int = int(input("請輸入體重:"))
        
        print(f"體重:{weight} Kg")
        
        height:int = int(input("請輸入身高:")) 
        
        print(f'身高:{height} cm')

        BMI = calculate_BMI(height, weight)

        print(f'BMI:{BMI:.2f}')
        
        print(get_state(bmi))
        

    except ValueError:
        print("輸入數值非int型態")

    except Exception as e:
        print(e)
        
    print("應用程式結束")

if __name__ == "__main__":
    main()

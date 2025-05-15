def calculate_BMI(h:int, w:int):
    BMI = w/(h/100)**2
    return BMI

def main():
    #計算BMI
    try:
        weight:int = int(input("請輸入體重:"))
        if weight < 30 or weight > 200:
            raise Exception("輸入體重低於30或高於200")
        print(f"體重:{weight} Kg")
        
        height:int = int(input("請輸入身高:")) 
        if height < 120 or height > 220:
            raise Exception("輸入身高低於120或高於220")
        print(f'身高:{height} cm')

        BMI = calculate_BMI(height, weight)

        print(f'BMI:{BMI:.2f}')

        if BMI >=18.5 and BMI < 24:
            print("BMI為正常範圍")
        elif BMI < 18.5:
            print("體重過輕")
        elif  BMI >= 24 and BMI < 27:
            print("體重過重")
        elif BMI >= 27 and BMI < 30:
            print("輕度肥胖")
        elif BMI >= 30 and BMI < 35:
            print("中度肥胖")
        else:
            print("重度肥胖")

    except ValueError:
        print("輸入數值非int型態")

    except Exception as e:
        print(e)
        
    print("應用程式結束")

if __name__ == "__main__":
    main()

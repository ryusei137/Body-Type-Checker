bodyfat = float(input("体脂肪率を入力: "))
muscle = float(input("筋肉率を入力: "))

if bodyfat < 10 and muscle < 31:
    result = "痩せ型"

elif bodyfat < 10 and 31 <= muscle <= 35:
    result = "細身筋肉質"

elif bodyfat < 10 and muscle >= 36:
    result = "筋肉質"

elif 10 <= bodyfat < 20 and muscle < 31:
    result = "運動不足"

elif 10 <= bodyfat < 20 and 31 <= muscle <= 35:
    result = "標準"

elif 10 <= bodyfat < 20 and muscle >= 36:
    result = "筋肉質"

elif bodyfat >= 20 and muscle < 31:
    result = "隠れ肥満"

elif bodyfat >= 20 and 31 <= muscle <= 35:
    result = "肥満型"

elif bodyfat >= 20 and muscle >= 36:
    result = "固太り"

else:
    result = "判定できません"

print(f"あなたの体型は{result}です。")
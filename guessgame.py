import random

def guess_number():
    print("🎮 ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'УГАДАЙ ЧИСЛО'!")
    print("=" * 50)
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    print("У тебя есть 10 попыток.")
    print("=" * 50)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}/{max_attempts}. Твоя догадка: "))
            
            if guess < secret_number:
                print("📈 Слишком маленькое число! Попробуй больше.")
            elif guess > secret_number:
                print("📉 Слишком большое число! Попробуй меньше.")
            else:
                print("🎉 ПОЗДРАВЛЯЮ! Ты угадал число!")
                print(f"💫 Ты справился за {attempts + 1} попыток!")
                break
            
            attempts += 1
            
            if attempts == 5:
                if secret_number % 2 == 0:
                    print("💡 Подсказка: число ЧЁТНОЕ")
                else:
                    print("💡 Подсказка: число НЕЧЁТНОЕ")
                    
        except ValueError:
            print("❌ Ошибка! Вводи только цифры!")
    
    if attempts == max_attempts:
        print(f"\n💔 К сожалению, попытки закончились!")
        print(f"🔢 Я загадал число: {secret_number}")
    
    play_again = input("\n🔄 Хочешь сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        guess_number()
    else:
        print("\n👋 Спасибо за игру! До встречи!")

if __name__ == "__main__":
    guess_number()
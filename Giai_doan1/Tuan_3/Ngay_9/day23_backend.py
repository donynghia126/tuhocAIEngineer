# File: game_lib.py
import random

class Character:
    def __init__(self, name, hp, dame, ap, giap, kp, speed, crit):
        self.name = name
        self.hp = hp
        self.max_hp = hp # Lưu máu tối đa để hồi máu không bị lố
        self.dame = dame # Sát thương vật lý
        self.ap = ap     # Sát thương phép
        self.giap = giap # Giáp
        self.kp = kp     # Kháng phép
        self.speed = speed
        self.crit = crit # Tỷ lệ chí mạng (0 - 100%)

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        return f"🔰 {self.name} | HP: {self.hp}/{self.max_hp} | Dame: {self.dame} | AP: {self.ap}"

    # Hàm gây sát thương vật lý (Dành cho Đấu sĩ, Sát thủ)
    def attack_physic(self, target):
        print(f"⚔️ {self.name} lao vào chém {target.name}!")
        
        # Tính chí mạng
        actual_dame = self.dame
        if random.randint(1, 100) <= self.crit:
            actual_dame *= 2
            print("  🔥 CHÍ MẠNG!!!")

        # Công thức giảm sát thương: (Dame - Giáp đối thủ)
        # Nếu Giáp to hơn Dame thì vẫn trừ ít nhất 1 máu
        damage_taken = max(1, actual_dame - target.giap)
        
        target.hp -= damage_taken
        if target.hp < 0: target.hp = 0
        
        print(f"  => 💢 {target.name} mất {damage_taken} máu (Giáp chặn {target.giap}).")

    # Hàm gây sát thương phép (Dành cho Pháp sư)
    def attack_magic(self, target):
        print(f"✨ {self.name} niệm chú bắn cầu lửa vào {target.name}!")
        
        damage_taken = max(1, self.ap - target.kp)
        
        target.hp -= damage_taken
        if target.hp < 0: target.hp = 0
        
        print(f"  => 💥 {target.name} mất {damage_taken} máu phép (Kháng phép chặn {target.kp}).")

# --- CÁC VAI TRÒ CỤ THỂ ---

# 1. Đấu Sĩ: Máu trâu, Giáp to, Dame ổn, Speed chậm
class DauSi(Character):
    def __init__(self, name):
        # Gọi hàm __init__ của cha và điền sẵn chỉ số đặc trưng
        super().__init__(name, hp=200, dame=40, ap=0, giap=30, kp=10, speed=10, crit=10)

# 2. Pháp Sư: Máu giấy, Dame vật lý = 0, AP cực to, Kháng phép ổn
class PhapSu(Character):
    def __init__(self, name):
        super().__init__(name, hp=120, dame=5, ap=60, giap=5, kp=20, speed=20, crit=5)
    
    # Pháp sư đánh thường sẽ dùng phép thuật (Ghi đè hành động attack cũ)
    def attack(self, target):
        self.attack_magic(target)

# 3. Sát Thủ: Máu cực giấy, Dame to, Crit cực cao (50%), Speed nhanh
class SatThu(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, dame=55, ap=0, giap=5, kp=5, speed=50, crit=50)

    def attack(self, target):
        self.attack_physic(target)
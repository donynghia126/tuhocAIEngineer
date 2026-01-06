# File: main.py
from day23_backend import DauSi, PhapSu, SatThu
import time

def main():
    print("=== CHỌN TƯỚNG ===")
    print("1. Đấu Sĩ (Máu trâu)")
    print("2. Pháp Sư (Sát thương phép)")
    print("3. Sát Thủ (Chí mạng cao)")
    
    choice = input("👉 Chọn nhân vật của bạn (1-3): ")
    name = input("Tên nhân vật: ")

    # Tạo nhân vật dựa trên lựa chọn (Polymorphism)
    if choice == '1':
        player = DauSi(name)
    elif choice == '2':
        player = PhapSu(name)
    else:
        player = SatThu(name)

    # Tạo kẻ thù mặc định là Đấu Sĩ cho trâu bò
    enemy = DauSi("Boss Quỷ")

    print(f"\n✅ Bạn đã chọn: {player.show_status()}")
    print(f"👿 Đối thủ: {enemy.show_status()}")
    print("-" * 40)

    # --- VÒNG LẶP CHIẾN ĐẤU (Logic so tốc độ) ---
    while player.is_alive() and enemy.is_alive():
        time.sleep(1)
        
        # Ai có tốc độ cao hơn được đánh trước (Logic nâng cao)
        first, second = (player, enemy) if player.speed >= enemy.speed else (enemy, player)

        print(f"\n⚡ {first.name} (Speed {first.speed}) ra tay trước!")
        
        # Người thứ nhất đánh (Nếu là Pháp sư nó tự dùng phép, Đấu sĩ tự dùng kiếm)
        if hasattr(first, 'attack'): 
            first.attack(second) 
        else: 
            first.attack_physic(second) # Mặc định đánh thường

        if not second.is_alive(): break

        # Người thứ hai đánh trả
        print(f"\n🛡️ {second.name} phản công!")
        if hasattr(second, 'attack'):
            second.attack(first)
        else:
            second.attack_physic(first)

    # Kết quả
    print("\n" + "="*30)
    if player.is_alive():
        print(f"🎉 CHIẾN THẮNG! {player.name} còn {player.hp} máu.")
    else:
        print(f"💀 BẠN ĐÃ THUA! {enemy.name} còn {enemy.hp} máu.")

if __name__ == "__main__":
    main()
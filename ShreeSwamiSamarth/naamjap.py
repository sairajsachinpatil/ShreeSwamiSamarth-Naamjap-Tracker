from playsound import playsound

#  Welcome Message
print("🌼 Welcome to Shree Swami Samarth Naamjap 🙏")
print("")
print("_____________________________________________________")
print("🕉️ Instructions:")
print("➡️  Press the **Enter** key each time you chant the naam.")
print("➡️  Do **not type anything**, just press Enter to count.")
print("➡️  Type 'q' and press Enter to exit early (optional).")
print("_____________________________________________________\n")

naam_jap = 0 #intialization

# 📿 Main Counting Loop
for _ in range(1, 109):
    key = input()
    
    if key == "":
        naam_jap += 1
        playsound("ShreeSwamiSamarth/ShreeSwamiSamarth.mp3")  #sound on enter
        print(naam_jap, "SHREE SWAMI SAMARTH 🙏")

        if naam_jap == 108:
            print("\n✅ You have completed 108 Naamjaps!")
            print("📿 You have completed 1 Mala 🙏")
            print("🕉️ Shri Swami Samarth Maharaj ki Jay!\n")
            break  # Stop the loop after 108
          
    elif key.lower() == 'q':
        print("\n📿 Even a few naamjaps bring peace to the soul.")
        print("✨ Come back anytime. Shree Swami Samarth is always with you.")
        print("🕉️ Shree Swami Samarth Maharaj ki Jay!")
        print("Total Naam Jap:", naam_jap)
        break

    else:
        print("⚠️  Please press only the Enter key to count your Naamjap.")
        print("🙏 Type 'q' to quit anytime.\n")

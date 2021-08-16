import morse_talk as mtalk
# from gpiozero import LED
import time

# led = LED(4)

phrase = 'Alpha Ranger 45 departed'
encoded = mtalk.encode(phrase)
print(encoded)

unit = .3

# for char in encoded:
#     print(char)
#     if char == ' ':
#         time.sleep(unit)
#     else:
#         # led.on()
#         sleep = unit if char == '.' else unit*3
#         time.sleep(sleep)
#         # led.off()
#         time.sleep(unit)


for char in phrase:
    if char == ' ':
        print("*space*")
        time.sleep(unit*6)
    else:
        print(char + ": ", end="")

        charE = mtalk.encode(char)

        for elem in charE:
            print(elem, end="")
            # led.on()
            sleep = unit if elem == '.' else unit*3
            time.sleep(sleep)
            # led.off()
            time.sleep(unit)
        print()

        time.sleep(unit*2)


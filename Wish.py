import time

def clear_screen():
    print("\033[2J")  

def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def animate_eid_mubarak_wish():
    poem = [
        "On this auspicious day of Eid,",
        "May all your joys be multiplied indeed.",
        "May Allah's blessings never cease,",
        "And your life be filled with eternal peace.",
        "Wishing you a joyous Eid filled with delight,",
        "May your path be always bright.",
        "Eid Mubarak to you and your family, dear friend,",
        "May this festive season never come to an end!"
    ]

    frames = [
        r"""
              
██████╗░░█████╗░██╗░░░░░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░██╔╝
██████╦╝███████║██║░░░░░██║░░╚═╝█████═╝░404
██╔══██╗██╔══██║██║░░░░░██║░░██╗██╔═██╗░
██████╦╝██║░░██║███████╗╚█████╔╝██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝

{poem_line1}
{poem_line2}
{poem_line3}
{poem_line4}
{poem_line5}
{poem_line6}
{poem_line7}
{poem_line8}
        """.format(
            poem_line1=poem[0],
            poem_line2=poem[1],
            poem_line3=poem[2],
            poem_line4=poem[3],
            poem_line5=poem[4],
            poem_line6=poem[5],
            poem_line7=poem[6],
            poem_line8=poem[7]
        ),
        r"""
    
███╗░░░███╗██████╗░░░░░░░░░██╗░█████╗░███╗░░░███╗███████╗░██████╗
████╗░████║██╔══██╗░░░░░░░░██║██╔══██╗████╗░████║██╔════╝██╔════╝
██╔████╔██║██████╔╝░░░░░░░░██║███████║██╔████╔██║█████╗░░╚█████╗░ Owner
██║╚██╔╝██║██╔══██╗░░░██╗░░██║██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
██║░╚═╝░██║██║░░██║██╗╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

{poem_line1}
{poem_line2}
{poem_line3}
{poem_line4}
{poem_line5}
{poem_line6}
{poem_line7}
{poem_line8}
        """.format(
            poem_line1=poem[0],
            poem_line2=poem[1],
            poem_line3=poem[2],
            poem_line4=poem[3],
            poem_line5=poem[4],
            poem_line6=poem[5],
            poem_line7=poem[6],
            poem_line8=poem[7]
        )
    ]

    for frame in frames:
        clear_screen()
        print(color_text(frame, "green"))
        time.sleep(1)  
animate_eid_mubarak_wish()


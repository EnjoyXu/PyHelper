#！Python
import keyboard
def runHotkey():
    # hot key

    text1='\sqrt{}'
    shortcut1 = 'ctrl+2' #define your hot-key

    text2 = '\\frac{}{}'
    shortcut2 = 'ctrl+/'


    # abbreviation

    ab1 = r'''
\begin{align}

\end{align}
    '''.strip()

    # {
    ab2 = r'\left\{}' + '\b'+\
    r'''
\begin{matrix}
    & \\
\end{matrix}\right.
    '''.strip()

    #}
    ab3 = r'''
\left.\begin{matrix}
    & \\
\end{matrix}\right\}
    '''.strip()

    #{ }
    ab4 = r'''
\begin{pmatrix}
    &
\end{pmatrix}
    '''.strip()

    #[ ]
    ab5 = r'''
\begin{bmatrix}
    &
\end{bmatrix}
    '''.strip()

    #| |
    ab6 = r'''
\begin{vmatrix}
    &
\end{vmatrix}
    '''.strip()

    #||   ||
    ab7 = r'''
\begin{Vmatrix}
    &
\end{Vmatrix}
    '''.strip()

    # color
    ab8 = r"{\color{ }  }"
    # color text
    ab9 = r"{\color{ } \text{  } }"


    keyboard.add_hotkey(shortcut1, lambda:keyboard.write(text1),suppress=True) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut2,lambda:keyboard.write(text2),suppress=True)

    keyboard.add_abbreviation("@align",ab1)
    keyboard.add_abbreviation("@lb",ab2)
    keyboard.add_abbreviation("@rb",ab3)
    keyboard.add_abbreviation("@lrb",ab4)
    keyboard.add_abbreviation("@lrB",ab5)
    keyboard.add_abbreviation("@det",ab6)
    keyboard.add_abbreviation("@abs",ab7)

    keyboard.add_abbreviation("@c",ab8)
    keyboard.add_abbreviation("@ctext",ab9)

    keyboard.add_abbreviation("@bec",r"\because")
    keyboard.add_abbreviation("@so",r"\therefore")
    keyboard.add_abbreviation("@del",r"\nabla")



    # print("Press alt+F12 to stop.")
    keyboard.wait()



if __name__ == "__main__":
    runHotkey()
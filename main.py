from flet import *

def main(page: Page):
    page.bgcolor = "#000000"
    page.spacing = 10
    ### equasions Text Field
    tf1 = TextField(label = 'Equasion', hint_text = '60 + 7 = 67', bgcolor="#ffffff", color = 'black',  border_radius=0, border_color='white')
    page.add(tf1)

    def handle_event(b: ControlEvent, textfeild = tf1):
            if b.control.content != '=':
                if b.control.content in ['0','1','2','3','4','5','6','7','8','9']:
                    t = textfeild.value + b.control.content
                    textfeild.value = t
                else:
                    if b.control.content != 'X':
                        textfeild.value = textfeild.value + b.control.content
                    else:
                        textfeild.value = textfeild.value + '*'

                textfeild.update()
            else:
                try:   
                    textfeild.label = textfeild.value
                    textfeild.value = str(eval(textfeild.value))
                    textfeild.update()
                except:
                    textfeild.label = 'Equasion'
                    textfeild.value = ''
                    textfeild.hint_text = 'Error'
                    textfeild.update()


    ### first row buttons
    btn1 = Button('-', expand=True,bgcolor = 'black', color='amber',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'amber'), text_style=TextStyle(30)), on_click =handle_event)
    btn2 = Button('3', expand=True,bgcolor = 'black', color='White',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn3 = Button('2', expand=True,bgcolor = 'black', color='White',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn4 = Button('1',expand=True, bgcolor = 'black', color='White',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    
    row = Row([btn1, btn2, btn3, btn4])
    page.add(row)
    ### second row buttons
    btn5 = Button('+',expand=True, bgcolor = 'black', color='amber',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'amber'), text_style=TextStyle(30)), on_click =handle_event)
    btn6 = Button('6', expand=True,bgcolor = 'black', color='White',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn7 = Button('5', expand=True,bgcolor = 'black', color='White',  style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn8 = Button('4',expand=True, bgcolor = 'black', color='White', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    
    row1 = Row([btn5, btn6, btn7, btn8])
    page.add(row1)
        
    ### third row buttons
    btn9 = Button('X', expand=True,bgcolor = 'black', color='amber', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'amber'), text_style=TextStyle(30)), on_click =handle_event)
    btn10 = Button('9',expand=True, bgcolor = 'black', color='White', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn11 = Button('8',expand=True, bgcolor = 'black', color='White', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn12 = Button('7',expand=True, bgcolor = 'black', color='White', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    
    row2 = Row([btn9, btn10, btn11, btn12])
    page.add(row2)

    ### fourth row buttons
    btn13 = Button('/',expand=True, bgcolor = 'black', color='amber', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'amber'), text_style=TextStyle(30)), on_click =handle_event)
    btn14 = Button('0',expand=True, bgcolor = 'black', color='White', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'white'), text_style=TextStyle(30)), on_click =handle_event)
    btn15 = Button('=',expand=True, bgcolor = 'black', color='amber', style = ButtonStyle(shape = RoundedRectangleBorder(radius = 1), side = BorderSide(2, 'amber'), text_style=TextStyle(30)), on_click =handle_event)

    row4 = Row([btn13, btn14, btn15])
    page.add(row4)


    page.update()

app(target = main)

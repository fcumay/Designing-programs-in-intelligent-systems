KV = """
<FirstPage>:
    BoxLayout:
        orientation: 'vertical'
        padding:150
        spacing:50
        Button:
            text:'New'
            background_color: .45, .76, .76, .5
            on_press:
                root.new_game()
                root.manager.transition.direction = 'up'
                root.manager.current = 'main'   
                
        Button:
            text:'Continue'
            background_color: .45, .76, .76, .5
            on_press: 
                root.continue_game()
                root.manager.transition.direction = 'down'
                root.manager.current = 'main' 
            
<MainPage>:
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Rectangle:
                pos: 0, 0
                size: 250, 200
                source: 'images/Thomas.jpg'
            Rectangle:
                pos: 250, 0
                size: 550, 200
                source: 'images/railwayst.png'          
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id:train_goods
                    text:'Press any button'
                    
                Label:
                    id:st_A_goods
                    text:''

                Label:
                    id:st_B_goods
                    text:''

                Label:
                    id:st_C_goods
                    text:''

                Label:
                    id:st_D_goods
                    text:''  

                Label:
                    id:st_E_goods
                    text:''

                Label:
                    id:st_F_goods
                    text:''  
                               
            BoxLayout:
                orientation: 'vertical'
                spacing:10
                TextInput:
                    id:txt
                    hint_text:'Input number'
                Button:
                    text:'Next station'
                    background_color: .45, .76, .76, .5
                    on_press:root.next_station(txt.text)
                Button:
                    text:'Load train'
                    background_color: .45, .76, .76, .5
                    on_press:root.load(txt.text)
                Button:
                    text:'Unload train'
                    background_color: .45, .76, .76, .5
            
        Label:
            text:''
            size_hint: 1,.5
    

"""

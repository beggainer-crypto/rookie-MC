from ursina import *
from ursina.prefabs.first_person_controller import *

app = Ursina()
selected_block = 0

def update():
    global selected_block

    if held_keys['1']: selected_block = 1
    if held_keys['2']: selected_block = 2
    if held_keys['3']: selected_block = 3
    if held_keys['4']: selected_block = 4
    if held_keys['5']: selected_block = 5
    if held_keys['6']: selected_block = 6
    if held_keys['7']: selected_block = 7
    if held_keys['g']: selected_block = 8

    if player.position.y <= -300:
        player.set_position((7, 200, 7))


class Block(Button):
    def __init__(self, pos:tuple = (0,0,0), texture='grass'):
        super().__init__(
            parent = scene,
            model = 'cube',
            color = color.color(0,0,random.uniform(0.9,1.0)),
            texture = texture,
            position = pos,
            scale = (1.2, 1.2, 1.2),
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:

            if key == 'left mouse down':
                destroy(self)
            
            if key == 'right mouse down':
                
                if selected_block == 1:
                    block = Block(pos = (self.position + mouse.normal*1.2), texture='grass')

                if selected_block == 2:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='white_cube')

                if selected_block == 3:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='brick')

                elif selected_block == 4:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='cog')

                elif selected_block == 5:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='noise')

                elif selected_block == 6:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='arrow_down')

                elif selected_block == 7:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='arrow_right')

                elif selected_block == 8:
                    block = Block(pos=(self.position + mouse.normal*1.2), texture='reflection_map_3')

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'sky_default',
            scale = (150, 150 , 150),
            position = (7, 1, 7),
            double_sided = True,
            collider = 'sphere_collider',
            visible = True
        )

# class UI_overlay(Entity):
#     def __init__(self):
#         super().__init__(
#             parent = camera.ui,
#             model = 
#         )



for x in range(15):
    for z in range(15):
        GroundCube = Block(pos = (x*1.2, 1.2, z*1.2))


player = FirstPersonController()
# Admin = EditorCamera()
sky = Sky()
app.run()
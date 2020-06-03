import pyglet
from pyglet.gl import *
class main (pyglet.window.Window):
    def __init__ (self):
        super(main, self).__init__(650, 380, fullscreen = False)
        self.button_texture = pyglet.image.load('popmaszynapic.png')
        self.button = pyglet.sprite.Sprite(self.button_texture)
        self.alive = 1
    def render(self):
        self.clear()
        self.button.draw()
        self.flip()
    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()
x = main()
x.run()
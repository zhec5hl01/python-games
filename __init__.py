"""
@author: xiaofengkz
@date: 2023-2-25
pgzero的template程序（模板文件）
pgzero本身就是pygame的简化版本，但是我——xiaofengkz又把他简化了一下
使用方法:
    :from template import * #必须得这样，否则无法运行
提供方法:
    :template_draw(screen, bg=(255, 255, 255)
    :template_update()
    :template_on_key_down(keys, key)
    :template_on_key_up(keys, key)
    :template_on_key_down_ESCAPE()
    :template_on_mouse_down(mouse, pos, button)
    :template_on_mouse_up(mouse, pos, button)
    :play_music(music_name='bg_music')
    :stop_music()
    :play_sound(sound_name)
How to use them:
    Some examples:
        :def draw():
            template_draw(screen)
        :def update():
            template_update()
        ...and so on

开源包，任何人都可以使用并修改！
"""
from template import *

__version__ = '1.0'
__all__ = [
    'template_on_key_down',
    'template_on_key_up',
    'template_on_mouse_down',
    'template_on_mouse_up',
    'template_draw',
    'template_update',
    'on_key_down_ESCAPE',
    'play_sound',
    'play_music',
    'stop_music'
]

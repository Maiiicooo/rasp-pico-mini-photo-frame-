import board
import busio
import displayio
from time import sleep
from fourwire import FourWire
from adafruit_st7735r import ST7735R

displayio.release_displays()

mosi_pin = board.GP11
clk_pin  = board.GP10
reset_pin = board.GP17
cs_pin    = board.GP18
dc_pin    = board.GP16

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = FourWire(
    spi,
    command=dc_pin,
    chip_select=cs_pin,
    reset=reset_pin
)

display = ST7735R(
    display_bus,
    width=128,
    height=160,
    bgr=True
)

# Bitmaps
bitmaps = [
    displayio.OnDiskBitmap("/0.bmp"),
    displayio.OnDiskBitmap("/1.bmp"),
    displayio.OnDiskBitmap("/2.bmp"),
 
]

group = displayio.Group()
display.root_group = group   # 👈 BELANGRIJK

tile_grid = None

while True:
    for bmp in bitmaps:
        if tile_grid:
            group.pop()      # vorige afbeelding weg

        tile_grid = displayio.TileGrid(
            bmp,
            pixel_shader=bmp.pixel_shader
        )

        group.append(tile_grid)
        sleep(10)

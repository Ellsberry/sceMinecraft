"""This module builds a house"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def buildFloor(material, x, y, z, xOffset, y, zOffset)
    mc.setBlocks(x, y, z, x + xOffset, position.y, position.z + zOffset, 4)

# set the starting location
x = 60
z = 153
y = mc.getHeight(x, z)
mc.player.setTilePos(x, y, z)
position = mc.player.getTilePos()
print(position)
# print(mc.getBlock(x, y, z))
# print(y)



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# while x < 300:
#     x = x + 50
#     z =-20
#     while z <300:
#         z = z + 50
#         print("x = ", x, "  y  ", y , "z = ", z)
#         # Change the player's position
#         mc.player.setTilePos(x, y, z)
#          # Wait 10 seconds
#         time.sleep(.5)
#         position = mc.player.getTilePos()
#         # mc.postToChat(position)
#         print(position)
# y = mc.getHeight(x, z)
# blocktype = mc.getBlock(x, y, z)
# print(blocktype)
# mc.setBlock(x, y, z, 57)
# mc.setBlocks(120,30,200,20,20,20)
# mc.postToChat(position)
# mc.postToChat(y)
# mc.setBlocks(position.x, position.y, position.z, position.x + 10, position.y + 20, position.z + 3, 4)
# mc.setBlocks(position.x + 1, position.y + 1, position.z, position.x + 49, position.y + 19, position.z + 49, 40)
# mc.setBlock(x,y,z, 40)
#
# tourch = mc.getEntities(50)
# tourch = entityIDs(50)
# mc.entity.setPos(tourch, x, y, z)
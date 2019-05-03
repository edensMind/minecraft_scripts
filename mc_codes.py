# Fill area with blocks
# /fill x1 y1 z1 x2 y2 z2 gold_block
fill 164 63 55 190 63 73 minecraft:air


# fill one block below you!
fill ~0 ~-1 ~0 ~0 ~-2 ~0 minecraft:dirt

# fill area with air
fill ~-10 ~0 ~-10 ~10 ~20 ~10 minecraft:air
fill ~-3 ~0 ~-3 ~3 ~20 ~3 minecraft:air


# fill straight line: for TNT line
fill ~0 ~0 ~0 ~-100 ~1 ~0 minecraft:air
fill ~101 ~0 ~0 ~1 ~1 ~0 minecraft:tnt


give @p minecraft:firework_rocket 64

# clone
clone 302 3 2 300 1 0 ~ ~2 ~


#clone tower wall  (North/South)
clone 35 79 39 29 90 46 ~ ~ ~  
clone 35 79 38 29 90 45 ~ ~ ~

#clone tower  (East/West)
clone 27 79 70 20 90 76 ~ ~ ~  
clone 27 79 70 20 90 76 ~ ~ ~  

#tower wall
clone 37 79 68 27 125 78 ~ ~ ~

give @p minecraft:spawner
give @p villager_spawn_egg

# give enchanted items
give @p minecraft:elytra{Enchantments:[{id:respiration,lvl:10}, {id:feather_falling ,lvl:10}, {id:unbreaking,lvl:1000}]}



give @p minecraft:diamond_pickaxe{Enchantments:[{id:silk_touch,lvl:10}, {id:efficiency,lvl:10}, {id:unbreaking,lvl:1000}]}
give @p minecraft:diamond_shovel{Enchantments:[{id:silk_touch,lvl:10}, {id:efficiency,lvl:10}, {id:unbreaking,lvl:1000}]}

give @p minecraft:diamond_pickaxe{Enchantments:[{id:fortune,lvl:10}, {id:efficiency,lvl:10}, {id:unbreaking,lvl:1000}]}

give @p minecraft:trident{Enchantments:[{id:loyalty,lvl:10}, {id:channeling,lvl:10}, {id:unbreaking,lvl:1000}]}

give @p minecraft:crossbow{Enchantments:[{id:multishot,lvl:10}, {id:quick_charge,lvl:4}, {id:infinity,lvl:10}, {id:unbreaking,lvl:1000}]}

give @p minecraft:diamond_pickaxe{Enchantments:[{id:efficiency,lvl:10}, {id:unbreaking,lvl:10}, {id:mending,lvl:10}]}

give @p minecraft:diamond_pickaxe{Enchantments:[{id:efficiency,lvl:100}, {id:unbreaking,lvl:1000}, {id:fortune,lvl:10}]}

give @p minecraft:diamond_axe{Enchantments:[{id:efficiency,lvl:10}, {id:unbreaking,lvl:1000}, {id:smite,lvl:10}]}

give @p minecraft:diamond_boots{Enchantments:[{id:aqua_infinity,lvl:10}, {id:frost_walker,lvl:10}, {id:depth_strider,lvl:10}]}

give @p minecraft:diamond_shovel{Enchantments:[{id:efficiency,lvl:100}, {id:unbreaking,lvl:1000}, {id:fortune,lvl:10}]}

# COORDS ------------------------------------------------------
tp 100 81 -23 		- home

tp 41 69 -1308 		- donkey

tp -76 81 -2664 	- jungle

tp -201 62 -3727 	- ocean

tp 960 62 -4561 	- coral reef
tp 1164 62 -8174 	- coral reef BIG

tp 919 64 -6048 	- swamp

tp 1504 65 -9489	- ice

tp 5 88 -12			- NETHER START

tp 169 255 -38 		- TOP FLIGHT POINT

tp 862 64 -4581		- northwest ocean

to 655 65 -4661		- iron mountain

tp 2531 76 5934		- desert 1

tp 26 69 -8139		- mushroom forest

tp 2923 67 5865		- Temple + Village ("Cool!") 

tp 2984 70 6662		- 2nd Icebergs

tp 4119 66 1062		- mesa 1


# COORDS II --1.14--------------------------------------------------

tp -167 70 242		- home house

tp -20 62 21		- NETHER START








#clone pyramid building
clone -67 67 205 -61 74 200 ~2 ~ ~2

clone -60 67 208 -54 77 203 ~2 ~ ~2



#stone villager house
clone -189 72 214 -182 90 208 ~ ~ ~

#white villager house
clone -171 70 190 -164 90 184 ~ ~ ~
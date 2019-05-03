#fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:dirt

blocks = ["andesite", "glowstone", "chiseled_quartz_block", "chiseled_red_sandstone"]

bi = 0

i = 20

while i > 0:

	if bi >= len(blocks):
		bi = 0

	fill_command = """
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
Send, /
Sleep 250
Send, fill ~-"""+str(i)+""" ~-1 ~-"""+str(i)+""" ~"""+str(i)+""" ~-1 ~"""+str(i)+""" minecraft:"""+blocks[bi]+"""
Send, {Enter}
"""
	print(fill_command)

	i -= 1
	bi += 1


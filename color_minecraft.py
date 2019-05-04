#git push https://github.com/edensMind/minecraft_scripts.git master

import xml.etree.ElementTree as ET
import re

#get XML file
file = 'mushy.xml'
tree = ET.parse(file)
root = tree.getroot()

# color dic
color_block_dict = {
	# black rgb(0, 0, 0)
	"#000000":"black_wool",

	# red rgb(255, 255, 255)
	"#FFFFFF":"white_wool",

	# brown rgb(127, 95, 31)
	"#7F5F1F":"brown_wool",

	# pink rgb(228, 166, 201)
	"#E4A6C9":"pink_wool",

	# yellow rgb(255, 255, 0)
	"#FFFF00":"yellow_wool",

	# red rgb(255, 0, 0)
	"#FF0000":"red_wool",

}

########################################################################
# get Style tags - defines colors 
styles_dict = {}
for child in root:
	if child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Styles":
		styles_tag = child
		for style in styles_tag:
			for s in style:
				if s.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Interior" and "Default" not in str(style.attrib):
					# get style number
					style_num_xml = str(style.attrib) #  ([a-z]\d\d)
					style_num_match = re.findall('([a-z]\\d\\d)', style_num_xml)
					style_num = style_num_match[0]

					# get style color
					color = ""
					if "Color" in str(s.attrib):
						color_xml = str(s.attrib)     #  (#[A-F\d]{6})
						color_match = re.findall('(#[A-F\\d]{6})', str(color_xml))
						color = color_match[0]

					# add style_num:color to styles dict
					styles_dict[style_num] = color
########################################################################

########################################################################
# get Rows
rows = []
for child in root:
	if child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Worksheet":
		for table in child:
			if "Table" in str(table):
				for row in table:
					# for each row, check the idex and style
					index = 0
					this_row = []
					for cell in row:
						# get index
						if "Index" in str(cell.attrib):
							index_match = re.findall("(Index': '\\d+)", str(cell.attrib))
							index_split = index_match[0].split("'")
							index = int(index_split[-1])
						else:
							index += 1

						# get style num
						style_num_match = re.findall('([a-z]\\d\\d)', str(cell.attrib))
						style_num = style_num_match[0]

						# add this cell to row
						this_row.append([index, style_num])

					# add this row to rows list
					rows.append(this_row)
########################################################################

# start AHK script - call by pushing Control+R
message = ";;; Making pixel art based off of: "+file+"\n;;; Output: art.ahk\n"
ahk = message
ahk += "^r::\n"

# build will show up just south and east of player

row_num = 1
for row in rows:
	print(row_num)
	#for each cell in a row...

	i = 0
	while i < len(row):
		# get cell components
		x_index = row[i][0]
		next_x_index = 0
		cell_style = row[i][1]

		# check if style is not blank
		if styles_dict[cell_style] != '':
			#get block type - from dictionaries
			block = color_block_dict[styles_dict[cell_style]]

			while True:
				if i+1 >= len(row):
					break

				if block == color_block_dict[styles_dict[row[i+1][1]]]:
					print("debug")
					next_x_index += 1
					i += 1
				else: 
					
					break

			ahk += """
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
Send, /
Sleep 250
Send, fill ~"""+str(x_index)+""" ~ ~"""+str(row_num)+""" ~"""+str(x_index+next_x_index)+""" ~ ~"""+str(row_num)+""" minecraft:"""+block+"""
Send, {Enter}\n
"""
		i += 1
	row_num += 1


print(message)
print()
print(styles_dict)


# write to circle.ahk
f = open("art.ahk", "w")
f.write(ahk)
f.close()
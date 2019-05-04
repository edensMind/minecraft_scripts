import xml.etree.ElementTree as ET
import re

#get XML file
tree = ET.parse('test.xml')
root = tree.getroot()

# color dic
color_block_dict = {
	# black rgb(0, 0, 0)
	"#000000":"black_wool",

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

row_num = 1
for row in rows:
	print(row_num)
	#if styles_dict[row[1]] != '':
	for cell in row:
		if styles_dict[cell[1]] != '':
			print(cell)
	row_num += 1

print()
print(styles_dict)

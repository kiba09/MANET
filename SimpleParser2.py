#usr/bin/python
#Author: King Alvin Bernabe
#A xml-parser for MobySimulator xml output
import xml.etree.ElementTree as ET
import sys


class HtmlGraphBuilder(self):
	def __init__():
		self.html = ''

	def GraphBar_speedtime(self,speed,time):
		
		return speed,time
	
	def GraphBar_posxy(self,posx,posy,speed,time,node_count):
		
		self.html += '''function drawChart() {'''
		self.html += '''var data = new google.visualization.DataTable();'''
		self.html += '''data.addColumn('string','Browser')'''
		self.html += '''data.addColumn('number','Percentage')'''
		self.html += '''data.addRows(['''



		self.html += ''']);'''

		self.html += ''' var options = {'title': 'Position of Nodes','width':500,'height':400};'''

		self.html += '''var chart = new google.visualization.PieChart(document.getElementById('container'));'''
		self.html += '''chart.draw(data,options);'''


		self.html += '''}'''
		self.html += '''google.charts.setOnloadCallback(drawChart);'''

	def begin_html(self):
		self.html += '''<html>'''

	def end_html(self):
		self.html += '''</html>'''


	def html_string_refresh(self):
		self.html = ''
		
class MobySimParser():	
	def __init__(self,xml_file):
		self.tree = ET.parse(xml_file)
		self.root = self.tree.getroot()
	def get_node_numbers(self):	
		for i in self.root.iter('Parameter'):
			if i.attrib.values()[0] == 'nodenumber':
				self.node_number = i.attrib.values()[1]
	def get_all_number_node(self):
		self.node_processes_count,dec = 0,True
		while dec:
			try:
				self.root[1][self.node_processes_count]	
				self.node_processes_count += 1
			except:dec = False	
	def parser(self):	
		#########print self.root[1][1].text	#raw data pulled from <t></t>		
		doom_time=[]
		doom_speed=[]	
		doom_posx=[]
		doom_posy=[]
		doom_angle = []
		for i in xrange(int(self.node_processes_count)):
			doom_time.append([''])
			doom_speed.append([''])
			doom_posx.append([''])
			doom_posy.append([''])
			doom_angle.append([''])	
		for i in xrange(self.node_processes_count):	
			cons= self.root[1][i].text.split(',')
			data_node =  cons[1]
			data_time = cons[0]
			data_speed = cons[4]			
			data_posx = cons[2]
			data_posy = cons[3]
			data_angle = cons[5]
	
			doom_time[int(data_node)] += ("%s	")%(data_time)
			doom_speed[int(data_node)] += ("%s	")%(data_speed)
			doom_posx[int(data_node)] += ("%s	")%(data_posx)
			doom_posy[int(data_node)] += ("%s	")%(data_posy)
			doom_angle[int(data_node)] += ("%s	")%(data_angle)
		print "Node count ",self.node_number
		file_open = open("timespeed.txt",'wb')
		file_open.truncate()
		node_final = 1
		pull_me = ''
		here = ''	
		for speedz,timez in zip(doom_speed,doom_time):
			if int(node_final) <= int(self.node_number): 
				here = ","* self.node_processes_count
				file_open.write("NODE%s\n"%(node_final))
				file_open.write("speed	%s\n"%(''.join(speedz)))
				file_open.write("time	%s\n"%(''.join(timez)))
				file_open.write('\n')
			node_final += 1
		file_open.close()
		
		file_open2 = open("positions.txt",'wb')
		file_open2.truncate()
		node_final2 = 1
		pull_me2 = ''
		here2= ''
		for posx_z,posy_z in zip(doom_posx,doom_posy):
			if int(node_final2)<= int(self.node_number):
				here2 = ","* self.node_processes_count
				file_open2.write("NODE%s\n"%(node_final2))
				file_open2.write("position x:	%s\n"%(''.join(posx_z)))
				file_open2.write("position y:	%s\n"%(''.join(posy_z)))
				file_open2.write('\n')
			node_final2 += 1
		file_open2.close()	
		
		#for posx_z,posy_z in zip(doom_posx,doom_posy):
	
		file_open3 = open("angle.txt",'wb')
		file_open3.truncate()
		node_final3 = 1
		pull_me3 = ''
		here3= ''
		for angle in doom_angle:
			if int(node_final3)<= int(self.node_number):
				here3 = ","* self.node_processes_count
				file_open3.write("NODE%s\n"%(node_final3))
				file_open3.write("Direction Angle:	%s\n"%(''.join(angle)))
				file_open3.write('\n')
			node_final3 += 1
		file_open3.close()
		
	def parser_js(self):
		#########print self.root[1][1].text	#raw data pulled from <t></t>		
		doom_time=[]
		doom_speed=[]	
		doom_posx=[]
		doom_posy=[]
		doom_angle = []
		for i in xrange(int(self.node_processes_count)):
			doom_time.append([''])
			doom_speed.append([''])
			doom_posx.append([''])
			doom_posy.append([''])
			doom_angle.append([''])	
		for i in xrange(self.node_processes_count):	
			cons= self.root[1][i].text.split(',')
			data_node =  cons[1]
			data_time = cons[0]
			data_speed = cons[4]			
			data_posx = cons[2]
			data_posy = cons[3]
			data_angle = cons[5]
	
			doom_time[int(data_node)] += ("%s	")%(data_time)
			doom_speed[int(data_node)] += ("%s	")%(data_speed)
			doom_posx[int(data_node)] += ("%s	")%(data_posx)
			doom_posy[int(data_node)] += ("%s	")%(data_posy)
			doom_angle[int(data_node)] += ("%s	")%(data_angle)
		print "Node count ",self.node_number
		file_open = open("timespeed.txt",'wb')
		file_open.truncate()
		node_final = 1
		pull_me = ''
		here = ''	
		
		for speedz,timez in zip(doom_speed,doom_time):
			if int(node_final) <= int(self.node_number): 
				here = ","* self.node_processes_count
				file_open.write("NODE%s\n"%(node_final))
				file_open.write("speed	%s\n"%(''.join(speedz)))
				file_open.write("time	%s\n"%(''.join(timez)))
				file_open.write('\n')
			node_final += 1
		file_open.close()
		
		file_open2 = open("positions.txt",'wb')
		file_open2.truncate()
		node_final2 = 1
		pull_me2 = ''
		here2= ''
		for posx_z,posy_z in zip(doom_posx,doom_posy):
			if int(node_final2)<= int(self.node_number):
				here2 = ","* self.node_processes_count
				file_open2.write("NODE%s\n"%(node_final2))
				file_open2.write("position x:	%s\n"%(''.join(posx_z)))
				file_open2.write("position y:	%s\n"%(''.join(posy_z)))
				file_open2.write('\n')
			node_final2 += 1
		file_open2.close()	
		#for posx_z,posy_z in zip(doom_posx,doom_posy):
		file_open3 = open("angle.txt",'wb')
		file_open3.truncate()
		node_final3 = 1
		pull_me3 = ''
		here3= ''
		for angle in doom_angle:
			if int(node_final3)<= int(self.node_number):
				here3 = ","* self.node_processes_count
				file_open3.write("NODE%s\n"%(node_final3))
				file_open3.write("Direction Angle:	%s\n"%(''.join(angle)))
				file_open3.write('\n')
			node_final3 += 1
		file_open3.close()
		
		
		return None	
		
		
		
if __name__ == '__main__':
	print "NOTE: Make Sure the File must be an Output of the MobiSimulator"
	try:
		if sys.argv[1] == "--help":
			print "Example : "
			print "'SimpleParser2.exe file.xml' or 'python SimpleParser2.py file.xml'"
			print "Pa libre naman po pag mai time kayo :D"
		if sys.argv[1] != None or sys.argv[1] != '': 
			app = MobySimParser(str(sys.argv[1]))
			app.get_node_numbers()
			app.get_all_number_node()
			app.parser()
			print "File Generated : positions.txt,timespeed.txt,angle.txt"	
			print "Pa libre naman po pag mai time kayo :D"	
		else:print "NO FILE FOUND"	
	except:print "SimpleParser2.py --help"

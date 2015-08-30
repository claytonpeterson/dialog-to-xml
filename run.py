#! /usr/bin/env python

import os

from xml.etree.cElementTree import Element, SubElement, ElementTree

""" 
This software creates an xml file to represent a conversation tree

Tag list:
<conversation>
	<ai_dialog>
	<player_dialog_options>
		<choice>
			<reply>
			<conversation>
"""

print "Conversation-Generator" 

def build():

	character_name = raw_input("What is the name of this character? -> ")

	tree = Element("conversation")

	stack = []

	prompts = []

	stack.append(tree)
	
	prompts.append("as a greeting? -> ");

	while (len(stack)>0):
		
		# the current node in the conversation
		conversation = stack.pop()
		
		prompt = prompts.pop()

		# add an ai_dialog section to the conversation
		dialog = raw_input("What does the character say " + prompt)

		if (len(dialog) == 0):
			continue

		ai_dialog = SubElement(conversation, "ai_dialog").text = dialog

		# determine how many dialog options the player has at this point
		how_many_options = int(raw_input('how many dialog options does the player have from "' + ai_dialog +'" -> '))
		
		# if there are dialog options...
		if (how_many_options > 0):

			# create a branch for player dialog options
			player_dialog_options = SubElement(conversation, "player_dialog_options")

			for i in range(how_many_options):

				# create a new choice
				choice = SubElement(player_dialog_options, "choice")

				# convert the dialog option number into ordinal form
				ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

				# add the player's reply 
				reply = raw_input("what is the player's " + ordinal(i+1) + ' response to "'  + ai_dialog +'" -> ')
				SubElement(choice, "reply").text = reply

				# add a new conversation as a child of the selected choice
				stack.append(SubElement(choice, "conversation"))
				prompts.append('to "' + reply +'" -> ')

	output = ElementTree(tree)

	# save the tree to an xml file in a local directory named after the character
	path = os.path.dirname(os.path.realpath(__file__))+"/character-dialogs/"+character_name+"_conversation.xml"
	output.write(path)
	
build()

# dialog-to-xml

A command line tool for creating "bethesda-like" dialogs

This program requires python 2.7.

#### The nested XML structure
``` XML
<conversation> 
    <ai_dialog>Greetings</ai_dialog>
    <player_dialog_options>
        <choice>
            <reply>Well hello there stranger!</reply>
            <converstation>...</converstation>
        </choice>
    </player_dialog_options>
</conversation>
```
A "conversation" is defined as an "ai_dialog" followed by a collection of user "choices". A choice is a text "reply" and a resulting "conversation". 

#### How to
This program produces an XML dialog file by providing the user with "fill in the blank" prompts

Examples include: 

>- What is the name of this character? -> *HAL*

>- what is the player's 1st response to "Greetings Dave" -> *Open the pod bay doors, HAL.* 

>- What does the character say to "Open the pod bay doors, HAL. " -> *I'm sorry, Dave. I'm afraid I can't do that.* 

In order to close a branch of the dialog tree you must state that the player has 0 choices left. For example:

>how many dialog options does the player have from "This mission is too important for me to allow you to jeopardize it. " -> *0*

#### Result
HAL_conversation.xml (saved to the included "character-dialogs" folder)
```XML
<conversation>
    <ai_dialog>Greetings Dave</ai_dialog>
    <player_dialog_options>
        <choice>
            <reply>Open the pod bay doors, HAL. </reply>
            <conversation>
                <ai_dialog>I'm sorry, Dave. I'm afraid I can't do that. <ai_dialog>
                <player_dialog_options>
                    <choice>
                        <reply>What's the problem? </reply>
                        <conversation>
                            <ai_dialog>I think you know what the problem is just as well as I do. </ai_dialog>
                            <player_dialog_options>
                                <choice>
                                    <reply>What are you talking about, HAL? </reply>
                                    <conversation>
                                        <ai_dialog>This mission is too important for me to allow you to jeopardize it. </ai_dialog>
                                    </conversation>
                                </choice>
                            </player_dialog_options>
                        </conversation>
                    </choice>
                    <choice>
                        <reply>Ok HAL, you do you</reply>
                        <conversation>
                            <ai_dialog>Ok goodbye Dave</ai_dialog>
                        </conversation>
                    </choice>
                </player_dialog_options>
            </conversation>
        </choice>
        <choice>
            <reply>Not right now HAL</reply>
            <conversation>
                <ai_dialog>...</ai_dialog>
            </conversation>
        </choice>
    </player_dialog_options>
</conversation>
```

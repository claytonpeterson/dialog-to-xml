# dialog-to-xml

A command line tool for creating "bethesda-like" dialogs

The nested XML structure
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

text = open("AndroidManifest.xml","r")
textinhalt=''
for i in range(0,2):
    textinhalt+=text.readline()
packagename=input("Please enter you Package name ")
textinhalt+='    package="'+packagename+'"\n'
text.readline()
for i in range(0,30):
    textinhalt+=text.readline()

text.close()
text = open("AndroidManifest.xml","w")
text.write(textinhalt)
text.close()
textinhalt=''
text = open("res/values/strings.xml","r")
for i in range(0,2):
    textinhalt+=text.readline()
name=input("Please input the Name for the Launcher ")
textinhalt+='	<string name="title_activity_mcpemain">'+ name + '</string>\n'
textinhalt+='	<string name="app_name">'+ name + '</string>\n'
textinhalt+='</resources>'
text.close()
text = open("res/values/strings.xml","w")
text.write(textinhalt)
text.close()


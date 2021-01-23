'''
Script to remove LIGHTSHOW parameter from info.dat files in the
Custom Song directory for Beat Saber.  This resolves error of songs
not loading in game.

The issue is identified when the song preview plays when selecting a song
but the menu to select difficulty and the play button do no appear.  

NOTE:
Back up your CustomLevels folder prior to running this script just incase
something goes wrong

change the rootdir variable to your target CustomLevels directory:
\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels

This seems to have a 90-95% success rate but not 100%.  still good for
an initial bulk solution.  continued problems can be hand modified if desired.

'''


import re
import os

#set your target directory
rootdir = '/home/jonr/Desktop/Projects/BeatSaber'

#Regex for the Song Name. only used in console.
names = re.compile( r'"_songName":.*')

#iterate through CustomLevels
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.upper() == 'INFO.DAT':

            f = open(os.path.join(subdir, file), "r")
            curFile = f.read()

            #Regex to target problem area
            targets = re.finditer(r'"_beatmapCharacteristicName":\s"Lightshow",', curFile) 
            brackets = re.finditer(r'\}', curFile) 

            #Print Song names to console, just for info.
            name = names.findall(curFile)
            for x in name:
                print(x)

            #primary Cleanup
            for m in targets:

                #initialize Bracket starting values
                startBracketPos = 0
                endBracketPos = len(curFile)

                #determine first open bracket of problematic area
                for bracket in brackets:
                    if bracket.start(0) > startBracketPos and bracket.start(0) < m.start(0):
                        startBracketPos = bracket.start(0)
                    else:
                        break

                temp = curFile[startBracketPos+2:endBracketPos]

                #print(temp)

                #determine last closed bracket
                bracketCount = 0
                passedCloseBracket = False

                for x in range(len(temp)-1):
                    if temp[x] == '}':
                        bracketCount += 1
                        passedCloseBracket =  True
                    if temp[x] == '{':
                        bracketCount -= 1
                        
                    if bracketCount == 0 and passedCloseBracket == True:
                        endBracketPos = x + startBracketPos +3
                        break

                #temp = curFile[startBracketPos+2:endBracketPos]
                #print(temp)

                #splice out the problemtic area via index positions
                curFile = curFile[0:startBracketPos+2:] + curFile[endBracketPos::]

            #closing file to reopen in write mode
            f.close()

            #clean up orphan commas
            curFile = re.sub(pattern = r'\},\s*\}', repl = r'}}', string = curFile)
            curFile = re.sub(pattern = r'\},\s*\]', repl = r'}]', string = curFile)
            curFile = curFile.replace(',,', ',')
            curFile = curFile.replace('},]', '}]')
            curFile = curFile.replace('},}', '}}')

            #save the modified info.dat file 
            f = open(os.path.join(subdir, file), "w")
            f.write(curFile)
            f.close()
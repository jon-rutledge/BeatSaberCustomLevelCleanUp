# BeatSaber Custom Level Cleanup script

## How to use?

1. All you need is Python3 on your device.
2. Backup your CustomLevel directory to another location.
3. Modify the rootdir variable in the script to point to your CustomLevel directory.
4. Run the script.
5. Profit!

### What does this solve?

This is intended to resolve the "infinite loading" glitch on some custom tracts, specifically those downloaded from https://bsaber.com.


### What causes this issue?

After some testing, it appears that the following block for Lightshow needs to be removed:

```
{
      "_beatmapCharacteristicName": "Lightshow",
      "_difficultyBeatmaps": [
        {
            ...
        }
}
```

Once this piece is removed, everything seems to work.

### What does the script do?

The python script simply tries to parse the INFO.dat files inside of the CustomLevel directory and remove this portion from them.

### How effective is it?

Before creating this script, about 30-50 songs were not working.  after running the script, there are only 3.  I am satisfied with this was a personal project, and the outliers can be fixed manually if desired.


### But I am scared to run it across all my songs incase they break! 

That is why I highly reccomend backing up your CustomLevel folder prior to running.  You can also test in an isolated environment by only placing a few custom track folders in a seperate test directory first. 
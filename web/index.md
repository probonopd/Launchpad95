# Launchpad95: Improved Novation Launchpad remote scripts

These scripts are modified version of Ableton Live 9.2 scripts for
Novation Launchpad and provide the same functionality but add support
for editing the midi clips using a step sequencer, an Instrument
Controller and Device Controller and an improved Instrument Mode. It
does not require any external tool like Max for Live (M4L) in order to
work. This script is just a plain Live Control Surface Python Script.

> __Note__: Launchpad95 derives from Ableton Live 9.2 scripts. Would it be beneficial to recreate this from Ableton Live 11 scripts for RGB Launchpad and/or Push models, to get a more native user experience (e.g., matching what is printed on the buttons more to the functions performed by the software)?

## Installation

### Supported Hardware and Software

Ableton Live 9.2 or greater, 10 and 11 are supported.

> __Note__: Ableton Live 11 introduced support for MIDI Polyphonic Expression (MPE). However, at this point, Launchpad95 does not support MPE. Is it still possible to use [Polyphonic aftertouch like on the Push](https://www.youtube-nocookie.com/embed/m2KW_yahgYE)?

In terms of hardware the following are supported:

- Launchpad
- Launchpad S
- Launchpad Mini
- Launchpad MK2 (RGB)
- Launchpad Mini MK2 (RGB)
- Launchpad Mini MK3 (RGB)
- Launchpad X (RGB)
- ~~Launchpad PRO~~ see [Launchpad
  Pro95](http://motscousus.com/stuff/2015-12_Novation_Launchpad_Pro_Ableton_Live_Scripts/)
- ~~Launchpad PRO MK2~~ is not supported

### Setup

- Download the installation archive:
  **[Launchpad95.zip](https://github.com/hdavid/Launchpad95/archive/refs/heads/master.zip)**
- For Live 10 and above, Unzip the zip file and copy the folder
  Launchpad95 into you Ableton Live User Library, in a folder named
  "Remote Scripts". Create this folder if needed.
  <br><img src="setup-folders.png" style="margin:10px" /></br>
  On Windows, this folder is located at
  `C:\Users\...\AppData\Roaming\Ableton\Live 11.x.y\Preferences\User Remote Scripts/`.
- For Live 9 users, see [faq 4](#faq-4)
- After the folder has been copied, plug-in your Launchpad in the
  computer and start Ableton Live. Open up the preferences panel and go
  to "MIDI Sync" panel. Select Launchpad95 as your control surface and
  select the launchpad Midi Port MIDI ports like shown below.  
  Newer Launchpads (X and Mini MK3) offer two inputs and output ports.
  Make sure to use the 2nd one, both for input and output.  
  <img src="setup-script.png" style="margin:10px" />
- Make sure to enable "Track", "Sync" and "Remote" in the midi options
  below for the MIDI ports used by Launchpad95.  
  <img src="setup-ports.png" style="margin:10px" />
- For Live Suite users, in the M4LDevice folder is included an OSD (on
  screen display) Max4Live device that will display information,
  similarly to what one could see on an Ableton Push screen.  
  <img src="osd.png" style="margin:10px" />

## User Manual

Four modes are added on top of the existing modes. These are **Drum Step
Sequencer** mode to edit midi clips, a **medodic step sequencer**, and
**Device Controller** mode to edit any parameter of any instrument,
effect or device on any track of your arrangement, and finally an
**Instrument Mode** providing a tighter integration with Live.

Note the manual is also available in [french as a
PDF](Manual_%20Launchpad95_FR.pdf), thanks to François Lehérissier.

### Instrument Controller Mode

Instrument Mode replaces classic User Mode 1. To activate Instrument
Controller Mode, press User Mode 1 button (mode button remains amber).
Press User Mode 1 button once again, button turns green, activating the
Device Controller. Once more the button will turn red, activating the
plain old User Mode 1 in case you need it.

The top up/down navigation buttons allow to navigate scenes, while the
left/right button allow to navigate tracks. The scene buttons allow you
to control the currently selected track and clip, arm, solo, record,
play, stop etc (see below).

The matrix of buttons act as a midi keyboard proposing a drum rack
layout, and a melodic mode. Melodic mode enable you to select root note,
type of mode (major, minor etc), and the octave you play in.

Most of the scene buttons have alternate functions when you hold them
long (0.5 sec):  
- undo: a long press will perform a redo!  
- stop: a long press will DELETE currently selected clip. No worries
this is undoable!  
- solo: a long press on solo will enable/disable the selected track.  
- arm: holding arm for more than 0.5 seconds will toggle live's
metronome. A very long press (2 sec) will alternate between auto arm of
track and manual track arming. Colour of the button will reflect the
selected mode. This is really useful if you have more than one
controller/person interacting with Live.

|![](https://placehold.co/64x64?text=^)<br>prev scene|![](https://placehold.co/64x64?text=V)<br>next scene|![](https://placehold.co/64x64?text=<)<br>prev track|![](https://placehold.co/64x64?text=>)<br>next track|![](https://placehold.co/64x64?text=Session)<br>Session mode|![](https://placehold.co/64x64?text=Note)<br>user 1 Inst.|![](https://placehold.co/64x64?text=Custom)<br>user 2 step|![](https://placehold.co/64x64?text=Capture+MIDI)<br>mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Volume)<br>__enter scale edition mode__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Pan)<br>__undo. long press to redo__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Send+A)<br>__octave up__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Send+B)<br>__octave down__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Stop+Clip)<br>__stop selected clip__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Mute)<br>__start selected clip__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Solo)<br>__solo current track__|
|   |   |   |   |   |   |   |   |![](https://placehold.co/64x64?text=>+Record+Arm)<br>__session record__|

#### Scale edition mode

To enter scale edition mode press (and keep pressed) the 1st scene
button from Instrument mode.

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|absolute root|orient.|chromatic guitar|diatonic sequent|diatonic 3rd|diatonic 4th|chromatic|drumrack|__enter scale edition mode__|
|C#|D#|relative scale|F#|G#|A#|5th left|quick scale mode|__undo. long press to redo__|
|C|D|E|F|G|A|B|5th right|__octave up__|
|-2|-1|0|1|2|3|4|5|__octave down__|
|Major|Minor|Dorian|Mixolyd.|Lydian|Phrygian|Locrian|Diminish.|__stop selected clip__|
|Whole-half|Whole Tone|Minor Blues|Minor Penta.|Major Penta.|Harmonic Minor|Melodic Minor|Super Locrian|__start selected clip__|
|Bhairav|Hunga. Minor|Minor Gypsy|Hirojoshi|In-Sen|Iwato|Kumoi|Pelog|__solo current track__|
|Spanish|IonEol|   |   |   |   |   |   |__session record__|

* __Orient__: this button will change the orientation from vertical to horizontal of
the instrument mode.
* __Absolute root__: The bottom left left button will always be the root mode of the selected
root note.
* __Chromatic Guitar__: Scale Mode is pretty much like regular chromatic mode, except the top
four rows are all shifted by one semitone. This is so that the bottom 6
rows emulate standard guitar tuning.
* __Diatonic sequent__: Each row represents an octave, so each first and last button of each row
will be the root note.
* __Diatonic 3rd__: When moving from one button to the next top, you will move a 3rd degree
in the scale. 3rd is very practical to play chords vertically.
* __Diatonic 4th__: When moving from one button to the next top, you will move a 4th degree
in the scale. 4th is the default mode, also on the push.
* __Chromatic__: Each button to the left or right of a button will be a semitone lower or
higher.
* __C, C#, D, D#, E, F, F#, G, G#, A, A#, B__: Selects the root note of the scale.
* __Relative scale__: Changes current selected scale to its relative scale. IE. from C major
to C minor and vice versa.
* __5th left__: Changes current selected scale to the prior scale in the circle of
fifths (a 5th lower).
* __5th right__: Changes current selected scale to the next scale in the circle of fifths
(a 5th higher).
* __Quick scale mode__: Substitutes the top 2 rows of instrument mode for the quick scale modes
(see below).
* __-2, -1, 0, 1, 2, 3, 4, 5__: Changes the octave of the instrument mode.

#### Quick scale modes

If quick scale is activated (last button on the right on the 2nd row in scale edit mode), the two first rows of the launchpad allow you to quickly change the scale.

This shows the two first rows of the Launchpad. The last button of the first row changes between root note selection and mode selection.

#### Root note

In this mode you can select the root note of your scale. You can also quickly alternate between minor and major by pressing the button again.

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|C#|D#|relative scale|F#|G#|A#|5th left|scale/mode toggle|__enter scale edition mode__|
|C|D|E|F|G|A|B|5th right|__undo. long press to redo__|

#### Quick scale modes: modus

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|Major|Minor|Dorian|Mixolyd.|Lydian|Phrygian|Locrian|scale / mode toggle|__enter scale edition mode__|
|Diminish.|Minor Blues|Harmonic Minor|Melodic Minor|Super Locrian|Hunga. Minor|Minor Gypsy|Spanish|__undo. long press to redo__|

In this mode you can select the mode of your scale.

#### Note repeat

In this mode you can activate and configure note repeat.

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|Swing +2.5%|Swing -2.5%|Swing 0%|Swing 25%|Swing 50%|Swing 75%|Repeat On/Off|Scale / mode toggle|__enter scale edition mode__|
|1/4|1/4T|1/8|1/8T|1/16|1/16T|1/32|1/32T|__undo. long press to redo__|

### Drum Step Sequencer Mode

To activate the Drum Step Sequencer, select a midi clip in the clip view. Then press User Mode 2 button once, activating the step sequencer (in normal mode). Press user mode 2 button once more opens the Melodic Step Sequencer.

This sequencer has two sub modes detailed below. combined and multinotes. (note there is a second step sequencer, Melodic Step Sequencer detailed further down).

A playback/metronome indicator is scrolling thru the grid in amber to indicate the playing position of the clip as the clip is playing. This is just an overlay, it does not affect the functionality of the buttons.

Here are the colour codes used :
* Normal notes are shown in Green, intensity depending on their velocity.
* Muted notes are displayed in red.
* Notes being currently played are flashing in red.
* Notes being played and being outside of the currently displaying midi clip block will also flash in red.
Some other information is displayed, using orange colour :
*  Note markers help to better visualise what row correspond to which note:
     * Root note of the selected are marked with three orange left buttons lit up.
     * Other notes of the scale are marked with one orange button lit on the left-most row.
* While scrolling left and right along the clip, a vertical bar will display you where you are in the clip

A summary of functions assigned to the buttons is shown in the table below. Hover your mouse above a button to get detailed descriptions.

StepSeq by default works in combined mode. pressing the 4th scene button toggles between combined mode and multi note mode. Multinote mode works in similarly to the the previous step in launchpad85, while combined mode offers mode close to the way Push StepSeq behaves.

#### Combined Mode

The bottom left area let you select the note currently being edited on the top note editor.

The bottom right area allows you the select the currently clip part currently being displayed (single button press) and edited (double press or one button after the other).

Some buttons have combined function:

* Lock (2nd scene button):
  * Press long to switch between clip lock and play clip on locked track mode
  * Yellow : track lock mode. step sequencer is locked to current track and will follow playing clip on this track
  * Red : step sequencer is locked to current clip.
* Quantize (3rd scene button):
  * Press long duplicate clip in a new clip
* Mute (last scene button):
  * Hold mute button and click on a note to mute it
  * Hold mute button and press on a note in the bottom left quadrant to mute it
  * Hold mute button and select a loop range in the loop selector to delete it
* Velocity (7th scene button):
  * Hold velocity button and click on a note to change its velocity
  * Hold velocity button and click on a note to change in the note selector to ear a preview of the sound
  * Hold velocity button and select a loop range in the loop selector to extend the original clip content to the newly selected length
* Velocity (7th scene button) and mute
  * Hold velocity button and mute button at the same time and select a loop range in the loop selector in order to mute this time selection

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |__Scale__: Display Scale Selection Overlay|
|   |   |   |   |   |   |   |   |__Lock__: Lock step seq to current clip (very useful !).|
|   |   |   |   |   |   |   |   |__Quant.__: Cycle thru available quantisations|
|   |   |   |   |   |   |   |   |__Modes__: Switches between combined and multinote modes|
|   |   |   |   |   |   |   |   |__Up__: Scroll up (notes)|
|   |   |   |   |   |   |   |   |__Down__: Scroll down (notes)|
|   |   |   |   |   |   |   |   |__Velocity__: Cycle thru velocities and velocity shift notes|
|   |   |   |   |   |   |   |   |__Mute__: Hold and press a note in the matrix to (un)mute it. Hold and press a note in the note selector to mute a lane. Hold+nav keys to scroll up/down one octave|

* __user 2 step__: Cycle thru StepSequencers and User Mode 2

#### Multinote Mode

To activate this mode, press the 4th scene button while in Combined Mode (pressing the same button again will take you back to Combined Mode).

This mode uses the grid as a 8*8 matrix. one midi note per row. It follows the scale mode selected. Note that the left and right arrows are used to navigate left and right in the clip.

Buttons as above, plus:
* __user 2 step__: Cycle thru StepSequencers and User Mode 2
* __prev scene__: Select prev scene
* __next scene__: Select next scene
* __prev page__: Select prev clip page
* __next page__: Select next clip page

### Melodic StepSequencer

To activate this mode, press user mode 2 button until it turns green.

This mode behave more how a hardware stepsequencer works. it uses the grid as a 7*8 matrix to edit note pitch, velocity, length and octave. one function per page. of course notes pitches follow the selected scale !

The last row of the matrix acts as a page selector and work in the similar fashion to the combined step stequencer loop selector.

Double press on the last scene button toggles between monophonic and polyphonic modes.

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |__Scale__: Display Scale Selection Overlay|
|   |   |   |   |   |   |   |   |__Lock__: Lock step seq to current clip (very useful !).|
|   |   |   |   |   |   |   |   |__Quant.__: Cycle thru available quantisations|
|   |   |   |   |   |   |   |   |__Random__: randomise the selected function (pitch,length,velocity,octave)|
|   |   |   |   |   |   |   |   |__Length__|
|   |   |   |   |   |   |   |   |__Octave__|
|   |   |   |   |   |   |   |   |__Velocity__|
|   |   |   |   |   |   |   |   |__Notes__|

* __prev scene__: Select prev scene
* __next scene__: Select next scene
* __user 2 step__: Cycle thru StepSequencers and User Mode 2

### Device Controller Mode

### Navigation

Navigation among tracks and devices is done using the top left navigation buttons.

### Editing parameters

You can edit eight parameters of the selected device on the selected track at once. One parameter per column. You can navigate banks of parameters using scene buttons 2 and 3. depending on the type of parameter edited launchpad will display then in different ways.

* __On/Off parameters__:
Using the color code red. only one button will be used to change the
parameter.

* __Parameter with list of values__: 
For the parameters that have a list of values, the colour code it amber,
for example a Synth wave form selector (square, sine, triangle). If the
parameter has less that 8 values, they will be directly acessible one by
one. if more values are available, you can scroll thru the values. the
closer the button to the center the more precise. the closer the top or
bottom of the launchpad, the greater the value change will be at each
press.

* __Parameter continuous values__: 
For the parameters that have a continuous value, like Volume, Panning,
etc, the colour code is green. by default Launchpad displays the
parameter like a volume slider on the mixer mode. if you activate the
precision slider mode (by pressing scene 4 button), the sliders will
then work in the similar way to the case of parameter with list of
values.

#### Locking to devices

You can save up to 4 devices using the 4 bottom scene button. if not device is saved, the button will be pink. To save a device, first select the desired device, then press one of the 4 last scene buttons for more than half a second. the button turn red ! your device is saved. You can recall it at any time by a short press on the scene button. To unsave a device, apply a long press again on the button.

|Device+|Device-|Track-|Track+|Session mode|user 1 device|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |__On/Off__|
|   |   |   |   |   |   |   |   |__Bank+__|
|   |   |   |   |   |   |   |   |__Bank-__|
|   |   |   |   |   |   |   |   |__Precision__|
|   |   |   |   |   |   |   |   |__Lock1__|
|   |   |   |   |   |   |   |   |__Lock2__|
|   |   |   |   |   |   |   |   |__Lock3__|
|   |   |   |   |   |   |   |   |__Lock4__|

### Session Mode

|scenes up|senes down|tracks left|tracks right|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |__Undo__|
|   |   |   |   |   |   |   |   |__Shift Se/LaunQ__|
|   |   |   |   |   |   |   |   |__BPM CopyPst__|
|   |   |   |   |   |   |   |   |__Quant. RecQ__|
|   |   |   |   |   |   |   |   |__Double FixLen__|
|   |   |   |   |   |   |   |   |__Delete Mute__|
|   |   |   |   |   |   |   |   |__Duplic. Solo__|
|   |   |   |   |   |   |   |   |__Record Arm__|

### Pro Session Mode

This mode adds functions to the classic Session Mode. To activate Pro Session Mode, press and release Session button (mode button remains amber). Repat to back to normal Session Mode.

The down navigation buttons allow to navigate using the Session Box (note that it olny have 7 rows) The scene buttons allow you to perform several functions as shown below.

* __Undo__
  * Long press: Redo
* __Shift Se/LaunQ__
  * Also acts as Shift button
  * Double click: hide detail view
  * Shift + Matrix: select clip and show details
  * Shift + Last Row: clip launch quantization
* __BPM CopyPst__
  * Double click: Metronome ON/OFF
  * Tempo + Matrix: Fold/Unfold track
  * Shift + Tempo + Matrix: Launch scene
  * Tempo + Last Row: Tempo
* __Quant. RecQ__
  * Double click: Record Quantization ON/OFF
  * Quantize + Matrix: Quantizes clip
  * Shift + Quantize + Matrix: Create new Scene
  * Quantize + Last Row: record quantizatin
* __Double FixLen__
  * Double click: Unsolo all tracks
  * Duplicate + Matrix: Duplicate clip
  * Shift + Duplicate + Matrix: Duplicate Scene
  * Duplicate + Last Row: Solo Track
* __Delete Mute__
  * Double click: Unmute all tracks
  * Delete + Matrix: Delete clip
  * Shift + Delete + Matrix: Delete Scene
  * Delete + Last Row: Mute Track
* __Duplic. Solo__
  * Double click: Unsolo all tracks
  * Duplicate + Matrix: Duplicate clip
  * Shift + Duplicate + Matrix: Duplicate Scene
  * Duplicate + Last Row: Solo Track
* __Record Arm__
  * Shift + Record: Single/Multi Record mode
  * Single Record
    * Single click: Session Record ON/OFF
    * Record + Matrix: Arm track and launch clip (Record/Overdub clip)
    * Record + Last Row: Arm Track
  * Multi Record
    * Single click: Jump to the next available clip slot and start recording for each armed track
    * Matrix Button: Arm clip track and launch clip (Record/Overdub clip)
    * Record + Last Row: Arm Track

Below are the last matrix row for each of the modes:

#### Launch and Record Quantization, and fixed clip length recording

|on/off|decrease|increase|value1|value2|value3|value4|value5|Record Arm|
|---|---|---|---|---|---|---|---|---|

#### Metronome and Tempo

|on/off|nudge left|nudge right|-5|-1|+1|+5|tap|Record Arm|
|---|---|---|---|---|---|---|---|---|

#### Mute, Solo, Arm

|arm mute solo|arm mute solo|arm mute solo|arm mute solo|arm mute solo||||Record Arm|
|---|---|---|---|---|---|---|---|---|

### User1 Mode

Note that User1 Mode is now disabled by default. It can be activated again by editing `Settings.py`.

### User2 Mode

Note that User2 Mode is now disabled by default. It can be activated again by editing `Settings.py`.

### Mixer Mode

#### Volume

If you wish to override default mapping for volume slider buttons you can set it via `VOLUME_LEVELS` setting in the `Settings.py` file.

|prev scene|next scene|prev track|next track|Session mode|user 1 Inst.|user 2 step|mixer mode|   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |__Volume__|
|   |   |   |   |   |   |   |   |__Pan__|
|   |   |   |   |   |   |   |   |__Send A__|
|   |   |   |   |   |   |   |   |__Send B__|
|   |   |   |   |   |   |   |   |__Stop All__|
|   |   |   |   |   |   |   |   |__Active all__|
|   |   |   |   |   |   |   |   |Unsolo II|
|   |   |   |   |   |   |   |   |Unarm All|


## Max For Live On Screen Display / Helper

Launchpad95 comes packaged with a Max for Live device that will display useful information about currently selected tracks, clips and other parameters. Make sure to try it!

<img src="osd.png" style="margin:10px" />

It is available in `Launchpad95/M4LDevice/Launchpad95 OSD.amxd`.

## Source

https://github.com/hdavid/Launchpad95/

## FAQ

1\. Which Launchpad flavours are supported__: 
Launchpad, Launchpad S, Mini, Mini MK2 and MK2 (RGB), Mini MK3, and
Launchpad X are supported  
Basically all Launchpad but the pro are supported by this script.  
Launchpad Pro is supported by [Launchpad
Pro95](http://motscousus.com/stuff/2015-12_Novation_Launchpad_Pro_Ableton_Live_Scripts/)

2\. Which Ableton live versions are supported  
Launchpad 95 works with Live 9.2+, and Live10 32 bit or 64 bit, Mac or
Windows, suite or intro or standard. Basically with every combination
you may think of as long at it is live 9.2 or greater.  
Of course Ableton from time to time change their Python Live without
notification and therefore Launchpad95 might stop working, but i am
trying to keep up and the changes.  
if Launchpad95 stopped worked after an update, make sure to download the
last version from this site.  

3\. Where should I put the script (for live 10 & 11)?  
From Live Browser, head to your "User Library". and create a folder
"Remote Scripts"  
Right click this folder and select "show in finder/explorer".  
Copy the Launchpad95 folder there.  
<img src="setup-folders.png" style="margin:10px" />

4\. Where should I put the script (for live 9)?  
On pc/windows 7: inside
"C:\ProgramData\Ableton\Live 9 Suite\Resources\MIDI Remote Scripts"  
On a mac right-click the Live application you use (there might more than
one installed!) and select "view package content", then browse to
"App-Resources/MIDI Remote Scripts".  
  
Inside this "MIDI Remote Scripts" folder, you should have a folder
called "Launchpad95". inside this folder you should have a bunch of .py
files, and a for each of them a .pyc file. (.pyc files are compiled
version of the .py that live compiles as you start it.)  
  
Sometimes a picture is worth 1000 words. Take a look at these
screenshots.  
- On a mac it look like this:  
<img src="setup-folders-9.png" style="margin:10px" />  
- on a pc like that:
<img src="setup-folder-9-win.png" style="margin:10px" />  

5\. It does not work, I installed everything, but the launchpad does not light up when I select Launchpad95 in the dropdown in the preferences. what is wrong?  
It is hard to guess what you did wrong. You must have installed not the
right way somehow. Try to install it from scratch again, download from
this site, extract install, restart live. Among the list of things you
can try to do:

- \- check the you installed at the right place. (check [question
  \#3](#faq-3) and [question \#4](#faq-4)!)
- \- Pay attention to the folder name AND its full path. (again see
  screenshots in above in [question \#3](#faq-3) [question \#4](#faq-4))
- \- how many versions of live do you have installed?
- \- are you running live 9.2 or greater? for live 8 please use
  launchpad85. For live 9.0, upgrade to live 9.2+.

6\. It does not work, I installed everything, but Launchpad95 does not appears the dropdown in the preferences. what is wrong?  
See [question 5](#faq-5).  
  
7\. Note Feedback is not working in Instrument Controller  
Make sure you activated the launchapd midi in/out as "track" in Live
midi preferences.  

8\. Live 8?  
For Live 8.4: [Launchpad85](launchpad85.html).

9\. good work! I wish to donate! is there a way to donate somehow?  
Sure! Your donations allowed me to pay for the Launchpad Pro that is
now supported! thank you for this.  
[paypal](https://www.paypal.com/us/cgi-bin/webscr?cmd=_send-money&nav=1&email=hdavid@mail.com)
to my account hdavid@mail.com.

## Known Issues

- in live 9, moving notes in clip editor while stepseq is open
  duplicates notes.
- [Launchpad85](launchpad85.html) for live 8 is now longer
  maintained/improved.

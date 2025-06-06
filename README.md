# simracing-telemetry-to-openrgb
This repo contains an attempt at creating a "telemetry wrapper" which can communicate with OpenRGB. The goal is to take telemetry data from some games (currently Assetto Corsa Competizione and Le Mans Ultimate), and represent it through the PCs lighting.
<br> => The current main goal is to use my PC as a shift light. Based on RPM, the case will lighten up either green, yellow or red.

It's written in Python, and where possible, existing telemetry or shared-memory-scrapers were used - they can be found linked in the respective chapters below.

## Setup

### Assetto Corsa Competizione (ACC)

There is no setup needed for ACC - the game already exposes telemetry via shared memory

### Le Mans Ultimate (LMU)

In order to be able to read from shared memory you need a plugin. There are 3 ways to get to this plugin:

1. If you're using SimHub: 
   1. Open SimHub
   2. On the right side of the notification saying "Le Mans Ultimate telemetry is not configured", click on "Fix it automatically"
      1. While this installs the plugin, it will show a red exclamation mark next to the game's title. This is only there to indicate that it's using a plugin from rFactor2 - as it's built on the same engine, the plugin still works
2. If you're using CrewChief
   1. Open CrewChief
   2. In the top left corner you'll find a drop-down where you can pick the game you want to use CrewChief with > select "Le Mans Ultimate"
   3. The program will now install the plugin and restart
3. Manual installation
   1. To manually install the plugin, download it from [here](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin) - you can find it under the title "Download"
   2. Unzip the `.zip` file and go into `rf2_sm_tools_3.7.15.1/rf2smmp/` to find the plugin as a `.dll` file
   3. Go to your game directory by going into Steam > right click the game > Manage > Browse local files > go to the "Plugins" directory
   4. Move the `.dll` file into the plugins folder

### OpenRGB

> Make sure to check their [list of all supported devices](https://openrgb.org/devices.html) to ensure that your device is supported before going into this

Before being able to do anything with OpenRGB, it has to be installed. You can find both a stable as well as an experimental build at the bottom of [their page](https://openrgb.org/). 

Once you downloaded it, make sure to start it up and see if you can find your relevant devices - depending on your setup, that can be your headphones, your keyboard, your PC fans, etc. 
If you're able to find the devices, you're ready to go and you can hop into the code:


## Implementation

> I'm going to assume that you have a python environment ready to use. If not, try to follow some guides online - I can highly recommend using pyCharm, as it does most of the annoying work for you

With all the preparations done, we can dive into the code:

First and foremost, you need some libraries to get this project going. This includes [pyRfactor2SharedMemory](https://github.com/TonyWhitley/pyRfactor2SharedMemory) for LMU, [PyAccSharedMemory](https://github.com/rrennoir/PyAccSharedMemory) for ACC and [openrgb-python](https://github.com/jath03/openrgb-python). 
For ACC and OpenRGB, you can find the download/`pip` commands on their repository - for LMU, however, you're best off either cloning their repo locally (`git clone https://github.com/TonyWhitley/pyRfactor2SharedMemory.git`) or copying over the relevant files - more on that later.

### Testing the individual components


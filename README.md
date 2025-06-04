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

With the telemetry data ready to be used, we need to 


## Implementation

> See [pyRfactor2SharedMemory](https://github.com/TonyWhitley/pyRfactor2SharedMemory) for the code used to access the shared memory


> See [PyAccSharedMemory](https://github.com/rrennoir/PyAccSharedMemory) to find out how to access the shared memory data of Assetto Corsa Competizione

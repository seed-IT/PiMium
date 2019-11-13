---
title: Seed-IT
subtitle: Manual WiFi configuration on Raspberry Pi devices
author: 
    - Melvin Campos Casares
date: 13 novembre 2019
lang: fr
papersize: a4
fontsize: 11pt
whitespace: small
margin-top: 1.5cm
margin-left: 2.5cm
margin-right: 2.5cm
margin-bottom: 1.5cm
keywords: [Project, integration, seed-IT, dev, tutorial, WiFi, configuration, EPHEC, 3TI]
titlepage: true
titlepage-rule-color: "2abf2a"
footer-left: Manual - WiFi configuration on Raspberry Pi devices
titlepage-rule-height: 6
toc: true
toc-own-page: true
toc-title: Manual - how to manually configure WiFi networks onto Raspberry Pi devices
logo: "seed-it-logo.png"
logo-width: 300
---

# Add WiFi network info onto Raspberry Pi devices

Create a file in the root of boot called: `wpa_supplicant.conf` (instructions below).
Then, paste the following into it (adjusting for your [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes), network name and network password):

```conf
country=BE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```

Save the file and reboot the Raspberry Pi.

## Access the boot folder

### Raspbian instructions

Here, we suppose you're either directly working on the Raspberry Pi or via SSH, but always under root access.

1. Open a terminal
2. Go to the boot folder : `cd \boot\`
3. Create the new file either with vim or nano (example with vim): `sudo vim wpa_supplicant.conf`
4. Don't forget to save the file before quitting vim or nano

### Mac instructions

For those instructions, we suppose you burned fresh Raspbian on a microSD card.

1. Create a new empty file that will hold network info
2. Via terminal : `touch /Volumes/boot/wpa_supplicant.conf`
3. Edit the file and then save it.

### Windows instructions

1. Run Notepad
2. Paste in the contents holding network info
3. Click **File / Save as...**
4. Be sure to set **Save as type** to **All files** (so the file is NOT saved with a .txt extension)
5. Call the file `wpa_supplicant.conf` and save it
6. Close the file

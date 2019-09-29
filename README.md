# ARTY

This project is a device that rescuing drowning victim in pool.

## Getting Started

Set up a Raspberry Pi Desktop on Window and MacOS

### 1. Download Raspberry Desktop ISO:

Go to following link and download Raspberry Pi Desktop (for PC and Mac), this link gives you an iso file or debian OS image:

```
https://www.raspberrypi.org/downloads/
```

### 2. Download Virtual Box:

Go to following link to download and install a Virtual Box:

``` 
https://www.virtualbox.org/
```

### 3. Setup Virtual Box:

```
Open Virtual Box, click new

Give your virtual PC a name, Type Linux, Version Debian (64GB)

Give a memory size you like

Create a virtual hard disk now

VDI should be selected as default, click next

Next, next, next, until the setup closed 

On Virtual Box front page:

Select your virtual box, click setting

Go to storage, under controller IDE, add the Raspberry iso image

Click Ok

Start the virtual PC

At the prompt, select Install and Enter

Choose "Guided – use the entire disk" 

Keep pressing Enter to "Select disk to partition", choose the Partitioning scheme, and 

"Finish partitioning and write changes to disk"

After a while, at the prompt “Install the GRUB boot loader to the master boot record?” 

Select Yes, and choose /dev/sda.

### 4. To access network:

In Setting, set the network type to Bridge, click advanced, for promiscous mode, select "Allow VMs"

Enjoy :)

```

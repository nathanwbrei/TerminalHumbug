
Terminal Humbug
===============

A Humbug client for the terminal. Implemented as a Chrome extension+Python script. Provides an unobtrusive feed of humbug messages on stdout. It will be obsolete in a week when the Humbug read API is released, but I can't wait that long.

This project deliberately avoids message sending functionality, even though this would be easy with the existing Humbug write API. The aim is to provide an unobtrusive, noninteractive feed so that the user can keep abreast of recent developments without undue distraction or context switching. If the user wishes to respond, they merely switch to the open Chrome tab, and interact there.


How it works
------------

The Chrome extension's Javascript watches an open Humbug tab. When messages are pushed, it scrapes, parses, and sends via HTTP to the python script. The Python script 


Installation
------------

1. git clone nathanwbrei/terminalhumbug 
2. chrome://extensions
3. enable dev mode
4. load unpacked extension
5. open humbug in a tab somewhere
6. python humbug.py


# Oberlo-Bot

This is a bot fully automating the Oberlo order process. No need to go to a computer to start the oberlo order or to get tracking info.
This bot logs in Aliexpress, logs in Oberlo. Start the orders and then get all the tracking info from the preivously done orders.

Place your username and password for Oberlo and Aliexpress in the config file (it has to be the same for the 2 services)
Launch the script and abort it, install the Oberlo plugin in the Chrome profile the scripted created.

You can now launch the scrip again and it will order all the products in the oberlo queue, it will then get the tracking code for the sent orders.

You could run this scrip all day long on a raspberry pi or a server but be carefull not to run it too often as the captcha will be triggered.
Capcha will also be triggered if you do more than 4 orders in a row so be sure to run the scrip more than once a day if you have many order (maybe like every 2 hours).

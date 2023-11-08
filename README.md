# Velkommen til internettet (eller ihvertfald APC220 projektet)

## What is this?

Det der forsøges lavet her er et communikations interface mellem to APC220'er radio moduler :D
Planen er at receiver (rballoon) skal køre på balloonen, sende telemetry en gang imellem, og ellers bare lytte.
Transmitter (tballoon) skal sende kommandoer til rballoon, og ellers modtage telemetry på timeout.

## Cool - så hvad sker der for filerne?

APC220.py er ment som et slags library (eller modul eller pakke eller something), og er der de fleste kommandoer der handler om at sende eller modtage skal ligge.

rballoon.py og tballoon.py er ment som de filer der reelt skal køre på ballon og i bil/gnd.

transmit.py og receive.py er bygget til eksempel, men også lidt for at teste ting..

## Hvad er status, og hvad er up next?

Status er at rballoon og tballoon kan pinge frem og tilbage - det kører noglelunde som det skal, transmitter "telemetry" og data korrekt.

Next up er bedre data indpakning - pt bliver alting pakket som UTF-8 encoded strings, hvilket fungerer okay, men skaber en del mere data end nødvendigt. Dette begynder dog at kræve at vi kender hvad der skal sendes

@IDE:
Man kunne evt sende en ekstra byte per information, som indikerer datatypen af det der sendes? Det skaber en byte overhead per information, men et mere fleksibelt system?

Tror det er noglelunde det - fang mig hvis der er spørgsmål :D

Beklager alt det der ikke er ordenligt kommenteret :i

Bugs:
1:
b = self.read_until(expected=endChar)
Giver "unknown parameter: Expected"

    2:
    read = read.removesuffix("#!")
    Findes ikke for string

    3:
    Inputimeout modulet kunne jeg ikke hente til rpi

Istedet for at basere på tid, basere på request??

https://realpython.com/python-sockets/

# KommDes-TypographyVisualiser

---
## Ausführung


### 1. Python Installation

Zu allererst, muss sicher gegangen werden, dass Python auf dem Gerät installiert ist.
Hierzu kann eine Kommandozeile/Terminal mittels `Win/Command + R` geöffnet und der Befehl

````` cmd
python --version
`````

ausgeführt werden.

Liefert dieser Befehl folgendes Ergebnis (oder eine neuere Version), ist python installiert.
Bei einer älteren Version sollte python auf den neusten Stand gebracht werden.

![image-20200511155420353](TypographyVisualiser/ressources/python%20install%20verification.jpg)

Wenn nicht, muss python vorerst über die [offizielle Python Webseite][1] heruntergeladen und installiert werden.

---
### (Optional) 1.5 Virtuelle Umgebung

Es wird empfohlen, python module in einer virtuellen Umgebung zu installieren.
Das Programm [Anaconda][3] vereinfacht dieses Vorgehen.

Ist Anaconda installiert, kann mit dem Kommandozeilen-Befehl 
`conda create -n umgebungs_name python=<version von python --<version>` eine neue Umgebung erstellt 

z.B. `conda create -n Test python=3.8.1` 

und mittels
`conda activate umgebungs_name` besucht werden.

--- 

### 2. Installation aller Requirements

Als nächstes müssen die zur Ausführung des Programms notwendigen Module installiert werden.

Hierzu reicht es aus, in der Kommandozeile `pip install -r requirements.txt` im Projektverzeichnis 
'KommDes - TypographyVisualiser/TypgoraphyVisualiser' 
auszuführen.


### 3. Starten des Programms

Zum Ausführen des Programms muss in der Kommandozeile (vom Grundordner, ansonsten Pfad zu Datei anpassen) der Befehl 

`python TypographyVisualizer/main.py` 

ausgeführt werden.

Dies startet den Flask Server, welcher dann unter `127.0.0.1:5000` über den Webbrowser erreichbar ist. Die IP wird nach Server-Start ebenso in der Kommandozeile ausgegeben und kann von dort kopiert werden, wenn nötig.

Zum Beenden der Anwendung muss lediglich in der Kommandozeile die Tastenkombination Strg+C unter Windows bzw. Command+C unter Mac gedrückt, oder das Kommandofenster geschlossen werden.

---

Dieses Projekt wurde im Rahmen des Moduls Kommunikations-Design im Sommersemester 2020 erstellt.

### Projektteilnehmer

* Angela Lisse
* Jasmin Esser
* Leon Krüger
* Niklas Tluk

[1]: https://www.python.org/downloads/
[3]: https://www.anaconda.com/products/individual

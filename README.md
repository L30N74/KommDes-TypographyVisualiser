# KommDes-TypographyVisualiser

---
## Ausführung


### 1. Python Installation

Zu aller erst, muss sicher gegangen werden, dass Python auf dem Gerät installiert ist.
Hierzu kann eine Kommandozeile/Terminal mittels `Win/Command + R` geöffnet und der Befehl

````` cmd
python --version
`````

ausgeführt werden.

<<<<<<< HEAD
Liefert dieser Befehl folgendes Ergebnis (oder eine neuere Version), ist python installiert.
Bei einer älteren Version sollte python auf den neusten Stand gebracht werden.
=======
![image 20200511155420353][python install]
>>>>>>> 26b9397aee53b237c87e7d2165c3881b4bc62ad6

Wenn nicht, muss Python vorerst über die [offizielle Python Webseite][python download] heruntergeladen und installiert werden.

---
### (Optional) 1.5 Virtuelle Umgebung

Es wird empfohlen, Python-Module in einer virtuellen Umgebung zu installieren.
Das Programm [Anaconda][anaconda download] vereinfacht dieses Vorgehen.

Ist Anaconda installiert, kann mit dem Kommandozeilen-Befehl 
<<<<<<< HEAD
`conda create -n umgebungs_name python=<version von python --version>` eine neue Umgebung erstellt 

z.B. `conda create -n Test python=3.8.1` 

und mittels
`conda activate umgebungs_name` besucht werden.

--- 

### 2. Installation aller Requirements

Als nächstes müssen die zur Ausführung des Programms notwendigen Module installiert werden.
=======

````cmd
conda create -n umgebungs_name python=<version von python --version>
````

eine neue Umgebung erstellt und mittels
>>>>>>> 26b9397aee53b237c87e7d2165c3881b4bc62ad6

```` cmd
conda activate umgebungs_name
````

 besucht werden.

Als nächstes müssen die zur Ausführung des Programms notwendigen Module installiert werden.

Hierzu reicht es aus, in der Kommandozeile folgenden Befehl auszuführen:

<<<<<<< HEAD
### 3. Starten des Programms

Zum Ausführen des Programms muss in der Kommandozeile (vom Grundordner, ansonsten Pfad zu Datei anpassen) der Befehl 

`python TypographyVisualizer/main.py` 

ausgeführt werden.

Dies startet den Flask Server, welcher dann unter `127.0.0.1:5000` über den Webbrowser erreichbar ist. Die IP wird nach Server-Start ebenso in der Kommandozeile ausgegeben und kann von dort kopiert werden, wenn nötig.

Zum Beenden der Anwendung muss lediglich in der Kommandozeile die Tastenkombination Strg+C unter Windows bzw. Command+C unter Mac gedrückt, oder das Kommandofenster geschlossen werden.

---

Dieses Projekt wurde im Rahmen des Moduls Kommunikations-Design im Sommersemester 2020 erstellt.

### Projektteilnehmer
=======
![dependencies_mittels_requirements.txt][dependencies]
>>>>>>> 26b9397aee53b237c87e7d2165c3881b4bc62ad6

* Angela Lisse
* Jasmin Esser
* Leon Krüger
* Niklas Tluk

[python download]: https://www.python.org/downloads/
[anaconda download]: https://www.anaconda.com/products/individual
[python install]: TypographyVisualiser/ressources/python%20install%20verification.jpg
[dependencies]: TypographyVisualiser/ressources/dependencies%20installation.JPG

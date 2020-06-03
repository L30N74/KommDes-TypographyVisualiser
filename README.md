# KommDes-TypographyVisualiser

---

## Requirements

Zu allererst, muss sicher gegangen werden, dass Python auf dem Gerät installiert ist.
Hierzu kann eine Kommandozeile/Terminal mittels `Win/Command + R` geöffnet und der Befehl

````` cmd
python --version
`````

ausgeführt werden.

Liefert dieser Befehl folgendes Ergebnis (oder neuer), ist python installiert.
Bei einer älteren Version sollte python auf den neusten Stand gebracht werden.

![image-20200511155420353](TypographyVisualiser/ressources/python%20install%20verification.jpg)

Wenn nicht, muss python vorerst über die [offizielle Python Webseite][1] heruntergeladen und installiert werden.

---

Es wird empfohlen, python module in einer virtuellen Umgebung zu installieren.
Das Programm [Anaconda][3] vereinfacht dieses Vorgehen.

Ist Anaconda installiert, kann mit dem Kommandozeilen-Befehl 
`conda create -n umgebungs_name python=<version von python --version>` eine neue Umgebung erstellt und mittels
`conda activate umgebungs_name` besucht werden.

Als nächstes müssen die zur Ausführung des Programms notwendigen Module installiert werden.

Hierzu reicht es aus, in der Kommandozeile `pip install -r requirements.txt` im Projektverzeichnis 
'KommDes - TypographyVisualiser/TypgoraphyVisualiser' 
auszuführen.




[1]: https://www.python.org/downloads/
[3]: https://www.anaconda.com/products/individual

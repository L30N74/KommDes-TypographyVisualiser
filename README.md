# KommDes-TypographyVisualiser

---

## Requirements

Zu aller erst, muss sicher gegangen werden, dass Python auf dem Gerät installiert ist.
Hierzu kann eine Kommandozeile/Terminal mittels `Win/Command + R` geöffnet und der Befehl

````` cmd
python --version
`````

ausgeführt werden.

![image 20200511155420353][python install]

Wenn nicht, muss Python vorerst über die [offizielle Python Webseite][python download] heruntergeladen und installiert werden.

---

Es wird empfohlen, Python-Module in einer virtuellen Umgebung zu installieren.
Das Programm [Anaconda][anaconda download] vereinfacht dieses Vorgehen.

Ist Anaconda installiert, kann mit dem Kommandozeilen-Befehl 

````cmd
conda create -n umgebungs_name python=<version von python --version>
````

eine neue Umgebung erstellt und mittels

```` cmd
conda activate umgebungs_name
````

 besucht werden.

Als nächstes müssen die zur Ausführung des Programms notwendigen Module installiert werden.

Hierzu reicht es aus, in der Kommandozeile folgenden Befehl auszuführen:

![dependencies_mittels_requirements.txt][dependencies]


[python download]: https://www.python.org/downloads/
[anaconda download]: https://www.anaconda.com/products/individual
[python install]: TypographyVisualiser/ressources/python%20install%20verification.jpg
[dependencies]: TypographyVisualiser/ressources/dependencies%20installation.jpg

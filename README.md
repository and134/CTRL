# CTRL – Raspberry Pi Line Following Car with Web and Auto Modes

CTRL este o mașinuță autonomă construită pe baza unei platforme cu Raspberry Pi 3B care poate fi controlată manual printr-o interfață web sau poate rula automat urmărind o linie neagră pe un traseu dedicat. Proiectul integrează servo pentru direcție, senzori IR, control cu motor driver și control Wi-Fi din browser.

## Obiectiv

Scopul proiectului este dezvoltarea unei mașinuțe cu două moduri de operare:
- **Manual** – control în timp real printr-o aplicație web.
- **Automat** – urmărirea unei linii folosind senzori IR și corecții fine (fine trimming) pentru direcție.

---

## Componente necesare

| Componentă                  | Cantitate |
|----------------------------|-----------|
| Raspberry Pi 3B            | 1         |
| Servomotor MG995           | 1         |
| Modul driver motor L298N   | 1         |
| Motoare DC + roți          | 2         |
| Senzori IR (3 pini)        | 3         |
| Breadboard (sau PCB custom)| 2         |
| Fire M-F / M-M             | Multe     |
| Baterie externă 5V/12V     | 1         |
| Cutie baterii 6V           | 1         |
| Conectori + șuruburi       | după caz  |

---

## Unelte și software

- Raspberry Pi OS Lite (fără GUI)
- Python 3 + Flask
- Visual Studio Code + SSH
- Flask

---

## Schema electrică

> Vezi fișierul `CTRL_Scheme` pentru schema completă:  [CTRL_Scheme.pdf](https://github.com/user-attachments/files/20432788/CTRL_Scheme.pdf)

Diagrama logică include:

- Conexiune între Raspberry Pi și:
  - L298N (pentru motoare DC)
  - Servomotor (GPIO cu PWM)
  - Senzori IR (left, center, right)

**GND trebuie să fie comun** pentru toate componentele: servo, motoare și Raspberry Pi!

---

##  Instalare & configurare

###  **1. Setup Raspberry Pi**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install flask RPi.GPIO
```

### **2. Run script**
```bash
python3 web_control.py
```
### **3. Acces web server**
```bash
http://<raspberry_pi_ip>:5000 
```


---
## Poveste

Acest prototip a fost gândit și construit de studenți ai Facultății de Automatică și Calculatoare din Iași.

Caroseria este în totalitate printată 3D, gândită modular pentru a permite acces facil la componente și modificări ulterioare. Proiectarea a fost realizată în Fusion 360, iar piesele au fost printate folosind PETG pentru rezistență sporită.

Mașina are două moduri de funcționare:
- **Mod Manual** – Controlată direct dintr-o interfață web responsive creată cu Flask.
- **Mod Autonom** – Urmărește o linie neagră folosind 3 senzori IR, iar corecția direcției se face printr-un servomotor conectat la un sistem de direcție de tip Ackerman.

Un element interesant este integrarea unei interfețe web care permite comutarea între modurile de funcționare în timp real. 

Partea de electronica a fost documentată complet în KiCad, cu o schemă electrică clară, pentru a putea fi ușor reprodus de alți pasionați.

Prototipul a fost testat pe un traseu real cu linii tăiate și curbe de tip sens giratoriu. Logica software este capabilă să detecteze aceste marcaje și să reacționeze în mod inteligent pentru a reveni pe linie sau a efectua viraje corecte.


---

## Next Steps

Urmatorul pas in continuarea acestui proiect este sa se adauge un senzor inflarosu montat pe un servo pentru a se putea implementa Collision Detection.

---

## Must Change For Future Projects

Schimbat cutia de baterii de 6V cu un acumulator si un modul step-down



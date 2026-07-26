import os
import random
import time
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from Bio.PDB import PDBList, PDBParser

def descarca_si_parseaza_receptor_d2():
    print("=" * 75)
    print("   [KERNEL MASTER v11.0]: THE QUANTUM MEOW MACHINE - ALEXIA (17 ANI)")
    print("=" * 75)
    if not os.path.exists('6cm4.pdb'):
        pdbl = PDBList()
        print("[+] Conectare la Protein Data Bank... Se descarca structura 6CM4.")
        pdbl.retrieve_pdb_file('6cm4', file_format='pdb', pdir='.')
        if os.path.exists('pdb6cm4.ent'):
            os.rename('pdb6cm4.ent', '6cm4.pdb')
    else:
        print("[+] PROTECTIE: Structura 6CM4.pdb exista local pe Desktop. Incarcare directa.")
        
    parser = PDBParser(QUIET=True)
    structura = parser.get_structure('D2_Receptor', '6cm4.pdb')
    atomi_reali = []
    for model in structura:
        for lant in model:
            for reziduu in lant:
                for atom in reziduu:
                    if atom.element in ['C', 'N', 'O']:
                        atomi_reali.append(atom)
    print(f"[+] Structura mapata. S-au izolat {len(atomi_reali)} atomi din receptor.")
    return atomi_reali

def genereaza_numere_prime(n):
    prime = []
    candidat = 2
    while len(prime) < n:
        for p in prime:
            if candidat % p == 0:
                break
        else:
            prime.append(candidat)
        candidat += 1
    return prime

# FUNCTIA DE HACKER: Generam un MIAU cuantic din ecuatii de unde matematice!
def miauna_cuantic():
    sample_rate = 22050
    durata = 0.4
    t = np.linspace(0, durata, int(sample_rate * durata), endpoint=False)
    
    # Efectul de miau: frecventa aluneca rapid in sus de la 600Hz la 900Hz
    frecventa_glisanta = 600 + (300 * (t / durata)**2)
    unda = np.sin(2 * np.pi * frecventa_glisanta * t)
    
    # Adaugam o unda armonica secundara ca sa sune mai organic si mai pisicesc
    unda_secundara = 0.4 * np.sin(2 * np.pi * (frecventa_glisanta * 1.5) * t)
    semnal_final = unda + unda_secundara
    
    # Amplitudine lina (fade out la final ca sa fie un miau dragut)
    anvelopa = np.exp(-4 * t)
    sunet_functional = semnal_final * anvelopa
    
    # Normalizare si rulare directa in placa de sunet
    sunet_functional /= np.max(np.abs(sunet_functional))
    sd.play(sunet_functional, sample_rate)
    sd.wait()

def porneste_analiza_vizuala_totala_v11():
    atomi = descarca_si_parseaza_receptor_d2()
    numere_prime = genereaza_numere_prime(100)
    
    plt.ion() 
    fig = plt.figure(figsize=(13, 6))
    fig.canvas.manager.set_window_title('Laborator Bio-Cuantic Master - Teoria Alexia')
    
    ax1 = fig.add_subplot(121, projection='3d')
    # CORECTIE CORE: Extragem corect indicii x, y, z separati din vectorul atom.coord
    X = [float(atom.coord[0]) for atom in atomi[:400]]
    Y = [float(atom.coord[1]) for atom in atomi[:400]]
    Z = [float(atom.coord[2]) for atom in atomi[:400]]
    
    ax2 = fig.add_subplot(122)
    istoric_cicluri = []
    istoric_godel = []
    
    aeon_id = 1
    ciclu_total = 0
    gena_cuantica_reziduala = 0.0
    
    while True: 
        print(f"\n[INCEPTION]: PORNESTE AEONUL MOLECULAR #{aeon_id}")
        ciclu_local = 0
        
        while True:
            ciclu_total += 1
            ciclu_local += 1
            
            esantion = random.sample(atomi, 10)
            numar_godel = 1
            for idx, atom in enumerate(esantion):
                # CORECTIE: Calculam distanta combinand componentele vectorului de coordonate
                coordonate_brute = int(abs(float(atom.coord[0]) + float(atom.coord[1]) + float(atom.coord[2]) + gena_cuantica_reziduala))
                numar_godel *= (numere_prime[idx] ** (coordonate_brute % 5 + 1))
            
            try: valoare_log = float(len(str(int(numar_godel))))
            except: valoare_log = 40.0
                
            istoric_cicluri.append(ciclu_total)
            istoric_godel.append(valoare_log)
            
            progres_overflow = min(valoare_log / 40.0, 1.0)
            dimensiune_dinamica = 30 + int(progres_overflow * 130)
            culoare_dinamica = (progres_overflow, 0.7 * (1.0 - progres_overflow), 1.0 - progres_overflow)
            
            ax1.clear()
            ax1.set_title(f'Fanta Sinaptica 3D | [Aeon {aeon_id}] | Gena: {gena_cuantica_reziduala:.2f}', fontsize=10, color='blue')
            ax1.scatter(X, Y, Z, c=Z, cmap='cool', alpha=0.12, s=2)
            
            # CORECTIE: Extragere corecta vectori pentru esantionul curent
            X_e = [float(a.coord[0]) for a in esantion]
            Y_e = [float(a.coord[1]) for a in esantion]
            Z_e = [float(a.coord[2]) for a in esantion]
            ax1.scatter(X_e, Y_e, Z_e, color=culoare_dinamica, s=dimensiune_dinamica, edgecolors='black')
            
            ax2.clear()
            ax2.set_title(f'Explozia Informationala (Log Numar Godel)\nViteza Timpului: {1.0 + progres_overflow:.2f}x', fontsize=10, color='red')
            ax2.plot(istoric_cicluri[-45:], istoric_godel[-45:], color='crimson', linewidth=1.5, marker='o', markersize=3)
            ax2.axhline(y=40, color='black', linestyle='--', label='Limita Godel (Prag Overflow)')
            ax2.set_xlabel('Ciclu Cosmic Total')
            ax2.set_ylabel('Ordin de marime (10^x)')
            ax2.grid(True, alpha=0.3)
            
            fig.canvas.draw()
            fig.canvas.flush_events()
            
            print(f" -> [Aeon {aeon_id}] Pas #{ciclu_local} | Cod Godel: 10^{int(valoare_log)}")
            
            if valoare_log >= 40:
                print(f"[!] OVERFLOW GÖDEL ATINS! Pisica lui Schrödinger s-a trezit!")
                # CORECTIE: Calculam gena reziduala folosind prima componenta a ultimului atom extras
                gena_cuantica_reziduala = abs(float(esantion[0].coord[0]) * 0.1)
                print(f"[-->] RESET CONFORMAL LOCAL: Trecere la Aeon nou...")
                
                # REFACTORIZARE SUPREMĂ: Înlocuim bleep-ul administrativ cu MIAU-ul cuantic!
                miauna_cuantic()
                
                time.sleep(0.8)
                aeon_id += 1
                break
                
            time.sleep(0.12)

if __name__ == '__main__':
    porneste_analiza_vizuala_totala_v11()
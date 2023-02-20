from tkinter import *
import random

def mainFunction():

    nome = ['Rockinbi,''Dian', 'Bonsonaryo', 'Falledrick', 'Lulo', 'Valhein', 'Dol', 'Earl', 'Cedria', 'Azulei', 'Yun', 'Cybel', 'Ina', 'Foolly', 'Skili', 'Juddol', 'Janver', 'Viska', 'Hirschendy', 'Silka', 'Hellsturn', 'Essa', 'Mykonos', 'Fenton', 'Tyrena', 'Inqoul', 'Mankov', 'Derilia', 'Hexema', 'Wyton', 'Kaedum', 'Gouram', 'Libertia', 'Berasailles', 'Juxta', 'Taehr', 'Comtol', 'Gherak', 'Hest', 'Qony', 'Masamka', 'Twyll', 'Tenos', 'Axim', 'Westrynda', 'Saphros', 'Olkham', 'Handok', 'Kemetra', 'Yos', 'Wentingle', 'Anddrade', 'Molosh', 'Inkov', 'Phasasia', 'Ziedinghal', 'Bregul', 'Eishvack', 'Lora', 'Krenting', 'Symbole', 'Elignoir', 'Keligkrul', 'Qwey', 'Vindinglag', 'Kusakira', 'Weme', 'Fayd', 'Rushvita', 'Vulkor',' Amers', 'Ortos', 'Vanius', 'Chandellia', 'Lilikol', 'Catca', 'Cormus', 'Yuela', 'Ariban', 'Tryton', 'Fesscha', 'Opalul', 'Zakzos', 'Hortimer', 'Anklos', 'Dushasiez', 'Polop', 'Mektal', 'Orinphus', 'Denatra', 'Elkazzi', 'Dyne', 'Domos', 'Letryal', 'Manniv', 'Sylestia', 'Esnol', 'Fasafuros',' Ghanfer', 'Kahnite', 'Sweyda', 'Uylis', 'Retenia', 'Bassos', 'Arkensval', 'Impelos', 'Grandius', 'Fulcrux', 'Lassahein', 'Edsveda', 'Earakun', 'Fous', 'Maas', 'Basenphal', 'Jubidya', 'Divya', 'Kosunten', 'Ordayius', 'Dozzer', 'Gangher', 'Escha', 'Manchul', 'Kempos', 'Kulo', 'Urtench', 'Kesta', 'Helahona', 'Ryte', 'Falcia', 'Umannos', 'Urkensvall', 'Fedra', 'Bulkensar', 'Comia', 'Tyul', 'Lasendarl']
    nome_result = random.choice(nome)
    subnome = random.choice(nome)

    historias = [
    "Este personagem nasceu em uma pequena aldeia, onde cresceu trabalhando na fazenda da família. Certo dia, uma caravana de aventureiros passou pela aldeia e o personagem se  juntou a eles, desejando ver o mundo lá fora.",

    "Este personagem era um soldado em uma grande guerra, mas abandonou a causa quando percebeu que seus superiores estavam cometendo atrocidades. Agora, ele busca redenção em suas viagens, tentando ajudar as pessoas que encontrar pelo caminho.",

    "Este personagem é um ser de uma divindade pouco conhecida, que decidiu se aventurar pelo mundo para espalhar a palavra de sua fé. Ele acredita que sua devoção e seus poderes divinos podem fazer a diferença no mundo.",

    "Este personagem é um órfão que foi adotado por uma guilda de ladrões. Ele cresceu aprendendo as artes do roubo e da furtividade, mas agora deseja deixar essa vida para trás e se tornar um aventureiro respeitável.",
    
    "Este personagem é um ser que cresceu na montanha, trabalhando nas minas de sua família. Ele decidiu se aventurar pelo mundo para encontrar novas riquezas e aventuras, mas também para honrar a memória de seus ancestrais.",

    "Este personagem é um ser que nasceu na floresta, onde aprendeu a caçar e rastrear. Ele decidiu se aventurar pelo mundo para encontrar novos desafios e testar suas habilidades de arquearia.",

    "Este personagem é um ser que cresceu em uma comunidade agrícola pacífica, mas sempre sonhou em se aventurar pelo mundo. Ele decidiu deixar sua vida tranquila para trás e se tornar um aventureiro, ansioso por novas experiências e emoções.",

    "Este personagem é um grande inventor, obcecado por criar novas máquinas e dispositivos. Ele decidiu se aventurar pelo mundo para\n encontrar novas inspirações e testar suas criações em situações reais.",

    "Este personagem cresceu em uma tribo guerreira, onde aprendeu a lutar desde jovem. Ele decidiu se aventurar pelo mundo para testar sua força e habilidades de combate, mas também para descobrir seu lugar na sociedade."
    
    ]

    historia_result = random.choice(historias)


    raça = ['Anão da montanha','Anão da Colina','Elfo da Floresta','Alto elfo','Elfo negro','Halfling','Humano','Draconato','Gnomo','Meio-elfo','meio-orc','Tiefling','Gnomo da Floresta','Halfling Robusto','Gnomo das rochas','Drow','Halfling pés-leves']
    raça_result = random.choice(raça)

    classe = ['Paladino','Monge','Mago','Ladino','Guerreiro','Guardião','Feiticeiro','Druida','Clérigo','Bruxo','Bardo','Bárbaro']
    classe_result = random.choice(classe)

    tendencias = ['Leal Bom','Neutro Bom','Caótico Bom','Leal Neutro','Neutro','Caótico Neutro','Leal Mau','Neutro Mau','Caótico Mau',]
    tendencias_result = random.choice(tendencias)

    #Atributos
    força = random.randint(1,18)
    destreza = random.randint(1,18)
    constituição = random.randint(1,18)
    inteligencia = random.randint(1,18)
    sabedoria = random.randint(1,18)
    carisma = random.randint(1,18)

    idiomas = ['Anão','Élfico','Gigante','Gnômico','Goblin','Halfling','Orc']
    idiomas_result = random.choice(idiomas)


    Info = f"""
    Nome:{nome_result} {subnome}
    História:{historia_result}
    Raça:{raça_result}
    Classe:{classe_result}
    Tendencia:{tendencias_result}
    Atributos:
    Força:{força} | Destreza:{destreza} | Constituição:{constituição}
    Inteligencia:{inteligencia} | Sabedoria:{sabedoria} | Carisma:{carisma} 

    Deslocamento: Padrão (Varia de acordo com o personagem)

    Idiomas: Comum {idiomas_result}
    
    
    """
    #raça_resultado = raça_select
    infoLabel ['text'] = Info
    generateButton ['text'] = 'Gerar novamente'


#GUI
App = Tk()
App.title('RPG Generator')

Title = Label(App, text='Generate a random D&D character', font='Arial 15 bold')
Title.grid(column=0,row=0)

infoLabel = Label(App, text='')
infoLabel.grid(column=0,row=1)

generateButton = Button(App,command=mainFunction,text='Gerar Personagem')
generateButton.grid(column=0,row=2, pady=2)

App.mainloop()

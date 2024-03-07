from PyQt5.QtCore import Qt#prizivam stvari koje su mi potrebne
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QRadioButton,QPushButton,QGroupBox,QButtonGroup

from random import shuffle,randint

class Question():
    def __init__(self,question1,right_answer1,wrong1,wrong2,wrong3):
        self.question = question1
        self.right_answer = right_answer1
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []

question_list.append(Question("Kome pripada Korzika?","Francuskoj","Italiji","Španiji","Alžiru"))
question_list.append(Question("Ko je pobjedio u Svjetskom prvenstvu 2014?","Njemacka","Italija","Argentina","Brazil"))
question_list.append(Question("Koji je najveci kontinent na Zemlji?","Azija","Sjeverna Amerika","Evropa","Afrika"))
question_list.append(Question("Kome pripada Grenland?","Danskoj","SAD","Norveškoj","Kanadi"))
question_list.append(Question("Kada su saveznici u 2.sv,ratu pokrenuli operaciju D-Day?","1944","1945","1943","1946"))
question_list.append(Question("Koji je glavni grad Turske?","Ankara","Istanbul","Izmir","Bursa"))
question_list.append(Question("Ko je osvoio Svjetsko prvenstvo 2010?","Španija","Njemačka","Brazil","Argentina"))
question_list.append(Question("Koji se kalendar danas najviše koristi?","gregorijanski","julijanski","arapski","muslimanski"))
question_list.append(Question("Kome pripada kaljiljingradska oblast?","Rusiji","Bjelorusiji","Poljskoj","Litvaniji"))
question_list.append(Question("Koji je glavni grad Italije?","Rim","Napulj","Firenca","Venecja"))


app = QApplication([])#pravimo aplikaciju
my_win = QWidget()#pravim prozor
my_win.setWindowTitle("Memory card")#naslov prozora

lbQuestion = QLabel("Whic nationality does not exist?")#pravim pitanje na prozoru
answer_btn = QPushButton("Answer")#pravim dugme "Answer"
RadioGroupBox = QGroupBox("Answer options")#pravim grupu i dajem joj naslov

rbtn1 = QRadioButton("Enets")#pravim dugmice 
rbtn2 = QRadioButton("Smurfs")#pravim dugmice 
rbtn3 = QRadioButton("Chulyms")#pravim dugmice 
rbtn4 = QRadioButton("Aleuts")#pravim dugmice 

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)



vertikala1 = QVBoxLayout()#pravim vertikalnu liniju
vertikala2 = QVBoxLayout()#pravim vertikalnu liniju
horizontala = QHBoxLayout()#pravim horizontalnu liniju

vertikala1.addWidget(rbtn1)#na vertikalnu liniju dodajmo dugmiće
vertikala1.addWidget(rbtn2)#na vertikalnu liniju dodajmo dugmiće
vertikala2.addWidget(rbtn3)#na vertikalnu liniju dodajmo dugmiće
vertikala2.addWidget(rbtn4)#na vertikalnu liniju dodajmo dugmiće

horizontala.addLayout(vertikala1)#dodajem vertikalne linije na horizontalnu liniju
horizontala.addLayout(vertikala2)#dodajem vertikalne linije na horizontalnu liniju

RadioGroupBox.setLayout(horizontala)#postavio sam dugmiće unutar "Boxa"

AnsGroupBox = QGroupBox("Test result")
lb_Results = QLabel("Are you correct")
lb_Correct = QLabel("The answer will be here!")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Results, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter , stretch = 2)

AnsGroupBox.setLayout(layout_res)




hor1 = QHBoxLayout()#pravim horizontalnu liniju
hor2 = QHBoxLayout()#pravim horizontalnu liniju
hor3 = QHBoxLayout()#pravim horizontalnu liniju
ver1 = QVBoxLayout()#pravim vertikalnu liniju

hor1.addWidget(lbQuestion,alignment = (Qt.AlignHCenter | Qt.AlignVCenter))#dodajem pitanje na horizontalnu
hor2.addWidget(RadioGroupBox)#dodajem "Box" na horizontalnu
hor2.addWidget(AnsGroupBox)
hor3.addStretch(1)#razvlacenje linije
AnsGroupBox.hide()
hor3.addWidget(answer_btn,stretch = 2)#dodajem dugme "answer" na 3 horizontalnu liniju
hor3.addStretch(1)#razvlacenje linije

ver1.addLayout(hor1,stretch = 2)#dodajem horizontalnu liniju na vertikalnu liniju
ver1.addLayout(hor2,stretch = 8)#dodajem horizontalnu liniju na vertikalnu liniju
ver1.addStretch(1)#razvlačim liniju
ver1.addLayout(hor3,stretch = 1)#dodajem horizontalnu liniju na vertikalnu liniju
ver1.addStretch(1)#razvlačim liniju
ver1.setSpacing(5)#pravim razmak 5 pixela između dugmića

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer_btn.setText("Next Question")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer_btn.setText("Answer")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn1,rbtn2,rbtn3,rbtn4]


def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbQuestion.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Results.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Correct")
        my_win.score += 1
        print("Statistics\n-Total questions: ",my_win.total, "\n-Right answer: ",my_win.score)
        print("Rating: ", (my_win.score/my_win.total*100),"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect")
            print("Rating: ", (my_win.score/my_win.total*100),"%")




def next_question():
    my_win.total += 1
    print("Statistics\n-Total questions: ",my_win.total, "\n-Right answer: ",my_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def Click_OK():
    if answer_btn.text() == "Answer":
        check_answer()
    else:
        next_question()


my_win.setLayout(ver1)#prikazujemo sve




answer_btn.clicked.connect(Click_OK)

my_win.total = 0
my_win.score = 0
next_question()


my_win.show()
app.exec()

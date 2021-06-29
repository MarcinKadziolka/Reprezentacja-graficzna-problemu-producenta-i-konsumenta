######################## IMPORTS ########################

from __future__ import annotations
from abc import ABC, abstractmethod
import pygame
import sys     # let  python use your file system
import os      # help python identify your OS
from math import floor
import random
from threading import Thread, Condition
import time
import random

"""
 start()

    Start the thread’s activity.

    It must be called at most once per thread object.
    It arranges for the object’s run() method to be invoked in a separate thread of control.


 run()

    Method representing the thread’s activity.

    You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with positional and keyword arguments taken from the args and kwargs arguments, respectively.

 acquire(blocking=True, timeout=-1)

    Acquire a lock, blocking or non-blocking.

    When invoked with the blocking argument set to True (the default), block until the lock is unlocked, then set it to locked and return True.


 release()

    Release a lock. This can be called from any thread, not only the thread which has acquired the lock.

    When the lock is locked, reset it to unlocked, and return.
    If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.


 class threading.Condition(lock=None)

    This class implements condition variable objects. A condition variable allows one or more threads to wait until they are notified by another thread.


 wait(timeout=None)

    Wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.

    This method releases the underlying lock,
    and then blocks until it is awakened by a notify() or notify_all() call for the same condition variable in another thread,
    or until the optional timeout occurs.
    Once awakened or timed out, it re-acquires the lock and returns.

 notify(n=1)

    By default, wake up one thread waiting on this condition, if any. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.

    This method wakes up at most n of the threads waiting for the condition variable; it is a no-op if no threads are waiting.


"""


######################## VARIABLES ########################

worldx = 960
worldy = 720

fps   = 45  # frame rate
ani   = 4

###### COLORS ######
blue = pygame.Color("#6CBEED")
dark_blue = (3, 0, 173)
black = (23, 23, 23)
white = (255, 255, 255)

dark_red = (130, 0, 0)
light_red = (255, 0, 0)
gray = pygame.Color("#3a3a3a")

dark_green = (32, 122, 23)
light_green = (3, 252, 40)


###### ICONS ######
x_icon = pygame.image.load(r'C:\Users\user\Desktop\Semestr VI\Systemy czasu rzeczywistego\project\images\x_icon.png')
play_icon = pygame.image.load(r'C:\Users\user\Desktop\Semestr VI\Systemy czasu rzeczywistego\project\images\play_icon.png')
pause_icon = pygame.image.load(r'C:\Users\user\Desktop\Semestr VI\Systemy czasu rzeczywistego\project\images\pause_icon.png')
background_icon = pygame.image.load(r'C:\Users\user\Desktop\Semestr VI\Systemy czasu rzeczywistego\project\images\background_icon.png')

x_icon_rect = x_icon.get_rect()
play_icon_rect = play_icon.get_rect()
pause_icon_rect = pause_icon.get_rect()
background_icon_rect = background_icon.get_rect()

x_icon_rect.center = (900, 50)
play_icon_rect.center = (worldx/2 - 50, 100)
background_icon_rect.center = (worldx/2 + 50, 100)

##################

buffer = []
MAX_NUM = 4

# Utworzenie obiketu condition,
# który będzie zarządzał funkcjami synchornizacyjnymi
condition = Condition()


# Prędkość poruszania się obiektów
delay = 0.01











######################## CLASSES ########################

# Klasa producenta, która posłuży do reprezentacji graficznej
# Posiada funkcje, przemieszcającej producenta w odpowiedni sposób,
# zależnie od akcji wykonywanej przez kod

class Producer():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []

        self.target_positionx = worldx/2
        self.starting_positionx = worldx/2+260
        self.starting_positiony = 180

        self.rect = pygame.Rect(0, 0, 90, 90)

        self.rect.center = (self.starting_positionx, self.starting_positiony)

        self.movex = 10
        self.movey = 10

        self.number = ""

    # Wraca producenta do strefy bufora
    # następnie przesuwa go na przycisk notify
    # symbolizując użycie funkcji notify()
    def notify(self):
        while(self.rect.centerx < self.target_positionx + 100):
            self.rect.x += self.movex
            time.sleep(delay)

        while(self.rect.centery > notify_1.centery):
            self.rect.y -= self.movey
            time.sleep(delay)
        time.sleep(0.2)

    # Przesuwa producenta na przycisk wait
    # symbolizując wstrzymanie procesu
    def wait(self):
        while(self.rect.centery < worldy-60):
            self.rect.y += self.movey
            time.sleep(delay)
        time.sleep(0.2)


    # Przemieszcza producenta do bufora
    # symbolizując użycie zamka 
    def acquire(self):
        while(self.rect.centerx > self.target_positionx + 100):
            self.rect.x -= self.movex
            time.sleep(delay)
        time.sleep(0.1)

    # Umieszcza producenta na wysokości pierwszej pustej komórki
    # przygotowując go do dodania elementu
    def count_buffor(self):
        if len(buffer) == 0:
            if (self.rect.centery < elementy_bufora[0][0].centery):
                while(self.rect.centery < elementy_bufora[0][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if (self.rect.centery > elementy_bufora[0][0].centery):
                while(self.rect.centery > elementy_bufora[0][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
        
        if len(buffer) == 1:
            if (self.rect.centery < elementy_bufora[1][0].centery):
                while(self.rect.centery < elementy_bufora[1][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if (self.rect.centery > elementy_bufora[1][0].centery):
                while(self.rect.centery > elementy_bufora[1][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
                    
        if len(buffer) == 2:
            if (self.rect.centery < elementy_bufora[2][0].centery):
                while(self.rect.centery < elementy_bufora[2][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if (self.rect.centery > elementy_bufora[2][0].centery):
                while(self.rect.centery > elementy_bufora[2][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
        if len(buffer) == 3:
            if (self.rect.centery < elementy_bufora[3][0].centery):
                while(self.rect.centery < elementy_bufora[3][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if (self.rect.centery > elementy_bufora[3][0].centery):
                while(self.rect.centery > elementy_bufora[3][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)

        if len(buffer) == 4:
            if (self.rect.centery < elementy_bufora[3][0].centery):
                while(self.rect.centery < elementy_bufora[3][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)

    # Symbolizuje dodanie elementu
    # poprzez przesunięcie producenta na miejsce w buforze
    # Oddaje liczbę na to miejsce, samemu zerując swoją
    def append(self):
        time.sleep(0.2)
        while(self.rect.centerx > self.target_positionx):
            self.rect.x -= self.movex
            time.sleep(delay)
        time.sleep(0.1)
        self.number = ""


    # Wychodzi ze strefu buforowej i udaje się na pozycję startową
    def release(self):
        while(self.rect.centerx < self.starting_positionx):
            self.rect.x += self.movex
            time.sleep(delay)

        while(self.rect.centerx > self.starting_positionx):
            self.rect.x -= self.movex
            time.sleep(delay)

        while(self.rect.centery < self.starting_positiony):
            self.rect.y += self.movey
            time.sleep(delay)

    # Wyświetla obiekt na ekranie, w odpowiednim kolorze
    def draw(self):
        pygame.draw.rect(world, dark_blue, self.rect)

# Klasa konsumenta, która posłuży do reprezentacji graficznej
# Posiada funkcje, przemieszcającej konsumenta w odpowiedni sposób,
# zależnie od akcji wykonywanej przez kod

class Consumer():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []

        self.target_positionx = worldx/2
        self.starting_positionx = worldx/2-260
        self.starting_positiony = 180

        self.rect = pygame.Rect(0, 0, 90, 90)

        self.rect.center = (self.starting_positionx, self.starting_positiony)

        self.movex = 10
        self.movey = 10

        self.number = ""

    # Wraca konsumenta do strefy bufora
    # następnie przesuwa go na przycisk notify
    # symbolizując użycie funkcji notify()
    def notify(self):
        while(self.rect.centerx > self.target_positionx - 100):
            self.rect.x -= self.movex
            time.sleep(delay)

        while(self.rect.centery > notify.centery):
            self.rect.y -= self.movey
            time.sleep(delay)
        time.sleep(0.2)

    # Przesuwa konsumenta na przycisk wait
    # symbolizując wstrzymanie procesu
    def wait(self):
        while(self.rect.centery < worldy-60):
            self.rect.y += self.movey
            time.sleep(delay)
        time.sleep(0.2)

    # Przemieszcza konsumenta do bufora
    # symbolizując użycie zamka 
    def acquire(self):
        while(self.rect.centerx < self.target_positionx - 100):
            self.rect.x += self.movex
            time.sleep(delay)
        time.sleep(0.2)

    # Umieszcza konsumenta na wysokości ostatniej pełnej komórki
    # przygotowując go do pobrania elementu
    def count_buffor(self):
        if len(buffer) == 1:
            if(self.rect.centery < elementy_bufora[0][0].centery):
                while(self.rect.centery < elementy_bufora[0][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if(self.rect.centery > elementy_bufora[0][0].centery):
                while(self.rect.centery > elementy_bufora[0][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
        if len(buffer) == 2:
            if(self.rect.centery < elementy_bufora[1][0].centery):
                while(self.rect.centery < elementy_bufora[1][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if(self.rect.centery > elementy_bufora[1][0].centery):
                while(self.rect.centery > elementy_bufora[1][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
        if len(buffer) == 3:
            if(self.rect.centery < elementy_bufora[2][0].centery):
                while(self.rect.centery < elementy_bufora[2][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if(self.rect.centery > elementy_bufora[2][0].centery):
                while(self.rect.centery > elementy_bufora[2][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)
        if len(buffer) == 4:
            if(self.rect.centery < elementy_bufora[3][0].centery):
                while(self.rect.centery < elementy_bufora[3][0].centery):
                    self.rect.y += self.movey
                    time.sleep(delay)
            if(self.rect.centery > elementy_bufora[3][0].centery):
                while(self.rect.centery > elementy_bufora[3][0].centery):
                    self.rect.y -= self.movey
                    time.sleep(delay)

    # Najeżdża na miejsce w buforze 
    def pop(self):
        while(self.rect.centerx < self.target_positionx):
            self.rect.x += self.movex
            time.sleep(delay)
        time.sleep(0.1)

    # Opuszcza bufor, symbolizując użycie funkcji condition.relase()
    # Konsumuje liczbę, poprzez wyzerowanie jej
    def release(self):
        while(self.rect.centerx > self.starting_positionx):
            self.rect.x -= self.movex
            time.sleep(delay)

        while(self.rect.centerx < self.starting_positionx):
            self.rect.x += self.movex
            time.sleep(delay)
        
        consumer.number = ""

        while(self.rect.centery < self.starting_positiony):
            self.rect.y += self.movey
            time.sleep(delay)
    
    # Wyświetla obiekt na ekranie w odpowiednim kolorze
    def draw(self):
        pygame.draw.rect(world, pygame.Color(gray), self.rect)


# Utworzenie obiektów producenta i konsumenta
producer = Producer()
consumer = Consumer()



# Klasa wątku producenta
# Jest poprawnie zsynchronizowana za pomocą funkcji acquire(), release(), wait() i notify()
# Każda wcześniej wymieniona funkcja jest adekwatnie reprezentowana graficznie
# przez funkcje z klasy Producer
# Nazewnictwo tych funkcji odpowiada oryginałom
class ProducerThread(Thread):
    def run(self):
        global num
        nums = range(5)
        global buffer
        while True:

            producer.count_buffor()

            # Zablokowanie dostępu innym wątkom do sekcji
            condition.acquire()
            
            producer.acquire()
            
            
            # Sprawdzenie, czy bufor jest zapełniony
            if len(buffer) == MAX_NUM:
                print ("buffer full, producer is waiting")
                # Jeśli jest, wstrzymanie wątku aż do czasu otrzymania powiadomienia
                # od konsumenta o tym, że pobrał element i można dodać kolejny
                
                producer.wait()
                condition.wait()
                
                print ("Space in buffer, Consumer notified the producer")

            # Produkowanie losowej liczby i przypisanie jej do obiektu graficznego
            num = random.choice(nums)
            producer.number = str(num)

            # Przesunięcie producenta na odpowiednią wysokość
            producer.count_buffor()

            # Dodanie liczby do bufora
            buffer.append(num)
            producer.append()

            # Powiadomienie konsumenta o tym, że w buforze znajduje się
            # produkt

            producer.notify()
            condition.notify()

            producer.release()       
            condition.release()
            
            time.sleep(random.randrange(4))

            
# Klasa wątku konsumenta
# Jest poprawnie zsynchronizowana za pomocą funkcji acquire(), release(), wait() i notify()
# Każda wcześniej wymieniona funkcja jest adekwatnie reprezentowana graficznie
# przez funkcje z klasy Consumer
# Nazewnictwo tych funkcji odpowiada oryginałom
class ConsumerThread(Thread):
    def run(self):
        global buffer
        while True:

            consumer.count_buffor()

            # Zablokowanie dostępu innym wątkom do sekcji
            condition.acquire()
            consumer.acquire()

            
            # Sprawdzenie, czy bufor jest pusty
            if not buffer:
                print ("Nothing in buffer, consumer is waiting")
                # Jeśli jest, wstrzymanie wątku aż do czasu
                # otrzymania powiadomienia od producenta o tym,
                # że dodał element i można go pobrać

                consumer.wait()
                condition.wait()
                
                print ("Producer added something to buffer and notified the consumer")
                
            
            consumer.count_buffor()

            # Pobieranie elementu z bufora
            consumer.pop()
            num = buffer.pop(0)
            
            
            
            # Powiadomienie producenta o tym
            # że w buforze znajduje się miejsce

            consumer.notify()
            condition.notify()

            # Zwolnienie dostępu do sekcji
            consumer.release()
            condition.release()

            
            
            time.sleep(random.randrange(4))


######################## FUNCTIONS ########################


# Zwraca obiekt pygame.Rect, o współrzędnych środka x, y
def create_button(x, y, width, height):
   
    button = pygame.Rect(x, y, width, height)

    button.center = (x, y)
        
    return button

# Wyświetla przekazany obiekt pygame.Rect w danym kolorze
def draw_button(button, color):
    pygame.draw.rect(world, color, button)


# Tworzy listę obiektów pygame.Rect, wszystkie o współrzędnej x
# zaczynając od początkowej współrzędnej y
# Każdy kolejny obiekt jest tworzony o y_skok niżej
# Zwraca pionową listę obiektów
def create_buttons(x, starting_y, width, height, liczba_przyciskow, y_skok):
    y = starting_y
    buttons = []
    licznik_przyciskow = 0
    while(licznik_przyciskow < liczba_przyciskow):
        buttons.append([create_button(x, y, width, height), "", False])
        licznik_przyciskow += 1
        y += y_skok
    return buttons
        
# Wypisuje tekst na obiekcie pygame.Rect, w danym kolorze i czcionce
def draw_text_on_button(button, text, color, size):
    text_surface_obj = pygame.font.SysFont('Garamond',size).render(text, True, color, None)

    text_rect_obj = text_surface_obj.get_rect()

    text_rect_obj.center = button.center

    world.blit(text_surface_obj, text_rect_obj)


#play_button = create_button(worldx/2, 300, 140, 40)


# Wypisuje tekst bezpośrednio na ekranie,
# Środek tekstu będzie znajdował się na x, y
def draw_text_on_screen(text, x, y, size = 35, color = white):
    text_surface_obj = pygame.font.SysFont('Garamond',size).render(text, True, color, None)

    text_rect_obj = text_surface_obj.get_rect()

    text_rect_obj.center = x, y

    world.blit(text_surface_obj, text_rect_obj)

play_button = create_button(worldx/2, 300, 140, 40)




###################### SETUP #######################


clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
pygame.display.set_caption('Producent i konsument')


####### OBIEKTY RECT ########

bufor = create_button(worldx/2, worldy/2-60, 340, 590)

wait = create_button(worldx/2-100, worldy-60, 110, 110)
wait_1 = create_button(worldx/2+100, worldy-60, 110, 110)

notify = create_button(worldx/2-100, 70, 110, 110)
notify_1 = create_button(worldx/2+100, 70, 110, 110)

#create_buttons(x, starting_y, width, height, liczba_przyciskow, y_skok)
elementy_bufora = create_buttons(worldx/2, 180, 70, 70, 4, 120)

prect = create_button(producer.starting_positionx, producer.starting_positiony, 90, 90)
crect = create_button(consumer.starting_positionx, consumer.starting_positiony, 90, 90)

# Funkcja wyświetlająca statyczny obraz startowy, przed uruchomieniem wątków
def opis():
    main = True

    while main:
        # Wyświetlenie niebieskiego tła
        world.fill(blue)
        # Pobranie koordynatów pozycji myszki
        mouse = pygame.mouse.get_pos()
        
        click = False

        # Pętla rejestrująca zdarzenia wykonane przez użytkownika
        # takie jak wciśnięcie klawisza lub kliknięcie myszą
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Rejestruje kliknięcie lewego przycisku myszy
                    if event.button == 1:
                        click = True               


        # Wyświetla strefę reprezentującą użycie acquire()
        draw_button(bufor, white)

        # Wyświetla czerwone kwadraty, na które będą udawać się
        # producent oraz konsument po użyciu wait()
        draw_button(wait, dark_red)
        draw_button(wait_1, dark_red)

        # Wyświetla zielone kwadraty, na które będą udawać się
        # producent oraz konsument po użyciu notify()
        draw_button(notify, dark_green)
        draw_button(notify_1, dark_green)



	# Wyświetlanie odpowiednich napisów na kwadratach
        draw_text_on_button(notify, "Notify", white, 40)
        draw_text_on_button(notify_1, "Notify", white, 40)
        draw_text_on_button(wait, "Wait", white, 50)
        draw_text_on_button(wait_1, "Wait", white, 50)

        
          

        # Pętla iterująca po każdym elemencie bufora
        for element in elementy_bufora:
            # Rysowanie czarnego kwadraciku na ekran
            draw_button(element[0], black)

    
        # Wyświetlanie ikony x
        world.blit(x_icon, x_icon_rect)

        # Jeśli koordynaty myszy pokrywają się z koordynatami
        # ikony x oraz zarejestrowane zostało kliknięcie
        # następuje powrót do menu
        if (x_icon_rect.collidepoint(mouse) and click):
            main = False
            
        
        # Rysowanie kwadratów symbolizujących producenta i konsumenta
        draw_button(prect, dark_blue)
        draw_button(crect, gray)

        # Wyświetlanie odpowiednich literek, P - Producent, C - Consumer
        draw_text_on_button(prect, "P", white, 80)
        draw_text_on_button(crect, "C", white, 80)

        # Aktualizacja obrazu
        pygame.display.flip()
        clock.tick(fps)


def main_menu():
    main = True

    while main:
        # Wyświetlenie niebieskiego tła
        world.fill(blue)
        # Pobranie koordynatów pozycji myszki
        mouse = pygame.mouse.get_pos()
        
        click = False

        # Pętla rejestrująca zdarzenia wykonane przez użytkownika
        # takie jak wciśnięcie klawisza lub kliknięcie myszą
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Rejestruje kliknięcie lewego przycisku myszy
                    if event.button == 1:
                        click = True                  
            
        # Wyświetlenie ikon play oraz background
        world.blit(play_icon, play_icon_rect)
        world.blit(background_icon, background_icon_rect)

        # Jeśli koordynaty myszy pokrywają się z koordynatami
        # ikony play oraz zarejestrowane zostało kliknięcie
        # uruchamia się funkcja symulująca
        if (play_icon_rect.collidepoint(mouse) and click):
            synchronised()

        # Jeśli koordynaty myszy pokrywają się z koordynatami
        # ikony background oraz zarejestrowane zostało kliknięcie
        # uruchamia się funkcja podglądu
        if (background_icon_rect.collidepoint(mouse) and click):
            opis()
   
        # Odświeżenie obrazu i tick fps
        pygame.display.flip()
        clock.tick(fps)


global run
run = False

# Funkcja wyświetlająca przebieg symulacji problemu producenta i konsumenta
def synchronised():
    global run
    if (not run):
        ConsumerThread().start()
        ProducerThread().start()
        run = True
        
    main = True

    while main:
        # Wyświetlenie niebieskiego tłą
        world.fill(blue)
        # Pobranie koordynatów pozycji myszki
        mouse = pygame.mouse.get_pos()
        
        click = False

        # Pętla rejestrująca zdarzenia wykonane przez użytkownika
        # takie jak wciśnięcie klawisza lub kliknięcie myszą
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Rejestruje kliknięcie lewego przycisku myszy
                    if event.button == 1:
                        click = True           

        # Wyświetla strefę reprezentującą użycie acquire()
        draw_button(bufor, white)

        # Wyświetla czerwone kwadraty, na które będą udawać się
        # producent oraz konsument po użyciu wait()
        draw_button(wait, dark_red)
        draw_button(wait_1, dark_red)

        # Wyświetla zielone kwadraty, na które będą udawać się
        # producent oraz konsument po użyciu notify()
        draw_button(notify, dark_green)
        draw_button(notify_1, dark_green)

        # Jeśli producent lub konsument najadą na swoje przyciki wait
        # to się podświetlą 
        if(wait.collidepoint(consumer.rect.x, consumer.rect.y)):
            draw_button(wait, light_red)
        if(wait_1.collidepoint(producer.rect.x, producer.rect.y)):
            draw_button(wait_1, (255, 0, 0))
        

        
        # Jeśli producent lub konsument najadą na swoje przyciki wait
        # to się podświetlą
        # Dodatkowo, jeśli na przycisku wait czeka adekwatnie producent
        # lub konsument, to kwadrat wait też podświelti się na zielono
        # obrazując otrzymanie powiadomienia i zwolnienie blokady
        if(notify.collidepoint(consumer.rect.x, consumer.rect.y)):
            draw_button(notify, light_green)
            if(wait_1.collidepoint(producer.rect.x, producer.rect.y)):
                draw_button(wait_1, light_green)

        if(notify_1.collidepoint(producer.rect.x, producer.rect.y)):
            draw_button(notify_1, light_green)
            if(wait.collidepoint(consumer.rect.x, consumer.rect.y)):
                draw_button(wait, light_green)


        # Wyświetlanie odpowiednich napisów na kwadratach
        draw_text_on_button(notify, "Notify", white, 40)
        draw_text_on_button(notify_1, "Notify", white, 40)
        draw_text_on_button(wait, "Wait", white, 50)
        draw_text_on_button(wait_1, "Wait", white, 50)


        # Pętla iterująca po każdym elemencie bufora
        for element in elementy_bufora:
            # Rysowanie czarnego kwadraciku na ekran
            draw_button(element[0], black)

            # Jeśli producent najechał na element, następuje
            # przekazanie wartości producenta na miejsce w buforze
            # i ustawienie flagi wyświetlania liczby na True
            if element[0].center == producer.rect.center:
                element[1] = producer.number
                element[2] = True

            # Jeśli konsument najechał na element, następuje
            # odebranie wartości przez konsumenta
            # i ustawienie flagi wyświetlania liczby na False
            # tak, aby zasymulować przekazanie liczby
            if element[0].center == consumer.rect.center:
                consumer.number = element[1]
                element[2] = False

            # Jeśli flaga wyświetlania jest True
            # na miejscu w buforze będzie wyświetlana liczba
            if element[2]:
                draw_text_on_button(element[0], str(element[1]), white, 50)


        # Wyświetlanie ikony x
        world.blit(x_icon, x_icon_rect)

        # Jeśli koordynaty myszy pokrywają się z koordynatami
        # ikony x oraz zarejestrowane zostało kliknięcie
        # następuje powrót do menu
        if (x_icon_rect.collidepoint(mouse) and click):
            main = False



            
        # Wyświetlanie obiektów producenta i konsumenta
        producer.draw()
        consumer.draw()

        # Wyświetlanie odpowiednich napisów na obiektach producenta i konsumenta
        draw_text_on_button(producer.rect, "P" + str(producer.number), white, 80)
        draw_text_on_button(consumer.rect, "C" + str(consumer.number), white, 80)

        # Odświeżenie obrazu i tick fps
        pygame.display.flip()
        clock.tick(fps)


main_menu()


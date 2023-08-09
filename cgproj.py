import pygame
from math import pi, cos, sin
import datetime


# Setting differnt height and width of clock and radius of clock
WIDTH, HEIGHT = 1000,700
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 350

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()
FPS = 60

# setting colors as rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE1=(200,0,0)
LINE2=(169,169,169)
LINE3=(112,112,112)
AQUA=(127,255,212)


def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, BLACK)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)


def main():
    

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.today().isoweekday()
        calendar = current_time.today().isocalendar()

        weekdays_abbr = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thurday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        weekday_abbr = weekdays_abbr.get(weekday)

        months_abbr = {1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN", 7: "JUL",
                       8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC"}
        month_abbr = months_abbr.get(month)

        if day < 10:
            day = "0" + str(day)

        screen.fill(AQUA)
        
        pygame.draw.rect(screen, BLACK, [WIDTH / 2 - 450, HEIGHT / 2 - 300, 200, 60], 2)

        numbers('Designed by:',25,(WIDTH / 2 - 360, HEIGHT / 2 - 320))
        numbers('Pragyan Adhikari', 28, (WIDTH / 2 -353, HEIGHT / 2 - 280))


        pygame.draw.circle(screen, BLACK, center, clock_radius - 10, 10)
        pygame.draw.circle(screen,BLACK, center, 12)
        
        pygame.draw.rect(screen, BLACK, [WIDTH / 2 -250, HEIGHT / 2 - 30, 85, 60], 1)
        pygame.draw.rect(screen, BLACK, [WIDTH / 2 - 165, HEIGHT / 2 - 30, 80, 60], 1)
        pygame.draw.rect(screen, BLACK, [WIDTH / 2 +45, HEIGHT / 2 - 30, 200, 60], 1)
        pygame.draw.rect(screen, BLACK, [WIDTH / 2 - 50, HEIGHT / 2 - 30 - 160, 100, 60], 1)
       
       
        numbers('Month',25,(WIDTH / 2 - 210, HEIGHT / 2 - 44))
        numbers(str(month_abbr), 40, (WIDTH / 2 -210, HEIGHT / 2))
        
        numbers('Date',25,(WIDTH / 2 - 130, HEIGHT / 2 - 44))
        numbers(str(day), 40, (WIDTH / 2  - 130, HEIGHT / 2))

        numbers('Day',25,(WIDTH / 2 + 148, HEIGHT / 2 - 44))
        numbers(str(weekday_abbr), 40, (WIDTH / 2 +148, HEIGHT / 2))

        numbers('Year',25,(WIDTH / 2 , HEIGHT / 2 - 205))
        numbers(str(year), 40, (WIDTH / 2, HEIGHT / 2 - 160))

        # For printing number in clock
        for number in range(1, 13):
            numbers(str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))

         
        for number in range(0, 360, 6):
            # For showing minute  IN CLOCK
            if number % 5:
                pygame.draw.line(screen, BLACK, polar_to_cartesian(clock_radius - 15, number),
                                 polar_to_cartesian(clock_radius - 30, number), 2)
            # For showing 5 minute line(longer line) IN CLOCK
            else:
                pygame.draw.line(screen, BLACK, polar_to_cartesian(clock_radius - 15, number),
                                 polar_to_cartesian(clock_radius - 35, number), 6)
          

        # Hour Line
        r = 225
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, LINE3, center, polar_to_cartesian(r, theta),20)


        # Minute Line
        r = 265
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, LINE2, center, polar_to_cartesian(r, theta), 10)

        # Second Line
        r = 300
        theta = second * (360 / 60)
        pygame.draw.line(screen, LINE1, center, polar_to_cartesian(r, theta), 4)

        pygame.display.update()

        clock.tick(FPS)

    
    pygame.quit()


main()




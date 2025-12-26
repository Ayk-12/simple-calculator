import pygame
pygame.init()

infoObject = pygame.display.Info()
WIDTH, HEIGHT = 560, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
L_GRAY = (200, 200, 200)
D_GRAY = (100, 100, 100)

BUTTON_WIDTH = int((WIDTH - 60)/ 5) #100
BUTTON_HEIGHT = 100

ButtonsList = []
dummy = []

operation = ''
answer_dummy = 0
ans = 0
old_ans = 0
error_dummy = 0

ANSWER_AREA = pygame.Rect(10, 10, WIDTH - 20, 150) #X_POS, Y_POS, WIDTH, HEIGHT

ZERO_BUTTON = pygame.Rect(10, 150 + 6 * 10 + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

ONE_BUTTON = pygame.Rect(10, 150 + 5 * 10 + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
TWO_BUTTON = pygame.Rect(20 + BUTTON_WIDTH, 150 + 5 * 10 + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
THREE_BUTTON = pygame.Rect(30 + 2 * BUTTON_WIDTH, 150 + 5 * 10 + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

FOUR_BUTTON = pygame.Rect(10, 150 + 4 * 10 + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
FIVE_BUTTON = pygame.Rect(20 + BUTTON_WIDTH, 150 + 4 * 10 + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
SIX_BUTTON = pygame.Rect(30 + 2 * BUTTON_WIDTH, 150 + 4 * 10 + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

SEVEN_BUTTON = pygame.Rect(10, 150 + 3 * 10 + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
EIGHT_BUTTON = pygame.Rect(20 + BUTTON_WIDTH, 150 + 3 * 10 + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
NINE_BUTTON = pygame.Rect(30 + 2 * BUTTON_WIDTH, 150 + 3 * 10 + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

PLUS_BUTTON = pygame.Rect(40 + 3 * BUTTON_WIDTH, 150 + 5 * 10 + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
MINUS_BUTTON = pygame.Rect(50 + 4 * BUTTON_WIDTH, 150 + 5 * 10 + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
TIMES_BUTTON = pygame.Rect(40 + 3 * BUTTON_WIDTH, 150 + 4 * 10 + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
DIVIDE_BUTTON = pygame.Rect(50 + 4 * BUTTON_WIDTH, 150 + 4 * 10 + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
EQUALS_BUTTON = pygame.Rect(50 + 4 * BUTTON_WIDTH, 150 + 6 * 10 + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
POINT_BUTTON = pygame.Rect(20 + BUTTON_WIDTH, 150 + 6 * 10 + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)

DEL_BUTTON = pygame.Rect(40 + 3 * BUTTON_WIDTH, 150 + 3 * 10 + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT) #delete
AC_BUTTON = pygame.Rect(50 + 4 * BUTTON_WIDTH, 150 + 3 * 10 + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT) #all clear
TIMES_TEN_POWER_BUTTON = pygame.Rect(30 + 2 * BUTTON_WIDTH, 150 + 6 * 10 + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
ANS_BUTTON = pygame.Rect(40 + 3 * BUTTON_WIDTH, 150 + 6 * 10 + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
POWER_BUTTON = pygame.Rect(30 + 2 * BUTTON_WIDTH, 150 + 2 * 10, BUTTON_WIDTH, BUTTON_HEIGHT)

OPEN_PARANTHESES_BUTTON = pygame.Rect(10, 150 + 2 * 10, BUTTON_WIDTH, BUTTON_HEIGHT)
CLOSE_PARANTHESES_BUTTON = pygame.Rect(20 + BUTTON_WIDTH, 150 + 2 * 10, BUTTON_WIDTH, BUTTON_HEIGHT)

ButtonsList.append(ZERO_BUTTON)
ButtonsList.append(ONE_BUTTON)
ButtonsList.append(TWO_BUTTON)
ButtonsList.append(THREE_BUTTON)
ButtonsList.append(FOUR_BUTTON)
ButtonsList.append(FIVE_BUTTON)
ButtonsList.append(SIX_BUTTON)
ButtonsList.append(SEVEN_BUTTON)
ButtonsList.append(EIGHT_BUTTON)
ButtonsList.append(NINE_BUTTON)

ButtonsList.append(PLUS_BUTTON)
ButtonsList.append(MINUS_BUTTON)
ButtonsList.append(TIMES_BUTTON)
ButtonsList.append(DIVIDE_BUTTON)
ButtonsList.append(EQUALS_BUTTON)
ButtonsList.append(POINT_BUTTON)
ButtonsList.append(POWER_BUTTON)

ButtonsList.append(DEL_BUTTON)
ButtonsList.append(AC_BUTTON)
ButtonsList.append(TIMES_TEN_POWER_BUTTON)
ButtonsList.append(ANS_BUTTON)

ButtonsList.append(OPEN_PARANTHESES_BUTTON)
ButtonsList.append(CLOSE_PARANTHESES_BUTTON)


ANSWER_FONT = pygame.font.SysFont('ds digital', 80)

BUTTON_FONT = pygame.font.SysFont('falling sky', 80)
SMALL_BUTTON_FONT = pygame.font.SysFont('falling sky', 60)
BIG_BUTTON_FONT = pygame.font.SysFont('falling sky', 100)

TEXT_0 = BUTTON_FONT.render('0', True, BLACK)
TEXT_1 = BUTTON_FONT.render('1', True, BLACK)
TEXT_2 = BUTTON_FONT.render('2', True, BLACK)
TEXT_3 = BUTTON_FONT.render('3', True, BLACK)
TEXT_4 = BUTTON_FONT.render('4', True, BLACK)
TEXT_5 = BUTTON_FONT.render('5', True, BLACK)
TEXT_6 = BUTTON_FONT.render('6', True, BLACK)
TEXT_7 = BUTTON_FONT.render('7', True, BLACK)
TEXT_8 = BUTTON_FONT.render('8', True, BLACK)
TEXT_9 = BUTTON_FONT.render('9', True, BLACK)

TEXT_PLUS = BUTTON_FONT.render('+', True, BLACK)
TEXT_MINUS = BIG_BUTTON_FONT.render('-', True, BLACK)
TEXT_TIMES = BIG_BUTTON_FONT.render('*', True, BLACK)
TEXT_DIVIDE = BIG_BUTTON_FONT.render('/', True, BLACK)
TEXT_EQUALS = BIG_BUTTON_FONT.render('=', True, BLACK)
TEXT_POINT = BIG_BUTTON_FONT.render('.', True, BLACK)
TEXT_POWER = BIG_BUTTON_FONT.render('**', True, BLACK)

TEXT_DEL = SMALL_BUTTON_FONT.render('DEL', True, BLACK)
TEXT_AC = SMALL_BUTTON_FONT.render('AC', True, BLACK)
TEXT_TIMES_TEN_POWER = SMALL_BUTTON_FONT.render('*10^', True, BLACK)
TEXT_ANS = SMALL_BUTTON_FONT.render('ANS', True, BLACK)

TEXT_OPEN_PARANTHESES = BUTTON_FONT.render('(', True, BLACK)
TEXT_CLOSE_PARANTHESES = BUTTON_FONT.render(')', True, BLACK)

ERROR_MESSAGE = ANSWER_FONT.render('ERROR', True, BLACK)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse[0], mouse[1], 1, 1)
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    screen.fill(WHITE)

    pygame.draw.rect(screen, L_GRAY, ANSWER_AREA, border_radius = 3)

    OPERATION_TEXT = ANSWER_FONT.render(str(operation), True, BLACK)
    ANSWER_TEXT = ANSWER_FONT.render(str(ans), True, BLACK)

    for Button in ButtonsList:
        pygame.draw.rect(screen, GRAY, Button, border_radius = 5)
        
        if mouse_rect.colliderect(Button):
            pygame.draw.rect(screen, L_GRAY, Button, border_radius = 5)

            if mouse_rect.colliderect(ZERO_BUTTON) and len(dummy) == 1:
                operation += '0'
            if mouse_rect.colliderect(ONE_BUTTON) and len(dummy) == 1:
                operation += '1'
            if mouse_rect.colliderect(TWO_BUTTON) and len(dummy) == 1:
                operation += '2'
            if mouse_rect.colliderect(THREE_BUTTON) and len(dummy) == 1:
                operation += '3'
            if mouse_rect.colliderect(FOUR_BUTTON) and len(dummy) == 1:
                operation += '4'
            if mouse_rect.colliderect(FIVE_BUTTON) and len(dummy) == 1:
                operation += '5'
            if mouse_rect.colliderect(SIX_BUTTON) and len(dummy) == 1:
                operation += '6'
            if mouse_rect.colliderect(SEVEN_BUTTON) and len(dummy) == 1:
                operation += '7'
            if mouse_rect.colliderect(EIGHT_BUTTON) and len(dummy) == 1:
                operation += '8'
            if mouse_rect.colliderect(NINE_BUTTON) and len(dummy) == 1:
                operation += '9'

            if mouse_rect.colliderect(PLUS_BUTTON) and len(dummy) == 1:
                operation += '+'
            if mouse_rect.colliderect(MINUS_BUTTON) and len(dummy) == 1:
                operation += '-'
            if mouse_rect.colliderect(TIMES_BUTTON) and len(dummy) == 1:
                operation += '*'
            if mouse_rect.colliderect(DIVIDE_BUTTON) and len(dummy) == 1:
                operation += '/'
            if mouse_rect.colliderect(POINT_BUTTON) and len(dummy) == 1:
                operation += '.'
            if mouse_rect.colliderect(TIMES_TEN_POWER_BUTTON) and len(dummy) == 1:
                operation += '*10**'
            if mouse_rect.colliderect(POWER_BUTTON) and len(dummy) == 1:
                operation += '**'
            if mouse_rect.colliderect(OPEN_PARANTHESES_BUTTON) and len(dummy) == 1:
                operation += '('
            if mouse_rect.colliderect(CLOSE_PARANTHESES_BUTTON) and len(dummy) == 1:
                operation += ')'
            if mouse_rect.colliderect(ANS_BUTTON) and len(dummy) == 1:
                operation += str(old_ans)

            if mouse_rect.colliderect(DEL_BUTTON) and len(dummy) == 1:
                operation = operation[:-1]
            if mouse_rect.colliderect(AC_BUTTON) and len(dummy) == 1:
                operation = ''
                ans = 0
                error_dummy = 0

            if mouse_rect.colliderect(EQUALS_BUTTON) and len(dummy) == 1:
                try:
                    ans = str(round(eval(operation), 8))
                    old_ans = round(float(ans), 3)

                    if len(ans) >= 10 and ans.find('.') == -1:
                        if float(ans) > 0:
                            ans = f'{ans[0]}.{ans[1]}{ans[2]}E{int(len(ans) - 1)}'
                        if float(ans) < 0:
                            ans = f'-{ans[1]}.{ans[2]}{ans[3]}E{int(len(ans) - 2)}'

                except:
                    error_dummy = 1

        pygame.draw.rect(screen, D_GRAY, Button, border_radius = 5, width = 3)

    if left:
        dummy.append(1)
    if not left:
        dummy.clear()

    screen.blit(OPERATION_TEXT, (15, 10))

    screen.blit(TEXT_OPEN_PARANTHESES, (48, 190))
    screen.blit(TEXT_CLOSE_PARANTHESES, (162, 191))

    screen.blit(TEXT_7, (45, 304))
    screen.blit(TEXT_8, (153, 304))
    screen.blit(TEXT_9, (265, 304))
    screen.blit(TEXT_DEL, (349, 310))
    screen.blit(TEXT_AC, (469, 310))

    screen.blit(TEXT_4, (44, 415))
    screen.blit(TEXT_5, (154, 415))
    screen.blit(TEXT_6, (266, 415))
    screen.blit(TEXT_TIMES, (376, 422))
    screen.blit(TEXT_DIVIDE, (490, 410))

    screen.blit(TEXT_1, (44, 525))
    screen.blit(TEXT_2, (154, 525))
    screen.blit(TEXT_3, (265, 525))
    screen.blit(TEXT_PLUS, (374, 520))
    screen.blit(TEXT_MINUS, (490, 515))

    screen.blit(TEXT_0, (44, 635))
    screen.blit(TEXT_POINT, (160, 635))
    screen.blit(TEXT_TIMES_TEN_POWER, (236, 643))
    screen.blit(TEXT_ANS, (345, 643))
    screen.blit(TEXT_EQUALS, (480, 623))
    screen.blit(TEXT_POWER, (255, 204))

    if error_dummy != 1:
        screen.blit(ANSWER_TEXT, (WIDTH - len(str(ans)) * 36 - 35, 85))
    if error_dummy == 1:
        screen.blit(ERROR_MESSAGE, (350, 85))

    pygame.display.update()
    clock.tick(60)

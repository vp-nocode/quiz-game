import pygame
import quiz_lib as qlib

FPS = 30


def get_score(quiz_set):
    score = 0
    true_answers = 0
    for question in quiz_set:
        if question['user_answer'] == question['correct']:
            score += question['ball']
            true_answers += 1

    return {'score': score, 'true_answers': true_answers, 'number_of_questions': len(quiz_set)}

def draw_quiz_result_page(screen, state, quiz_set):

    fonts = qlib.create_fonts()
    clock = pygame.time.Clock()
    score = get_score(quiz_set)
    button_next = qlib.create_button('Начать новую Викторину', 80, 500, 340, 40, qlib.TEXT_COLOR, font=fonts['font32'])
    button_end = qlib.create_button('Закончить игру', 450, 500, 220, 40, qlib.TEXT_COLOR, font=fonts['font32'])
    background_image = pygame.image.load('img/fon1.png')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

            elif state == 'quiz_result':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_next['bt_rect'].collidepoint(event.pos):
                        return 'category'

                    elif button_end['bt_rect'].collidepoint(event.pos):
                        return 'profile'

        # screen.fill(qlib.BG_COLOR)
        screen.blit(background_image, (0, 0))

        qlib.draw_text(screen, "Ваш результат", (200, 50), False, fonts['font32'])

        qlib.draw_text(screen, f"Всего вопросов: {score['number_of_questions']}", (100, 150), False, fonts['font32'])
        qlib.draw_text(screen, f"Правильных ответов: {score['true_answers']}", (100, 200), False, fonts['font32'])
        qlib.draw_text(screen, f"Набрано очков: {score['score']}", (100, 250), False, fonts['font32'])

        qlib.draw_button(screen, button_next)
        qlib.draw_button(screen, button_end)

        pygame.display.flip()
        clock.tick(FPS)

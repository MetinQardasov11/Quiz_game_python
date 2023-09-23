import pygame
import sys
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Quiz Game")

# Load fonts
font = pygame.font.Font(None, 36)

# Define the questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Earth"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Giraffe", "Elephant", "Blue Whale", "Lion"],
        "correct_answer": "Blue Whale",
    },
]

# Shuffle the questions
random.shuffle(questions)

# Initialize variables
current_question = 0
score = 0

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def show_question(question_data):
    screen.fill(WHITE)
    draw_text(question_data["question"], WIDTH // 2, 100)

    option_y = 200
    for i, option in enumerate(question_data["options"], start=1):
        draw_text(f"{i}. {option}", WIDTH // 2, option_y)
        option_y += 50

def show_score():
    screen.fill(WHITE)
    draw_text("Quiz Completed!", WIDTH // 2, 100)
    draw_text(f"Your score: {score}/{len(questions)}", WIDTH // 2, 200)

# Game loop
running = True
quiz_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not quiz_started:
            quiz_started = True
            show_question(questions[current_question])
        elif event.type == pygame.KEYDOWN and quiz_started:
            if event.unicode.isdigit():
                selected_option = int(event.unicode)
                if 1 <= selected_option <= len(questions[current_question]["options"]):
                    if questions[current_question]["options"][selected_option - 1] == questions[current_question]["correct_answer"]:
                        score += 1
                    current_question += 1
                    if current_question < len(questions):
                        show_question(questions[current_question])
                    else:
                        show_score()
                else:
                    pass  # Invalid option, do nothing

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

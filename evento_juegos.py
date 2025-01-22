import pygame
pygame.init()

# Configuración inicial
pantalla = pygame.display.set_mode((640, 480))
personaje = pygame.Rect(100, 100, 50, 50)
puerta = pygame.Rect(300, 100, 50, 80)

# Preguntas y opciones
questions = [
    {"question": "¿Cuánto es 2 + 2?", "options": ["3", "4", "5"], "correct": "4"},
    {"question": "¿Cuál es la raíz cuadrada de 16?", "options": ["3", "4", "5"], "correct": "4"},
    {"question": "¿Cuál es el resultado de 9/3?", "options": ["2", "3", "4"], "correct": "3"}
]
current_question = 0
player_health = 3  # Salud del jugador

# Renderizar texto
font = pygame.font.Font(None, 36)

def mostrar_pregunta(pregunta):
    texto = font.render(pregunta["question"], True, (0, 0, 0))
    pantalla.blit(texto, (20, 20))

    for i, option in enumerate(pregunta["options"]):
        option_texto = font.render(f"{i + 1}. {option}", True, (0, 0, 0))
        pantalla.blit(option_texto, (20, 60 + i * 40))

def actualizar_salud():
    global player_health
    player_health -= 1

def mostrar_barra_salud():
    pygame.draw.rect(pantalla, (255, 0, 0), (10, 440, 200, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (10, 440, 200 * (player_health / 3), 20))

# Bucle principal
corriendo = True
preguntando = False
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Eventos de teclado
        if evento.type == pygame.KEYDOWN and preguntando:
            if evento.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                respuesta = evento.key - pygame.K_1
                if questions[current_question]["options"][respuesta] == questions[current_question]["correct"]:
                    current_question += 1
                    if current_question >= len(questions):
                        print("¡Felicidades, completaste todas las preguntas!")
                        corriendo = False  # Fin del juego.
                    preguntando = False
                else:
                    actualizar_salud()
                    if player_health <= 0:
                        print("¡Game Over!")
                        corriendo = False

    # Movimiento del personaje
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje.x -= 1
    if teclas[pygame.K_RIGHT]:
        personaje.x += 1

    # Chequeo de colisión con la puerta
    if personaje.colliderect(puerta) and not preguntando:
        preguntando = True
        mostrar_pregunta(questions[current_question])

    # Dibujar
    pantalla.fill((255, 255, 255))
    pygame.draw.rect(pantalla, (0, 0, 250), personaje)
    pygame.draw.rect(pantalla, (0, 250, 0), puerta)

    if preguntando:
        mostrar_pregunta(questions[current_question])

    mostrar_barra_salud()
    pygame.display.flip()

pygame.quit()

import pygame
import sys
import random
from objects import MovableObject, GlitterObject

# ==================== INITIALIZATION ====================
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adventure of Hope")
pygame.display.set_icon(pygame.image.load("assets/images/phunny.png"))

clock = pygame.time.Clock()

#NEXT STEPS


# ==================== LOAD ASSETS ====================
# Background and floor

backgrounds = {
    "room": pygame.image.load("assets/images/house.png"),
    "city": pygame.image.load("assets/images/city.png"),
    "guardpost": pygame.image.load("assets/images/guardpost.jpg"),
    "blacksmith": pygame.image.load("assets/images/blacksmith.jpg"),
    "forest": pygame.image.load("assets/images/forest.jpg"),
    "dragon": pygame.image.load("assets/images/dragon.png"),
    "darkness": pygame.image.load("assets/images/dark.jpg"),
    "birthday": pygame.image.load("assets/images/birthday.jpg"),
}

floors = {
    "room": pygame.image.load("assets/images/carpet.png"),
    "city": pygame.image.load("assets/images/cityroad.png"),
    "guardpost": pygame.image.load("assets/images/blank.png"),
    "blacksmith": pygame.image.load("assets/images/blank.png"),
    "forest": pygame.image.load("assets/images/blank.png"),
    "dragon": pygame.image.load("assets/images/blank.png"),
    "darkness": pygame.image.load("assets/images/blank.png"),
    "birthday": pygame.image.load("assets/images/blank.png"),
}

for key in backgrounds:
    backgrounds[key] = pygame.transform.scale(backgrounds[key], (800, 600))

for key in floors:
    floors[key] = pygame.transform.scale(floors[key], (800, 75))
    

# Character images
character = pygame.image.load("assets/images/hope, normal.png")
character = pygame.transform.scale(character, (100, 150))
character_flipped = pygame.transform.flip(character, True, False)

character_jumping = pygame.image.load("assets/images/hope, jumping.png")
character_jumping = pygame.transform.scale(character_jumping, (100, 150))
character_jumping_flipped = pygame.transform.flip(character_jumping, True, False)

character_crouch = pygame.image.load("assets/images/hope, crouching.png")
character_crouch = pygame.transform.scale(character_crouch, (75, 88))
character_crouch_flipped = pygame.transform.flip(character_crouch, True, False)

# Sword character images
character_sword = pygame.image.load("assets/images/hope, sword.png")
character_sword = pygame.transform.scale(character_sword, (100, 150))
character_sword_flipped = pygame.transform.flip(character_sword, True, False)

character_sword_jumping = pygame.image.load("assets/images/hope, jumping, sword.png")
character_sword_jumping = pygame.transform.scale(character_sword_jumping, (100, 150))
character_sword_jumping_flipped = pygame.transform.flip(character_sword_jumping, True, False)

# Running animations with sword
character_sword_run1 = pygame.image.load("assets/images/running with sword step1.png")
character_sword_run1 = pygame.transform.scale(character_sword_run1, (100, 150))
character_sword_run1_flipped = pygame.transform.flip(character_sword_run1, True, False)

character_sword_run2 = pygame.image.load("assets/images/running with sword step2.png")
character_sword_run2 = pygame.transform.scale(character_sword_run2, (100, 150))
character_sword_run2_flipped = pygame.transform.flip(character_sword_run2, True, False)

# Running animations without sword
character_run1 = pygame.image.load("assets/images/running without sword step1.png")
character_run1 = pygame.transform.scale(character_run1, (100, 150))
character_run1_flipped = pygame.transform.flip(character_run1, True, False)

character_run2 = pygame.image.load("assets/images/running without sword step2.png")
character_run2 = pygame.transform.scale(character_run2, (100, 150))
character_run2_flipped = pygame.transform.flip(character_run2, True, False)

# Goblin images
goblin_1 = pygame.image.load("assets/images/goblin_1.png")
goblin_1 = pygame.transform.scale(goblin_1, (80, 120))
goblin_1 = pygame.transform.flip(goblin_1, True, False)  # Flip to face left

goblin_2 = pygame.image.load("assets/images/goblin_2.png")
goblin_2 = pygame.transform.scale(goblin_2, (80, 120))
goblin_2 = pygame.transform.flip(goblin_2, True, False)  # Flip to face left

# Slash/attack animations
slash_1 = pygame.image.load("assets/images/slash_1.png")
slash_1 = pygame.transform.scale(slash_1, (60, 60))
slash_1_flipped = pygame.transform.flip(slash_1, True, False)

slash_2 = pygame.image.load("assets/images/slash_2.png")
slash_2 = pygame.transform.scale(slash_2, (60, 60))
slash_2_flipped = pygame.transform.flip(slash_2, True, False)

# Hole image
hole_image = pygame.image.load("assets/images/hole.png")
hole_image = pygame.transform.scale(hole_image, (500, 800))  # Wide enough and tall enough to stretch below frame

# Cake images
cake_image = pygame.image.load("assets/images/cake1.png")
cake_image = pygame.transform.scale(cake_image, (200, 200))

cake1_image = pygame.image.load("assets/images/cake1.png")
cake1_image = pygame.transform.scale(cake1_image, (200, 200))

cake2_image = pygame.image.load("assets/images/cake2.png")
cake2_image = pygame.transform.scale(cake2_image, (200, 200))

cake3_image = pygame.image.load("assets/images/cake3.png")
cake3_image = pygame.transform.scale(cake3_image, (200, 200))

cake4_image = pygame.image.load("assets/images/cake4.png")
cake4_image = pygame.transform.scale(cake4_image, (200, 200))

# Heros image for birthday
heros_image = pygame.image.load("assets/images/hero.png")
heros_image = pygame.transform.scale(heros_image, (350, 300))  # Adjust size as needed

# Game objects (only for room level)
bookshelf_image = pygame.image.load("assets/images/bookshelf.png")
bookshelf_width = bookshelf_image.get_width() // 3
bookshelf_height = bookshelf_image.get_height() // 3
bookshelf = MovableObject("assets/images/bookshelf.png", 150, 450 - bookshelf_height // 2, bookshelf_width, bookshelf_height)

letter = GlitterObject("assets/images/letter.jpg", 400, 120, 20, 24)

# Font
font = pygame.font.Font(None, 24)

# ==================== GOBLIN CLASS ====================
class Goblin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 120
        self.speed = 2
        self.alive = True
        self.dying = False
        self.death_timer = 0
        self.blink_timer = 0
        self.animation_frame = 0
        
    def update(self):
        if self.alive and not self.dying:
            # Move left towards player
            self.x -= self.speed
            self.animation_frame += 1
        elif self.dying:
            # Handle death animation
            self.death_timer += 1
            if self.death_timer >= 60:  # Die after 1 second (60 frames)
                self.alive = False
    
    def draw(self, screen):
        if self.alive:
            if self.dying:
                # Blink effect during death
                if (self.death_timer // 5) % 2 == 0:  # Blink every 5 frames
                    current_goblin = goblin_1 if (self.animation_frame // 8) % 2 == 0 else goblin_2
                    screen.blit(current_goblin, (self.x, self.y))
            else:
                # Normal animation
                current_goblin = goblin_1 if (self.animation_frame // 8) % 2 == 0 else goblin_2
                screen.blit(current_goblin, (self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def start_death(self):
        self.dying = True
        self.death_timer = 0

# ==================== LEVEL NAME ====================
def draw_level_indicator(screen, level_name, font):
    """Draw a box with the current level name in the top-right corner"""
    # Format the level name nicely
    level_display = level_name.upper()
    
    # Render the text
    text_surface = font.render(level_display, True, (255, 255, 255))
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    
    # Box dimensions (slightly larger than text)
    padding = 10
    box_width = text_width + padding * 2
    box_height = text_height + padding * 2
    
    # Position in top-right corner
    box_x = 800 - box_width - 10  # 10 pixels from right edge
    box_y = 10  # 10 pixels from top
    
    # Draw border (grey)
    pygame.draw.rect(screen, (100, 100, 100), 
                    (box_x - 2, box_y - 2, box_width + 4, box_height + 4))
    
    # Draw box background (black)
    pygame.draw.rect(screen, (0, 0, 0), 
                    (box_x, box_y, box_width, box_height))
    
    # Draw text
    text_x = box_x + padding
    text_y = box_y + padding
    screen.blit(text_surface, (text_x, text_y))

# ==================== GAME STATE ====================
# Current level
current_level = "room"

# Character position and physics
hope_x = 350
hope_y = 425
hope_size = 150
hope_width = 100
facing_right = True

ground_level = 425
hope_velocity_y = 0
gravity = 0.8

# Character states
is_jumping = False
is_crouching = False
is_running = False
has_sword = False
read_letter = False
met_guard = False
killed_gob = False

# Health system
character_health = 3
max_health = 3
invincible = False
invincible_timer = 0
invincible_duration = 120  # 2 seconds of invincibility after getting hit
at_medic = False
medic_timer = 0

# Combat states
is_attacking = False
attack_animation_frame = 0
attack_animation_speed = 5
attack_range = 100  # Range for attacking goblins

# Animation variables
run_animation_frame = 0
run_animation_speed = 8  # Change frame every 8 game frames

# Goblin management
goblins = []
goblin_spawn_timer = 0
goblin_spawn_interval = 180  # Spawn goblin every 3 seconds (180 frames at 60 FPS)
max_goblins = 5
goblins_killed = 0
total_goblins_to_kill = 10

# Darkness dialogue system
darkness_dialogues = [
    "Carter: Hope...",
    "Hope: Carter... Is that you???",
    "Carter: Yes, you finally found me...",
    "Carter: Happy Birthday Hopeeeeee!!!",
    "Others: Happy Birthday!!!"
]
current_dialogue = 0
dialogue_active = True
enter_pressed_last_frame = False

# Birthday cake system
cake_stage = 0  # 0 = cake.png, 1-4 = cake1-4.png
birthday_complete = False

# End game
game_ended = False
end_dialogue_stage = 0  # 0 = first message, 1 = second message, 2 = quit message

# Blacksmith quest states
blacksmith_active = False
blacksmith_dialogue_shown = False
blacksmith_dialogue_complete = False
current_question = 0
questions_correct = 0
waiting_for_answer = False
show_result = False
result_message = ""
result_timer = 0

# Blacksmith questions - SQL questions from the quiz
blacksmith_questions = [
    {
        "question": "Easy one... Who is the most beautifull, specially today?",
        "options": [
            "A) Divit",
            "B) Hope",
            "C) Me, the blacksmith...",
            "D) Anne Hathaway;"
        ],
        "correct": "B"
    },
    {
        "question": "What was the colour of bouquet Carter gave you?",
        "options": [
            "A) Pink and White",
            "B) Red and White",
            "C) Pink, Red and White",
            "D) What Bouquet?????"
        ],
        "correct": "A"
    },
    {
        "question": "What are we eating today???",
        "options": [
            "A) Each other >.< (Just Kidding!)",
            "B) Ramen",
            "C) Naan with Panner",
            "D) Mummy ke chappal"
        ],
        "correct": "B"
    }
]

# Initialize platforms here
platforms = []

# Game locations
locations = {
    "room": False,
    "city": False,
    "guardpost": False,
    "blacksmith": False,
    "forest": False,
    "dragon": False,
    "birthday": False
}

# Game control
running = True

# ==================== MAIN GAME LOOP ====================
while running:
    # ==================== EVENT HANDLING ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ==================== INPUT HANDLING ====================
    keys = pygame.key.get_pressed()
    
    # Reset running state
    is_running = False
    
    # Left movement
    if keys[pygame.K_LEFT]:
        if current_level == "blacksmith" and has_sword is True:
            if hope_x < 800:    
                facing_right = False
                is_running = True
                if is_crouching or is_jumping:
                    hope_x -= 3
                else: 
                    hope_x -= 5
        if hope_x > 0 or current_level == "guardpost" and has_sword is False:
            facing_right = False
            is_running = True
            if is_crouching or is_jumping:
                hope_x -= 3
            else: 
                hope_x -= 5
    
    # Right movement
    if keys[pygame.K_RIGHT]:
        # Forest level movement restriction
        if current_level == "forest":
            if killed_gob or hope_x < 760:
                facing_right = True
                is_running = True
                if is_crouching or is_jumping:
                    hope_x += 3
                else:
                    hope_x += 5
        elif current_level == "guardpost" and has_sword is False:
            if hope_x < 340:
                facing_right = True
                is_running = True
                if is_crouching or is_jumping:
                    hope_x += 3
                else: 
                    hope_x += 5    
        elif hope_x < 760 or read_letter is True:
            if current_level != "guardpost":                
                facing_right = True
                is_running = True
                if is_crouching or is_jumping:
                    hope_x += 3
                else: 
                    hope_x += 5
            else:
                if has_sword is True:
                        facing_right = True
                        is_running = True
                        if is_crouching or is_jumping:
                            hope_x += 3
                        else: 
                            hope_x += 5  
    
    # Update running animation
    if is_running and not is_jumping and not is_crouching:
        run_animation_frame += 1
    else:
        run_animation_frame = 0
    
    # Jump
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        hope_velocity_y = -20
    
    # Crouch
    if keys[pygame.K_DOWN]:
        is_crouching = True
    else:
        is_crouching = False

    # Darkness dialogue progression with ENTER
    if current_level == "darkness" and dialogue_active:
        if keys[pygame.K_RETURN] and not enter_pressed_last_frame:
            current_dialogue += 1
            if current_dialogue >= len(darkness_dialogues):
                dialogue_active = False
                current_level = "birthday"
                hope_x = 350
                ground_level = 425
                hope_y = ground_level
            enter_pressed_last_frame = True
        elif not keys[pygame.K_RETURN]:
            enter_pressed_last_frame = False
    
    # End game dialogue progression with ENTER
    if current_level == "darkness" and game_ended:
        if keys[pygame.K_RETURN] and not enter_pressed_last_frame:
            if end_dialogue_stage < 2:
                end_dialogue_stage += 1
            enter_pressed_last_frame = True
        elif not keys[pygame.K_RETURN]:
            enter_pressed_last_frame = False
        
        # Quit game with Q
        if keys[pygame.K_q] and end_dialogue_stage == 2:
            running = False
    
    # Birthday cake interaction with TAB
    if current_level == "birthday" and not game_ended:
        if keys[pygame.K_TAB]:
            if cake_stage < 4:
                cake_stage += 1
                pygame.time.wait(300)
            elif cake_stage == 4 and not birthday_complete:
                birthday_complete = True
                current_level = "darkness"
                game_ended = True
                end_dialogue_stage = 0
                pygame.time.wait(300)

    # Attack with TAB (only in forest with sword)
    if keys[pygame.K_TAB]:
        if current_level == "forest" and has_sword and not is_attacking:
            is_attacking = True
            attack_animation_frame = 0
            
            # Check if any goblin is in range
            hope_rect = pygame.Rect(hope_x, hope_y, hope_width, hope_size)
            for goblin in goblins:
                if goblin.alive and not goblin.dying:
                    goblin_rect = goblin.get_rect()
                    # Calculate distance
                    if facing_right:
                        attack_rect = pygame.Rect(hope_x, hope_y, hope_width + attack_range, hope_size)
                    else:
                        attack_rect = pygame.Rect(hope_x - attack_range, hope_y, hope_width + attack_range, hope_size)
                    
                    if attack_rect.colliderect(goblin_rect):
                        goblin.start_death()
                        goblins_killed += 1
            
            pygame.time.wait(100)  # Prevent spam clicking
        
        # Blacksmith interaction (non-forest levels)
        elif current_level == "city" and met_guard is True and not has_sword:
            # Check if character is in the left part of the city (x < 300)
            if hope_x < 300:
                current_level = "blacksmith"
                ground_level = 375
                hope_y = ground_level
                hope_x = 750
                blacksmith_active = True
                blacksmith_dialogue_shown = True
                blacksmith_dialogue_complete = False
                current_question = 0
                questions_correct = 0
                waiting_for_answer = False
                pygame.time.wait(300)  # Prevent double trigger
    
    # Update attack animation
    if is_attacking:
        attack_animation_frame += 1
        if attack_animation_frame >= attack_animation_speed * 4:  # Attack lasts for 4 frames
            is_attacking = False
            attack_animation_frame = 0
    
    # Progress from dialogue to questions - ENTER key
    if keys[pygame.K_RETURN]:
        if current_level == "blacksmith" and blacksmith_dialogue_shown and not blacksmith_dialogue_complete:
            blacksmith_dialogue_complete = True
            waiting_for_answer = True
            pygame.time.wait(300)

    # Handle blacksmith questions (only after dialogue is complete)
    if current_level == "blacksmith" and blacksmith_active and blacksmith_dialogue_complete and not has_sword:
        if waiting_for_answer and not show_result:
            answer = None
            
            # Check for answer keys
            if keys[pygame.K_a]:
                answer = "A"
            elif keys[pygame.K_b]:
                answer = "B"
            elif keys[pygame.K_c]:
                answer = "C"
            elif keys[pygame.K_d]:
                answer = "D"
            
            # Process answer if one was given
            if answer is not None:
                waiting_for_answer = False
                show_result = True
                
                if answer == blacksmith_questions[current_question]["correct"]:
                    questions_correct += 1
                    result_message = "Correct!"
                else:
                    result_message = f"Wrong! Correct answer: {blacksmith_questions[current_question]['correct']}"
                
                result_timer = 120  # Show result for 2 seconds (120 frames at 60 FPS)
                pygame.time.wait(300)  # Prevent double input
        
        # Handle result display and progression
        if show_result:
            result_timer -= 1
            if result_timer <= 0:
                show_result = False
                current_question += 1
                
                # Check if all questions answered
                if current_question >= len(blacksmith_questions):
                    if questions_correct >= 3:
                        # All correct - give sword!
                        has_sword = True
                        blacksmith_active = False
                    else:
                        # Failed - restart questions
                        current_question = 0
                        questions_correct = 0
                        waiting_for_answer = True
                        result_message = f"You got {questions_correct}/3. Try again!"
                        show_result = True
                        result_timer = 180
                else:
                    waiting_for_answer = True

    # ==================== GOBLIN SPAWNING ====================
    if current_level == "forest" and not killed_gob:
        goblin_spawn_timer += 1
        
        # Spawn new goblins at character level
        if goblin_spawn_timer >= goblin_spawn_interval and len(goblins) < max_goblins:
            new_goblin = Goblin(820, ground_level)  # Spawn at ground level (character level)
            goblins.append(new_goblin)
            goblin_spawn_timer = 0
        
        # Update goblins
        for goblin in goblins[:]:
            goblin.update()
            # Remove dead goblins
            if not goblin.alive:
                goblins.remove(goblin)
        
        # Check if enough goblins killed
        if goblins_killed >= total_goblins_to_kill:
            killed_gob = True

    # ==================== CONFIGURATIONS ====================
    # Update platforms based on current level
    if current_level == "room":
        bookshelf.update_platform()
        platforms = [bookshelf.get_platform()]
    else:
        # Clear platforms for other levels
        platforms = []

    # ==================== PHYSICS ====================
    # Apply gravity when jumping
    if is_jumping:
        hope_y += hope_velocity_y
        hope_velocity_y += gravity
        
        if hope_y >= ground_level:
            hope_y = ground_level
            is_jumping = False
            hope_velocity_y = 0
    
    # Apply gravity when falling
    if not is_jumping and hope_y < ground_level:
        hope_y += hope_velocity_y
        hope_velocity_y += gravity
        if hope_y >= ground_level:
            hope_y = ground_level
            hope_velocity_y = 0

    # ==================== COLLISION DETECTION ====================
    # Character collision rect
    hope_rect = pygame.Rect(hope_x, hope_y, hope_width, hope_size)
    
    # Platform collision (only if platforms exist)
    if platforms:
        for platform in platforms:
            if hope_rect.colliderect(platform):
                if hope_velocity_y > 0:
                    if hope_y + hope_size <= platform.top + 15:
                        hope_y = platform.top - hope_size
                        is_jumping = False
                        hope_velocity_y = 0
    
    # Letter collision (only in room)
    if current_level == "room":
        if hope_x < 300:
            city_backgrounds = "assets/images/city2.png"
            
        if letter is not None:
            letter_rect = pygame.Rect(letter.x, letter.y, letter.width, letter.height)
            if hope_rect.colliderect(letter_rect) and not read_letter:
                read_letter = True
                letter = None
    
    # Goblin collision and damage (only in forest)
    if current_level == "forest" and not invincible:
        for goblin in goblins:
            if goblin.alive and not goblin.dying:
                goblin_rect = goblin.get_rect()
                # Check if goblin touches character (within -5 of character width)
                damage_rect = pygame.Rect(hope_x - 5, hope_y, hope_width + 10, hope_size)
                if damage_rect.colliderect(goblin_rect):
                    character_health -= 1
                    invincible = True
                    invincible_timer = 0
                    
                    # If health reaches 0, send to medic
                    if character_health <= 0:
                        current_level = "city"
                        hope_x = 600
                        ground_level = 425
                        hope_y = ground_level
                        character_health = max_health
                        at_medic = True
                        medic_timer = 180  # Show message for 3 seconds
                        
                        # Clear all goblins
                        goblins.clear()
                        goblins_killed = 0
                        killed_gob = False
                    break
    
    # Update invincibility timer
    if invincible:
        invincible_timer += 1
        if invincible_timer >= invincible_duration:
            invincible = False
            invincible_timer = 0
    
    # Update medic message timer
    if at_medic:
        medic_timer -= 1
        if medic_timer <= 0:
            at_medic = False

    # ==================== RENDERING ====================
    # Draw background based on current level
    screen.blit(backgrounds[current_level], (0, 0))
    
    # Draw floor based on current level
    screen.blit(floors[current_level], (0, 525))
    
    # Draw level indicator in top-right corner
    draw_level_indicator(screen, current_level, font)
    
    # ==================== BLACKSMITH UI ====================
    if current_level == "blacksmith":
        if blacksmith_active and not has_sword:
            # Draw main textbox
            textbox_width = 750
            textbox_height = 240
            textbox_x = 25
            textbox_y = 40
            
            # Draw black background with grey border
            pygame.draw.rect(screen, (100, 100, 100), 
                            (textbox_x - 2, textbox_y - 2, textbox_width + 4, textbox_height + 4))
            pygame.draw.rect(screen, (0, 0, 0), 
                            (textbox_x, textbox_y, textbox_width, textbox_height))
            
            # Show dialogue first, then questions
            if blacksmith_dialogue_shown and not blacksmith_dialogue_complete:
                # Display Blacksmith dialogue
                dialogue_lines = [
                    "Blacksmith: Oh Rose... Carter left you a sword, it is called",
                    "'Reliance Mart Knife'... he says once you had used same to cut",
                    "your hand a bit so he took it away from you...",
                    "",
                    "Alright. Answer three questions for me to verify you are not",
                    "the impostor, and sword is yours..."
                ]
                
                line_height = 22
                start_y = textbox_y + 30
                
                for i, line in enumerate(dialogue_lines):
                    if i == 1:  # Highlight the sword name
                        text_surface = font.render(line, True, (255, 215, 0))  # Gold color
                    else:
                        text_surface = font.render(line, True, (255, 255, 255))
                    screen.blit(text_surface, (textbox_x + 20, start_y + i * line_height))
                
                # Draw instruction
                instruction = "Press ENTER to continue..."
                instruction_surface = font.render(instruction, True, (200, 200, 200))
                instruction_rect = instruction_surface.get_rect(center=(400, textbox_y + textbox_height - 20))
                screen.blit(instruction_surface, instruction_rect)
            
            elif blacksmith_dialogue_complete:
                # Show questions after dialogue
                if show_result:
                    # Show result message
                    result_color = (0, 255, 0) if "Correct" in result_message else (255, 0, 0)
                    result_surface = font.render(result_message, True, result_color)
                    result_rect = result_surface.get_rect(center=(400, 130))
                    screen.blit(result_surface, result_rect)
                    
                    # Show score
                    score_text = f"Score: {questions_correct}/{len(blacksmith_questions)}"
                    score_surface = font.render(score_text, True, (255, 255, 255))
                    score_rect = score_surface.get_rect(center=(400, 160))
                    screen.blit(score_surface, score_rect)
                    
                    # Show next instruction
                    if current_question < len(blacksmith_questions):
                        next_text = "Get ready for next question..."
                        next_surface = font.render(next_text, True, (200, 200, 200))
                        next_rect = next_surface.get_rect(center=(400, 190))
                        screen.blit(next_surface, next_rect)
                else:
                    # Display current question
                    question_data = blacksmith_questions[current_question]
                    
                    # Split question into lines for display
                    question_lines = question_data["question"].split('\n')
                    
                    line_height = 20
                    start_y = textbox_y + 10
                    
                    # Draw question
                    for i, line in enumerate(question_lines):
                        text_surface = font.render(line, True, (255, 255, 100))
                        screen.blit(text_surface, (textbox_x + 10, start_y + i * line_height))
                    
                    # Draw options
                    option_start_y = start_y + len(question_lines) * line_height + 15
                    for i, option in enumerate(question_data["options"]):
                        text_surface = font.render(option, True, (255, 255, 255))
                        screen.blit(text_surface, (textbox_x + 10, option_start_y + i * line_height))
                    
                    # Draw instruction
                    instruction = "Press A, B, C, or D to answer"
                    instruction_surface = font.render(instruction, True, (200, 200, 200))
                    instruction_rect = instruction_surface.get_rect(center=(400, textbox_y + textbox_height - 15))
                    screen.blit(instruction_surface, instruction_rect)
                
                # Draw progress (always show during questions)
                progress_text = f"Question {current_question + 1}/{len(blacksmith_questions)} | Score: {questions_correct}/{len(blacksmith_questions)}"
                progress_surface = font.render(progress_text, True, (150, 150, 150))
                screen.blit(progress_surface, (textbox_x + 10, textbox_y + textbox_height + 10))
        
        elif has_sword:
            # Show success message
            success_text = "You got the sword! Return to the city! (Go right)"
            success_surface = font.render(success_text, True, (0, 255, 0))
            success_rect = success_surface.get_rect(center=(400, 560))
            
            # Draw black border
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(success_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            screen.blit(success_surface, success_rect)
    
    # Draw game objects (only in room)
    if current_level == "room":
        if letter is not None:
            letter.draw(screen)
        
        bookshelf.draw(screen)

    # ==================== DRAW GOBLINS ====================
    if current_level == "forest":
        for goblin in goblins:
            goblin.draw(screen)

    # ==================== UI DRAWING ====================
    # Draw textbox or hint (only in room)
    if current_level == "room":
        if read_letter:
            textbox_width = 220
            textbox_height = 100
            textbox_x = 10
            textbox_y = 10
            
            # Draw black background with grey border
            pygame.draw.rect(screen, (100, 100, 100), (textbox_x - 2, textbox_y - 2, textbox_width + 4, textbox_height + 4))
            pygame.draw.rect(screen, (0, 0, 0), (textbox_x, textbox_y, textbox_width, textbox_height))
            
            # Draw white text with word wrapping
            text_lines = [
                "Hi Hope, Carter here.",
                "I am going to Misty Groves.",
                "A dragon has appeared.",
                "Duty Calls, I'll be back..."
            ]
            
            line_height = 18
            start_y = textbox_y + 5
            
            for i, line in enumerate(text_lines):
                text_surface = font.render(line, True, (255, 255, 255))
                screen.blit(text_surface, (textbox_x + 5, start_y + i * line_height))
        else:
            # Draw hint text at bottom center with black border
            hint_text = "Hint: Find the letter, try to jump over things."
            hint_surface = font.render(hint_text, True, (200, 200, 200))
            
            # Draw black border (offset by 1 pixel in all directions)
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(hint_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            # Draw white/grey text on top
            hint_rect = hint_surface.get_rect(center=(400, 560))
            screen.blit(hint_surface, hint_rect)
    
    if current_level == "city":
        if at_medic:
            # Show medic message
            medic_text = f"You are at Medic, health restored {character_health}/{max_health}."
            medic_surface = font.render(medic_text, True, (0, 255, 0))
            medic_rect = medic_surface.get_rect(center=(400, 560))
            
            # Draw black border
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(medic_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            screen.blit(medic_surface, medic_rect)
        elif read_letter is True and not met_guard:
            hint_text = "You have arrived at the city! Keep Moving!"
            hint_surface = font.render(hint_text, True, (200, 200, 200))
            
            # Draw black border
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(hint_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            hint_rect = hint_surface.get_rect(center=(400, 560))
            screen.blit(hint_surface, hint_rect)
            
        elif read_letter is True and met_guard and not has_sword:
            if hope_x < 300:
                hint_text = "Press TAB to interact with Blacksmith."
            else:
                hint_text = "Move left to find the Blacksmith. Press TAB to interact."
            hint_surface = font.render(hint_text, True, (200, 200, 200))
            
            # Draw black border
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(hint_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            hint_rect = hint_surface.get_rect(center=(400, 560))
            screen.blit(hint_surface, hint_rect)
    
    if current_level == "guardpost":
        if has_sword:
            hint_text = "Gates are open!"
            hint_surface = font.render(hint_text, True, (200, 200, 200))
        else:
            hint_text = "Guard - Aye! Its dangerous ahead. You are not allowed without a sword!"
            hint_surface = font.render(hint_text, True, (200, 200, 200))
        
        # Draw black border (offset by 1 pixel in all directions)
        border_offset = 1
        for x_offset in [-border_offset, 0, border_offset]:
            for y_offset in [-border_offset, 0, border_offset]:
                if x_offset != 0 or y_offset != 0:
                    border_surface = font.render(hint_text, True, (0, 0, 0))
                    border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                    screen.blit(border_surface, border_rect)
        
        # Draw white/grey text on top
        hint_rect = hint_surface.get_rect(center=(400, 560))
        screen.blit(hint_surface, hint_rect)
        
        if met_guard and not has_sword:
            hint_text2 = "Find the blacksmith to get a sword!"
            hint_surface2 = font.render(hint_text2, True, (200, 200, 200))
            
            # Draw black border
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface2 = font.render(hint_text2, True, (0, 0, 0))
                        border_rect2 = border_surface2.get_rect(center=(400 + x_offset, 540 + y_offset))
                        screen.blit(border_surface2, border_rect2)
            
            hint_rect2 = hint_surface2.get_rect(center=(400, 540))
            screen.blit(hint_surface2, hint_rect2)

    if current_level == "forest":
        if not killed_gob:
            hint_text = f"GOBLINS! Press TAB to attack | Health: {character_health}/{max_health} | Kills: {goblins_killed}/{total_goblins_to_kill}"
        else:
            hint_text = "All goblins defeated! You can proceed!"
        hint_surface = font.render(hint_text, True, (200, 200, 200))
        
        # Draw black border
        border_offset = 1
        for x_offset in [-border_offset, 0, border_offset]:
            for y_offset in [-border_offset, 0, border_offset]:
                if x_offset != 0 or y_offset != 0:
                    border_surface = font.render(hint_text, True, (0, 0, 0))
                    border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                    screen.blit(border_surface, border_rect)
        
        hint_rect = hint_surface.get_rect(center=(400, 560))
        screen.blit(hint_surface, hint_rect)
    
    if current_level == "dragon":
        # Draw hole only when character crosses x=420 (surprise!)
        if hope_x > 420:
            screen.blit(hole_image, (300, 300))
        
        hint_text = "Dragon Temple... Beware."
        hint_surface = font.render(hint_text, True, (255, 0, 0))
        
        # Draw black border
        border_offset = 1
        for x_offset in [-border_offset, 0, border_offset]:
            for y_offset in [-border_offset, 0, border_offset]:
                if x_offset != 0 or y_offset != 0:
                    border_surface = font.render(hint_text, True, (0, 0, 0))
                    border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                    screen.blit(border_surface, border_rect)
        
        hint_rect = hint_surface.get_rect(center=(400, 560))
        screen.blit(hint_surface, hint_rect)
    
    if current_level == "darkness":
        if game_ended:
            # Show different messages based on end_dialogue_stage
            if end_dialogue_stage == 0:
                # First message
                msg1 = "I love you hope, this game took over 16 hours but its all worth it"
                msg2 = "for you Babygirl... PRESS ENTER Darling..."
                
                msg1_surface = font.render(msg1, True, (255, 255, 255))
                msg1_rect = msg1_surface.get_rect(center=(400, 280))
                
                msg2_surface = font.render(msg2, True, (255, 255, 255))
                msg2_rect = msg2_surface.get_rect(center=(400, 310))
                
                # Draw black borders
                border_offset = 1
                for x_offset in [-border_offset, 0, border_offset]:
                    for y_offset in [-border_offset, 0, border_offset]:
                        if x_offset != 0 or y_offset != 0:
                            border1 = font.render(msg1, True, (0, 0, 0))
                            border1_rect = border1.get_rect(center=(400 + x_offset, 280 + y_offset))
                            screen.blit(border1, border1_rect)
                            
                            border2 = font.render(msg2, True, (0, 0, 0))
                            border2_rect = border2.get_rect(center=(400 + x_offset, 310 + y_offset))
                            screen.blit(border2, border2_rect)
                
                screen.blit(msg1_surface, msg1_rect)
                screen.blit(msg2_surface, msg2_rect)
                
            elif end_dialogue_stage == 1:
                # Second message
                msg1 = "No need to walk through sun and spiders, what's there is already"
                msg2 = "waiting for you... And Again I LOVE YOU... Dearly..."
                msg3 = "MARRY ME ALREADY!!!"
                
                msg1_surface = font.render(msg1, True, (255, 100, 100))
                msg1_rect = msg1_surface.get_rect(center=(400, 270))
                
                msg2_surface = font.render(msg2, True, (255, 100, 100))
                msg2_rect = msg2_surface.get_rect(center=(400, 300))
                
                msg3_surface = font.render(msg3, True, (255, 50, 50))
                msg3_rect = msg3_surface.get_rect(center=(400, 330))
                
                # Draw black borders
                border_offset = 1
                for x_offset in [-border_offset, 0, border_offset]:
                    for y_offset in [-border_offset, 0, border_offset]:
                        if x_offset != 0 or y_offset != 0:
                            border1 = font.render(msg1, True, (0, 0, 0))
                            border1_rect = border1.get_rect(center=(400 + x_offset, 270 + y_offset))
                            screen.blit(border1, border1_rect)
                            
                            border2 = font.render(msg2, True, (0, 0, 0))
                            border2_rect = border2.get_rect(center=(400 + x_offset, 300 + y_offset))
                            screen.blit(border2, border2_rect)
                            
                            border3 = font.render(msg3, True, (0, 0, 0))
                            border3_rect = border3.get_rect(center=(400 + x_offset, 330 + y_offset))
                            screen.blit(border3, border3_rect)
                
                screen.blit(msg1_surface, msg1_rect)
                screen.blit(msg2_surface, msg2_rect)
                screen.blit(msg3_surface, msg3_rect)
                
            elif end_dialogue_stage == 2:
                # Third message - quit
                quit_msg = "Press Q to quit, maybe you can play again..."
                
                quit_surface = font.render(quit_msg, True, (200, 200, 200))
                quit_rect = quit_surface.get_rect(center=(400, 300))
                
                # Draw black border
                border_offset = 1
                for x_offset in [-border_offset, 0, border_offset]:
                    for y_offset in [-border_offset, 0, border_offset]:
                        if x_offset != 0 or y_offset != 0:
                            border = font.render(quit_msg, True, (0, 0, 0))
                            border_rect = border.get_rect(center=(400 + x_offset, 300 + y_offset))
                            screen.blit(border, border_rect)
                
                screen.blit(quit_surface, quit_rect)
            
        elif dialogue_active and current_dialogue < len(darkness_dialogues):
            # Show current dialogue
            dialogue_text = darkness_dialogues[current_dialogue]
            dialogue_surface = font.render(dialogue_text, True, (255, 255, 255))
            dialogue_rect = dialogue_surface.get_rect(center=(400, 300))
            
            # Draw black border
            border_offset = 1
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface = font.render(dialogue_text, True, (0, 0, 0))
                        border_rect = border_surface.get_rect(center=(400 + x_offset, 300 + y_offset))
                        screen.blit(border_surface, border_rect)
            
            screen.blit(dialogue_surface, dialogue_rect)
            
            # Show instruction
            instruction_text = "Press ENTER to continue..."
            instruction_surface = font.render(instruction_text, True, (150, 150, 150))
            instruction_rect = instruction_surface.get_rect(center=(400, 560))
            
            # Draw black border
            for x_offset in [-border_offset, 0, border_offset]:
                for y_offset in [-border_offset, 0, border_offset]:
                    if x_offset != 0 or y_offset != 0:
                        border_surface2 = font.render(instruction_text, True, (0, 0, 0))
                        border_rect2 = border_surface2.get_rect(center=(400 + x_offset, 560 + y_offset))
                        screen.blit(border_surface2, border_rect2)
            
            screen.blit(instruction_surface, instruction_rect)
    
    if current_level == "birthday":
        # Draw heros image behind the cake (5 pixels above ground level)
        screen.blit(heros_image, (250, 275))
        
        # Draw cake based on stage at ground level
        cake_y = 350  # Ground level position
        
        if cake_stage == 0:
            screen.blit(cake1_image, (300, cake_y))
            cake_text = "Reveal the cake"
        elif cake_stage == 1:
            screen.blit(cake1_image, (300, cake_y))
            cake_text = "Blow the candles"
        elif cake_stage == 2:
            screen.blit(cake2_image, (300, cake_y))
            cake_text = "Give a bite to hubby Carter"
        elif cake_stage == 3:
            screen.blit(cake3_image, (300, cake_y))
            cake_text = "Eat and Feast"
        elif cake_stage == 4:
            screen.blit(cake4_image, (300, cake_y))
            cake_text = "oopsies cake is gone..."
        
        # Draw cake stage text
        cake_text_surface = font.render(cake_text, True, (255, 200, 100))
        cake_text_rect = cake_text_surface.get_rect(center=(400, 300))
        
        # Draw black border for cake text
        border_offset = 1
        for x_offset in [-border_offset, 0, border_offset]:
            for y_offset in [-border_offset, 0, border_offset]:
                if x_offset != 0 or y_offset != 0:
                    border_surface = font.render(cake_text, True, (0, 0, 0))
                    border_rect = border_surface.get_rect(center=(400 + x_offset, 300 + y_offset))
                    screen.blit(border_surface, border_rect)
        
        screen.blit(cake_text_surface, cake_text_rect)
        
        # Draw instruction hint
        hint_text = "Press TAB to continue..."
        hint_surface = font.render(hint_text, True, (200, 200, 200))
        
        # Draw black border
        border_offset = 1
        for x_offset in [-border_offset, 0, border_offset]:
            for y_offset in [-border_offset, 0, border_offset]:
                if x_offset != 0 or y_offset != 0:
                    border_surface = font.render(hint_text, True, (0, 0, 0))
                    border_rect = border_surface.get_rect(center=(400 + x_offset, 560 + y_offset))
                    screen.blit(border_surface, border_rect)
        
        hint_rect = hint_surface.get_rect(center=(400, 560))
        screen.blit(hint_surface, hint_rect)

    # ==================== CHARACTER DRAWING ====================
    # Determine which animation frame to use for running
    current_run_frame = (run_animation_frame // run_animation_speed) % 2  # Alternates between 0 and 1
    
    # Choose character set based on sword status
    if has_sword:
        char_normal = character_sword
        char_normal_flipped = character_sword_flipped
        char_jump = character_sword_jumping
        char_jump_flipped = character_sword_jumping_flipped
        char_crouch_img = character_crouch  # Use regular crouch for now
        char_crouch_flipped = character_crouch_flipped
        char_run1 = character_sword_run1
        char_run1_flipped = character_sword_run1_flipped
        char_run2 = character_sword_run2
        char_run2_flipped = character_sword_run2_flipped
    else:
        char_normal = character
        char_normal_flipped = character_flipped
        char_jump = character_jumping
        char_jump_flipped = character_jumping_flipped
        char_crouch_img = character_crouch
        char_crouch_flipped = character_crouch_flipped
        char_run1 = character_run1
        char_run1_flipped = character_run1_flipped
        char_run2 = character_run2
        char_run2_flipped = character_run2_flipped
    
    if is_crouching:
        current_height = 75
        draw_y = hope_y + 75
        # Apply invincibility blink effect
        if not invincible or (invincible_timer // 10) % 2 == 0:
            if facing_right:
                screen.blit(char_crouch_img, (hope_x, draw_y))
            else:
                screen.blit(char_crouch_flipped, (hope_x, draw_y))
    elif is_jumping:
        current_height = hope_size
        draw_y = hope_y
        # Apply invincibility blink effect
        if not invincible or (invincible_timer // 10) % 2 == 0:
            if facing_right:
                screen.blit(char_jump, (hope_x, draw_y))
            else:
                screen.blit(char_jump_flipped, (hope_x, draw_y))
    elif is_running:
        current_height = hope_size
        draw_y = hope_y
        # Switch between run frames
        # Apply invincibility blink effect
        if not invincible or (invincible_timer // 10) % 2 == 0:
            if current_run_frame == 0:
                if facing_right:
                    screen.blit(char_run1, (hope_x, draw_y))
                else:
                    screen.blit(char_run1_flipped, (hope_x, draw_y))
            else:
                if facing_right:
                    screen.blit(char_run2, (hope_x, draw_y))
                else:
                    screen.blit(char_run2_flipped, (hope_x, draw_y))
    else:
        current_height = hope_size
        draw_y = hope_y
        # Apply invincibility blink effect
        if not invincible or (invincible_timer // 10) % 2 == 0:
            if facing_right:
                screen.blit(char_normal, (hope_x, draw_y))
            else:
                screen.blit(char_normal_flipped, (hope_x, draw_y))

    # ==================== ATTACK ANIMATION ====================
    if is_attacking and has_sword:
        # Determine slash position based on facing direction
        slash_offset_x = 70 if facing_right else -70
        slash_x = hope_x + slash_offset_x
        slash_y = hope_y + 45  # Position slash in middle of character
        
        # Alternate between slash_1 and slash_2
        current_slash_frame = (attack_animation_frame // attack_animation_speed) % 2
        
        if current_slash_frame == 0:
            if facing_right:
                screen.blit(slash_1, (slash_x, slash_y))
            else:
                screen.blit(slash_1_flipped, (slash_x, slash_y))
        else:
            if facing_right:
                screen.blit(slash_2, (slash_x, slash_y))
            else:
                screen.blit(slash_2_flipped, (slash_x, slash_y))

    # ==================== LEVEL TRANSITIONS ====================
    if read_letter is True and current_level == "room":
        if hope_x > 800:
            current_level = "city"
            hope_x = 20
            hope_y = ground_level

    if current_level == "city":
        if hope_x > 760:
            met_guard = True
            current_level = "guardpost"
            hope_x = 20
            ground_level = 350
            hope_y = ground_level
            

    if current_level == "guardpost":
        if hope_x < 0 and not has_sword:
            current_level = "city"
            hope_x = 750
            ground_level = 425
            hope_y = ground_level

    if current_level == "blacksmith":
        if hope_x > 800:
            current_level = "city"
            hope_x = 200
            ground_level = 425
            hope_y = ground_level

    if current_level == "guardpost":
        if hope_x > 760 and has_sword:
            current_level = "forest"
            hope_x = 20
            ground_level = 350
            hope_y = ground_level
    
    if current_level == "forest" and killed_gob:
        if hope_x > 800:
            current_level = "dragon"
            hope_x = 20
            ground_level = 400
            hope_y = ground_level
    
    # Dragon hole falling mechanic
    if current_level == "dragon" and hope_x > 420:
        ground_level = 1000
        if not is_jumping:
            is_jumping = True
    
    # Transition to darkness after falling
    if hope_y > 900 and current_level == "dragon":
        current_level = "darkness"
        hope_x = 350
        hope_y = 10
        is_jumping = True
        ground_level = 425
        if hope_y > 425:
            hope_y = 425
            is_jumping = False

    
    # ==================== DISPLAY UPDATE ====================
    pygame.display.flip()
    clock.tick(60)

# ==================== CLEANUP ====================
pygame.quit()
sys.exit()
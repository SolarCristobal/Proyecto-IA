import gymnasium
import keyboard

# Create the environment
env = gymnasium.make("ALE/DonkeyKong-v5", render_mode="human")

# Initialize the environment
observation = env.reset()

# Interact with the environment
running = True
while running:
    action = env.action_space.sample()
    env.step(action)
    
    # Detectar si se presiona la tecla de escape (Escape)
    if keyboard.is_pressed('esc'):
        running = False

# Close the environment
env.close()

import glfw  # OpenGl Windows Library
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np  # for arrays

vertex_src = """
# version 330 core

in vec3 a_position;

void main()
{
    gl_Position = vec4(a_position, 1.0);
}
"""

fragment_src = """
# version 330 core

out vec4 out_color;

void main()
{
    out_color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

if not glfw.init():
    raise Exception("glfw not initialised.")

window = glfw.create_window(1280, 720, "Shape-Oli", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw window cannot be created.")

glfw.set_window_pos(window, 400, 200)
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,    # Coordinates go from -1 to 1 for x (left to right screen)
             0.5, -0.5, 0.0,    # Coordinates go from -1 to 1 for y (bottom to top screen)
             0.0,  0.5, 0.0]    # Coordinates go from -1 to 1 (left to right)

colors = [1.0,  0.0, 0.0,
          0.0,  1.0, 0.0,
          0.0,  0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)  # Converting arrays for use with numpy
colors = np.array(colors, dtype=np.float32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

glUseProgram(shader)

""" Immediate mode - deprecated
glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)
"""

glClearColor(0, 0.1, 0.1, 1)      # Setting up the clear color for later

while not glfw.window_should_close(window): # Main Application Loop
    glfw.poll_events()            # Dealing with Windows messages
    glClear(GL_COLOR_BUFFER_BIT)  # Clearing background / color buffer

    glRotatef(2, 1, 1, 1)         # Some rotations for animations
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)     # Double buffering goodness

glfw.terminate()